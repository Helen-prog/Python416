from django.shortcuts import render
from django.views.generic import CreateView
from .forms import OrderForm
from django.urls import reverse_lazy


class OrderCreateView(CreateView):
    form_class = OrderForm
    template_name = 'orders/order-create.html'
    success_url = reverse_lazy('order-create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Store - оформление заказа"
        return context

    def form_valid(self, form):
        form.instance.initiator = self.request.user
        return super().form_valid(form)
