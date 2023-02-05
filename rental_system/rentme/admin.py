from django.contrib import admin
from .models import Property, Landlord, Tenant, Employee, MaintenanceRequest, MaintenanceTask, Payment

# Register your models here.

admin.site.register(Property)
admin.site.register(Landlord)
admin.site.register(Tenant)
admin.site.register(Employee)
admin.site.register(MaintenanceRequest)
admin.site.register(MaintenanceTask)
admin.site.register(Payment)