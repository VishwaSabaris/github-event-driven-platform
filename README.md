# GitHub Event-Driven Automation Platform

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Flask](https://img.shields.io/badge/Flask-Backend-black)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue)
![n8n](https://img.shields.io/badge/n8n-Workflow%20Automation-orange)
![GitHub Webhooks](https://img.shields.io/badge/GitHub-Webhooks-success)
![License](https://img.shields.io/badge/License-MIT-green)

---

## Project Overview

The GitHub Event-Driven Automation Platform is a real-time event processing system that captures GitHub repository activities using GitHub Webhooks, routes events through n8n automation workflows, applies business logic, and communicates with a Flask backend API for event processing.

The project demonstrates Event-Driven Architecture (EDA), REST APIs, Workflow Automation, Dockerized Services, Webhooks, and Backend Development.

---

## Problem Statement

Organizations often need to automate actions based on GitHub repository activities such as:

- Code Pushes
- Pull Requests
- Repository Updates
- Deployments
- Release Events

Monitoring these events manually is inefficient.

This platform automatically receives GitHub events, processes payloads, applies business rules, and forwards structured data to backend services for further automation.

---

## Key Features

- GitHub Webhook Integration
- Real-Time Event Processing
- Event-Driven Architecture (EDA)
- Workflow Automation with n8n
- Dockerized Automation Environment
- Flask Backend API
- JSON Payload Processing
- Conditional Event Routing
- GitHub Activity Monitoring
- REST API Communication
- Business Rule Classification
- Automated Event Validation

---

## Project Architecture

![Architecture Diagram](Architecture.png)

### High-Level Architecture

```text
GitHub Push Event
        │
        ▼
GitHub Webhook
        │
        ▼
ngrok Public URL
        │
        ▼
n8n Webhook Node
        │
        ▼
Code Node
        │
        ▼
IF Node
        │
        ▼
HTTP Request Node
        │
        ▼
Flask Backend API
        │
        ▼
JSON Response
```

---

## Workflow Diagram

![Workflow Diagram](Workflow.png)

---

## Technologies Used

### Programming

- Python

### Backend

- Flask

### Workflow Automation

- n8n

### Containerization

- Docker

### Networking

- ngrok

### Version Control

- Git
- GitHub

### Communication

- REST APIs
- Webhooks

### Data Format

- JSON

### Architecture

- Event-Driven Architecture (EDA)

---

# System Workflow

## Step 1

Developer pushes code to GitHub.

```bash
git push
```

---

## Step 2

GitHub automatically generates a webhook event.

---

## Step 3

Webhook payload is sent to the ngrok public URL.

Example:

```text
https://your-ngrok-url.ngrok-free.app/webhook/github-event
```

---

## Step 4

n8n receives the request through the Webhook Node.

---

## Step 5

The Code Node processes the payload.

Extracted Information:

- Repository Name
- Event Type
- Username
- Timestamp

---

## Step 6

Business Logic Classification

```python
if utc_hour >= 22:
    status = "Late Activity"
else:
    status = "Normal Activity"
```

---

## Step 7

IF Node evaluates workflow conditions.

Condition:

```python
status == "Late Activity"
```

---

## Step 8

Workflow Routing

### Late Activity

Forward to Flask Backend

### Normal Activity

Return Immediate Response

---

## Step 9

Flask Backend receives structured JSON data.

Endpoint:

```http
POST /webhook
```

---

## Step 10

Backend processes request and returns response.

---

# n8n Workflow Components

## Webhook Node

Purpose:

- Receive GitHub Events

Configuration:

```text
Method: POST
Path: github-event
```

---

## Code Node

Responsibilities:

- Extract Event Information
- Process Timestamp
- Classify Activity
- Generate Structured JSON

---

## IF Node

Responsibilities:

- Conditional Routing

Condition:

```text
status == Late Activity
```

---

## HTTP Request Node

Purpose:

Forward Processed Events to Flask API

```text
POST http://host.docker.internal:5000/webhook
```

---

## Respond to Webhook Node

Purpose:

Return workflow response.

---

# Backend Architecture

## Flask API

Main File:

```text
webhook_server.py
```

Responsibilities:

- Receive Payloads
- Validate Requests
- Process Events
- Generate Responses
- Log Activities

---

# API Documentation

## POST /webhook

### Request

```json
{
  "event": "push",
  "repo": "github-event-driven-platform",
  "time": "2026-05-04T23:45:00Z"
}
```

### Response

```json
{
  "success": true,
  "message": "Webhook processed successfully"
}
```

---

# Project Structure

```text
github-event-driven-platform/

├── webhook_server.py
├── requirements.txt
├── .gitignore
├── Architecture.png
├── Workflow.png
│
├── services/
│   ├── __init__.py
│   └── api_service.py
│
├── utils/
│   ├── __init__.py
│   └── processor.py
│
└── README.md
```

---

# File Descriptions

## webhook_server.py

Main Flask Backend Server

Responsibilities:

- API Execution
- Payload Validation
- Event Processing
- Response Generation

---

## services/api_service.py

Contains:

- Validation Logic
- Service Layer Functions

---

## utils/processor.py

Contains:

- Event Processing Logic
- Timestamp Processing
- Activity Classification
- Event Transformation

---

## requirements.txt

Project Dependencies

```text
Flask
python-dotenv
```

---

## .gitignore

Ignored Files

```text
venv/
__pycache__/
.env
```

---

# Installation Guide

## Clone Repository

```bash
git clone https://github.com/VishwaSabaris/github-event-driven-platform.git
```

```bash
cd github-event-driven-platform
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

Activate:

Linux

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Flask Server

```bash
python webhook_server.py
```

Server:

```text
http://localhost:5000
```

---

# Docker + n8n Setup

Run n8n Container

```bash
docker run -it --rm \
-p 5678:5678 \
n8nio/n8n
```

Access:

```text
http://localhost:5678
```

---

# Screenshots

## Architecture Diagram

![Architecture](Architecture.png)

---

## Workflow Diagram

![Workflow](Workflow.png)

---

# Features Implemented

- GitHub Webhook Listener
- Event Processing Pipeline
- Conditional Workflow Routing
- Flask Backend Integration
- Real-Time Automation
- JSON Payload Processing
- Business Logic Classification
- REST API Communication
- Dockerized Workflow Execution

---

# Challenges Faced

## Webhook Not Triggering

Cause:

Workflow inactive.

Solution:

Activate workflow.

---

## Docker Networking Issue

Cause:

Container could not access Flask API.

Solution:

```text
host.docker.internal
```

---

## Invalid JSON Payload

Cause:

Improper body configuration.

Solution:

Enable JSON request body.

---

## GitHub Authentication Failure

Cause:

Password authentication removed.

Solution:

Use GitHub Personal Access Token.

---

# Skills Demonstrated

- Event-Driven Architecture
- Workflow Automation
- Python Development
- Flask APIs
- REST API Design
- Docker
- GitHub Webhooks
- JSON Processing
- Backend Development
- API Integration
- Automation Engineering
- GitHub Integration

---

# Learning Outcomes

Through this project I learned:

- Event-Driven Architecture
- GitHub Webhooks
- REST APIs
- Flask Development
- Docker Networking
- Workflow Automation
- API Communication
- JSON Processing
- Backend Integration
- Request-Response Lifecycle
- Event Classification Systems

---

# Resume Description

Built a real-time GitHub Event-Driven Automation Platform using GitHub Webhooks, n8n, Docker, ngrok, and Flask APIs to automate repository event monitoring, process webhook payloads, implement conditional workflow execution, and integrate backend event processing using Event-Driven Architecture principles.

---

# Future Enhancements

## Phase 2

- PostgreSQL Integration
- Event Storage Layer

## Phase 3

- Email Notifications

## Phase 4

- Dockerized Flask Backend

## Phase 5

- Kubernetes Deployment

## Phase 6

- Terraform Infrastructure Provisioning

## Phase 7

- API Key Authentication
- Bearer Token Authentication
- Role-Based Access Control

---

# Author

**Vishwa Sabaris V**

AI | Cloud | DevOps Engineer

GitHub:
https://github.com/VishwaSabaris

LinkedIn:
https://www.linkedin.com/in/vishwa-sabaris-aa487837b/

---

## License

This project is licensed under the MIT License.
