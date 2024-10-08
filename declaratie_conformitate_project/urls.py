from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.conf import settings
from django.conf.urls.static import static
from authentication.reset_password.reset_password_forms import CustomResetPasswordForm, CustomSetPasswordForm
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('edeclaratieadmin/', admin.site.urls),
    path('', include('main.urls')),
    path('', include('users.urls')),
    path('', include('companies.urls')),
    path('', include('django.contrib.auth.urls')),
    path('', include('authentication.urls')),
    path('', include('create_declaration.urls')),
    path('', include('contact_us.urls')),
    #reset password urls 
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="reset_password_html/reset_password.html", form_class=CustomResetPasswordForm), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="reset_password_html/password_reset_done.html"), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="reset_password_html/password_reset_confirm.html", form_class=CustomSetPasswordForm), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="reset_password_html/password_reset_complete.html"), name='password_reset_complete'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
