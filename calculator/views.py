from django.shortcuts import render
import os

# Create your views here.
def calculator(request):
    print("hello")
    expr = str(request.GET.get('expression'))
    ans = eval(expr)

    return render(request, 'calculator.html', {'ans': ans})
