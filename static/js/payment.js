document.getElementById('payment-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const paymentMethod = document.getElementById('payment_method').value;

    if (paymentMethod === 'card') {
        const cardNumber = document.getElementById('card_number').value;
        const expiry = document.getElementById('expiry').value;
        const cvv = document.getElementById('cvv').value;

        if (!validateCard(cardNumber)) {
            alert("Invalid Card Number");
            return;
        }
        if (!expiry.match(/^(0[1-9]|1[0-2])\/\d{2}$/)) {
            alert("Invalid Expiry Date (MM/YY)");
            return;
        }
        if (!cvv.match(/^[0-9]{3,4}$/)) {
            alert("Invalid CVV");
            return;
        }

        alert("Card Payment Successful!");
    } else if (paymentMethod === 'mobilemoney') {
        const mobileNumber = document.getElementById('mobile_number').value;
        if (!validateMobileNumber(mobileNumber)) {
            alert("Invalid Mobile Number");
            return;
        }

        alert("Mobile Money Payment Successful!");
    }
});

function togglePaymentFields() {
    const paymentMethod = document.getElementById('payment_method').value;
    document.getElementById('card-fields').style.display = paymentMethod === 'card' ? 'block' : 'none';
    document.getElementById('mobile-money-fields').style.display = paymentMethod === 'mobilemoney' ? 'block' : 'none';
}

function validateCard(number) {
    return /^(?:4[0-9]{12}(?:[0-9]{3})?|5[1-5][0-9]{14})$/.test(number);
}

function validateMobileNumber(number) {
    return /^(07\d{8})$/.test(number);
}