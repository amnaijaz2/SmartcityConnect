document.addEventListener('DOMContentLoaded', function() {
    // SIMPLE COPY FUNCTION
    function copyPhoneNumber(button) {
        const card = button.closest('.card-body');
        const phoneElement = card.querySelector('.phone-number');
        const phoneNumber = phoneElement.textContent.trim();
        
        // Create temporary element
        const textarea = document.createElement('textarea');
        textarea.value = phoneNumber;
        document.body.appendChild(textarea);
        textarea.select();
        
        try {
            // Try modern clipboard API first
            if(navigator.clipboard) {
                navigator.clipboard.writeText(phoneNumber);
                showCopySuccess(button);
                return;
            }
            // Fallback for older browsers
            if(document.execCommand('copy')) {
                showCopySuccess(button);
            } else {
                manualCopyFallback(phoneElement);
            }
        } catch (err) {
            manualCopyFallback(phoneElement);
        } finally {
            document.body.removeChild(textarea);
        }
    }

    // SHOW COPY SUCCESS FEEDBACK
    function showCopySuccess(button) {
        const originalHTML = button.innerHTML;
        button.innerHTML = '<i class="fas fa-check me-1"></i> Copied!';
        button.classList.replace('btn-outline-primary', 'btn-success');
        
        setTimeout(() => {
            button.innerHTML = originalHTML;
            button.classList.replace('btn-success', 'btn-outline-primary');
        }, 2000);
    }

    // MANUAL COPY FALLBACK
    function manualCopyFallback(element) {
        const range = document.createRange();
        range.selectNode(element);
        window.getSelection().removeAllRanges();
        window.getSelection().addRange(range);
        alert('Press Ctrl+C to copy the number');
    }

    // CALL FUNCTION
    function callPhoneNumber(button) {
        const card = button.closest('.card-body');
        const phoneElement = card.querySelector('.phone-number');
        const phoneNumber = phoneElement.textContent.replace(/\D/g, '');
        
        if (/Android|iPhone|iPad|iPod|BlackBerry/i.test(navigator.userAgent)) {
            window.location.href = `tel:${phoneNumber}`;
        } else {
            alert(`Please call: ${phoneElement.textContent.trim()}`);
        }
    }

    // COPY BUTTON CLICK
    document.querySelectorAll('.copy-btn').forEach(btn => {
        btn.addEventListener('click', function() {
            copyPhoneNumber(this);
        });
    });

    // CALL BUTTON CLICK
    document.querySelectorAll('.call-btn').forEach(btn => {
        btn.addEventListener('click', function() {
            callPhoneNumber(this);
        });
    });

    // HOVER EFFECTS
    document.querySelectorAll('.hover-lift').forEach(btn => {
        btn.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-2px)';
            this.style.boxShadow = '0 4px 8px rgba(0, 0, 0, 0.1)';
        });
        btn.addEventListener('mouseleave', function() {
            this.style.transform = '';
            this.style.boxShadow = '';
        });
    });
});