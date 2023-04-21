from django import forms
from .models import Task
from django.contrib.auth import authenticate



class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["task","description","due_date"]

        widgets = {
            'due_date': forms.widgets.DateTimeInput(attrs={'type': 'date'}),
        }


class EditTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["task","description","status","due_date"]

        widgets = {
            'due_date': forms.widgets.DateTimeInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance:
            self.fields['due_date'].initial = self.instance.due_date


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("Invalid username or password")
        return cleaned_data