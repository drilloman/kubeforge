# KubeForge

> Hands-on Kubernetes labs documenting my journey toward the **Certified Kubernetes Administrator (CKA)** certification.

---

# About

KubeForge is my personal Kubernetes learning project.

The goal is to learn Kubernetes by building practical, progressively more advanced labs instead of following isolated tutorials.

Each demo introduces new Kubernetes concepts while reinforcing previous knowledge, creating a structured learning path from Kubernetes fundamentals to production-oriented deployments.

---

# Objectives

* Learn Kubernetes through hands-on practice
* Build a public portfolio of Kubernetes projects
* Prepare for the **Certified Kubernetes Administrator (CKA)** certification
* Follow Infrastructure as Code (IaC) and Kubernetes best practices
* Document every project from design to deployment

---

# Learning Roadmap

## ✅ Demo 1 – Kubernetes Fundamentals

**Status:** Completed

### Topics Covered

* Namespace
* Deployment
* ReplicaSet
* Pods
* Service (NodePort)
* ConfigMap
* Secret
* Persistent Volume Claim (PVC)
* MariaDB
* Flask Application
* Scaling
* Self-Healing

---

## ✅ Demo 2 – Multi-Node Kubernetes Cluster

**Status:** Completed

### Topics Covered

* Built a 3-node MicroK8s cluster
* Configured a Control Plane and two Worker Nodes
* Deployed an internal container registry
* Distributed container images across the cluster
* Observed Kubernetes Pod scheduling
* Simulated worker node failures
* Performed real-world infrastructure troubleshooting
* Published complete project documentation

---

## 🔜 Planned Demos

* Demo 3 – Ingress Controller
* Demo 4 – Horizontal Pod Autoscaler (HPA)
* Demo 5 – Rolling Updates & Rollbacks
* Demo 6 – Helm
* Demo 7 – Monitoring
* Demo 8 – Production-Ready Application

---

# Repository Structure

```text
kubeforge/
│
├── demo1/
│   ├── app/
│   ├── namespace.yaml
│   ├── secret.yaml
│   ├── configmap.yaml
│   ├── mariadb-deployment.yaml
│   ├── mariadb-service.yaml
│   ├── mariadb-pvc.yaml
│   ├── web-deployment.yaml
│   ├── web-service.yaml
│   └── README.md
│
├── demo2/
│   ├── app/
│   ├── namespace.yaml
│   ├── secret.yaml
│   ├── configmap.yaml
│   ├── mariadb-deployment.yaml
│   ├── mariadb-service.yaml
│   ├── mariadb-pvc.yaml
│   ├── web-deployment.yaml
│   ├── web-service.yaml
│   └── README.md
│
├── demo3/
│
└── README.md
```

---

# Technologies

### Container Orchestration
- Kubernetes
- MicroK8s

### Containerization
- Docker
- Podman

### Application
- Python
- Flask
- MariaDB

### DevOps
- Git
- GitHub

### Operating System
- Linux

---

# Certification Goal

The ultimate goal of this project is to achieve the **Certified Kubernetes Administrator (CKA)** certification while developing practical skills applicable to real-world Kubernetes environments.

Each completed demo represents another milestone in that journey.

---

# License

This repository is intended for educational purposes and personal portfolio development.
