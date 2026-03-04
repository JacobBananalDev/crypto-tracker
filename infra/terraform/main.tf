# ------------------------------------------------------------
# ECS Cluster
#
# This cluster will run our containerized services.
# ------------------------------------------------------------

resource "aws_ecs_cluster" "crypto_cluster" {

  name = "${var.project_name}-cluster"

}