# mysite 폴더 안에 있는 urls를 bookmark에 urls.py 파일 생성 후 복사

"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from bookmark.views import *

app_name = 'bookmark' # 해당 애플리케이션의 네임스페이스명

# from bookmark.views import index, detail

urlpatterns = [

    path('',BookmarkLV.as_view(), name='index'),
    path('<int:pk>/',BookmarkDV.as_view(),name='detail'),
    # path('admin/', admin.site.urls), # 404 error 나올 때 봐야할 것
    # path('bookmark/', BookmarkLV.as_view(), name='index'),
    # path('bookmark/<int:pk>', BookmarkDV.as_view(), name='detail'),
    # path(url_pattern/<보고자하는 값(path variable)>, 담당하는 뷰)
    # path('bookmark/', index, name='index'),
    # path('bookmark/<int:pk>', detail, name='detail')

    # Example: /bookmark/add/
    path('add/', BookmarkCreateView.as_view(), name="add"),

    # Example: /bookmark/change/
    path('change/', BookmarkChangeLV.as_view(), name="change"),

    # Example: /bookmark/99/update/
    path('<int:pk>/update/', BookmarkUpdateView.as_view(), name="update"),

    # Example: /bookmark/99/delete/
    path('<int:pk>/delete/', BookmarkDeleteView.as_view(), name="delete"),

]
