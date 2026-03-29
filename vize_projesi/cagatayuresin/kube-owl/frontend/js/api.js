/**
 * KubeOps Agent — Backend API İstemcisi
 * Tüm backend API çağrıları bu modül üzerinden yapılır.
 */

const API_BASE = '/api';

/**
 * Genel fetch wrapper — hata yönetimi ve JSON parse dahil.
 */
async function apiFetch(url, options = {}) {
    try {
        const response = await fetch(`${API_BASE}${url}`, {
            headers: {
                'Accept': 'application/json',
                ...(options.headers || {}),
            },
            ...options,
        });

        if (!response.ok) {
            let errorDetail = `HTTP ${response.status}`;
            try {
                const errorData = await response.json();
                errorDetail = errorData.detail || errorDetail;
            } catch {
                // JSON parse edilemediyse status text kullan
                errorDetail = response.statusText || errorDetail;
            }
            throw new Error(errorDetail);
        }

        return await response.json();
    } catch (error) {
        if (error.name === 'TypeError' && error.message.includes('fetch')) {
            throw new Error('Sunucuya bağlanılamadı. Backend çalışıyor mu?');
        }
        throw error;
    }
}

// ═══════════ DOKÜMAN API ═══════════

/**
 * Doküman dosyası yükler ve indexler.
 * @param {File} file — Yüklenecek dosya
 * @param {string} provider — Embedding provider ('ollama' veya 'gemini')
 * @returns {Promise<Object>} — Doküman bilgileri
 */
async function uploadDocument(file, provider) {
    const formData = new FormData();
    formData.append('file', file);

    const providerParam = provider ? `?provider=${provider}` : '';

    const response = await fetch(`${API_BASE}/documents/upload${providerParam}`, {
        method: 'POST',
        body: formData,
    });

    if (!response.ok) {
        let errorDetail = `HTTP ${response.status}`;
        try {
            const errorData = await response.json();
            errorDetail = errorData.detail || errorDetail;
        } catch {}
        throw new Error(errorDetail);
    }

    return await response.json();
}

/**
 * Yüklü dokümanların listesini getirir.
 * @returns {Promise<Object>} — {documents: [...], total: N}
 */
async function listDocuments() {
    return apiFetch('/documents');
}

/**
 * Tek bir dokümanın detayını getirir.
 * @param {string} docId — Doküman ID'si
 * @returns {Promise<Object>}
 */
async function getDocument(docId) {
    return apiFetch(`/documents/${docId}`);
}

/**
 * Bir dokümanı siler.
 * @param {string} docId — Silinecek doküman ID'si
 * @returns {Promise<Object>}
 */
async function deleteDocument(docId) {
    return apiFetch(`/documents/${docId}`, { method: 'DELETE' });
}

// ═══════════ AJAN API ═══════════

/**
 * Ajana soru sorar.
 * @param {string} query — Kullanıcı sorusu
 * @param {string} provider — LLM provider ('ollama' veya 'gemini')
 * @returns {Promise<Object>} — {answer, steps, sources, provider, model, duration_ms}
 */
async function queryAgent(query, provider) {
    return apiFetch('/agent/query', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            query: query,
            provider: provider || null,
        }),
    });
}

// ═══════════ SİSTEM API ═══════════

/**
 * Sistem sağlık durumunu kontrol eder.
 * @returns {Promise<Object>}
 */
async function checkHealth() {
    return apiFetch('/health');
}

/**
 * Mevcut konfigürasyonu getirir.
 * @returns {Promise<Object>}
 */
async function getConfig() {
    return apiFetch('/config');
}

/**
 * Kullanılabilir LLM provider'larını listeler.
 * @returns {Promise<Object>}
 */
async function getProviders() {
    return apiFetch('/config/providers');
}

/**
 * Kubernetes bağlantı durumunu kontrol eder.
 * @returns {Promise<Object>}
 */
async function getK8sStatus() {
    return apiFetch('/config/k8s-status');
}
