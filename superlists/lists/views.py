#  from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import ensure_csrf_cookie
from lists.models import Item

@ensure_csrf_cookie
def home_page(request):
    if request.method == 'POST':
        new_item_text = request.POST['item_text']
        Item.objects.create(text=new_item_text)
        return redirect('/lists/the-only-list-in-the-world/')

    #  items = Item.objects.all()
    return render(request, 'home.html')


@ensure_csrf_cookie
def view_list(request):
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})
    
