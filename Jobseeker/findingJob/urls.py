from django.urls import path

from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [

    path('register/', views.register, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    path('', views.home, name="home"),
    path(r'^jobList/$', views.jobList, name="jobList"),
    path('jobDetail/<int:jobid>', views.jobDetail, name="jobDetail"),
    path('jobPost/', views.jobPost, name="jobPost"),

    path('jobpostedListedperuser/', views.jobpostedListedperuser, name="jobpostedListedperuser"),
    path('delete_jobDetail/<str:pk>/', views.deletejobDetail, name="delete_jobDetail"),
    path('update_jobDetail/<str:pk>/', views.updatejobDetail, name="update_jobDetail"),
    path(r'^contact/', views.contact, name="contact"),
    path(r'^about/$', views.about, name="about"),

    path(r'^error404/$', views.error404, name="error404"),
    path(r'^termandcondition/$', views.termandcondition, name="termandcondition"),
    path(r'^PrivacyPolicy/$', views.PrivacyPolicy, name="PrivacyPolicy"),
    path(r'^Cookies/$', views.Cookies, name="Cookies"),


]
