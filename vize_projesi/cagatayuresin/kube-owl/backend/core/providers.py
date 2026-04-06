"""
KubeOps Agent — LLM Provider Yönetimi
Ollama ve Gemini LLM/Embedding model factory fonksiyonları.
"""

import logging
from ..config import settings

logger = logging.getLogger(__name__)


def get_llm(provider: str = None):
    """
    Seçilen provider'a göre LlamaIndex LLM objesi döndürür.

    Args:
        provider: 'ollama' veya 'gemini'. None ise config'deki default kullanılır.

    Returns:
        LlamaIndex LLM instance
    """
    provider = provider or settings.default_provider

    if provider == "ollama":
        from llama_index.llms.ollama import Ollama
        logger.info(f"Ollama LLM oluşturuluyor: {settings.ollama_model} @ {settings.ollama_base_url}")
        return Ollama(
            model=settings.ollama_model,
            base_url=settings.ollama_base_url,
            context_window=4096,
            request_timeout=300.0,
        )
    elif provider == "gemini":
        from llama_index.llms.gemini import Gemini
        if not settings.gemini_api_key or settings.gemini_api_key == "your-api-key-here":
            raise ValueError("Gemini API key ayarlanmamış. .env dosyasında GEMINI_API_KEY değerini girin.")
        logger.info(f"Gemini LLM oluşturuluyor: {settings.gemini_model}")
        return Gemini(
            model=settings.gemini_model,
            api_key=settings.gemini_api_key,
        )
    else:
        raise ValueError(f"Bilinmeyen provider: {provider}. 'ollama' veya 'gemini' kullanın.")


def get_embed_model(provider: str = None):
    """
    Seçilen provider'a göre LlamaIndex embedding modeli döndürür.

    Args:
        provider: 'ollama' veya 'gemini'. None ise config'deki default kullanılır.

    Returns:
        LlamaIndex Embedding model instance
    """
    provider = provider or settings.default_provider

    if provider == "ollama":
        from llama_index.embeddings.ollama import OllamaEmbedding
        logger.info(f"Ollama Embedding oluşturuluyor: {settings.ollama_embed_model}")
        return OllamaEmbedding(
            model_name=settings.ollama_embed_model,
            base_url=settings.ollama_base_url,
        )
    elif provider == "gemini":
        from llama_index.embeddings.gemini import GeminiEmbedding
        if not settings.gemini_api_key or settings.gemini_api_key == "your-api-key-here":
            raise ValueError("Gemini API key ayarlanmamış. .env dosyasında GEMINI_API_KEY değerini girin.")
        logger.info(f"Gemini Embedding oluşturuluyor: {settings.gemini_embed_model}")
        return GeminiEmbedding(
            model_name=settings.gemini_embed_model,
            api_key=settings.gemini_api_key,
        )
    else:
        raise ValueError(f"Bilinmeyen provider: {provider}. 'ollama' veya 'gemini' kullanın.")


def get_provider_info(provider: str = None) -> dict:
    """Provider hakkında bilgi döndürür."""
    provider = provider or settings.default_provider
    if provider == "ollama":
        return {
            "provider": "ollama",
            "llm_model": settings.ollama_model,
            "embed_model": settings.ollama_embed_model,
            "base_url": settings.ollama_base_url,
        }
    elif provider == "gemini":
        return {
            "provider": "gemini",
            "llm_model": settings.gemini_model,
            "embed_model": settings.gemini_embed_model,
            "api_key_set": bool(settings.gemini_api_key and settings.gemini_api_key != "your-api-key-here"),
        }
    return {"provider": provider, "error": "Bilinmeyen provider"}
