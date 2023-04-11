from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Project,Tag
from .forms import ProjectForm
from django.contrib import messages
from .utils import searchProjects,paginateProjects
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
# Create your views here. 

def projects(request):
    search_query,projects=searchProjects(request)
    custom_range,projects=paginateProjects(request,projects,2)
    context={'plist':projects,'search_query':search_query,'custom_range':custom_range}
    return render(request,'projects/projects.html',context)

def project(request,pk):
    ProObj=Project.objects.get(id=pk)
    tags=ProObj.tags.all()
    return render(request,'projects/single-project.html',{'projectobj':ProObj,'tags':tags})

@login_required(login_url='login')
def createProject(request):
    profile=request.user.profile
    form=ProjectForm()
    if request.method=='POST':
        form=ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            project=form.save(commit=False)
            project.owner=profile
            project.save()
            messages.success(request,"Project was created successfully!")
            return redirect('projects')
    context={'form':form}
    return render(request,'projects/project-form.html',context)

@login_required(login_url='login')
def updateProject(request,pk):
    profile=request.user.profile
    project=profile.project_set.get(id=pk)
    form=ProjectForm(instance=project)
    if request.method=='POST':
        form=ProjectForm(request.POST,request.FILES,instance=project)
        if form.is_valid():
            form.save()
            messages.success(request,"Project was udapted successfully!")
            return redirect('projects')

    context={'form':form}
    return render(request,'projects/project-form.html',context)

@login_required(login_url='login')
def deleteProject(request,pk):
    profile=request.user.profile
    project=profile.project_set.get(id=pk)
    context={'object':project}
    if request.method=='POST':
        project.delete()
        messages.success(request,"Project was deleted successfully!")
        return redirect('projects')
    else:
        return render(request,'delete_template.html',context)

