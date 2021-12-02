#Variables

variable "aws_access_key" {}
variable "aws_secret_key" {}
variable "aws-region"{
    default = ""
}

#Provider
provider "aws"{
  access_key = "var.access_key"
  secret_key = "var.secret_key"
  region = "var.aws_region"

}

# NETWORKING #
resource "aws_vpc" {
  cidr_block = ""
  enable_dns_hostnames = "true"
}

#Resource
resource "aws_instance"{
 ami = nonsensitive(data.aws_ssm_)

}

# CONFIG #
resource "aws_iam_role" ""{
 name = "${var.bucket_name}"
 assume_role_policy = <<EOF
 {
   
 }

}