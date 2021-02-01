from django.contrib import admin
from django.urls import path, include
from enroll import views as enroll_v
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', enroll_v.home, name="home"),
    path('register/', enroll_v.register, name="register"),
    path('login/', auth_views.LoginView.as_view(template_name='enroll/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='enroll/logout.html'), name="logout"),
    path('miscursos/', enroll_v.miscursosview, name="miscursos"),
    path('miscursos/<str:course_id>', enroll_v.miscursosDitView, name="miscursosDitView"),
    path('detail/<str:course_id>', enroll_v.detailcourseview, name="detail")
]
