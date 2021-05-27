from django import forms
from django.forms import widgets
from tasks.models import Task

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=255)
    message = forms.CharField(max_length=65536, widget = forms.Textarea())
    sender = forms.EmailField()

    # class Meta:
    #     widgets = {
    #         'message': forms.Textarea()
    #     }

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        # fields = '__all__'  # to include all fields
        fields = ['content', 'deadline', 'tags']
    
        widgets = {
            'deadline': forms.DateTimeInput(attrs = {'type': 'datetime-local'})
        }