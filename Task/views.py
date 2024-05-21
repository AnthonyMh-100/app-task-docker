from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from .forms import TaskForm
from .models import Task
from django.core.paginator import Paginator
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from django.contrib.auth.models import User
# Create your views here.

def view_form(request):
    if request.method == 'POST':
        task_form = TaskForm(request.POST)
        if task_form.is_valid():
            form = task_form.cleaned_data
            Task.objects.create(title=form['title'],
                                 description=form['description'],
                                 customer=form['customer'],
                                 date_from=form['date_from'],
                                 date_to=form['date_to'],
                                 user_id=request.user.id,
                                 state='backlog')
        return redirect('Task:home_task')

    else:
        task_form = TaskForm()
        return render(request,'forms/form_task.html',{"task_form":task_form})

def edit_form(request,task_id):
    
    task = get_object_or_404(Task,id=task_id)
    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.customer = request.POST.get('customer')
        task.date_from = request.POST.get('date_from')
        task.date_to = request.POST.get('date_to')
        task.save()
        
        return redirect('Task:index')
    else:
        
        return render(request,'forms/form_edit.html',{'task':task})
    

@login_required
def view_backlog(request):
    tasks = Task.objects.filter(user_id=request.user.id,state='backlog').order_by('-title')
  
    paginator = Paginator(tasks,6)
    page_number = request.GET.get('page',1)
    tasks_backlog = paginator.page(page_number)
    return render(request,'cards/task_backlog.html',{"tasks_backlog":tasks_backlog,'long':len(list(tasks_backlog))})


@login_required
def change_doing(request,task_id):
    task = get_object_or_404(Task,id=task_id,user_id=request.user.id)
    task.state = 'doing'
    task.save()
    return redirect('Task:home_task')

@login_required
def change_done(request,task_id):
    task = get_object_or_404(Task,id=task_id,user_id=request.user.id)
    task.state = 'done'
    task.save()
    return redirect('Task:home_task')


@login_required
def task_doing(request):
    tasks = Task.objects.filter(user_id=request.user.id,state='doing')
  
    paginator = Paginator(tasks,6)
    page_number = request.GET.get('page',1)
    task_doing = paginator.page(page_number)
    
    return render(request,'cards/task_doing.html',{'task_doing':task_doing})

@login_required
def view_index(request):
    task_backlog = Task.objects.filter(user_id=request.user.id,state='backlog').count()
    task_doing = Task.objects.filter(user_id=request.user.id,state='doing').count()
    task_done = Task.objects.filter(user_id=request.user.id,state='done').count()
    
    task_total = Task.objects.filter(user_id=request.user.id).count()
    
    
    return render(request,'cards/index.html',{
        'task_backlog':task_backlog,
        'task_doing':task_doing,
        'task_done':task_done,
        'task_total':task_total,
    })

@login_required
def view_task_completed(request):
    # tasks = Task.objects.all()
    tasks = Task.objects.filter(completed=True,user_id=request.user.id).order_by('-title')
    paginator = Paginator(tasks,6)
    page_number = request.GET.get('page',1)
    p_tasks = paginator.page(page_number)
        
    return render(request,'cards/task_completed.html',{"p_tasks":p_tasks ,'long':len(list(p_tasks))})

def one_task(request,task_id):
    task = get_object_or_404(Task,id=task_id,user_id=request.user.id)
    
    return render(request,'cards/task.html',{'task':task})

def completed_task(request,task_id):
    task = get_object_or_404(Task,id=task_id)
    task.completed = True
    task.save()    
    return redirect('Task:index')

def delete_task(request,task_id):
    task = get_object_or_404(Task,id=task_id,user_id=request.user.id)
    task.delete()
    
    return redirect('Task:home_task')
    

@login_required
def view_home(request):
    
    tasks_backlog = Task.objects.filter(user_id=request.user.id, state='backlog').order_by('-id')
    tasks_doing = Task.objects.filter(user_id=request.user.id, state='doing').order_by('-id')
    tasks_done = Task.objects.filter(user_id=request.user.id, state='done').order_by('-id')
    
    tasks_backlog_pag = Paginator(tasks_backlog,4)
    page_number = request.GET.get('backlog',1)
    tasks_backlog_paginate = tasks_backlog_pag.page(page_number)
    
    tasks_doing_pag = Paginator(tasks_doing,4)
    page_number = request.GET.get('doing',1)
    tasks_doing_paginate = tasks_doing_pag.page(page_number)
    
    tasks_done_pag = Paginator(tasks_done,4)
    page_number = request.GET.get('done',1)
    tasks_done_paginate = tasks_done_pag.page(page_number)
    
    
    
    return render(request, 'cards/home.html', {
        "tasks_backlog": tasks_backlog_paginate,
        "tasks_doing": tasks_doing_paginate,
        "tasks_done": tasks_done_paginate,
    })


def view_login(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST.get('username'),
        password = request.POST.get('password'))
        
        if user is not None:
            if user.is_active:
                login(request,user)
                return redirect('Task:home_task')
            else:
                return HttpResponse('Disables account')
        else:
            return HttpResponse('Invalid login')
    else:
        return render(request,'login.html')

def view_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username=username, email=email, password=password)
            login(request,user)
            return redirect('Task:home_task')
            
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def view_logout(request):
    logout(request)
    return redirect('Task:login_task')