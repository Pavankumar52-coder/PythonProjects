# views.py
import logging
from django.shortcuts import render
from django.http import HttpResponse
import cloudinary.uploader
import cloudinary

logger = logging.getLogger(__name__)

def image_upload(request):
    if request.method == 'POST' and request.FILES.get('image'):
        image = request.FILES['image']
        try:
            logger.debug(f'Uploading image: {image}')
            response = cloudinary.uploader.upload(image)
            logger.debug(f'Cloudinary Response: {response}')
            return HttpResponse(f'Image uploaded successfully. URL: {response["url"]}')
        except Exception as e:
            logger.error(f'Error uploading image: {str(e)}')
            return HttpResponse(f'Error: {e}', status=500)
    return render(request, 'Images/image_upload.html')