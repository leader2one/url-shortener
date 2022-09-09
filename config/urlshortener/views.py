import uuid
import base64

from django.shortcuts import render, HttpResponse, redirect

from .models import Url


def index(request):
    return render(request, 'index.html')


def create(request):
    if request.method == 'POST':
        url = request.POST['url']
        string_bytes = url.encode("ascii")
        base64_bytes = base64.b64encode(string_bytes)
        base64_string = base64_bytes.decode("ascii")
        print(base64_string)
        encoded_short = base64_string[:6]
        new_url = Url(link=url, shortened = encoded_short)
        new_url.save()
        return HttpResponse(f'127.0.0.1:8000/{encoded_short}')


def go(request, pk):
    url_details = Url.objects.get(shortened=pk)
    print('go function is working')
    return redirect('https://' + url_details.link)