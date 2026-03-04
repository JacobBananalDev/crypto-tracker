# ------------------------------------------------------------
# Variables used throughout the infrastructure
# ------------------------------------------------------------

variable "aws_region" {
  description = "AWS region to deploy resources"
  default     = "us-east-1"
}

variable "project_name" {
  description = "Project name prefix"
  default     = "crypto-tracker"
}