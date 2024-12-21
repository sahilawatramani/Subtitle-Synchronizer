document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('form');
    form.addEventListener('submit', (e) => {
        const videoInput = document.getElementById('video');
        if (!videoInput.files.length) {
            alert('Please upload a video file.');
            e.preventDefault();
        }
    });
});
