from django.contrib import admin
import csv
from django.http import HttpResponse
from .models import MenuItem , NewsLetter

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
admin.site.site_header=('AmanteDelCaffe Aministration')



class MenuAdmin(admin.ModelAdmin):
    list_display=('item_name','item_price','item_category')

class EmailNewsLetter(admin.ModelAdmin , ExportCsvMixin):
    list_display=('email_address','email_name','telephone_number','description')
    actions = ["export_as_csv"]

admin.site.register(MenuItem, MenuAdmin)
admin.site.register(NewsLetter, EmailNewsLetter)