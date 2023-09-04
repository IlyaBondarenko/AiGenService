from django.shortcuts import render
from django.http import HttpResponse

posts = [
{
    	'author': 'Администратор',
    	'title': 'Это первый пост',
    	'content': 'Содержание первого поста.',
    	'date_posted': '12 мая, 2022'
	},
	{
    	'author': 'Пользователь',
    	'title': 'Это второй пост',
    	'content': 'Подробное содержание второго поста.',
    	'date_posted': '13 мая, 2022'
	}
]
def home(reqest):
    context = {
        'posts': posts
    }
    return render(reqest, 'AiJpegSite/home.html', context)
def about(request):
    return render(request,'AiJpegSite/about.html',{'title':'О нас великих парашниках'})