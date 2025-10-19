from django.shortcuts import render

import requests
from django.http import JsonResponse
from datetime import datetime, timezone

def me(request):
    try:
        # Fetch cat fact with timeout
        response = requests.get("https://catfact.ninja/fact", timeout=5)
        if response.status_code == 200:
            cat_fact = response.json().get("fact")
        else:
            cat_fact = "Could not fetch cat fact at the moment."
    except requests.RequestException:
        cat_fact = "Cat facts unavailable — try again later."

    data = {
        "status": "success",
        "user": {
            "email": "Sjaypeter.sjp@gmail.com",
            "name": "Peter Saint-John",
            "stack": "Python/Django"
        },
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "fact": cat_fact
    }

    return JsonResponse(data, content_type="application/json", status=200)