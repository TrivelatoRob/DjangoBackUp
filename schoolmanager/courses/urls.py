from django.urls import path
from .views import CoursesListView, CoursesDetailView, CoursesCreateView

urlpatterns = [
    path('', CoursesListView.as_view(), name='courses_list'),
    path('create/', CoursesCreateView.as_view(), name='courses_create'),  # POST para criar curso
    path('edit/<int:courses_id>/', CoursesDetailView.as_view(), name='courses_detail'),
]