terraform {
  required_version = ">= 1.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

resource "aws_db_instance" "main" {
  identifier        = var.db_identifier
  engine            = var.engine
  engine_version    = var.engine_version
  instance_class    = var.instance_class
  allocated_storage = var.allocated_storage
  
  db_name  = var.db_name
  username = var.master_username
  password = var.master_password
  
  skip_final_snapshot = true
  
  backup_retention_period = var.backup_retention_days
  backup_window          = var.backup_window
  maintenance_window     = var.maintenance_window
  
  multi_az = var.multi_az
  
  tags = merge(
    var.tags,
    {
      ManagedBy = "Terraform"
      Module    = "aws-rds"
    }
  )
}

resource "aws_db_subnet_group" "main" {
  name       = "${var.db_identifier}-subnet-group"
  subnet_ids = var.subnet_ids
  
  tags = var.tags
}
