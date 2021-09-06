## Role Name
deploy_image

## Author Information
Gorb Anna: a.gorb@innopolis.university

## How to use
```
devops/ansible$ ansible-playbook playbooks/app_python_deploy.yaml
```

## What this role will do?
- Remove all old containers and images
- Run docker-compose up
