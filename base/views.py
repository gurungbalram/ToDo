from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ToDo

# Create your views here.
def home(request):
    todo_queryset = ToDo.objects.all()
    content = {'todo':todo_queryset}
    return render(request, 'home.html', context=content)

def create_todo(request):
    if request.method == 'POST': #Request comes from html file's form and url.
            # so we should check the request method before implementing data creation
        title = request.POST.get('title')
        description = request.POST.get('description')
        status = request.POST.get('status')
        ToDo.objects.create(title=title, description=description, status=status)
        return redirect('home') 
    content = {'method':'post'}   
    return render(request, 'create.html', context=content)

def edit_todo(request, pk):
    queryset = ToDo.objects.get(id=pk)
    if request.method == 'POST':
        queryset.title = request.POST.get('title')
        queryset.description = request.POST.get('description')
        queryset.status = request.POST.get('status')
        queryset.save()
        print(request.POST)
        return redirect('home')

    content = {'object':queryset, 'method':'edit'}
    return render(request, 'create.html', context=content)

def delete_todo(request, pk):
    queryset = ToDo.objects.get(id=pk)
    queryset.delete()
    return redirect('home')