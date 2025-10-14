from django.shortcuts import render
import requests


def exchange(request):
    response = requests.get(url='https://www.cbr-xml-daily.ru/latest.js').json()
    currencies = response.get('rates')

    if request.method == "GET":
        context = {'currencies': currencies}
        return render(request, 'exchange/index.html', context)
    else:
        from_amount = request.POST.get("from-amount")
        from_curr = request.POST.get("from-curr")
        to_curr = request.POST.get("to-curr")

        convert_amount = round((currencies[to_curr] / currencies[from_curr]) * float(from_amount), 2)

        context = {
            'from_curr': from_curr,
            'to_curr': to_curr,
            'from_amount': from_amount,
            'currencies': currencies,
            'convert_amount': convert_amount
        }
        return render(request, 'exchange/index.html', context)

