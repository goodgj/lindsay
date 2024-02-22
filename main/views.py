from django.shortcuts import render

# Create your views here.

# 아래 다 새로
def index(request):
    return render(request,'main/index.html')  # 템플릿 메인 속 index를 불러온다.
  
 
def doc_detail(request, doc):
    path_template = 'main/'
    # 한글버전
    if doc == 'about':
        path_template += 'about.html'
    elif doc == 'first':
        path_template += 'first.html'
    elif doc == 'index':
        path_template += 'index.html'
    elif doc == 'gallery':
        path_template += 'gallery.html'
    elif doc == 'contact':
        path_template += 'contact.html'
    elif doc == 'place_food':
        path_template += 'place_food.html'
    elif doc == 'place_attraction':
        path_template += 'place_attraction.html'     
    elif doc == 'place_market':
        path_template += 'place_market.html'  
    # 영어버전
    elif doc == 'en_main':
        path_template += 'en_main.html'  
    # 에러   
    else:
        path_template += 'error.html'
    return render(request, path_template)
