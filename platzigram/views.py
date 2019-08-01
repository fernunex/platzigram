"""" platzigram views"""

#Django

from django.http import HttpResponse
from django.http import JsonResponse

#Utilities
from datetime import datetime
import json


def hello_world(request):
    """Return a greeting."""
    
    return HttpResponse('Oh, hi! Current server time is {now}'.format
    (now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')))


def sorted_numbers(request):
    """ JSON respond sorted_numbers."""
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    numbersorted = sorted(numbers)
    data = {
            'status':'ok',
            'numbers': numbersorted,
            'message' : 'Succesfully sorted.'       
    }
    return HttpResponse(
        json.dumps(data, indent=5), 
        content_type = 'application/json')


def say_hi(request, name , age):
    """Return a greeting."""
    if age < 12:
        message = 'Sorry {}, you are not allowed here'.format(name)

    else:
        message = 'Hi, {}! Welcome to Platzigram'.format(name)

    return HttpResponse(message)