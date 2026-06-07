resource "tls_private_key" "my_private_key" {
  algorithm = "RSA"
  rsa_bits  = 4096
}

resource "aws_key_pair" "task_manager_key" {
  key_name   = "task_manager"
  public_key = tls_private_key.my_private_key.public_key_openssh
}

resource "local_file" "pem_file" {
  filename        = "${path.module}/task_manager.pem"
  content         = tls_private_key.my_private_key.private_key_pem
  file_permission = "0400"
}