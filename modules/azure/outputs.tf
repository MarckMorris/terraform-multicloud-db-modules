output "server_id" {
  description = "Server ID"
  value       = azurerm_postgresql_server.main.id
}

output "server_fqdn" {
  description = "Server FQDN"
  value       = azurerm_postgresql_server.main.fqdn
}

output "database_id" {
  description = "Database ID"
  value       = azurerm_postgresql_database.main.id
}
