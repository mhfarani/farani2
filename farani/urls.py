
from django.contrib import admin
from django.contrib.auth import views as auth_veiws
from django.urls import path,include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
    path('accounts/', include('allauth.urls')),
    path('login/',auth_veiws.LoginView.as_view(template_name='user/login.html'),name='login'),
    path('logout/', auth_veiws.LogoutView.as_view(template_name='user/logout.html'), name='logout'),
     path('', include('user.urls')),
]
