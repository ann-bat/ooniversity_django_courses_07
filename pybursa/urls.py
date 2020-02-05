from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^courses/', include('courses.urls', namespace='courses')),
    url(r'^students/', include('students.urls', namespace='students')),
    url(r'^quadratic/results/', include('quadratic.urls')),
    url(r'^contact/$', views.contact, name="contact"),
    url(r'^student_list/$', views.student_list, name="student_list"),
    url(r'^student_detail/$', views.student_detail, name="student_detail"),
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', admin.site.urls),
]
