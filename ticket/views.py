from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Ticket
from django.urls import reverse_lazy


class TicketListView(ListView):
    model = Ticket
    template_name = 'ticket/ticket_list.html'


class TicketDetailView(DetailView):
    model = Ticket
    template_name = 'ticket/ticket_detail.html'


class TicketCreateView(CreateView):
    model = Ticket
    template_name = 'ticket/ticket_new.html'
    fields = '__all__'


class TicketUpdateView(UpdateView):
    model = Ticket
    template_name = 'ticket/ticket_edit.html'
    fields = '__all__'


class TicketDeleteView(DeleteView):
    model = Ticket
    template_name = 'ticket/ticket_delete.html'
    success_url = reverse_lazy('ticket_list')
