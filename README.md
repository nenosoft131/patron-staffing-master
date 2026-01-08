**Patron Staffing API**
A modern, scalable backend for Patron Staffing Solutions — enabling role-based user management, secure document uploads, and candidate profile building for staffing, recruitment, and HR compliance.

✨ **Features**
✅ Role-Based User Management: admin, client, candidate, staff
✅ Secure Authentication: BCrypt password hashing, email uniqueness
✅ Document Gateway: Upload resumes, certifications, IDs with type categorization
✅ Candidate Profiles: Build skillset profiles linked to documents
✅ Cloud-Ready Storage: S3/MinIO integration with signed URLs
✅ Clean Architecture: Domain-Driven Design with low coupling
✅ Async-First: Fully asynchronous I/O with SQLAlchemy 2.0 + asyncpg
✅ Mobile & Web Ready: Consistent RESTful APIs with OpenAPI docs
✅ Compliance-Ready: GDPR-compliant deletion, audit trails

🏗️ **Architecture**

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

🔑 **Principles**
Domain is pure — no FastAPI, SQLAlchemy, or cloud SDKs
Adapters implement interfaces — swap DB/cloud without touching business logic
Request-scoped sessions — safe async DB access
Immutable domain models — thread-safe, testable entities

🛠️ **Quick Start**
Python 3.10+
PostgreSQL 12+ (or SQLite for dev)
Docker (optional for MinIO)

1.  **Clone & Install**
    git clone https://github.com/your-org/patron-staffing-api.git
    cd patron-staffing-api
    python -m venv venv
    source venv/bin/activate # Linux/macOS # .\venv\Scripts\activate # Windows
    pip install -r requirements.txt

2.  **Configure Environment**
    cp .env.example .env # Edit .env: # DATABASE_URL=postgresql+asyncpg://user:pass@localhost:5432/patron_dev # MINIO_ENDPOINT=http://localhost:9000 # MINIO_ACCESS_KEY=patron # MINIO_SECRET_KEY=supersecret

3.  Start Services (Optional)

    # Start PostgreSQL + MinIO via Docker

        docker-compose up -d

4.  **Run the API**
    uvicorn main:app --reload --port 8000

🗺️ **Roadmap**
Version Features
v1.0 ✅ User management, document upload, candidate profiles
v1.1 🔐 JWT auth, password reset, email verification
v1.2 📱 Mobile sync, offline support, push notifications
v1.3 🤖 AI resume parsing → auto-skill extraction
v1.4 📊 Client portal: job postings, candidate matching
v1.5 🌐 Multi-tenant support (enterprise clients)
