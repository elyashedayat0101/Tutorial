from django import forms
from django.core.validators import ValidationError

from .models import User


class CreateUserForm(forms.ModelForm):
    password = forms.CharField(max_length=125, widget=forms.PasswordInput)
    password_confirm = forms.CharField(max_length=125, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("email",)

    # def clean_password_confirm(self):
    #     if (self.cleaned_data['password'] and self.cleaned_data["password_confirm"]) and (
    #             self.cleaned_data['password'] != self.cleaned_data["password_confirm"]):
    #         raise ValidationError("Password are not match")
    #     return self.cleaned_data['password_confirm']

    def clean(self):
        clean_data = super(CreateUserForm, self).clean()
        if clean_data["password"] != clean_data["password_confirm"]:
            raise ValidationError("message")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
