from django.urls import path
from .views import TeacherListView, TeacherCreateView , TeacherDetailView 

urlpatterns = [
    path('', TeacherListView.as_view(), name='teacher_list'),
    path('create/', TeacherCreateView.as_view(), name='teacher_create'),  # POST para criar professor
    path('<int:teacher_id>/', TeacherDetailView.as_view(), name='teacher_detail'),
]