const form = document.getElementById("id_purchase_game");
form.addEventListener('submit', function (event) {
    const purchasedButton = document.getElementById("purchasedButton");
    purchasedButton.innerText = "Purchased";
    purchasedButton.disabled = true;
});

window.onload = function () {
    const urlParams = new URLSearchParams(window.location.search);
    const checkForm = document.getElementById("id_check_game_purchased");
    checkForm.addEventListener('submit', function (event) {
        event.preventDefault();
        const checkPurchasedButton = document.getElementById("checkPurchasedButton");
        checkPurchasedButton.innerText = "Checking...";
        checkPurchasedButton.disabled = true;
        checkForm.submit();

    });

    if (urlParams.has('purchased') && urlParams.get('purchased') === 'true') {
        checkGamePurchasedTrue();
    } else
        if (urlParams.has('purchased') && urlParams.get('purchased') === 'false') {
            checkGamePurchasedFalse();
        } else {
            checkGameFirstLoad();
        }


};

function checkGameFirstLoad() {
    console.log("First Load");
    document.getElementById("checkPurchasedButton").click();
}

function checkGamePurchasedTrue() {
    console.log("TRUE");
    const purchaseButton = document.getElementById('purchasedButton');
    purchaseButton.textContent = 'Purchased';
    purchaseButton.disabled = true;

}

function checkGamePurchasedFalse() {
    console.log("FALSE");
    const purchaseButton = document.getElementById('purchasedButton');
    purchaseButton.textContent = 'Purchase';
    purchaseButton.disabled = false;
    return;
}