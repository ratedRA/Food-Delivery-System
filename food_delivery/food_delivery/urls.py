"""food_delivery URL Configuration

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
from django.urls import path, include, re_path
from home.views import home
from django.conf.urls.static import static
from django.conf import settings

app_name =(

			'home',
			'providers',
			'delivery_partners',
            'user_profiles'
	)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('home.urls')),
    path('providers/', include('providers.urls')),
    path('providers/', include('user_profiles.urls')),
    re_path('api/(?P<version>(v1|v2))/', include('providers.urls')),
    re_path('api/(?P<version>(v1|v2))/', include('user_profiles.urls'))
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
