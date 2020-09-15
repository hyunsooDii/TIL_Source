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
from django.urls import path, include # bookmark/urls 에 있는 파일 include
from bookmark.views import BookmarkLV, BookmarkDV
# from bookmark.views import index, detail
from mysite.views import HomeView, UserCreateView, UserCreateDoneTV
from blog.views import PostAV

urlpatterns = [
    path('', HomeView.as_view(), name='home'),

    path('admin/', admin.site.urls), # 404 error 나올 때 봐야할 것
    # path('bookmark/', BookmarkLV.as_view(), name='index'),
    # path('bookmark/<int:pk>', BookmarkDV.as_view(), name='detail'),
    # path(url_pattern/<보고자하는 값(path variable)>, 담당하는 뷰)
    # path('bookmark/', index, name='index'),
    # path('bookmark/<int:pk>', detail, name='detail')
    path('bookmark/',include('bookmark.urls')), # 공통적인 bookmark가 들어가고 include는 bookmark/urls에 있는 소스가 들어감
    path('blog/', include('blog.urls')),

    path('accounts/', include('django.contrib.auth.urls')), # 로그인, 로그아웃, 비밀번호 변경 등 담당

    # 회원 가입 및 처리
    path('accounts/register/', UserCreateView.as_view(), name='register'),
    path('accounts/register/done/', UserCreateDoneTV.as_view(), name='register_done'),

    path('tinymce/', include('tinymce.urls')),
]
