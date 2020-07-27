from .models import image
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home/index.html')


def Submissions(request):
    if request.method == 'POST':
        img_name = request.POST.get('img_name')
        img_desc = request.POST.get('img_desc')
        img_by = request.POST.get('img_by')
        img_url = request.POST.get('img_url')
        s = image(img_name = img_name,img_desc = img_desc,img_by = img_by,img_url = img_url)
        s.save()

    show = image.objects.all()
    context = {
        'show' : show
        }
    return render(request,'home/sub.html',context)