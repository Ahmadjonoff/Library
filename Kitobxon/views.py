from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import *
from .models import *

def hello(request):
    return HttpResponse('Hello World!')

def Ustoz1(request):
    t1 = Muallif.objects.get(id = 2)
    return HttpResponse(t1)

def muallif(request):
    return HttpResponse(Muallif.objects.all().order_by('tugilgan_sanasi').first())

def record(request):
    return HttpResponse(Muallif.objects.get(id = 1))

def ilmiy(request):
    return HttpResponse(Kitob.objects.filter(janr = 'ilmiy').first())

def erkak(request):
    return HttpResponse(Muallif.objects.exclude(familiyasi__endswith = 'a').first())

def home(request):
    return render(request, "home.html")

def Mualliflar(request):
    if request.method == 'POST':
        Muallif.objects.create(
            ismi = request.POST['ism'],
            familiyasi = request.POST['fam'],
            tugilgan_sanasi = request.POST['sana'],
            asarlar_soni = request.POST['son']
        )
        return redirect('/mualliflar/')
    mualliflar = Muallif.objects.all()
    return render(request, 'mualliflar.html', {'Yozuvchilar' : mualliflar})

def Kitoblar(request):
    if request.method == 'POST':
        m = Muallif.objects.get(id = request.POST['muallif'])
        forma = KitobForm(request.POST)
        if forma.is_valid():
            forma.save()
        return redirect('/kitoblar/')

    f = KitobForm()
    m = Muallif.objects.all()
    books = Kitob.objects.all()
    return render(request, 'kitoblar.html', {'kitoblarim' : books, 'mualliflar' : m, 'forma' : f})

def records(request):
    if request.method == 'POST':
        forma = RecordForm(request.POST)
        if forma.is_valid():
            forma.save()
        return redirect('/recordlar/')
    f = RecordForm()
    Records = Record.objects.all()
    books = Kitob.objects.all()
    return render(request, 'recordlar.html', {'Records' : Records, 'Kitoblar' : books, 'forma' : f})

def kitob_ochir(request, pk):
    Kitob.objects.get(id = pk).delete()
    return redirect('/kitoblar/')

def edit_book(request, son):
    if request.method == 'POST':
        m = Muallif.objects.get(id = request.POST['muallif'])
        b = Kitob.objects.get(id = son)
        b.nomi = request.POST['nom']
        b.muallif = m
        b.sahifa = request.POST['son']
        b.janr = request.POST['janr']
        b.save()
        return redirect('/kitoblar/')

    book = Kitob.objects.get(id = son)
    mualliflar = Muallif.objects.all()
    return render(request, 'edit_book.html', {'book': book, 'mualliflar' : mualliflar})

def edit_auth(request, son):
    if request.method == 'POST':
        auth = Muallif.objects.get(id = son)
        auth.ismi = request.POST['ism']
        auth.familiyasi = request.POST['fam']
        auth.asarlar_soni = request.POST['son']
        auth.save()
        return redirect('/mualliflar/')

    m = Muallif.objects.get(id = son)
    return render(request, 'edit.html', {'auth' : m})