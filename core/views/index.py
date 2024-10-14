from django.shortcuts import render, redirect
from core.models.contact import Contact 


def index_view(request):
    '''Trang chủ'''
    return render(request, 'core/index.html', status=200)


def about_view(request):
    '''Trang giới thiệu'''
    return render(request, 'core/about.html', status=200)


def activities_view(request):
    '''Trang hoạt động'''
    return render(request, 'core/activities.html', status=200)


def contact_view(request):
    '''Trang liên hệ tư vấn'''
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        title = request.POST.get('title')
        content = request.POST.get('content')

        contact = Contact.objects.create(
            name=name,
            email=email,
            phone=phone,
            title=title,
            content=content,
        )

        return render(request, 'core/contact-success.html', status=200)


    return render(request, 'core/contact.html', status=200)


def login_view(request):
    return render()


def register_view(request):
    return render()
