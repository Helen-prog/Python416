from django.db import models


class PriceCard(models.Model):
    pc_value = models.CharField(max_length=20, verbose_name="Цена")
    pc_description = models.CharField(max_length=200, verbose_name="Описание")

    def __str__(self):
        return self.pc_description

    class Meta:
        verbose_name = 'цену'
        verbose_name_plural = 'цены'


class PriceTable(models.Model):
    pt_title = models.CharField(max_length=200, verbose_name="Услуга")
    pt_old_price = models.CharField(max_length=200, verbose_name='Старая цена')
    pt_new_price = models.CharField(max_length=200, verbose_name='Новая цена')

    def __str__(self):
        return self.pt_title

    class Meta:
        verbose_name = 'услугу'
        verbose_name_plural = 'услуги'

