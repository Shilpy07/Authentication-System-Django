from django import forms
from Learnings.models import Login

class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = ('Username', 'Password')