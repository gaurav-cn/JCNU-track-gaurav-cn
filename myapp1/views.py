from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from myapp1.models import User, Project, Project_User
from django.views.decorators.csrf import csrf_exempt
from rest_framework_swagger import renderers
from rest_framework.decorators import api_view, renderer_classes
from django.utils.decorators import method_decorator
import json
from json import JSONDecodeError

def index(request):
    return HttpResponse("CN-Assignment1!")

def exception_handler(function):
    def wrapper(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except JSONDecodeError as e:
            response = {"error": "Invalid json data"}
            return HttpResponse(json.dumps(response), status = 400)
        except Exception as e:
            response = {"error": str(e)}
            return HttpResponse(json.dumps(response), status = 400)
        
    return wrapper

@method_decorator(csrf_exempt, name='dispatch')
class UserView(View):
    @exception_handler
    def get(self, request):
        response = [{"user_id": user.id, "name": user.name} for user in User.objects.all()]
        return HttpResponse(json.dumps(response), status = 200, content_type = "application/json")

    @exception_handler
    def post(self, request):
        json_data = json.loads(request.body.decode("utf-8"))
        u = User(name = json_data.get("name"))
        u.save()
        return HttpResponse(status = 201)

@method_decorator(csrf_exempt, name='dispatch')
class ProjectView(View):
    @exception_handler
    def get(self, request):
        response = [project.get_details() for project in Project.objects.all()]
        return HttpResponse(json.dumps(response), status = 200, content_type = "application/json")

    @exception_handler
    def post(self, request):
        json_data = json.loads(request.body.decode("utf-8"))
        p = Project(name = json_data.get("name"))
        p.save()
        return HttpResponse(status = 201)

@csrf_exempt
@exception_handler
def assign_users(request, project_id):
    json_data = json.loads(request.body.decode("utf-8"))
    project = Project.objects.get(id = project_id)
    for user_id in json_data.get("users"):
        user = User.objects.get(id = user_id)
        Project_User.objects.create(user = user, project = project)
    return HttpResponse(status = 201)

@csrf_exempt
@exception_handler
def assign_mentor(request, project_id, user_id):
    Project_User.objects.create(user_id = user_id, project_id = project_id, is_mentor = True)
    return HttpResponse(status = 201)

@api_view(['GET'])
@exception_handler
def get_mentees(request, user_id):
    response = []
    s = set()
    projects = [row.project_id for row in Project_User.objects.filter(user_id = user_id, is_mentor = True)]
    for row1 in Project_User.objects.filter(is_mentor = False, project_id__in = projects):
        s.add(int(row1.user_id))
    for id in s:
        user = User.objects.get(id = id)
        response.append({
            "user_id": user.id,
            "name": user.name
        })
    return HttpResponse(json.dumps(response), content_type = "application/json", status = 200)

@api_view(['GET'])
@exception_handler
def get_mentoring_projects(request, user_id):
    response = []
    for row in Project_User.objects.filter(user_id = user_id, is_mentor = True):
        response.append({
            "project_id": row.project.id,
            "name": row.project.name
            })
    return HttpResponse(json.dumps(response), content_type = "application/json", status = 200)

@api_view(['GET'])
@exception_handler
def get_users_and_mentors(request, project_id):
    response = Project.objects.get(id = project_id).get_details()
    return HttpResponse(json.dumps(response), content_type = "application/json", status = 200)
        
    
