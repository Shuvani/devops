# GitHub Actions CI best practices
- Minimal
- No unnecessary dependencies
- Use of caching mechanism
- Environment variables are limited to the narrowest possible scope
- No hardcoded secrets
- Automatic detection of the project version  
- Don’t use self-hosted runners in a public repository  
  
# Jenkins best practices
- Don’t use older plugins for pipeline build
- Pipeline was developed as code
- All work is done within a logical stages
- Do not use input within a node (I did not use it at all)
- Wrap input in a timeout (I did not use it at all)
- Don't use env global variable
- Stash files instead of archiving (I do not use it at all)