# Terraform best practices
- Use a Workspace
- One workspace for each environment
- Name workspace with component and environment
- Validate and format terraform code
- Give minimum AWS permissions necessary for a Terraform run

### How to set up
```
aws configure
mkdir terraform
cd terraform
terraform workspace new moscow_time
touch main.tf
terraform init
terraform fmt
terraform validate
terraform apply
terraform destroy
```

### Useful commands
```
terraform workspace show
terraform workspace list
terraform workspace new (name)
terraform workspace select
terraform workspace delete
```