from django.urls import path
from crud.api import views


urlpatterns = [
    path('stuinfo/<int:pk>',views.StudentDetails.as_view()),
    path('stuinfo/',views.StudentList.as_view()),
    path('stucreate/',views.CreateStudent.as_view()),
    path('updatestu/<int:pk>',views.UpdateStudent.as_view()),
    path('deletestu/<int:pk>',views.DeleteStudent.as_view()),

]