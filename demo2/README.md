# KubeForge Demo 2 – Multi-Node Kubernetes Cluster

## Overview

This demo extends the single-node environment created in Demo 1 into a fully functional three-node Kubernetes cluster using MicroK8s.

The goal is to understand how Kubernetes behaves in a distributed environment by deploying the same application across multiple nodes, introducing an internal container registry, and observing scheduling, scaling and self-healing mechanisms.

---

## Objectives

By completing this demo I learned how to:

- Build a multi-node Kubernetes cluster
- Join worker nodes to a control plane
- Configure an internal container registry
- Build and distribute container images across the cluster
- Deploy workloads on multiple nodes
- Observe Kubernetes scheduling decisions
- Scale applications across the cluster
- Test self-healing capabilities
- Simulate node failures

---

## Cluster Architecture

```
                    +----------------------+
                    |     Client Browser   |
                    +----------+-----------+
                               |
                               |
                         NodePort Service
                               |
                   +-----------+-----------+
                   |           |           |
             Flask Pod    Flask Pod    Flask Pod
           kubeforge-cp kubeforge-w1 kubeforge-w2
                   |           |           |
                   +-----------+-----------+
                               |
                       ClusterIP Service
                               |
                         MariaDB Pod
                               |
                    Persistent Volume Claim
```

---

## Cluster Nodes

| Hostname | Role | IP Address |
|----------|------|------------|
| kubeforge-cp | Control Plane | 10.0.0.51 |
| kubeforge-w1 | Worker Node | 10.0.0.52 |
| kubeforge-w2 | Worker Node | 10.0.0.53 |

---

## Environment

### Hypervisor

- VMware ESXi 8

### Operating System

- Ubuntu Server 24.04 LTS

### Kubernetes

- MicroK8s

### Networking

- Calico CNI

### Storage

- HostPath Storage

### Container Runtime

- containerd

### Container Registry

- MicroK8s Registry

### Image Builder

- Podman

---

## Installation

### Install MicroK8s

```bash
sudo snap install microk8s --classic
```

Configure the current user:

```bash
sudo usermod -aG microk8s $USER
newgrp microk8s

mkdir -p ~/.kube
sudo chown -R $USER ~/.kube
```

---

### Create the Cluster

On the Control Plane:

```bash
microk8s add-node
```

Run the generated join command on each Worker Node.

Verify:

```bash
kubectl get nodes -o wide
```

---

### Enable Required Add-ons

```bash
microk8s enable dns
microk8s enable hostpath-storage
microk8s enable registry
```

---

### Build and Push the Image

```bash
cd app

podman build -t localhost:32000/demo2-flask:1.0 .

podman push --tls-verify=false localhost:32000/demo2-flask:1.0
```

---

### Deploy

```bash
kubectl apply -f .
```

Verify:

```bash
kubectl get pods -n demo2 -o wide
kubectl get svc -n demo2
```

---

## Kubernetes Concepts

- Multi-Node Cluster
- Control Plane
- Worker Nodes
- Scheduler
- Cluster Networking
- Internal Registry
- Deployments
- ReplicaSets
- Pods
- Services
- ConfigMaps
- Secrets
- Persistent Volumes
- Scaling
- Self-Healing

---

## Validation

The following scenarios were successfully tested:

- Multi-node cluster creation
- Worker node registration
- Internal registry deployment
- Container image distribution
- Application deployment
- Pod scheduling across multiple nodes
- Horizontal scaling
- Pod self-healing
- Worker node failure simulation

---

## Lessons Learned

Moving from a single-node cluster to a multi-node environment introduces several new challenges.

Key lessons learned during this demo include:

- Local container images are not shared between nodes.
- An internal registry is required to distribute images.
- Kubernetes automatically schedules Pods across available nodes.
- Node failures do not immediately trigger Pod recreation.
- Storage becomes significantly more important in a distributed environment.

---

## Next Steps

The next demo will focus on production-oriented Kubernetes features such as shared storage, ingress, advanced scheduling and high availability.