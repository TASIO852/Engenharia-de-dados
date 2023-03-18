variable "amis" {
  type = map(any)

  default = {
    "us-east-1" = "ami-02f3f602d23f1659d"
    "us-east-2" = "ami-05502a22127df2492"
  }
}

variable "cdirs_remote_acess" {
  type = list(any)

  default = ["138.99.35.7/32", "138.99.35.7/32"]
}

variable "key_name" {
  type = string

  default = "terraform-aws"
}
