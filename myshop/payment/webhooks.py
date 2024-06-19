import stripe
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from orders.models import Order
from shop.models import Product
from shop.recommender import Recommender
from .tasks import payment_completed

@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None


    event = stripe.Webhook.construct_event(
                    payload,
                    sig_header,
                    settings.STRIPE_WEBHOOK_SECRET)
    try:
        pass
    except ValueError as e:
        return HttpResponse(status = 400)
    except stripe.error.SignatureVerificationError as e:
        return HttpResponse(status = 400)

    if event.type == 'checkout.session.completed':
        session = event.data.object
        if session.mode == 'payment' and session.payment_status == 'paid':
            try:
                order = Order.objects.get(id = session.client_reference_id)
            except Order.DoesNotExist:
                return HttpResponse(status = 400)
            order.stripe_id = session.payment_intent
            order.paid = True
            order.save()

            product_ids = order.items.values_list('product_id')
            products = Product.objects.filter(id__in=product_ids)
            r = Recommender()
            r.products_bought(products)

            payment_completed.delay(order.id)

    return HttpResponse(status = 200)
