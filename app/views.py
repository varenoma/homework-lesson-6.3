from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def homepage(request):
    respone = 'Bosh sahifa <br> <a href="http://127.0.0.1:8000/page_1/">Page 1</a>'
    respone += "<p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Eveniet temporibus soluta quo sunt <br> ab impedit. Sapiente est voluptatibuspossimus consectetur? Eos nobis facilis est minus <br> vel accusamus molestias autem repellat?</p>"
    respone += "<button>click</button>"
    return HttpResponse(respone)

def func_1(request):
    respone = '1-sahifa <br> <a href="http://127.0.0.1:8000/page_2/">Page 2</a>'
    respone += "<p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Eveniet temporibus soluta quo sunt <br> ab impedit. Sapiente est voluptatibuspossimus consectetur? Eos nobis facilis est minus <br> vel accusamus molestias autem repellat?</p>"
    respone += "<button>click</button>"
    return HttpResponse(respone)

def func_2(request):
    respone = '2-sahifa <br> <a href="http://127.0.0.1:8000/page_3/">Page 3</a>'
    respone += "<p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Eveniet temporibus soluta quo sunt <br> ab impedit. Sapiente est voluptatibuspossimus consectetur? Eos nobis facilis est minus <br> vel accusamus molestias autem repellat?</p>"
    respone += "<button>click</button>"
    return HttpResponse(respone)

def func_3(request):
    respone = '3-sahifa<br> <a href="http://127.0.0.1:8000/page_4/">Page 4</a>'
    respone += "<p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Eveniet temporibus soluta quo sunt <br> ab impedit. Sapiente est voluptatibuspossimus consectetur? Eos nobis facilis est minus <br> vel accusamus molestias autem repellat?</p>"
    respone += "<button>click</button>"
    return HttpResponse(respone)

def func_4(request):
    respone = '4-sahifa<br> <a href="http://127.0.0.1:8000/page_5/">Page 5</a>'
    respone += "<p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Eveniet temporibus soluta quo sunt <br> ab impedit. Sapiente est voluptatibuspossimus consectetur? Eos nobis facilis est minus <br> vel accusamus molestias autem repellat?</p>"
    respone += "<button>click</button>"
    return HttpResponse(respone)

def func_5(request):
    respone = 'oxirgi 5-sahifa<br> <a href="http://127.0.0.1:8000">Bosh sahifaga qaytish</a>'
    respone += "<p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Eveniet temporibus soluta quo sunt <br> ab impedit. Sapiente est voluptatibuspossimus consectetur? Eos nobis facilis est minus <br> vel accusamus molestias autem repellat?</p>"
    respone += "<button>click</button>"
    return HttpResponse(respone)