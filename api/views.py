from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from .serializers import ProjectSerializer
from projects.models import Project,Review,Tag
from django.contrib import messages


@api_view(['GET'])
def getRoutes(request):
    routes=[
        {'GET':'/api/projects'},
        {'GET':'/api/projects/id'},
        {'POST':'/api/projects/id/vote'},
        {'POST':'/api/users/token'},
        {'POST':'/api/users/token/refresh'},
    ]
    return Response(routes)

@api_view(['GET'])
def getProjects(request):
    projects=Project.objects.all()
    serializer=ProjectSerializer(projects,many=True)
    return Response(serializer.data)

dic={
    'key':'key'
}
@api_view(['GET'])
def getProject(request,pk):
    project=Project.objects.get(id=pk)
    serializer=ProjectSerializer(project,many=False)
    return Response(dic)
 
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def projectVote(request,pk):
    project=Project.objects.get(id=pk)
    user=request.user.profile
    data=request.data 
    try:
        #  if user!=project.owner:
        review,created=Review.objects.get_or_create(
            owner=user,
            project=project,
            )
        review.value=data['value']
        review.save()
        project.getVoteCount
        serializer=ProjectSerializer(project,many=False)
        return Response(serializer.data)   
    except:
        messages.success(request,'Your review was successfully submitted!')

@api_view(['DELETE'])
def removeTag(request):
    tagId=request.data['tag']
    projectId=request.data['project']
    project=Project.objects.get(id=projectId)
    tag=Tag.objects.get(id=tagId)
    project.tags.remove(tag)
    return Response('Tag was deleted!')
         
    

