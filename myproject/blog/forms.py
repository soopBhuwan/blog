from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,forms
from .models import Post

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']
    
    def __init__(self,*args,**kwargs):
        super(CustomUserCreationForm,self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs.update({'class':'form-control','placeholder':'Enter Username'})
        self.fields['password1'].widget.attrs.update({'class':'form-control','placeholder':'Enter password...'})
        self.fields['password2'].widget.attrs.update({'class':'form-control','placeholder':'Confirm password...'})
        
class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title','subtitle','content','status']
        
    def __init__(self,*args,**kwargs):
        super(PostForm,self).__init__(*args,**kwargs)
        self.fields['title'].widget.attrs.update({'class':'form-control form-group form-control-sm'})
        self.fields['subtitle'].widget.attrs.update({'class':'form-control form-group form-control-sm'})
        
        self.fields['content'].widget.attrs.update({'class':'form-control form-group form-control-sm'})
        self.fields['content'].widget.attrs['rows'] =4
        self.fields['content'].widget.attrs['cols'] =20
        

class FormPost(ModelForm):
    class Meta: 
        model = Post
        fields = ['title','subtitle','content']
        labels = {'title':'Title','subtitle':'Subtitle','content':'Content'}
        widgets = {'title': forms.TextInput(attrs={'class':'form-control'}),
                   'subtitle': forms.TextInput(attrs={'class':'form-control'}),
                   'content': forms.TextInput(attrs={'class':'form-control'}),
                   }