resource "aws_vpc" "my_taskmanager_vpc" {
  cidr_block = "10.0.0.0/16"

  tags = { Name = "My-TaskManager-VPC" }
}