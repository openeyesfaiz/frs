from django.shortcuts import render
from . import models

import websocket
import time

# Create your views here.
def index(request):
    

    return render(request, 'frs/index.html', {})