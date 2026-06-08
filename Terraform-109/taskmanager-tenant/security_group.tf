resource "aws_security_group" "my_taskmanager_sg" {
  name   = "My-Taskmanger-Sg"
  vpc_id = aws_vpc.my_taskmanager_vpc.id

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port = 0
    to_port = 0
    protocol = "-1"
    cidr_blocks = [ "0.0.0.0/0" ]
  }
}