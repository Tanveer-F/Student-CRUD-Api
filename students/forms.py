from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'password']

   
   
   ## Bootstrap ##

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        # Adding Bootstrap classes to form fields
        self.fields['name'].widget.attrs.update({
            'class': 'form-control mb-3',
            'placeholder': 'Enter your name',
        })
        self.fields['email'].widget.attrs.update({
            'class': 'form-control mb-3',
            'placeholder': 'Email address',
        })
        self.fields['password'].widget.attrs.update({
            'class': 'form-control mb-3',
            'placeholder': 'Password',
        })
