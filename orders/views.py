import stripe
from django.shortcuts import render
from django.contrib.auth.models import Permission
from django.views.generic import TemplateView
from django.conf import settings


stripe.api_key = settings.STRIPE_TEST_SECRET_KEY

class OrdersView(TemplateView):
    template_name = 'orders/purchase.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stripe_key'] = settings.STRIPE_TEST_PUBLISHABLE_KEY
        return context


def charge(request):
    # get permission
    standard_pack_permission = Permission.objects.get(codename='standard_pack')

    # current user
    user = request.user

    # add permission to user
    user.user_permissions.add(standard_pack_permission)

    # charging payment
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=4000,
            currency='usd',
            description='Buy all books',
            source=request.POST.get('stripeToken')
        )
    return render(request, 'orders/charge.html')