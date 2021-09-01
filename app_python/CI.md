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
- Use declarative syntax  
- All work is done within a logical stages
- Use parallel steps  
- Do not use input within a node (I did not use it at all)
- Wrap input in a timeout (I did not use it at all)
- Don't use env global variable
- Stash files instead of archiving (I do not use it at all)
- Use single steps
- No complex Groovy code
- No repetition of similar steps
- No shared libraries
- No large global variable declaration files
- Store the job definition within GitHub
- Do all work within an agent

# How to configure Jenkins
```
docker run -p 8080:8080 --user root -v /var/run/docker.sock:/var/run/docker.sock jenkinsci/blueocean
```

- open http://localhost:8080 and enter the password from the console
- Choose Docker, Docker pipeline and Workspace Cleanup Plugin
- Configure credentials (login and password) with id DockerHub
- Create the Jenkins Job: New item -> Multibranch Pipeline -> Branch Sources -> Add source -> GitHub -> ->
repository HTTPS URL -> Save
