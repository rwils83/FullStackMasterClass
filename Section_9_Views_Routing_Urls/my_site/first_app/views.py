from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
# Create your views here.

# Create Function based views
def home_view(request):
    return HttpResponse("Home Page")

def simple_view(request):
    return HttpResponse("Simple View")

#Dynamic Views Lesson

articles = {'sports': 'Sports Page',
        'finance': 'Finance Page',
        'politics': 'Politics Page'}


def dynamic_view(request, topic):
    try:
        return HttpResponse(articles[topic])
    except:
        return HttpResponse("Error 404: Page not found")

def add_view_myway(request, num1, num2):
    try:
        return HttpResponse(f'{num1} + {num2} = {num1+num2}')
    except:
        return HttpResponse("I fucked up")

def add_view_classway(request, num1, num2):
    try:
        value = f"{num1} + {num2} = {num1+num2}"
        return HttpResponse(str(value))
    except:
        return HttpResponse("I fucked up their way")

def proper_response_not_found(request, topic):
    try:
        return HttpResponse(articles[topic])
    except:
        value = "This is not the droid you are looking for"
        return HttpResponseNotFound(value)

def proper_404(request, topic):
    try:
        return HttpResponse(articles[topic])
    except:
        value = "Generic 404"
        raise Http404(value)

def redirect_test(request, page):
    topic_list = list(articles.keys())
    topic = topic_list[page]

    return HttpResponseRedirect(f"../{topic}")
