from django.urls import path, re_path  # re_path = regular expression (정규표현식)
from blog.views import *

app_name = 'blog'  # 해당 어플리케이션의 네임스페이스 명

urlpatterns = [
    # Example: /blog/
    path('', PostLV.as_view(), name='index'),
    # Example: /blog/post/
    path('post/', PostLV.as_view(), name='index'),
    re_path(r'^post/(?P<slug>[-\w]+)/$', PostDV.as_view(), name='detail'),
    # slug라는 이름의 경로변수를 배정, w - word(알파벳, 숫자), + - 한개 이상 나온다
    # 슬러그라는 환경변수로 공백없이 글자, 숫자, 대시만 허용한다, 마지막은 /로 끝나야 하는 것을 받겠다.
    # ^ - 이걸로 시작한다, $ - 이걸로 끝난다 ?
    # ex)^h - h로 시작한다, s$ - s로 끝난다
    # ex) ^h(.) 글자 하나, ^h(.)* - 글자 하나 이상

    # Example: /blog/archive/
    path('archive/', PostAV.as_view(), name='post_archive'),

    # Example: /blog/archive/2019/
    path('archive/<int:year>/', PostYAV.as_view(),
         name='post_year_archive'),

    # Example: /blog/archive/2019/nov/
    path('archive/<int:year>/<str:month>/', PostMAV.as_view(),
         name='post_month_archive'),

    # Example: /blog/archive/2019/nov/10/
    path('archive/<int:year>/<str:month>/<int:day>/', PostDAV.as_view(),
         name='post_day_archive'),

    # Example: /blog/archive/today/
    path('archive/today/', PostTAV.as_view(), name='post_today_archive'),

    # Example: /blog/tag/
    path('tag/', TagCloudTV.as_view(), name='tag_cloud'),


    # Example : /blog/tag/tagname
    path('tag/<str:tag>/', TaggedObjectLV.as_view(),name='tagged_object_list'),

    # Example: /blog/search
    path('search/', SearchFormView.as_view(), name='search'),

    # Example: /blog/add/
    path('add/', PostCreateView.as_view(), name="add"),

    # Example: /blog/99/update/
    path('<int:pk>/update/', PostUpdateView.as_view(), name="update"),

    # Example: /blog/99/delete/
    path('<int:pk>/delete/', PostDeleteView.as_view(), name="delete"),

    # Example: /blog/download/99/
    path('download/<int:id>', download, name='download'),

 ]