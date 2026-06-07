---
layout: post
title: Getting Started with Kubernetes
date: 2026-05-28 16:45:00 +0530
categories: [devops, cloud]
tags: [kubernetes, k8s, containerization, orchestration]
image:
  path: /N-Infinity-no-bg.png
  alt: Kubernetes
---

# Getting Started with Kubernetes

Kubernetes (K8s) can seem overwhelming at first, but understanding the basics makes it much more approachable. Let's break it down.

## What is Kubernetes?

Kubernetes is an open-source orchestration platform for automating deployment, scaling, and management of containerized applications.

Think of it as a **smart container manager** that:
- Deploys containers across a cluster
- Handles scaling up/down automatically
- Restarts failed containers
- Manages networking and storage
- Enables rolling updates

## Core Concepts

### 1. Pod
The smallest deployable unit - usually one container, sometimes multiple.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-app
spec:
  containers:
  - name: app
    image: myapp:1.0
    ports:
    - containerPort: 8000
```

### 2. Deployment
Manages replicas of pods and rolling updates.

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: my-app
  template:
    metadata:
      labels:
        app: my-app
    spec:
      containers:
      - name: app
        image: myapp:1.0
        ports:
        - containerPort: 8000
```

### 3. Service
Exposes pods internally or externally.

```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-app-service
spec:
  selector:
    app: my-app
  type: LoadBalancer
  ports:
  - protocol: TCP
    port: 80
    targetPort: 8000
```

### 4. ConfigMap & Secrets
Manage configuration and sensitive data.

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  LOG_LEVEL: "debug"
  DATABASE_HOST: "db.example.com"
---
apiVersion: v1
kind: Secret
metadata:
  name: db-credentials
type: Opaque
data:
  password: ZGJwYXNzd29yZA==  # base64 encoded
```

## Why Kubernetes?

✅ **Auto-scaling** - Automatically scale based on load  
✅ **Self-healing** - Restart failed containers  
✅ **Rolling updates** - Zero-downtime deployments  
✅ **Service discovery** - Automatic DNS  
✅ **Load balancing** - Built-in load balancing  
✅ **Resource management** - Efficient resource utilization  

## Getting Started

### 1. Install kubectl
```bash
# macOS
brew install kubectl

# Linux
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
```

### 2. Set Up a Local Cluster
```bash
# Docker Desktop (easiest)
# Enable Kubernetes in Docker Desktop settings

# Or use Minikube
brew install minikube
minikube start
```

### 3. Deploy Your First App
```bash
kubectl create deployment my-app --image=nginx:latest
kubectl expose deployment my-app --port=80 --type=LoadBalancer
kubectl get pods
kubectl get services
```

## Common kubectl Commands

```bash
# View resources
kubectl get pods
kubectl get deployments
kubectl get services

# Describe resources
kubectl describe pod <pod-name>

# View logs
kubectl logs <pod-name>

# Port forwarding
kubectl port-forward pod/<pod-name> 8000:8000

# Execute command in pod
kubectl exec -it <pod-name> -- /bin/sh

# Apply configuration
kubectl apply -f deployment.yaml

# Delete resources
kubectl delete pod <pod-name>
```

## Next Steps

1. **Learn YAML** - Kubernetes uses YAML for configuration
2. **Understand namespaces** - Logical clusters within K8s
3. **Explore Helm** - Package manager for Kubernetes
4. **Study networking** - How pods communicate
5. **Master volumes** - Persistent data storage

## Resources

- [Kubernetes Official Docs](https://kubernetes.io/docs/)
- [kubectl Cheat Sheet](https://kubernetes.io/docs/reference/kubectl/cheatsheet/)
- [Play with Kubernetes](https://labs.play-with-k8s.com/)

---

**Start Small:** Begin with simple deployments locally. Complexity builds naturally as your needs grow.
