/**
 * KubeOps Agent — Ana Uygulama
 * Başlatma, global state, event listener'lar, notification sistemi.
 */

// ═══════════ BAŞLATMA ═══════════

document.addEventListener('DOMContentLoaded', async () => {
    console.log('KubeOps Agent başlatılıyor...');

    // Event listener'ları kur
    initEventListeners();

    // Dosya yükleme alanını başlat
    initFileUpload();

    // Paralel olarak başlangıç verilerini çek
    await Promise.allSettled([
        loadDocuments(),
        loadK8sStatus(),
        loadConfig(),
    ]);

    console.log('KubeOps Agent hazır!');
});

// ═══════════ EVENT LISTENERS ═══════════

function initEventListeners() {
    const chatInput = document.getElementById('chat-input');

    // Enter ile gönderme (Shift+Enter = yeni satır)
    chatInput.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            handleSend();
        }
    });

    // Textarea auto-resize
    chatInput.addEventListener('input', () => {
        chatInput.style.height = 'auto';
        chatInput.style.height = Math.min(chatInput.scrollHeight, 120) + 'px';
    });

    // Provider değişikliği
    document.getElementById('provider-select').addEventListener('change', (e) => {
        const provider = e.target.value;
        showNotification(`Provider değiştirildi: ${provider === 'ollama' ? 'Ollama (Lokal)' : 'Gemini (Cloud)'}`, 'info');
    });
}

// ═══════════ K8s DURUMU ═══════════

async function loadK8sStatus() {
    const badge = document.getElementById('k8s-status');

    try {
        const status = await getK8sStatus();

        if (status.mode === 'real') {
            badge.className = 'tag kubeops-k8s-badge is-real';
            badge.innerHTML = '<i class="ti ti-circle-filled" style="font-size:0.5rem"></i>&nbsp; Real K8s';
        } else {
            badge.className = 'tag kubeops-k8s-badge is-mock';
            badge.innerHTML = '<i class="ti ti-circle-filled" style="font-size:0.5rem"></i>&nbsp; Mock K8s';
        }
    } catch (error) {
        badge.className = 'tag kubeops-k8s-badge is-mock';
        badge.innerHTML = '<i class="ti ti-circle-filled" style="font-size:0.5rem"></i>&nbsp; Mock K8s';
    }
}

// ═══════════ KONFİGÜRASYON ═══════════

async function loadConfig() {
    try {
        const config = await getConfig();

        // Provider dropdown'u ayarla
        const select = document.getElementById('provider-select');
        if (config.default_provider) {
            select.value = config.default_provider;
        }
    } catch (error) {
        console.warn('Config yüklenemedi:', error);
    }
}

// ═══════════ BİLDİRİM SİSTEMİ ═══════════

/**
 * Bildirim gösterir.
 * @param {string} message — Bildirim mesajı
 * @param {string} type — 'success', 'error', 'info', 'warning'
 * @param {number} duration — Otomatik kapanma süresi (ms)
 */
function showNotification(message, type = 'info', duration = 4000) {
    const container = document.getElementById('notification-container');

    // İkon seç
    let icon;
    switch (type) {
        case 'success': icon = 'ti-check'; break;
        case 'error': icon = 'ti-alert-circle'; break;
        case 'warning': icon = 'ti-alert-triangle'; break;
        default: icon = 'ti-info-circle';
    }

    const notifEl = document.createElement('div');
    notifEl.className = `kubeops-notification ${type}`;
    notifEl.innerHTML = `
        <i class="ti ${icon}"></i>
        <span>${escapeHtml(message)}</span>
    `;

    container.appendChild(notifEl);

    // Otomatik kapanma
    setTimeout(() => {
        notifEl.style.opacity = '0';
        notifEl.style.transform = 'translateX(20px)';
        notifEl.style.transition = 'all 0.3s ease';
        setTimeout(() => notifEl.remove(), 300);
    }, duration);
}
