from django.contrib import admin
from .models import ProductCategory, Product, Photo

from django.urls import path
from django.shortcuts import render, redirect
from django.contrib import messages
from django import forms


class CsvImportForm(forms.Form):
    csv_uploader = forms.FileField()


class ProductCategoryAdmin(admin.ModelAdmin):
    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path("upload-csv/", self.upload_csv)]
        return new_urls + urls

    def upload_csv(self, request):
        if request.method == "POST":
            csv_file = request.FILES['csv_uploader']

            if not csv_file.name.endswith('.csv'):
                messages.warning(request, "Ошибочный тип файла")
                return redirect('.')

            file_data = csv_file.read().decode("utf-8")
            csv_data = file_data.split("\n")

            for x in csv_data:
                fields = x.split(",")
                # print(fields)
                ProductCategory.objects.update_or_create(
                    id=fields[0],
                    name=fields[1],
                    description=fields[2]
                )
            return redirect('admin:index')

        form = CsvImportForm()
        data = {"form": form}
        return render(request, "admin/csv_uploader.html", data)


admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(Product)
admin.site.register(Photo)

