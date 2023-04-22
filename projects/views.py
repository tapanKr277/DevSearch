from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Project,Tag
from .forms import ProjectForm,ReviewForm
from django.contrib import messages
from .utils import searchProjects,paginateProjects

# Create your views here. 

def projects(request):
    search_query,projects=searchProjects(request)
    custom_range,projects=paginateProjects(request,projects,6)
    context={'plist':projects,'search_query':search_query,'custom_range':custom_range}
    return render(request,'projects/projects.html',context)

def project(request,pk):
    ProObj=Project.objects.get(id=pk)
    form=ReviewForm()
    if request.method=="POST":
        form=ReviewForm(request.POST)
        review=form.save(commit=False)
        review.project=ProObj
        review.owner=request.user.profile
        review.save()
        ProObj.getVoteCount
        messages.success(request,'Your review was successfully submitted!')
        return redirect('project',pk=ProObj.id)
    tags=ProObj.tags.all()
    return render(request,'projects/single-project.html',{'projectobj':ProObj,'tags':tags,'form':form})

@login_required(login_url='login')
def createProject(request):
    profile=request.user.profile
    form=ProjectForm()
    if request.method=='POST':
        newtags=request.POST.get('newtags').replace(',', ' ').split()
        form=ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            project=form.save(commit=False)
            project.owner=profile
            project.save()
            for tag in newtags:
                tag,created=Tag.objects.get_or_create(name=tag)
                project.tags.add(tag)
            messages.success(request,"Project was created successfully!")
            return redirect('projects')
    context={'form':form,'project':project}
    return render(request,'projects/project-form.html',context)

@login_required(login_url='login')
def updateProject(request,pk):
    profile=request.user.profile
    project=profile.project_set.get(id=pk)
    form=ProjectForm(instance=project)
    if request.method=='POST':
        newtags=request.POST.get('newtags').replace(',',' ').split()
        form=ProjectForm(request.POST,request.FILES,instance=project)
        if form.is_valid():
            project=form.save()
            for tag in newtags:
                tag,created=Tag.objects.get_or_create(name=tag.lower())
                project.tags.add(tag)
            messages.success(request,"Project was udapted successfully!")
            return redirect('projects')

    context={'form':form,'project':project}
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

