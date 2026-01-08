# app/interfaces/storage/file_storage.py
from abc import ABC, abstractmethod
from typing import BinaryIO

class IFileStorage(ABC):

    @abstractmethod
    async def upload(
        self,
        file: BinaryIO,
        file_path: str,
        content_type: str = "application/octet-stream"
    ) -> None:
        
        raise NotImplementedError

    @abstractmethod
    async def get_signed_url(self, file_path: str, expires: int = 3600) -> str:
       
        raise NotImplementedError

    @abstractmethod
    async def delete(self, file_path: str) -> None:
       
        raise NotImplementedError