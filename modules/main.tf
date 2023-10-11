
module "web-application" {
  source        = "./web-app"
  instance_type = var.instance_type
  ami           = var.ami
}