"""
KubeOps Agent — Sistem API Endpoint'leri
Health check, config bilgisi, k8s bağlantı durumu.
"""

import logging
import subprocess
from datetime import datetime, timezone
from fastapi import APIRouter

from backend.config import settings
from backend.core.indexer import get_all_documents, get_collection_count

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api", tags=["Sistem"])


@router.get("/health")
async def health_check():
    """Sistem sağlık durumu."""
    return {
        "status": "ok",
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }


@router.get("/config")
async def get_config():
    """Mevcut sistem konfigürasyonu."""
    documents = get_all_documents()
    collection_count = get_collection_count()

    return {
        "default_provider": settings.default_provider,
        "available_providers": ["ollama", "gemini"],
        "k8s_mode": "real" if settings.has_kubeconfig else "mock",
        "indexed_documents": len(documents),
        "chroma_collection_count": collection_count,
    }


@router.get("/config/providers")
async def get_providers():
    """Kullanılabilir LLM provider'larının listesi."""
    providers = [
        {
            "id": "ollama",
            "name": "Ollama (Lokal)",
            "model": settings.ollama_model,
            "embed_model": settings.ollama_embed_model,
            "base_url": settings.ollama_base_url,
            "description": "Lokal LLM — veriler dışarı çıkmaz, ücretsiz",
        },
        {
            "id": "gemini",
            "name": "Google Gemini (Cloud)",
            "model": settings.gemini_model,
            "embed_model": settings.gemini_embed_model,
            "api_key_set": bool(settings.gemini_api_key and settings.gemini_api_key != "your-api-key-here"),
            "description": "Cloud LLM — daha güçlü ve hızlı, API key gerektirir",
        },
    ]

    return {
        "default_provider": settings.default_provider,
        "providers": providers,
    }


@router.get("/config/k8s-status")
async def get_k8s_status():
    """kubectl bağlantı durumu."""
    result = {
        "mode": "real" if settings.has_kubeconfig else "mock",
        "kubeconfig_found": settings.has_kubeconfig,
        "cluster_reachable": False,
        "context": "",
    }

    if settings.has_kubeconfig:
        try:
            # Mevcut context'i al
            context_result = subprocess.run(
                ["kubectl", "config", "current-context"],
                capture_output=True,
                text=True,
                timeout=5,
            )
            if context_result.returncode == 0:
                result["context"] = context_result.stdout.strip()

            # Cluster erişilebilirliğini test et
            cluster_result = subprocess.run(
                ["kubectl", "cluster-info"],
                capture_output=True,
                text=True,
                timeout=10,
            )
            result["cluster_reachable"] = cluster_result.returncode == 0

        except (subprocess.TimeoutExpired, FileNotFoundError) as e:
            logger.warning(f"kubectl erişim kontrolü başarısız: {e}")
        except Exception as e:
            logger.error(f"kubectl durumu kontrol hatası: {e}")

    return result
