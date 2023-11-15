# Sources:
# For general setup: https://developer.hashicorp.com/terraform/tutorials/aws-get-started/aws-build
# For private key generation: https://stackoverflow.com/questions/49743220/how-to-create-an-ssh-key-in-terraform
# For variables: https://developer.hashicorp.com/terraform/language/values/variables

terraform {
  backend "local" { path = "/opt/selinux-training-tf/.terraform.tfstate" }
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }

  required_version = ">= 1.2.0"
}

provider "aws" {
  region = "eu-west-1"
}

variable "instance_count" {
  type        = number
  description = "The count of instance to create."

  validation {
    condition     = var.instance_count > 0 && var.instance_count < 10
    error_message = "The instance_count value must be between 1 and 9."
  }
}

variable "block_egress" {
  type        = bool
  description = "Decides if egress from instances should be allowed or not."
}

# Generate a new private key
resource "tls_private_key" "example" {
  algorithm = "RSA"
  rsa_bits  = 4096
}

# Generate an AWS key pair
resource "aws_key_pair" "generated_key" {
  key_name   = "private-key"
  public_key = tls_private_key.example.public_key_openssh
}

resource "aws_security_group" "allow_ssh" {
  name        = "allow_ssh"
  description = "Allow SSH inbound traffic"

  tags = {
    Name = "allow_ssh"
  }
}

resource "aws_security_group_rule" "ssh_ingress" {
  type              = "ingress"
  description      = "Allow SSH inbound traffic"
  from_port        = 22
  to_port          = 22
  protocol         = "tcp"
  cidr_blocks      = ["0.0.0.0/0"]
  ipv6_cidr_blocks = ["::/0"]
  security_group_id = "${aws_security_group.allow_ssh.id}"
}

resource "aws_security_group_rule" "allow_all_outbound" {
  count = (var.block_egress) ? 0 : 1
  type              = "egress"
  description      = "Allow all outbound"
  from_port        = 0
  to_port          = 0
  protocol         = "-1"
  cidr_blocks      = ["0.0.0.0/0"]
  ipv6_cidr_blocks = ["::/0"]
  security_group_id = "${aws_security_group.allow_ssh.id}"
}

resource "aws_instance" "selinux" {
  ami           = "ami-0f2cb8c8044faf2da"
  instance_type = "t2.micro"
  key_name      = aws_key_pair.generated_key.key_name
  vpc_security_group_ids = [aws_security_group.allow_ssh.id]
  count = var.instance_count

  tags = {
    Name = "selinux"
  }
}

output "private_key" {
  value     = tls_private_key.example.private_key_pem
  sensitive = true
}
