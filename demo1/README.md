# Demo 1 – Kubernetes Fundamentals

## Overview

This project demonstrates the deployment of a simple web application on a Kubernetes cluster using MicroK8s.

The objective is to understand the core Kubernetes resources by deploying a Flask application connected to a MariaDB database while following common Kubernetes best practices.

---

## Prerequisites

- Ubuntu Server
- MicroK8s
- kubectl
- Docker image already available on the cluster

---

## Objectives

By completing this demo you I learned how to:

* Create and manage a Namespace
* Deploy applications using Deployments
* Understand the relationship between Deployments, ReplicaSets and Pods
* Expose applications through a Service
* Store configuration using ConfigMaps
* Protect sensitive information using Secrets
* Persist data using a Persistent Volume Claim (PVC)
* Scale an application
* Observe Kubernetes self-healing capabilities

---

## Architecture

```text
                +----------------------+
                |     Client Browser   |
                +----------+-----------+
                           |
                           |
                     NodePort Service
                           |
                +----------v-----------+
                |      Flask Pods      |
                |      Deployment      |
                +----------+-----------+
                           |
                    ClusterIP Service
                           |
                +----------v-----------+
                |       MariaDB        |
                |      Deployment      |
                +----------+-----------+
                           |
                           |
                  Persistent Volume Claim
```

---

## Project Structure

```text
demo1/
│
├── app/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── namespace.yaml
├── configmap.yaml
├── secret.yaml
├── mariadb-pvc.yaml
├── mariadb-deployment.yaml
├── mariadb-service.yaml
├── web-deployment.yaml
└── web-service.yaml
```

---

## Kubernetes Resources

| Resource   | Purpose                                 |
| ---------- | --------------------------------------- |
| Namespace  | Isolates the demo environment           |
| Deployment | Maintains the desired application state |
| ReplicaSet | Ensures the requested number of Pods    |
| Pod        | Runs the application containers         |
| Service    | Provides network access                 |
| ConfigMap  | Stores application configuration        |
| Secret     | Stores sensitive credentials            |
| PVC        | Persists MariaDB data                   |

---

## Deploy

Create all Kubernetes resources:

```bash
kubectl apply -f .
```

Verify resources:

```bash
kubectl get all -n demo1
```

---

## Demonstrations

### Scaling

Increase the number of web application replicas:

```bash
kubectl scale deployment web --replicas=3 -n demo1
```

Verify:

```bash
kubectl get pods -n demo1
```

---

### Self-Healing

Delete one running Pod:

```bash
kubectl delete pod <pod-name> -n demo1
```

Kubernetes automatically creates a replacement Pod.

---

### ConfigMap

Modify the ConfigMap and restart the Deployment to apply the new configuration.

---

### Secret

Database credentials are injected into the application through Kubernetes Secrets instead of being hardcoded.

---

### Persistent Storage

MariaDB data is stored inside a Persistent Volume Claim so that it survives Pod recreation.

---

## Cleanup

Delete all project resources:

```bash
kubectl delete namespace demo1
```

---

## Lessons Learned

This demo provides a practical introduction to the most important Kubernetes objects and demonstrates how they work together to deploy and maintain an application in a Kubernetes cluster.
