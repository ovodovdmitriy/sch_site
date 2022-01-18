from django.shortcuts import render

def index(request):
    return render(request,'mainapp/mainpage.html')

def babush(request):
    return render(request,'mainapp/babush.html')

def sviblovo(request):
    return render(request, 'mainapp/sviblovo.html')

def aleks(request):
    return render(request, 'mainapp/alekseevsky.html')

def smedved(request):
    return render(request, 'mainapp/sevmedvedkovo.html')

def altu(request):
    return render(request, 'mainapp/altufevsky.html')

def bibi(request):
    return render(request, 'mainapp/bibirevo.html')

def buty(request):
    return render(request, 'mainapp/butyrsky.html')

def lian(request):
    return render(request, 'mainapp/lianozovo.html')

def los(request):
    return render(request, 'mainapp/losinoostrovsky.html')

def marf(request):
    return render(request, 'mainapp/marfino.html')

def mary(request):
    return render(request, 'mainapp/marynaroshya.html')

def ost(request):
    return render(request, 'mainapp/ostankinsky.html')

def otr(request):
    return render(request, 'mainapp/otradnoye.html')

def ros(request):
    return render(request, 'mainapp/rostokino.html')

def sev(request):
    return render(request, 'mainapp/severniy.html')

def ymedved(request):
    return render(request, 'mainapp/yujnoyemedvedkovo.html')

def yar(request):
    return render(request, 'mainapp/yaroslavskiy.html')
