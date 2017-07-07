from django import forms
from .models import Post

#from froala_editor.widgets import FroalaEditor


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)
       

''' working send mail
class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)
'''
    