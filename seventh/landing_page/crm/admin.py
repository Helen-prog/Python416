from django.contrib import admin
from .models import Order, StatusCrm, CommentCrm


class Comment(admin.StackedInline):
    model = CommentCrm
    fields = ('comment_dt', 'comment_text')
    readonly_fields = ('comment_dt',)
    extra = 0


class OrderAdm(admin.ModelAdmin):
    list_display = ('id', 'order_status', 'order_name', 'order_phone', 'order_dt')
    list_display_links = ('id', 'order_name')
    list_editable = ('order_status', 'order_phone')
    search_fields = ('id', 'order_name', 'order_phone', 'order_dt')
    list_filter = ('order_status',)
    fields = ('id', 'order_status', 'order_dt', 'order_name', 'order_phone')
    readonly_fields = ('id', 'order_dt')
    inlines = [Comment]
    list_per_page = 10


admin.site.register(Order, OrderAdm)
admin.site.register(StatusCrm)
admin.site.register(CommentCrm)
