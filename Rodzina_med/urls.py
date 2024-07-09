"""
URL configuration for Rodzina_med project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.generic import TemplateView
from main.views import (main, DoctorCreateView, DoctorListView, DoctorUpdateView, DoctorDeleteView, PostCreateView, )
from users.views import (RegisterView, LoginView, LogoutView, UserInfoView, EmailVerifyView, ResetPasswordView, 
                         ResetPasswordV2View, UserProfileUpdateView, UserListView,)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name='main'),
    path('user/registration', RegisterView.as_view(), name='registration'),
    path('confirm_email/', TemplateView.as_view(template_name='confirm_email.html'), name='confirm_email'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('user/info/', UserInfoView.as_view(), name='user_info'),
    path('verify_email/<uidb64>/<token>/', EmailVerifyView.as_view(), name='verify_email'),
    path('invalid_verify/', TemplateView.as_view(template_name='invalid_verify.html'), name='invalid_verify'),
    path('reset_password/', ResetPasswordView.as_view(), name='reset_password'),
    path('reset_password/<uidb64>/<token>/', ResetPasswordV2View.as_view(), name='reset_password'),
    path('user/update/', UserProfileUpdateView.as_view(), name='user_update'),
    path('users/', UserListView.as_view(), name='user_list'),
    path('doctor_create/', DoctorCreateView.as_view(), name='doctor_create'),
    path('doctor_list/', DoctorListView.as_view(), name='doctor_list'),
    path('doctor_update/', DoctorUpdateView.as_view(), name='doctor_update'),
    path('doctor_delete/', DoctorDeleteView.as_view(), name='doctor_delete'),
    path('post_create/', PostCreateView.as_view(), name='post_create'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)