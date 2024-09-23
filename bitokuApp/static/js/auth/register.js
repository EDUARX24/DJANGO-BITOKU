document.addEventListener("DOMContentLoaded", function () {
    const dataElement = document.getElementById('notification-data');
    if (dataElement) {
        const dataText = dataElement.textContent.trim();
        if (dataText) {
            try {
                const data = JSON.parse(dataText);
                showNotification(data);
            } catch (error) {
                console.error("Error al parsear JSON:", error);
            }
        }
    }
});