variable "server_name" {
  description = "PostgreSQL server name"
  type        = string
}

variable "location" {
  description = "Azure region"
  type        = string
  default     = "eastus"
}

variable "resource_group_name" {
  description = "Resource group name"
  type        = string
}

variable "sku_name" {
  description = "SKU name"
  type        = string
  default     = "B_Gen5_1"
}

variable "postgresql_version" {
  description = "PostgreSQL version"
  type        = string
  default     = "11"
}

variable "storage_mb" {
  description = "Storage in MB"
  type        = number
  default     = 5120
}

variable "backup_retention_days" {
  description = "Backup retention days"
  type        = number
  default     = 7
}

variable "database_name" {
  description = "Database name"
  type        = string
}

variable "admin_username" {
  description = "Admin username"
  type        = string
  default     = "psqladmin"
}

variable "admin_password" {
  description = "Admin password"
  type        = string
  sensitive   = true
}
