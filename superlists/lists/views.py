from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie

@ensure_csrf_cookie
def home_page(request):
    #  return HttpResponse('<html><title>To-Do lists</title></html>')
    return render(request, 'home.html')
    
