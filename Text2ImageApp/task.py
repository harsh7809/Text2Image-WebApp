from celery import shared_task
from .models import GeneratedImage
import requests


@shared_task
def generate_image_task(prompt):
    api_key='Enter your api-key'
    generated_image_url = None
      
    response = requests.post(
            "https://api.stability.ai/v2beta/stable-image/generate/sd3",
            headers={
                "Authorization": "Bearer" + api_key,
                "Accept": "image/*"
            },
            files={"none": ''},
            data={
                "prompt": prompt,
                "output_format": "jpeg",
            },
        )
       
    if response.status_code == 200:
            # Save image to database
        generated_image = GeneratedImage.objects.create()
        generated_image.image.save(f'generated_image{prompt}.jpeg', response.content, save=True)
        generated_image_url = generated_image.image.url
            
    return   generated_image_url
    