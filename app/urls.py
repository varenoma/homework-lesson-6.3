from django.urls import path
from .views import homepage, func_1, func_2, func_3, func_4, func_5

urlpatterns = [
    path('',homepage),
    path('page_1/',func_1),
    path('page_2/',func_2),
    path('page_3/',func_3),
    path('page_4/',func_4),
    path('page_5/',func_5),
]