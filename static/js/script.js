document.addEventListener('DOMContentLoaded', () => {
    const purchaseButton = document.getElementById('purchaseButton');
    purchaseButton.addEventListener('click', () => {
        const modelTitle = document.getElementById('modelTitle').innerText;
        const user = {
            modelTitle: modelTitle,
            purchased: true
        };
        console.log(user);
    });
});