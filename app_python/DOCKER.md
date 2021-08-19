# BEST PRACTICES
- Ephemeral - can be rebuilt without any configurations
- Right build context
- Right order for caching
- Use specific tag for base image version
- Decouple applications - dockerize only one app
- Add metadata labels
- Minimalistic image to reduce the attacks probability
- Minimal required base container
- Do not install unnecessary packages
- Use trusted base image
- Reduce the number of container layers by instructions combination
- Expose only ports which are needed
- No confidential data leaks
- Use COPY instead of ADD
- Dockerignore
- **hadolint** as Dockerfile linter
```
hadolint Dockerfile
```