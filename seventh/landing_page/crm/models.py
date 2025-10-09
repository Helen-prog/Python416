from django.db import models


class StatusCrm(models.Model):
    status_name = models.CharField(max_length=200, verbose_name='Название статуса')

    def __str__(self):
        return self.status_name

    class Meta:
        verbose_name = 'статус'
        verbose_name_plural = 'статусы'


class Order(models.Model):
    order_dt = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    order_name = models.CharField(max_length=200, verbose_name='Имя')
    order_phone = models.CharField(max_length=200, verbose_name='Телефон')
    order_status = models.ForeignKey(StatusCrm, on_delete=models.PROTECT, blank=True, null=True, verbose_name='Статус')

    def __str__(self):
        return self.order_name

    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'


class CommentCrm(models.Model):
    comment_binding = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заявка')
    comment_text = models.TextField(verbose_name='Текст комментария')
    comment_dt = models.DateTimeField(auto_now=True, verbose_name='Дата создания')

    def __str__(self):
        return self.comment_text

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'

