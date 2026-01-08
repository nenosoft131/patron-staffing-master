from dataclasses import dataclass
from enum import Enum
from typing import Literal

EntityKind = Literal["candidate", "client", "admin", "vendor"]

@dataclass(frozen=True)
class Document:
    id: str                  # UUID
    entity_id: int           # ID of owner (e.g., user ID)
    entity_type: EntityKind  # "candidate", "client", etc.
    filename: str
    file_url: str            # signed URL (S3/MinIO)
    doc_type: str            # "resume", "work_permit", "business_license", etc.
    uploaded_by: int         # user_id (for audit)