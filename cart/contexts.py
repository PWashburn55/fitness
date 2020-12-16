from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from plans.models import Plan


def cart_contents(request):

    cart_items = []
    total = 0
    plan_count = 0
    cart = request.session.get('cart', {})

    for item_id, item_data in cart.items():
        if isinstance(item_data, int):
            plan = get_object_or_404(Plan, pk=item_id)
            total += item_data * plan.price
            plan_count += item_data
            cart_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'plan': plan,
            })

    grand_total = total

    context = {
        'cart_items': cart_items,
        'total': total,
        'plan_count': plan_count,
        'grand_total': grand_total,
    }

    return context