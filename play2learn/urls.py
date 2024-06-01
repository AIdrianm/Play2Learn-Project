from django.contrib import admin
from django.urls import path, include
from users import views as user_views

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),
    path('admin/doc/', include('django.contrib.admindocs.urls')),

    # Accounts
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('allauth.urls')),  
    
    # User Management
    path('account/', user_views.account, name='account'),

    # Local Apps
    path('', include('pages.urls')),
    path('reviews/', include('reviews.urls')),
    path('games/', include('games.urls')),  # Include games app URLs
]
