from django.shortcuts import render
from .utils import run_speed_test
from django.http import JsonResponse

def speed_test_view(request):
    if request.method == 'POST':
        results = run_speed_test()
        return JsonResponse(results)
    return render(request, 'test.html')

