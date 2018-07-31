from django.shortcuts import render
from django.utils import timezone
from .models import Casa
from django.shortcuts import render, get_object_or_404
#from .forms import PostForm

def lista_casas(request):
    casas = Casa.objects.filter()
    return render(request, 'blog/listadecasas.html', {'casas': casas})

def detalles_casas(request, pk):
    casas = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/detallescasas.html', {'casas': casas})

#def nueva_casa(request):
#    form = PostForm()
#    return render(request, 'blog/nuevacasa', {'form': form})