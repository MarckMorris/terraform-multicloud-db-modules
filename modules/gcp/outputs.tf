output "instance_name" {
  description = "Instance name"
  value       = google_sql_database_instance.main.name
}

output "connection_name" {
  description = "Connection name"
  value       = google_sql_database_instance.main.connection_name
}

output "public_ip" {
  description = "Public IP"
  value       = google_sql_database_instance.main.public_ip_address
}
