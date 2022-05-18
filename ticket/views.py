from django.views.generic import ListView, DetailView
from .models import Ticket


class TicketListView(ListView):
    model = Ticket
    template_name = 'ticket/ticket_list.html'


class TicketDetailView(DetailView):
    model = Ticket
    template_name = 'ticket/ticket_detail.html'
