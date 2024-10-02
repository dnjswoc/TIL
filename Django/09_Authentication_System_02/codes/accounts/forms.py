from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# django는 User 모델을 직접 참조하는 것을 권장하지 않는다.
# from .models import User
# 그래서 Django는 User 모델을 간접적으로 참조할 수 있는 방법을 별도로 제공한다.
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()


class CustomUserChangeForm(UserChangeForm):
    # password = None

    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email',)