from django.contrib import admin
from django.urls import include, path
from poultry_ops import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.public_homepage, name='home'),
    path('about/', views.about_page, name='about'),
    path('facilities/', views.facilities_page, name='facilities'),
    path('products/', views.products_page, name='products'),
    path('contact/', views.contact_page, name='contact'),
    
    path('', include('hr_admin.urls')),        # Your HR App
    path('farm/', include('farm_infra.urls')), # Your New Farm App
    path('ops/', include('poultry_ops.urls')),
    path('assets/', include('assets.urls')),
    path('finance/', include('supply_finance.urls')),
    path('ai_models/', include('ai_models.urls')),
    path('accounts/', include('accounts.urls')),
    path('hr_admin/', include('hr_admin.urls')),
    
    
]
