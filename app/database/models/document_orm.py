# adapters/database/models/document.py
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func, Index
# from sqlalchemy.dialects.postgresql import JSONB #PostgreSQL 
from sqlalchemy import JSON 
from app.database.models.base import Base
from uuid import uuid4

class DocumentORM(Base):
    __tablename__ = "documents"

    id = Column(String, primary_key=True, default=lambda: f"doc_{uuid4().hex}")  # e.g., "doc_a1b2c3"
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)           # ← links to user
    document_type = Column(String, nullable=False, index=True)                  # e.g., "resume"
    filename = Column(String, nullable=False)                                   # e.g., "john_resume.pdf"
    file_path = Column(String, nullable=False)                                  # e.g., "candidates/123/resume_abc.pdf"
    file_url = Column(String, nullable=False)                                   # signed URL (temp access)
    content_type = Column(String, nullable=False)                               # e.g., "application/pdf"
    size_bytes = Column(Integer, nullable=False)
    metadata_ = Column("metadata", JSON, default={})                           # extensible: parsed text, pages, etc.
    uploaded_at = Column(DateTime(timezone=True), server_default=func.now())

    # Critical indexes for performance
    __table_args__ = (
        Index('idx_docs_user_type', 'user_id', 'document_type'),  # ← FAST: get user's resumes
        Index('idx_docs_user', 'user_id'),                        # get all docs for user
        Index('idx_docs_type', 'document_type'),                  # get all resumes (admin)
    )