# app/use_cases/upload_document.py
from typing import Any
from fastapi import UploadFile
from app.database.models.document_orm import DocumentORM
from uuid import uuid4
from app.interfaces.file_storage import IFileStorage  # ← interface
from app.interfaces.document_repository import IDocumentRepository  # ← interface

class UploadDocument:
    def __init__(
        self,
        file_storage: IFileStorage,
        doc_repo: IDocumentRepository
    ):
        self.file_storage = file_storage
        self.doc_repo = doc_repo

    async def execute(self, user_id: int, document_type: str, file: UploadFile):
        # ... your logic (unchanged)
        ext = file.filename.split('.')[-1] if '.' in file.filename else "bin"
        filename = f"{document_type}_{uuid4().hex[:8]}.{ext}"
        file_path = f"candidates/{user_id}/{filename}"
        
        await self.file_storage.upload(file.file, file_path, file.content_type)
        file_url = await self.file_storage.get_signed_url(file_path, expires=3600)
        
        doc_orm = DocumentORM(
            user_id=user_id,
            document_type=document_type,
            filename=file.filename,
            file_path=file_path,
            file_url=file_url,
            content_type=file.content_type,
            size_bytes=file.size or 0,
            metadata_={}
        )
        await self.doc_repo.save(doc_orm)
        return doc_orm.to_domain()