from django.urls import path
from .views import *

urlpatterns = [
    path('create/<int:id>', createProject, name="create project"),
    path('userprojects/<int:id>', userProjects, name="user projects"),
    path('otherprojects/<int:id>', otherProjects, name="other projects"),
    path('otherprojects/desc/<int:userID>/<int:proID>', otherProjectDesc, name="other project desc"),
<<<<<<< HEAD
    path('', home, name='home'),
    path('search/', search_projects, name='search_projects'),
=======
    path('otherprojects/desc/<int:userID>/<int:proID>/<int:commentID>', deleteComment, name="delete comment"),
>>>>>>> 08825386362b04b17bd0c64e3666f7dcea3b1e8d
]