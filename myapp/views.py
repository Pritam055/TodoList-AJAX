from django.db import connections
from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse

from .models import Todo
from .forms import TodoForm
# Create your views here.

class HomeView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'form': TodoForm(),
            'todo_list': Todo.objects.all().order_by('complete')
        }
        return render(request,'myapp/home.html', context)

    def post(self, request, *args, **kwargs):
        form = TodoForm(request.POST)
        if form.is_valid():
            title =form.cleaned_data['title']
            desc = form.cleaned_data['description']
            comp = form.cleaned_data['complete']
            tid = request.POST.get('tid')
            
            if tid:
                todo = Todo.objects.get(id=tid)
                todo.title = title
                todo.description = desc
                todo.complete = comp
                print(comp)
            else:
                todo = Todo(title=title, description=desc, complete=comp)
    
            todo.save()
            todos = Todo.objects.values().order_by('complete')
            todo_list = list(todos)
            context = {
                'status': 'success',
                'todo_list': todo_list
            }
            return JsonResponse(context)
        else:
            return JsonResponse({"status": 'fail'})


class DeleteView(View):

    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        tid = request.POST.get("tid")
        # print(tid)
        try:
            todo = Todo.objects.get(id=tid)
            todo.delete()
            return JsonResponse({"status": "success"})
        except:
            return JsonResponse({'status':'fail'})


class EditView(View): 
    def get(self, request, *args, **kwargs):
        tid = request.GET.get('tid')
        todo = Todo.objects.get(id=tid)  
        todo =  {"id": todo.id, "title": todo.title, "description": todo.description, "complete": todo.complete} 
        return JsonResponse(todo)