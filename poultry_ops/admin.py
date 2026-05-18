from django.contrib import admin
from .models import FarmStatus

@admin.register(FarmStatus)
class FarmStatusAdmin(admin.ModelAdmin):
    list_display = ('single_egg_price', 'current_tray_price', 'box_price')
    
    def has_add_permission(self, request):
        # Prevent creating more than 1 status row
        if FarmStatus.objects.exists():
            return False
        return True