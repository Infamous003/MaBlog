from django import forms
from .models import Post
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'subtitle', 'content', 'tags')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'My first PC built'}),
            'subtitle': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'It was great, but I messed up'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'My first PC build was a modest Ryzen 5 5600 and an Nvidia RTX 3050(yeah, I know, a terrible choice, but it is not bad). Nothing too fancy...'}),
            'tags': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Tags'}),
        }