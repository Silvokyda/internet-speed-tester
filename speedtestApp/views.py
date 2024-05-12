from django.shortcuts import render
from .utils import run_speed_test, measure_speed
from django.http import JsonResponse

# def speed_test_view(request):
#     if request.method == 'POST':
#         results = run_speed_test()
#         return JsonResponse(results)
#     return render(request, 'test.html')

def speed_test_view(request):
    if request.method == 'POST':
        url = 'https://upload.wikimedia.org/wikipedia/commons/3/3e/Tokyo_Sky_Tree_2012.JPG'  
        file_size = 8185374
        download_speed = measure_speed(url, file_size)
        results = {'download_speed': download_speed}
        return JsonResponse(results)
    return render(request, 'test.html')

