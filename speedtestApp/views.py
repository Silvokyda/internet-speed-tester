from django.shortcuts import render
from .utils import run_speed_test

def speed_test_view(request):
    if request.method == 'POST':
        results = run_speed_test()
        return render(request, 'results.html', {'results': results})
    return render(request, 'test.html')
