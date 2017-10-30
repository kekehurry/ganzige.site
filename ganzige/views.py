from django.shortcuts import HttpResponse


def get_txt(request):
    with open(MP_verify_KdrNjdeEBujKWLaZ.txt, 'r', encoding='utf-8') as f:
        text = f.read()
        f.close()
    return HttpResponse(text)


def detail(request, page, image_id):
    image = Photo.objects.get(id=image_id)
    return render(request, 'photo/detail.html', {'image': image, 'page': page})
