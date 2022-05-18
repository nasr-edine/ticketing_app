from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Ticket


class TicketTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )
        self.ticket = Ticket(
            title='A good title',
            description='Nice body content',
            assignee=self.user,
        )
        self.ticket.save()

    def test_string_representation(self):
        ticket = Ticket(title='A sample title')
        print(ticket)
        self.assertEqual(str(ticket), ticket.title)

    def test_ticket_content(self):
        self.assertEqual(f'{self.ticket.title}', 'A good title')
        self.assertEqual(f'{self.ticket.assignee}', 'testuser')
        self.assertEqual(f'{self.ticket.description}', 'Nice body content')

    def test_ticket_list_view(self):
        response = self.client.get(reverse('ticket_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ticket/ticket_list.html')
        self.assertContains(response, 'Nice body content')

    def test_post_detail_view(self):
        response = self.client.get('/tickets/1/')
        self.assertTemplateUsed(response, 'ticket/ticket_detail.html')

        no_response = self.client.get('/ticket/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertTemplateUsed(response, 'ticket/ticket_detail.html')
        self.assertContains(response, 'A good title')
