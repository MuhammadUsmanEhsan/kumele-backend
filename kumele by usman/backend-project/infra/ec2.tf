resource "aws_instance" "fastapi" {
  ami                    = "ami-0c2b8ca1dad447f8a" # Ubuntu 22.04 LTS in us-east-1
  instance_type          = var.instance_type
  key_name               = var.key_name
  subnet_id              = aws_subnet.public.id
  vpc_security_group_ids = [aws_security_group.allow_all.id]

  tags = {
    Name = "FastAPI-App"
  }

  user_data = <<-EOF
              #!/bin/bash
              apt update -y
              apt install python3-pip -y
              pip3 install fastapi uvicorn[standard] psycopg2 redis python-dotenv
              echo "APP RUNNER TO BE DEPLOYED HERE (docker/systemd)"
              EOF
}
