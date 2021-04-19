from django.urls import path
from app1 import views
app_name="app1"

urlpatterns = [
    path('page1/',views.page1,name="page1"),
    path('page2/',views.page2,name='page2'),
    path('page3/<data>/<age1>/<email1>/',views.page3,name='page3'),
]