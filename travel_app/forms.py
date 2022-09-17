from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


# staff reg form
class CustomerRegForm(UserCreationForm):

    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2"
        )

    def save(self, commit=True):
        user = super(CustomerRegForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.is_customer = True
        if commit:
            user.save()
        return user