#!/usr/bin/env python3
"""
Terraform Multi-Cloud Module Validator
"""

import subprocess
import os
from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)


class TerraformModuleTester:
    
    def __init__(self):
        self.test_results = []
        self.modules = ['aws', 'gcp', 'azure']
        
    def run_command(self, cmd: str, cwd: str = None) -> tuple:
        try:
            result = subprocess.run(
                cmd,
                shell=True,
                cwd=cwd,
                capture_output=True,
                text=True,
                timeout=180  # 3 minutes
            )
            return result.returncode == 0, result.stdout, result.stderr
        except subprocess.TimeoutExpired:
            return False, "", "Command timed out after 180 seconds"
        except Exception as e:
            return False, "", str(e)
    
    def test_module(self, module_name: str) -> dict:
        logger.info(f"Testing {module_name} module...")
        
        module_path = f"modules/{module_name}"
        
        test_result = {
            'module': module_name,
            'timestamp': datetime.now().isoformat(),
            'tests': [],
            'all_passed': False
        }
        
        # Test 1: terraform init
        logger.info(f"  Running terraform init (may take 2-3 minutes)...")
        success, stdout, stderr = self.run_command(
            "terraform init -no-color",
            cwd=module_path
        )
        
        test_result['tests'].append({
            'name': 'terraform_init',
            'passed': success,
            'output': (stdout if success else stderr)[:200]
        })
        
        if not success:
            logger.error(f"  Init failed for {module_name}")
            test_result['all_passed'] = False
            return test_result
        
        # Test 2: terraform validate
        logger.info(f"  Running terraform validate...")
        success, stdout, stderr = self.run_command(
            "terraform validate -no-color",
            cwd=module_path
        )
        
        test_result['tests'].append({
            'name': 'terraform_validate',
            'passed': success,
            'output': (stdout if success else stderr)[:200]
        })
        
        # Test 3: Check structure
        logger.info(f"  Checking module structure...")
        required_files = ['main.tf', 'variables.tf', 'outputs.tf']
        files_exist = all(
            os.path.exists(os.path.join(module_path, f)) 
            for f in required_files
        )
        
        test_result['tests'].append({
            'name': 'module_structure',
            'passed': files_exist,
            'output': f"Required files present: {files_exist}"
        })
        
        test_result['all_passed'] = all(t['passed'] for t in test_result['tests'])
        
        return test_result
    
    def print_results(self, result: dict):
        print("\n" + "=" * 80)
        print(f"MODULE: {result['module'].upper()}")
        print("=" * 80)
        
        for test in result['tests']:
            status = "PASS" if test['passed'] else "FAIL"
            print(f"\n  {test['name']}: {status}")
            if test['output']:
                print(f"    {test['output'][:100]}")
        
        overall = "PASSED" if result.get('all_passed', False) else "FAILED"
        print(f"\n  Overall: {overall}")
        print("=" * 80)
    
    def run_all_tests(self):
        print("\n" + "=" * 80)
        print("TERRAFORM MULTI-CLOUD MODULE VALIDATOR")
        print("=" * 80)
        
        for module in self.modules:
            result = self.test_module(module)
            self.test_results.append(result)
            self.print_results(result)
        
        print("\n" + "=" * 80)
        print("TEST SUMMARY")
        print("=" * 80)
        
        passed = sum(1 for r in self.test_results if r.get('all_passed', False))
        total = len(self.test_results)
        
        print(f"\nModules Tested: {total}")
        print(f"Passed: {passed}")
        print(f"Failed: {total - passed}")
        
        print("\nModule Status:")
        for result in self.test_results:
            status = "PASS" if result.get('all_passed', False) else "FAIL"
            print(f"  {result['module']:10s}: {status}")
        
        print("=" * 80)
        
        return all(r.get('all_passed', False) for r in self.test_results)


def main():
    tester = TerraformModuleTester()
    success = tester.run_all_tests()
    
    if success:
        logger.info("All modules validated successfully!")
    else:
        logger.warning("Some modules failed validation")


if __name__ == "__main__":
    main()
