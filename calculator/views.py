from django.shortcuts import render

# Create your views here.
def calculator(request):
    print("hello")
    expr = str(request.GET.get('expression'))

    ans = eval(expr)

    print(ans)

    return render(request, 'calculator.html', {'ans': ans})
