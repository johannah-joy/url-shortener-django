from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
import string
import random
from django.utils import timezone

from .models import Storage

# Create your views here.

def index(request):
    short_url = ''
    context = {'short_url': short_url}
    return render(request, 'index.html', context)


def submission(request):
    short_url = ''
    short_length = 6
    # uppercase, lowercase, and digits for chars
    chars = string.ascii_letters + string.digits
    for x in range(short_length):
        short_url += ''.join(random.choice(chars))
    # long_url_input = request.POST.get('long_url')
    # Storage.objects.create(long_url=long_url_input, short_url=short_url, created_time=timezone.now())

    # # use timezone here
    Storage.objects.create(long_url=request.POST.get('long_url'),short_url=short_url, created_time=timezone.now())
    return HttpResponseRedirect(reverse('url_app:resulting',args=(short_url,)))


def redirection(request, short_url):
    short_url = Storage.objects.get(short_url=short_url)
    # use clicks here in redirection
    short_url.num_clicks += 1
    short_url.save()
    return HttpResponseRedirect(short_url.long_url)


def resulting(request, id_short):
    return render(request, 'index.html', {'short_url_link':Storage.objects.get(short_url=id_short)})