# Patron Staffing API

![Python](https://img.shields.io/badge/python-3.10+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Production-green)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

A **modern, scalable backend** for Patron Staffing Solutions — enabling **role-based user management**, **secure document uploads**, and **candidate profile building** for staffing, recruitment, and HR compliance.

Built with **FastAPI**, **async SQLAlchemy**, and cloud-ready storage for high performance and scalability.

---

## ✨ Features

- **Role-Based User Management**: Supports `admin`, `client`, `candidate`, and `staff` roles.
- **Secure Authentication**: BCrypt password hashing with email uniqueness.
- **Document Gateway**: Upload resumes, certifications, and IDs with type categorization.
- **Candidate Profiles**: Build skillset profiles linked to uploaded documents.
- **Cloud-Ready Storage**: S3/MinIO integration with signed URLs for secure access.
- **Clean Architecture**: Domain-Driven Design (DDD) with low coupling.
- **Async-First**: Fully asynchronous I/O using SQLAlchemy 2.0 + asyncpg.
- **Mobile & Web Ready**: Consistent RESTful APIs with OpenAPI documentation.
- **Compliance-Ready**: GDPR-compliant deletion and audit trails.

---

## 🏗️ Architecture

patron-staffing-api/
├── app/ # 🧠 Core domain & use cases
│ ├── domain/ # Pure business entities (no framework deps)
│ ├── use_cases/ # Application workflows
│ └── interfaces/ # Abstract ports (interfaces)
├── adapters/ # 🔌 Infrastructure adapters
│ ├── api/ # FastAPI routers, schemas, dependencies
│ ├── database/ # SQLAlchemy models, repositories
│ ├── storage/ # File storage (S3, MinIO)
│ └── auth/ # Password hashing, JWT (future)
├── config/ # Settings, DB config
├── scripts/ # DB init, utilities
├── tests/ # Unit, integration, e2e tests
├── main.py # App factory
└── requirements.txt

### 🔑 Design Principles

- **Pure Domain**: Business logic is framework-independent (no FastAPI, SQLAlchemy, or cloud SDK dependencies).
- **Adapters Implement Interfaces**: Easily swap databases or cloud providers without touching business logic.
- **Request-Scoped Sessions**: Safe async DB access for concurrency.
- **Immutable Domain Models**: Thread-safe and testable entities.

---

## 🛠️ Quick Start

### Requirements

- Python 3.10+
- PostgreSQL 12+ (or SQLite for development)
- Docker (optional, for MinIO)

### Installation

    bash
    git clone https://github.com/nenosoft131/patron-staffing-api.git
    cd patron-staffing-api
    python -m venv venv
    source venv/bin/activate  # Linux/macOS
    # .\venv\Scripts\activate # Windows
    pip install -r requirements.txt

### Configuration

    cp .env.example .env
    # Edit .env:
    # DATABASE_URL=postgresql+asyncpg://user:pass@localhost:5432/patron_dev
    # MINIO_ENDPOINT=http://localhost:9000
    # MINIO_ACCESS_KEY=patron
    # MINIO_SECRET_KEY=supersecret

### Running the API

    uvicorn main:app --reload --port 8000

### 📈 Roadmap

Version Features
v1.0 ✅ User management, document upload, candidate profiles
v1.1 🔐 JWT auth, password reset, email verification
v1.2 📱 Mobile sync, offline support, push notifications
v1.3 🤖 AI resume parsing → auto-skill extraction
v1.4 📊 Client portal: job postings, candidate matching
v1.5 🌐 Multi-tenant support (enterprise clients)
