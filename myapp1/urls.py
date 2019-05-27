from django.urls import path

from . import views

from rest_framework_swagger.views import get_swagger_view

urlpatterns = [
    path("", views.index, name = ""),
    path("users/", views.UserView.as_view(), name = "users"),
    path("projects/", views.ProjectView.as_view(), name = "projects"),
    path("projects/<int:project_id>/assign-users/", views.assign_users, name = "projects_assign_users"),
    path("projects/<int:project_id>/mentors/<int:user_id>/", views.assign_mentor, name = "projects_assign_mentor"),
    path("users/<int:user_id>/mentees/", views.get_mentees, name = "users_mentees"),
    path("users/<int:user_id>/mentoring-projects/", views.get_mentoring_projects, name = "users_mentoring_projects"),
    path("projects/<int:project_id>/", views.get_users_and_mentors, name = "projects_user_mentors"),
]
