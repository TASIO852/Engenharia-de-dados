resource "aws_security_group" "acesso_ssh" {
  name        = "acesso_ssh"
  description = "acesso_ssh"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = var.cdirs_remote_acess
  }

  tags = {
    Name = "ssh"
  }
}

# Security aws_security_group de outra regiao
resource "aws_security_group" "acesso_ssh_us_east_2" {
  provider    = aws.us-east-2
  name        = "acesso_ssh"
  description = "acesso_ssh"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = var.cdirs_remote_acess
  }

  tags = {
    Name = "ssh"
  }
}
