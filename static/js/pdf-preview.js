// Initialize PDF.js
pdfjsLib.GlobalWorkerOptions.workerSrc = 'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/2.11.338/pdf.worker.min.js';

function createPDFThumbnail(pdfUrl, canvas) {
    pdfjsLib.getDocument(pdfUrl).promise.then(function(pdf) {
        pdf.getPage(1).then(function(page) {
            const viewport = page.getViewport({scale: 0.5});
            const context = canvas.getContext('2d');
            canvas.height = viewport.height;
            canvas.width = viewport.width;

            const renderContext = {
                canvasContext: context,
                viewport: viewport
            };
            page.render(renderContext);
        });
    }).catch(function(error) {
        console.error('Error loading PDF:', error);
        canvas.style.display = 'none';
    });
}

// Initialize previews when document is ready
document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.pdf-preview').forEach(function(canvas) {
        const pdfUrl = canvas.dataset.pdfUrl;
        createPDFThumbnail(pdfUrl, canvas);
    });
});
