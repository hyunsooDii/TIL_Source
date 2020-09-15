from django.shortcuts import render

# 데이터를 준비하고 Rendering 호출하는게 View 의 역할

# Create your views here.

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView # generic, 내가 원하는 것을 import 받아서 사용
# generic 에는 CRUD 함수가 모두 내장되어 있음.
from bookmark.models import Bookmark
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from mysite.views import OwnerOnlyMixin


class BookmarkLV(ListView):
    model = Bookmark
    context_object_name = 'bookmark_list' # ListView에서 context_object_name default 값 - object_list이다.

class BookmarkDV(DetailView):
    model = Bookmark
    content_object_name = 'bookmark' # DetailView에서 context_object_name default 값 - object이다.

# def index(request):
#     object_list = Bookmark.objects.all()
#     print(object_list)
#     context = {'bookmark_list': object_list}
#     return render(request, 'bookmark/bookmark_list.html', context)
#
# def detail(request, pk):
#     object = Bookmark.objects.get(pk=pk) # .get(id=pk)
#     context = {'bookmark': object}
#     return  render(request, 'bookmark/bookmark_detail.html', context)

class BookmarkCreateView(LoginRequiredMixin, CreateView): # 부모클래스를 2개 가지는 다중상속
    # 로그인한 상태에서만 나오는 클래스
    model = Bookmark
    fields = ['title', 'url'] # 폼 모델에 사용할 필드 -> 폼 모델 자동 생성
    success_url = reverse_lazy('bookmark:index') # 성공했으면 목록을 보여주는 index페이지로 이동

    def form_valid(self, form): # submit 버튼 눌렀을 때 유효성검사를 통과했을 때 호출되는 함수
        form.instance.owner = self.request.user # 로그인한 사용자의 user instance를 owner에 추가
        return super().form_valid(form) # 폼으로 전달된 데이터(owner 추가)를 기반으로 DB 에 저장하고 succenss url로 이동

class BookmarkChangeLV(LoginRequiredMixin, ListView): # LoginRequiredMixin <- 반드시 로그인을 해야된다
    template_name = 'bookmark/bookmark_change_list.html'

    def get_queryset(self):
        return Bookmark.objects.filter(owner=self.request.user)
    # Bookmark의 owner가 현재 login한 사용자인 것만 return

class BookmarkUpdateView(OwnerOnlyMixin, UpdateView):
    model = Bookmark
    fields = ['title', 'url']
    success_url = reverse_lazy('bookmark:index')
    # 이미 owner 라는 fields 가 CreateView 에 의해 생성이 되어있어 override 할 필요가 없음

class BookmarkDeleteView(OwnerOnlyMixin, DeleteView):
    model = Bookmark
    success_url = reverse_lazy('bookmark:index')

