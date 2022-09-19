from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


# When create a new form to new users..
class CustomUserCreationForm(UserCreationForm):
    # def __init__(self, *args, **kwargs) -> None:
    #     super().__init__(*args, **kwargs)
    #     # we can override the help_text from here..
    #     self.fields["username"].help_text = "AnyThing"
    #     # we can hide the help_text from here..
    #     self.fields["username"].help_text = None

    class Meta:
        model = CustomUser
        fields = ("username", "email", "age")


# Form used in admin interface to change user's data.
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email", "age")
