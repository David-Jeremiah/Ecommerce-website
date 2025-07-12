import json
import requests
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.conf import settings

# FLUTTERWAVE CONFIG
FLW_PUBLIC_KEY = "your_public_key"
FLW_SECRET_KEY = "your_secret_key"
FLW_ENCRYPTION_KEY = "your_encryption_key"
FLW_API_URL = "https://api.flutterwave.com/v3/payments"


def payment_page(request):
    return render(request, "payment.html")


def process_payment(request):
    if request.method == "POST":
        email = request.POST.get("email")
        amount = request.POST.get("amount")
        currency = "UGX"  # Change to your preferred currency
        payment_method = request.POST.get("payment_method")

        headers = {
            "Authorization": f"Bearer {FLW_SECRET_KEY}",
            "Content-Type": "application/json",
        }

        data = {
            "tx_ref": f"TX-{email}-{amount}",
            "amount": amount,
            "currency": currency,
            "redirect_url": "http://127.0.0.1:8000/payment-success",
            "payment_options": "card, mobilemoneyuganda",
            "customer": {
                "email": email,
                "phonenumber": request.POST.get("phone"),
                "name": request.POST.get("name"),
            },
            "customizations": {
                "title": "My Store",
                "description": "Payment for items",
            },
        }

        response = requests.post(FLW_API_URL, headers=headers, json=data)
        response_data = response.json()

        if response_data["status"] == "success":
            return redirect(response_data["data"]["link"])
        else:
            return JsonResponse({"error": "Payment failed!"}, status=400)

    return JsonResponse({"error": "Invalid request!"}, status=400)


def payment_success(request):
    return render(request, "payment_success.html")
