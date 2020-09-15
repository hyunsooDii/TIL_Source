# 템플릿 파일만 관리하는 기능

from django.contrib.auth.mixins import AccessMixin
from django.views.defaults import permission_denied
from django.views.generic import TemplateView, CreateView, TodayArchiveView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from blog.models import Post

class OwnerOnlyMixin(AccessMixin):
    raise_exception = True
    permission_denied_message = "Owner only can update/delete the object"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object() # 모델 인스턴스 얻기
        if self.request.user != self.object.owner:
            self.handle_no_permission()
        return super().get(request, *args, **kwargs)

# TemplateView

# class HomeView(TemplateView):
#     template_name = 'home.html'

class HomeView(TodayArchiveView):
    template_name = 'home.html'
    model = Post
    date_field = 'modify_dt'
    allow_empty = True # 내용이 없어도 허용하겠다, 즉 오늘날짜 기사가 없어서 Home이 안나오는걸 방지

# User Creation

class UserCreateView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register_done')

class UserCreateDoneTV(TemplateView):
    template_name = 'registration/register_done.html'