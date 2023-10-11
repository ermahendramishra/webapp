resource "aws_instance" "web" {
  ami                    = var.ami
  instance_type          = var.instance_type
  vpc_security_group_ids = [aws_security_group.http.id]

  user_data =<<-EOF
  #!/bin/bash
  sudo apt-get update -y
  sudo apt-get install docker.io -y
  sudo docker run -itd -p 80:80 nginxdemos/hello
  EOF
}