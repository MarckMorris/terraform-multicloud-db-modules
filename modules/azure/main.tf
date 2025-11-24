terraform {
  required_version = ">= 1.0"
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0"
    }
  }
}

resource "azurerm_postgresql_server" "main" {
  name                = var.server_name
  location            = var.location
  resource_group_name = var.resource_group_name
  
  sku_name = var.sku_name
  version  = var.postgresql_version
  
  storage_mb        = var.storage_mb
  backup_retention_days = var.backup_retention_days
  
  administrator_login          = var.admin_username
  administrator_login_password = var.admin_password
  
  ssl_enforcement_enabled = true
}

resource "azurerm_postgresql_database" "main" {
  name                = var.database_name
  resource_group_name = var.resource_group_name
  server_name         = azurerm_postgresql_server.main.name
  charset             = "UTF8"
  collation           = "English_United States.1252"
}
