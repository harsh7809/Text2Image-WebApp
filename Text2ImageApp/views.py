from django.shortcuts import render
from celery import Celery
from Text2ImageApp.task import generate_image_task




def generate_image(request):
    if request.method == 'POST':
        prompt = request.POST['text']
        print(prompt)
        G_url= generate_image_task.delay(prompt)
        return render(request, 'home.html', {'generated_image_url': G_url})
    return render(request, 'home.html')
    
    
    
