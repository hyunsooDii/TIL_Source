from django import forms

class PostSearchForm(forms.Form):
    search_word = forms.CharField(label='Search Word') # form을 구성하는 모든 요소를 넣어주는 기능