from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def homepage(request):
    respone = 'Bosh sahifa <br> <a href="http://127.0.0.1:8000/page_1/">Page 1 ga utish</a>'
    respone += "<p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Eveniet temporibus soluta quo sunt <br> ab impedit. Sapiente est voluptatibuspossimus consectetur? Eos nobis facilis est minus <br> vel accusamus molestias autem repellat?</p>"
    respone += "<button>button</button>"
    return HttpResponse(respone)

def func_1(request):
    respone = '1-sahifa <br> <a href="http://127.0.0.1:8000/page_2/">Page 2 ga utish</a>'
    respone += '<a style="margin-left: 20px;" href="http://127.0.0.1:8000">Bosh sahifaga qaytish</a>'
    respone += "<p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Eveniet temporibus soluta quo sunt</p>"
    respone += "<button>button 1</button>"
    return HttpResponse(respone)

def func_2(request):
    respone = '2-sahifa <br> <a href="http://127.0.0.1:8000/page_3/">Page 3 ga utish</a>'
    respone += '<a style="margin-left: 20px;" href="http://127.0.0.1:8000/page_1">1-sahifaga qaytish</a>'
    respone += "<p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Eveniet temporibus soluta quo sunt <br> ab impedit. Sapiente est voluptatibuspossimus consectetur? Eos nobis facilis est minus <br> vel accusamus molestias autem repellat? vel accusamus molestias autem repellat?</p>"
    respone += "<button>button 2</button>"
    return HttpResponse(respone)

def func_3(request):
    respone = '3-sahifa<br> <a href="http://127.0.0.1:8000/page_4/">Page 4 ga utish</a>'
    respone += '<a style="margin-left: 20px;" href="http://127.0.0.1:8000/page_2">2-sahifaga qaytish</a>'
    respone += "<p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Eveniet temporibus soluta quo sunt <br> ab impedit. Sapiente est voluptatibuspossimus consectetur? vel accusamus molestias autem repellat? vel accusamus molestias autem repellat? Eos nobis facilis est minus <br> vel accusamus molestias autem repellat?</p>"
    respone += "<button>button 3</button>"
    return HttpResponse(respone)

def func_4(request):
    respone = '4-sahifa<br> <a href="http://127.0.0.1:8000/page_5/">Page 5 ga utish</a>'
    respone += '<a style="margin-left: 20px;" href="http://127.0.0.1:8000/page_3">3-sahifaga qaytish</a>'
    respone += "<p>Lorem ipsum vel accusamus molestias autem repellat? dolor sit amet consectetur adipisicing elit. Eveniet temporibus soluta quo sunt <br> ab impedit. Sapiente est voluptatibuspossimus consectetur? Eos nobis facilis est minus <br> vel accusamus molestias autem repellat?</p>"
    respone += "<button>button 4</button>"
    return HttpResponse(respone)

def func_5(request):
    respone = 'oxirgi 5-sahifa<br> <a href="http://127.0.0.1:8000">Bosh sahifaga qaytish</a>'
    respone += '<a style="margin-left: 20px;" href="http://127.0.0.1:8000/page_4">4-sahifaga qaytish</a>'
    respone += "<p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Eveniet temporibus soluta quo sunt <br> ab impedit. Sapiente est voluptatibuspossimus consectetur? Eos nobis vel accusamus molestias autem repellat? vel accusamus molestias autem repellat? vel accusamus molestias autem repellat? facilis est minus <br> vel accusamus molestias autem repellat?</p>"
    respone += "<button>button 5</button>"
    return HttpResponse(respone)