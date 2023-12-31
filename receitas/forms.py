from django import forms
from django.forms import ModelForm
from .models import Post, Comment

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = [
            'name',
            'ingredientes',
            'desc',
            'modo_de_preparo',
            'foto_url',
        ]
        labels = {
            'name': 'Título',
            'ingredientes': 'Ingredientes',
            'desc':'Descrição',
            'modo_de_preparo':'Modo de Preparo',
            'foto_url': 'URL da Foto da Comida',
        }

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = [
            'author',
            'text',
        ]
        labels = {
            'author': 'Usuário',
            'text': 'Comentário',
        }