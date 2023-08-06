from django.http import HttpResponse


class StripeWH_Handler:
    """Handles Stripe Webhooks"""

    def __init__(self, request):
        self.request = request


    def handle_event(self, request):
        """Handles Webhook events"""
        return HttpResponse(
            content=f'Webhook obtained: {event["type"]}',
            status=200
        )