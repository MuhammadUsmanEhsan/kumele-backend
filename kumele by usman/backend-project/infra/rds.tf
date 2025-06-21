resource "aws_db_instance" "postgres" {
  identifier        = "kumele-db"
  engine            = "postgres"
  instance_class    = "db.t3.micro"
  allocated_storage = 20
  username          = var.db_username
  password          = var.db_password
  skip_final_snapshot = true
  publicly_accessible = true
  vpc_security_group_ids = [aws_security_group.allow_all.id]
  db_subnet_group_name   = aws_db_subnet_group.rds.name
}

resource "aws_db_subnet_group" "rds" {
  name       = "rds-subnet-group"
  subnet_ids = [aws_subnet.public.id]
}
