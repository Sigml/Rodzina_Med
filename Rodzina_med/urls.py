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
from users.views import (RegisterView, LoginView, LogoutView, UserInfoView, EmailVerifyView, ResetPasswordView, 
                         ResetPasswordV2View, UserProfileUpdateView, UserListView,)
from main.views import (main, DoctorCreateView, DoctorListView, DoctorUpdateView, DoctorDeleteView, PostCreateView,
                        PostUpdateView, PostDeleteView, MessageCreateView, MessageListView, MessageUpdateView, MessageDeleteView,
                        ContactListView, ContactCreateView, ContactUpdateView, ContactDeleteView, RodoCreateView, RodoListView,
                        RodoUpdateView, RodoDeleteView, ReglaminCreateView, ReglaminListView, ReglaminUpdateView, ReglaminDeleteView,
                        FileToDownloadCreateView, FileToDownloadListView, FileToDownloadUpdateView, FileToDownloadDeleteView,
                        OffersListView, VaccinationsListView
                        )

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
    path('doctor_update/<int:pk>/', DoctorUpdateView.as_view(), name='doctor_update'),
    path('doctor_delete/<int:pk>/', DoctorDeleteView.as_view(), name='doctor_delete'),
    path('post_create/', PostCreateView.as_view(), name='post_create'),
    path('post_update/<int:pk>/', PostUpdateView.as_view(), name='post_update'),
    path('post_delete/<int:pk>/', PostDeleteView.as_view(), name='post_delete'),
    path('message_create/', MessageCreateView.as_view(), name='message_create'),
    path('message_list/', MessageListView.as_view(), name='message_list'),
    path('message_update/<int:pk>/', MessageUpdateView.as_view(), name='message_update'),
    path('message_delete/<int:pk>/', MessageDeleteView.as_view(), name='message_delete'),
    path('contact_create/', ContactCreateView.as_view(), name='contact_create'),
    path('contact_list/', ContactListView.as_view(), name='contact_list'),
    path('contact_update/<int:pk>/', ContactUpdateView.as_view(), name='contact_update'),
    path('contact_delete/<int:pk>/', ContactDeleteView.as_view(), name='contact_delete'),
    path('rodo_create/', RodoCreateView.as_view(), name='rodo_create'),
    path('rodo_list/', RodoListView.as_view(), name='rodo_list'),
    path('rodo_update/<int:pk>/', RodoUpdateView.as_view(), name='rodo_update'),
    path('rodo_delete/<int:pk>/', RodoDeleteView.as_view(), name='rodo_delete'),
    path('reglamin_create/', ReglaminCreateView.as_view(), name='reglamin_create'),
    path('reglamin_list/', ReglaminListView.as_view(), name='reglamin_list'),
    path('reglamin_update/<int:pk>/', ReglaminUpdateView.as_view(), name='reglamin_update'),
    path('reglamin_delete/<int:pk>/', ReglaminDeleteView.as_view(), name='reglamin_delete'),
    path('file_create/', FileToDownloadCreateView.as_view(), name='file_create'),
    path('file_list/', FileToDownloadListView.as_view(), name='file_list'),
    path('file_update/<int:pk>/', FileToDownloadUpdateView.as_view(), name='file_update'),
    path('file_delete/<int:pk>/', FileToDownloadDeleteView.as_view(), name='file_delete'),
    path('offers/', OffersListView.as_view(), name='offers'),
    path('vaccinations/', VaccinationsListView.as_view(), name='vaccinations'),
    path('intake_point/', TemplateView.as_view(template_name='intake_point.html'), name='intake_point'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)