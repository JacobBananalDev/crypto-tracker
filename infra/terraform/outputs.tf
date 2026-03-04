# ------------------------------------------------------------
# Terraform outputs
# ------------------------------------------------------------

output "ecs_cluster_name" {

  value = aws_ecs_cluster.crypto_cluster.name

}