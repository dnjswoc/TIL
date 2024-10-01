from django import forms
from .models import Article


# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea)


# 위젯 미적용
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        # exclude = ('title',)


# 위젯 적용
# class ArticleForm(forms.ModelForm):
#     title = forms.CharField(
#         label='제목',
#         widget=forms.TextInput(
#             attrs={
#                 'class': 'my-title',
#                 'placeholder': '제목을 입력해주세요',
#                 'maxlength': 10,
#             }
#         ),
#     )

#     content = forms.CharField(
#         label='내용',
#         widget=forms.Textarea(
#             attrs={
#                 'class': 'my-content',
#                 'placeholder': 'Enter the content',
#                 'rows': 5,
#                 'cols': 50,
#             }
#         ),
#         error_messages={'required': '내용을 입력해주세요.'},
#     )

#     class Meta:
#         model = Article
#         fields = '__all__'
#         exclude = ('title',)
