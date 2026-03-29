"""
KubeOps Agent — Doküman CRUD API Endpoint'leri
Doküman yükleme, listeleme, detay ve silme.
"""

import logging
from fastapi import APIRouter, UploadFile, File, Query, HTTPException

from backend.config import settings
from backend.utils.file_handler import validate_file, save_uploaded_file
from backend.core.indexer import (
    index_document,
    delete_document,
    get_all_documents,
    get_document,
)

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/documents", tags=["Dokümanlar"])


@router.post("/upload")
async def upload_document(
    file: UploadFile = File(...),
    provider: str = Query(default=None, description="Embedding provider: 'ollama' veya 'gemini'"),
):
    """
    Runbook dosyası yükler ve indexler.

    - Desteklenen formatlar: .pdf, .md, .txt
    - Maksimum boyut: 10MB
    - Provider belirtilmezse varsayılan kullanılır
    """
    # Dosya validasyonu
    is_valid, error_msg = validate_file(file)
    if not is_valid:
        raise HTTPException(status_code=400, detail=error_msg)

    provider = provider or settings.default_provider

    try:
        # Dosyayı kaydet
        file_path = await save_uploaded_file(file)

        # Indexle
        doc_info = index_document(file_path, provider)

        logger.info(f"Doküman başarıyla yüklendi ve indexlendi: {file.filename}")
        return doc_info

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Doküman yükleme hatası: {e}")
        raise HTTPException(
            status_code=500,
            detail=f"Doküman yükleme/indexleme sırasında hata oluştu: {str(e)}"
        )


@router.get("")
async def list_documents():
    """Yüklü tüm dokümanların listesini döndürür."""
    try:
        documents = get_all_documents()
        return {"documents": documents, "total": len(documents)}
    except Exception as e:
        logger.error(f"Doküman listeleme hatası: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{doc_id}")
async def get_document_detail(doc_id: str):
    """Tek bir dokümanın detayını döndürür."""
    doc = get_document(doc_id)
    if not doc:
        raise HTTPException(status_code=404, detail=f"Doküman bulunamadı: {doc_id}")
    return doc


@router.delete("/{doc_id}")
async def delete_document_endpoint(doc_id: str):
    """Bir dokümanı ve ilgili chunk'ları siler."""
    doc = get_document(doc_id)
    if not doc:
        raise HTTPException(status_code=404, detail=f"Doküman bulunamadı: {doc_id}")

    try:
        success = delete_document(doc_id)
        if success:
            return {"status": "deleted", "id": doc_id, "filename": doc.get("filename")}
        else:
            raise HTTPException(status_code=500, detail="Silme işlemi başarısız")
    except Exception as e:
        logger.error(f"Doküman silme hatası: {e}")
        raise HTTPException(status_code=500, detail=str(e))
