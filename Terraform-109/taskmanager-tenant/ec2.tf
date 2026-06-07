resource "aws_instance" "my_taskmanager_ec2" {
  ami = "ami-091138d0f0d41ff90"
  instance_type = "t3.micro"
  subnet_id = aws_subnet.public_subnet.id
  key_name = aws_key_pair.task_manager_key.key_name

  vpc_security_group_ids = [aws_security_group.my_taskmanager_sg.id]
  
  tags = {Name="Task-Manager-Server"}
}