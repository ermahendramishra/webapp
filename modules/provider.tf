terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~>5.0.0"

    }
  }
}

# For the production we will use s3 as a backend to store the terraform state file