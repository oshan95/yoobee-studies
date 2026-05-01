
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

def upload_page(request):
    image_url = None
    if request.method == 'POST' and request.FILES.get('image'):
        image = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        image_url = fs.url(filename)

    return render(request, 'upload.html', {'image_url': image_url})
