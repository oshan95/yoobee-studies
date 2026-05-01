
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


def bmi_calculator(request):
    bmi = None
    category = None

    if request.method == "POST":
        weight = float(request.POST.get("weight"))
        height = float(request.POST.get("height"))

        height_m = height / 100
        bmi = weight / (height_m ** 2)

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal weight"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

    return render(request, "bmi.html", {"bmi": bmi, "category": category})
