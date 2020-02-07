#  from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie

@ensure_csrf_cookie
def home_page(request):
    return render(request, 'home.html', {
        #  'new_item_text': request.POST['item_text']
        'new_item_text': request.POST.get('item_text', ''),
    })
    
