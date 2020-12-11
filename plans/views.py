from django.shortcuts import render
from .models import Plan

# Create your views here.


def all_plans(request):
    """ A view to show the workout plans """

    plans = Plan.objects.all()

    context = {
        'plans': plans
    }
    return render(request, "plans/plans.html", context)
