output "instance_type_public_ip" {
  value = aws_instance.my_taskmanager_ec2.public_ip
}

output "ssh_command" {
  value = "ssh -i task_manager.pem ubuntu@${aws_instance.my_taskmanager_ec2.public_ip}"
}