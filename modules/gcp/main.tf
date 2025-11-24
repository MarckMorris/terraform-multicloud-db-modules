terraform {
  required_version = ">= 1.0"
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 5.0"
    }
  }
}

resource "google_sql_database_instance" "main" {
  name             = var.instance_name
  database_version = var.database_version
  region           = var.region
  
  settings {
    tier = var.tier
    
    backup_configuration {
      enabled    = true
      start_time = var.backup_start_time
    }
    
    ip_configuration {
      ipv4_enabled = true
    }
  }
  
  deletion_protection = false
}

resource "google_sql_database" "main" {
  name     = var.database_name
  instance = google_sql_database_instance.main.name
}
