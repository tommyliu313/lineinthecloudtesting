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