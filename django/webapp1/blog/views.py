from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from blog.models import *
from django.views.generic.dates import  ArchiveIndexView, YearArchiveView, MonthArchiveView,\
                                        DayArchiveView, TodayArchiveView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from mysite.views import OwnerOnlyMixin

from django.views.generic import FormView # forms.py와 짝을 맞춤
from django.db.models import Q

from django.utils import timezone

from blog.forms import PostSearchForm

from django.http import FileResponse
import os
from django.conf import settings

# Create your views here.

# ListView
class PostLV(ListView):
    model = Post
    template_name = 'blog/post_all.html' # 템플릿 파일명 변경
    context_object_name = 'posts' # 컨텍스트 객체 이름 변병(object_list)
    paginate_by = 2 # 페이지네이션, 페이지당 문서 건 수

# DetailView
class PostDV(DetailView):
    model = Post
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        post.read_cnt += 1
        post.save()
        return context

# ArchiveView
class PostAV(ArchiveIndexView):
     model= Post
     date_field = 'modify_dt'

class PostYAV(YearArchiveView):
     model= Post
     date_field = 'modify_dt'
     make_object_list = True

class PostMAV(MonthArchiveView):
     model= Post
     date_field = 'modify_dt'
     month_format = '%m' # 숫자로 쓰기 위해 바꿈, 기본은 january, 등으로 나옴

class PostDAV(DayArchiveView):
     model= Post
     date_field = 'modify_dt'
     month_format = '%m'

class PostTAV(TodayArchiveView):
     model= Post
     date_field = 'modify_dt'
     month_format = '%m'

# Tag view

class TagCloudTV(TemplateView):
    template_name = 'taggit/taggit_cloud.html'

class TaggedObjectLV(ListView):
    template_name = 'taggit/taggit_post_list.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(tags__name=self.kwargs.get('tag'))
        # Post.objects의 Where 절 구성 (모델의멤버명(tags)__조건= )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tagname'] = self.kwargs['tag']

        return context

# FormView

class SearchFormView(FormView):
    form_class = PostSearchForm
    template_name = 'blog/post_search.html'

    def form_valid(self, form): # 유효성 검사를 통과했을 때 매개변수 form은 forms.py의 search_word
        searchWord = form.cleaned_data['search_word']
        post_list = Post.objects.filter( # where 절을 쓰고싶을때 filter를 사용
            Q(title__icontains=searchWord) | # title like 'searchword' 뜻 Q는 Query의 약자
            Q(description__icontains=searchWord) |
            Q(content__icontains=searchWord)
        ).distinct()

        context = {}
        context['form'] = form
        context['search_term'] = searchWord
        context['object_list'] = post_list

        return render(self.request, self.template_name, context)

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    # fields = ['title', 'slug', 'description', 'content', 'tags'] # 모델 view에서 form으로 저것들을 운영하겠다
    fields = ['title', 'description', 'content', 'tags']
    # initial = {'slug': 'auto-filling-do-not-input'} # 초기값을 담아 두는 사전
    success_url = reverse_lazy('blog:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.modify_dt = timezone.now() # 조회수가 올라가면 자동으로 날짜가 변경됨을 방지
        response = super().form_valid(form) # form에 저장

        files = self.request.FILES.getlist("files") # file 다운로드
        for file in files:
            attach_file = PostAttachFile(post= self.object, filename= file.name, size= file.size, content_type= file.content_type, upload_file= file)

            attach_file.save()

        return response

class PostUpdateView(OwnerOnlyMixin, UpdateView):
    model = Post
    # fields = ['title', 'slug', 'description', 'content', 'tags']
    fields = ['title', 'description', 'content', 'tags']
    success_url = reverse_lazy('blog:index')

    def form_valid(self, form):
        form.instance.modify_dt = timezone.now()


        #  파일 삭제
        # delete_files = self.request.POST["delete_files"]
        delete_files = self.request.POST.getlist("delete_files")
        for fid in delete_files: # fid는 문자열 타입
            file = PostAttachFile.objects.get(id=int(fid)) # PostAttachFile의 object중 id값을 받아옴
            file_path = os.path.join(settings.MEDIA_ROOT, str(file.upload_file)) # 파일 경로
            os.remove(file_path) # 실제 파일 삭제
            file.delete() # 모델 삭제 (테이블 행 삭제)

        response = super().form_valid(form)
        files = self.request.FILES.getlist("files")  # file 다운로드
        for file in files:
            attach_file = PostAttachFile(post= self.object, filename= file.name, size= file.size, content_type= file.content_type, upload_file= file)

            attach_file.save()

        return response

class PostDeleteView(OwnerOnlyMixin, DeleteView) :
    model = Post
    success_url = reverse_lazy('blog:index')

def download(request, id): # 함수 기반의 view
    file = PostAttachFile.objects.get(id=id)
    file_path = os.path.join(settings.MEDIA_ROOT, str(file.upload_file))

    return  FileResponse(open(file_path, 'rb')) # 파일의 경로와, rb(read binary)

# class HomeView(ListView):
#     template_name = "home.html"
#     model = Post
#     today_time = timezone.now()
#     context_object_name = 'posts'
#
#     def get_queryset(self): # 유효성 검사를 통과했을 때 매개변수 form은 forms.py의 search_word
#         return Post.objects.filter(
#             Q(title__icontains=searchWord) |
#             Q(description__icontains=searchWord) |
#             Q(content__icontains=searchWord)
#         )

# class HomeView(TodayArchiveView):
#     template_name = 'home.html'
#     model = Post
#     date_field = 'modify_dt'