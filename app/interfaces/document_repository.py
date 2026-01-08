# app/interfaces/repos/document_repository.py
from abc import ABC, abstractmethod
from typing import List, Optional
from app.domain.models.document import Document  # ← your domain model

class IDocumentRepository(ABC):
   

    @abstractmethod
    async def save(self, document: Document) -> Document:
       
        raise NotImplementedError

    @abstractmethod
    async def get_by_id(self, document_id: str) -> Optional[Document]:
       
        raise NotImplementedError

    @abstractmethod
    async def get_by_user_and_type(self, user_id: int, document_type: str) -> List[Document]:
       
        raise NotImplementedError

    @abstractmethod
    async def delete(self, document_id: str) -> bool:
       
        raise NotImplementedError