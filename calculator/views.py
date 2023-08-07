from django.shortcuts import render
import scout_apm.api

# Create your views here.
def calculator(request):
    print("hello")
    expr = str(request.GET.get('expression'))

    scout_apm.api.WebTransaction.start("Expression Evaluation")
    ans = eval(expr)
    scout_apm.api.WebTransaction.stop()

    print(ans)

    return render(request, 'calculator.html', {'ans': ans})
