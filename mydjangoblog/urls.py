from django.contrib import admin
from django.urls import path,include
from user import views as user_views
import django.contrib.auth.views as auth_views
from mydjangoblog import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # www.mysite.com/
    path('', include('blog.urls')),

    # www.mysite.com/register
    path('register/',user_views.register,name='register'),

    # www.mysite.com/login
    path('login/', auth_views.LoginView.as_view(template_name="user/login.html"),
    	name="login"),

    # www.mysite.com/logout
    path('logout/', auth_views.LogoutView.as_view(template_name="user/logout.html"),
    	name="logout"),

    #www.mysite.com/profile
    path('profile/', user_views.profile,name='profile'),

    #www.mysite.com/profile_update
    path('profile_update/', user_views.profile_update,name='profile_update'),

    #www.mysite.com/password_reset
    path('password_reset/',auth_views.PasswordResetView.as_view(
    	template_name="user/password_reset.html"),name="password_reset"),

    #www.mysite.com/password_reset_done
    path('password_reset_done/',auth_views.PasswordResetDoneView.as_view(
    	template_name="user/password_reset_done.html"),name="password_reset_done"),

    #www.mysite.com/password_reset_confirm
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
    	template_name="user/password_reset_confirm.html"),name="password_reset_confirm"),

    #www.mysite.com/password_reset_complete
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(
    	template_name="user/password_reset_complete.html"),name="password_reset_complete"),

]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
