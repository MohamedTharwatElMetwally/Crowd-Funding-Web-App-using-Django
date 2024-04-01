from django.urls import path
from .views import *

urlpatterns = [
    path('create/<int:id>', createProject, name="create project"),
    path('userprojects/<int:id>', userProjects, name="user projects"),
    path('otherprojects/<int:id>', otherProjects, name="other projects"),
    path('otherprojects/desc/<int:userID>/<int:proID>', otherProjectDesc, name="other project desc"),
    path('', home, name='home'),
    path('search/', search_projects, name='search_projects'),
    path('otherprojects/desc/<int:userID>/<int:proID>/<int:commentID>', deleteComment, name="delete comment"),
]