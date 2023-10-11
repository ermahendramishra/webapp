# webapp
This repository contain a terraform code of a stateless application <br>
Clone the repo code <br>
configure the aws in terminal with aws access key and secret key <br>
configure the terraform in the terminal <br>
## Run the below commands <br>
# terraform init
# terraform validate
# terraform plan
# terraform apply

It will create a ec2 vm in aws in which it automatically install docker and pull the nginxdemos/hello image <br>
After that it will create a container of that image which will run on port 80 <br>
This terraform code also create a security group in which it allow port 80 and 443 <br>

