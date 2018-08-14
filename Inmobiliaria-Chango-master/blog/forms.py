from django import forms
from .models import Post

class PostForm(forms.ModelForm):
	
	class Meta:
		model = Post
		fields = ('title', 'text', 'antiguedad','servicios','zona','direccion','alquiler')
