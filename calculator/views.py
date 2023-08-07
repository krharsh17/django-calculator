from django.shortcuts import render
import scout_apm.api
import os

# Create your views here.
def calculator(request):
    print("hello")
    expr = str(request.GET.get('expression'))

    config = {
        "name": os.environ['SCOUT_NAME'],
        "key": os.environ['SCOUT_KEY'],
        "monitor": os.environ['SCOUT_MONITOR'],
    }

    print(os.environ['SCOUT_NAME'])

    scout_apm.api.install(config=config)

    scout_apm.api.WebTransaction.start("Expression Evaluation")
    ans = eval(expr)
    scout_apm.api.WebTransaction.stop()

    print(ans)

    return render(request, 'calculator.html', {'ans': ans})
