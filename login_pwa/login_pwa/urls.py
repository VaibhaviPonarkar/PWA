"""login_pwa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from login import views
from django.views.generic import RedirectView, TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sw.js', (TemplateView.as_view(template_name="sw.js", content_type='application/javascript', )), name='sw.js'),
    path('', views.base, name='base'),
    path('base/', views.base,name='base'),
    path('', views.sign_up, name='sign_up'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('user_login/', views.user_login, name='user_login'),
    path('git/', views.git_view, name='git_view'),
    path('webpush/', include('webpush.urls')),
    path('push/', views.push_view, name='push_view'),
    path("stock_insert", views.stock_view, name="stock_insert"),
    path("stock_fetch", views.stock_fetch, name="stock_insert"),
    path("stock_disp", views.stock_disp, name="stock_disp"),
    path("stock_update", views.stock_update, name="stock_update"),

]
