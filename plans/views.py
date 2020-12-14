from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Plan

# Create your views here.


def all_plans(request):
    """ A view to show all products, including sorting and search queries """

    plans = Plan.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "No criteria entered")
                return redirect(reverse('plans'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            plans = plans.filter(queries)

    context = {
        'plans': plans,
        'search_term': query,
    }

    return render(request, 'plans/plans.html', context)


def plan_detail(request, plan_id):
    """ A view to show individual plan details """

    plan = get_object_or_404(Plan, pk=plan_id)

    context = {
        'plan': plan,
    }

    return render(request, 'plans/plan_detail.html', context)

