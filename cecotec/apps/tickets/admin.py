from django.contrib import admin
from cecotec.apps.tickets.models import ProductsInTicket, Ticket


# Register your models here.
class ProductsInTicketInline(admin.TabularInline):
    model = ProductsInTicket
    extra = 0


class TicketAdmin(admin.ModelAdmin):
    readonly_fields = ['id', 'total']
    search_fields = ['client__name', ]
    date_hierarchy = 'created_at'
    list_filter = ('client',)
    list_display = ('id', 'client', 'created_at')
    fields = ('id', 'client', 'total')
    inlines = [ProductsInTicketInline, ]

    def total(self, obj):
        return obj.total()


admin.site.register(ProductsInTicket)
admin.site.register(Ticket, TicketAdmin)
