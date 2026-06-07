---
layout: post
title: Docker Best Practices for Production
date: 2026-06-03 14:20:00 +0530
categories: [devops]
tags: [docker, containerization, production, best-practices]
---

# Docker Best Practices for Production

Docker is powerful, but using it incorrectly can lead to security vulnerabilities, performance issues, and operational nightmares. Here are battle-tested best practices.

## 1. Use Specific Base Image Tags

**Bad:**
```dockerfile
FROM python:latest
FROM ubuntu:latest
```

**Good:**
```dockerfile
FROM python:3.11-slim
FROM ubuntu:22.04
```

The `latest` tag is unpredictable and can break builds unexpectedly.

## 2. Minimize Image Size

**Use Multi-Stage Builds:**
```dockerfile
FROM python:3.11 AS builder
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

FROM python:3.11-slim
COPY --from=builder /app /app
WORKDIR /app
CMD ["python", "app.py"]
```

This reduces image size significantly by excluding build dependencies.

## 3. Security Considerations

```dockerfile
# Run as non-root user
RUN useradd -m appuser
USER appuser

# Don't run as root
# Don't include secrets in images
# Scan images for vulnerabilities
```

## 4. Optimize Layers

- Order dockerfile commands from least to most frequently changed
- Combine RUN commands to reduce layers
- Leverage build cache effectively

**Good Practice:**
```dockerfile
FROM python:3.11-slim

# Install dependencies first (rarely changes)
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements (changes less often)
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy source code (changes frequently)
COPY . .

CMD ["python", "app.py"]
```

## 5. Health Checks

```dockerfile
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:8000/health || exit 1
```

## 6. Resource Limits

Always set resource limits in orchestration:
```yaml
resources:
  limits:
    memory: "512Mi"
    cpu: "500m"
  requests:
    memory: "256Mi"
    cpu: "250m"
```

## Key Takeaways

1. ✅ Use specific, verified base images
2. ✅ Minimize image size with multi-stage builds
3. ✅ Never run as root
4. ✅ Keep secrets out of images
5. ✅ Implement health checks
6. ✅ Set resource limits
7. ✅ Scan for vulnerabilities regularly

---

**Pro Tip:** Use tools like `trivy` or `grype` to scan your Docker images for known vulnerabilities before pushing to production.
