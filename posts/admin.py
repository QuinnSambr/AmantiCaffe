from advanced_filters.admin import AdminAdvancedFiltersMixin
from django.contrib import admin
import csv
from django.http import HttpResponse
from .models import MenuItem , NewsLetter , Staff , Customer , Inventory, Shedule ,OnlineCustomer


#Export Selected Records as Excel CSV File
class ExportCsvMixin:
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected"



# Register your models here.
admin.site.site_header=('AmanteDelCaffe Administration')

class MenuAdmin(AdminAdvancedFiltersMixin,admin.ModelAdmin):
    list_display=('item_name','item_price','item_category')

    advanced_filter_fields = (
        'item_name',
        'item_price',
        'item_category',
    )

class EmailNewsLetter(admin.ModelAdmin , ExportCsvMixin):
    list_display=('email_address','email_name','telephone_number','home_address','description')
    actions = ["export_as_csv"]

class ProfileAdmin(AdminAdvancedFiltersMixin, admin.ModelAdmin,ExportCsvMixin):
    list_display=('staff_name','staff_email','staff_address','phone_number')
    actions = ["export_as_csv"]
    # specify which fields can be selected in the advanced filter
    # creation form
    advanced_filter_fields = (
        'staff_id',
        'staff_email',
        'staff_address',
        'staff_name',
    )

class CustomerAdmin(AdminAdvancedFiltersMixin, admin.ModelAdmin):
    list_display=('customer_name','customer_username','customer_password','customer_email')
    advanced_filter_fields = (
        'customer_id',
        'customer_username',
        'customer_name',
        'customer_email',
    )

class InventoryAdmin(AdminAdvancedFiltersMixin, admin.ModelAdmin):
    list_display=('inventory_id','inventory_name','inventory_item_cat','inventory_quantity')
    advanced_filter_fields = (
        'inventory_id',
        'inventory_name',
        'inventory_item_cat',
        'inventory_quantity'
    )

class SheduleAdmin(AdminAdvancedFiltersMixin, admin.ModelAdmin,ExportCsvMixin):
    list_display=('staff_id','shedule_clockin','shedule_clockout')
    actions = ["export_as_csv"]
    
    advanced_filter_fields = (
        'staff_id',
        'shedule_clockin',
        'shedule_clockout',
    )


class OnlineCustAdmin(AdminAdvancedFiltersMixin, admin.ModelAdmin):
    list_display=('online_recipt','item_id','item_price','online_status')

    advanced_filter_fields = (
        'online_status',
        'online_recipt',
        'item_id',
        'item_price',
    )


admin.site.register(MenuItem, MenuAdmin)
admin.site.register(NewsLetter, EmailNewsLetter)
admin.site.register(Staff, ProfileAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Inventory,InventoryAdmin)
admin.site.register(Shedule,SheduleAdmin)
admin.site.register(OnlineCustomer,OnlineCustAdmin)
