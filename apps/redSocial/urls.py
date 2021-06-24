from re import template
from django.urls import path
from.import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path ('', views.inicio),
    path ('feed',views.feed),
    path('perfil', views.profile),
    path('perfil/<int:id>', views.profile),
    path('register', views.register),
    path ('login', LoginView.as_view(template_name= 'login.html'),name ='login'),
    path ('logout', LogoutView.as_view(),name ='logout'),
    path ('post', views.post)


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)