from django import forms
from .models import Notes
from django.core.exceptions import ValidationError





class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ('title','text')
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control my-5'}),
            'text':forms.Textarea(attrs={'class':'forms-control mb-5'}),
        }
        labels = {
            'text':'place your texts here:'
        }

    # def clean_title(self):
    #     title = self.cleaned_data['title']
    #     if 'Django' not in title:
    #         raise ValidationError("Notes only about django")
        
        # return title
    


