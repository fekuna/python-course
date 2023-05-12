from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january": "ini january",
    "february": "ini february",
    "march": "ini march",
    "april": "ini april",
    "may": "ini may",
    "june": "ini june",
    "july": "ini july",
    "august": "ini august",
    "september": "ini september",
    "october": "ini october",
    "november": "ini november",
    "december": "ini december",
}

# Create your views here.

def index(request):
    print("hello")
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
    
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    
    if month > len(months):
        return HttpResponseNotFound("Invalid Month")
    
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])

    return HttpResponseRedirect(redirect_path) 


# aosdkas
def monthly_challenge(request, month):
    try:
        challenge = monthly_challenges[month]
        return HttpResponse(challenge)
    except:
        return HttpResponseNotFound("This month is not supported")
