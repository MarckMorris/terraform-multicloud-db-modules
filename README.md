# Terraform Multi-Cloud Database Modules
Reusable Terraform modules for provisioning managed database infrastructure across GCP and AWS behind a single, consistent interface.
[![Terraform](https://img.shields.io/badge/Terraform-1.5+-blue)](https://www.terraform.io/) [![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
**Project status.** Personal portfolio project. The modules are functional and validated in CI, but this is not a deployed production system. Treat the configurations as reference implementations rather than battle-tested infrastructure.
## What this solves
Provisioning a managed database on any single cloud is straightforward. Doing it consistently across providers, with the same variable contract, the same tagging conventions and the same high-availability defaults, is where teams usually end up maintaining two Terraform codebases that quietly drift apart.
These modules wrap GCP Cloud SQL and AWS RDS behind a common interface, so an equivalent module call produces equivalent infrastructure on either provider.
## Design decisions
**A shared variable contract.** The same inputs describe intent on both providers. Where the underlying resources differ, such as Cloud SQL high availability versus RDS Multi-AZ, the module absorbs the difference rather than pushing it onto the caller.
**High availability is the default, not an opt-in.** Making HA optional means it gets skipped under deadline pressure. Multi-zone deployment and automated backups are enabled by default; single-zone is the explicit override.
**GitOps over local state.** The modules assume plan and apply run through CI against remote state, not from an engineer's laptop.
## Repository structure
The `modules/` directory holds the Terraform modules, one per provider and resource type. `terraform/` contains the root configuration and example usage, `configs/` the environment configuration files, `scripts/` helper scripts for local workflows, and `tests/` the module validation tests. The CI pipeline lives in `.github/workflows/`.
## Requirements
Terraform 1.5 or later, OpenTofu also supported. A GCP or AWS account with credentials configured. Docker is optional, for the containerized workflow.
## Quick start
Clone with `git clone https://github.com/MarckMorris/terraform-multicloud-db-modules.git`, then copy `.env.example` to `.env` and fill in your project and account details. From the `terraform/` directory run `terraform init` followed by `terraform plan`.
Review the plan before applying. These modules create billable cloud resources.
## Configuration
Environment settings live in `configs/`. The main parameters are `database.type` for the engine, PostgreSQL or MySQL; `database.version` for the engine version; `database.instance_type` for sizing; and `scaling.min_replicas` and `scaling.max_replicas` to bound the read replica count.
## Continuous integration
The GitHub Actions workflow runs `terraform fmt -check`, `terraform validate` and a plan against each module on every push. It does not apply.
## Scope
What this repository is not: a deployed production system, a live monitoring stack, or a benchmarked workload. The `tests/` directory validates module correctness, not runtime performance. No performance figures are published here because none have been measured under load.
## License
MIT. See [LICENSE](LICENSE).
## Author
**Marcos Morris**, Cloud Infrastructure Engineer, Bentonville, AR.
LinkedIn <https://www.linkedin.com/in/marck-morris/> · Portfolio <https://marckmorris.github.io/> · marck.morris.pro@gmail.com
