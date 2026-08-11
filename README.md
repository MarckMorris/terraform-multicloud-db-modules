# Terraform Multi-Cloud Database Modules

Reusable Terraform modules for provisioning managed database infrastructure across GCP and AWS behind a single, consistent interface.

[![CI](https://github.com/MarckMorris/terraform-multicloud-db-modules/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/MarckMorris/terraform-multicloud-db-modules/actions/workflows/ci-cd.yml)
[![Terraform](https://img.shields.io/badge/Terraform-1.5+-blue)](https://www.terraform.io/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

## What this solves

Provisioning a managed database on any single cloud is straightforward. Doing it consistently across providers, with the same variable contract, the same tagging conventions and the same high-availability defaults, is where teams usually end up maintaining two Terraform codebases that quietly drift apart.

These modules wrap GCP Cloud SQL and AWS RDS behind a common interface, so an equivalent module call produces equivalent infrastructure on either provider.

## Design decisions

**A shared variable contract.** The same inputs describe intent on both providers. Where the underlying resources differ, such as Cloud SQL high availability versus RDS Multi-AZ, the module absorbs the difference rather than pushing it onto the caller.

**High availability is the default, not an opt-in.** Making HA optional means it gets skipped under deadline pressure. Multi-zone deployment and automated backups are enabled by default; single-zone is the explicit override.

**GitOps over local state.** The modules assume plan and apply run through CI against remote state, not from an engineer's laptop.

## Repository structure

| Path | Contents |
| --- | --- |
| `modules/` | Terraform modules, one per provider and resource type |
| `terraform/` | Root configuration and example usage |
| `configs/` | Environment configuration files |
| `scripts/` | Helper scripts for local workflows |
| `tests/` | Module validation tests |

## Requirements

Terraform 1.5 or later, OpenTofu also supported. A GCP or AWS account with credentials configured. Docker is optional, for the containerized workflow.

## Quick start

```bash
git clone https://github.com/MarckMorris/terraform-multicloud-db-modules.git
cd terraform-multicloud-db-modules

cp .env.example .env
# fill in your project and account details

cd terraform
terraform init
terraform plan
```

Review the plan before applying. These modules create billable cloud resources.

## Configuration

Environment settings live in `configs/`.

| Parameter | Description |
| --- | --- |
| `database.type` | Engine: PostgreSQL or MySQL |
| `database.version` | Engine version |
| `database.instance_type` | Instance sizing |
| `scaling.min_replicas` | Minimum read replicas |
| `scaling.max_replicas` | Maximum read replicas |

## Continuous integration

Every push runs `terraform init -backend=false` and `terraform validate` against the root configuration. The pipeline needs no cloud credentials, so it runs on any fork.

## License

MIT, see [LICENSE](LICENSE).

## Author

**Marcos Morris**, Cloud Infrastructure Engineer, Bentonville, AR

[LinkedIn](https://www.linkedin.com/in/marck-morris/) · [Portfolio](https://marckmorris.github.io/) · marck.morris.pro@gmail.com
