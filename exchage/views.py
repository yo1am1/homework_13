from django.shortcuts import render

from exchage.forms import ExchangeForm


def index(request):
    return render(request, "index.html")


def display(request):
    return render(request, "display.html")


def calculate(request):
    form = ExchangeForm(request.POST)
    if request.method == "POST" and form.is_valid():
        if "USD to UAH" in request.POST:
            num = form.cleaned_data["amount"]
            return render(
                request,
                "calculate.html",
                {"vendor": f"Your input: {num}", "form": form},
            )
    else:
        form = ExchangeForm()
        return render(request, "calculate.html", {"form": form})
