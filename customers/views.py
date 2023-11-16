from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.urls import reverse

from audit.signals import model_saved

from .forms import CustomerCreateForm, CustomerUpdateForm
from .models import Customer


# Create your views here.
@require_http_methods(['GET'])
def index(request):
    customers = Customer.objects.select_related('user').all()
    return render(request, 'customers/index.html', {'customers': customers})


@require_http_methods(['GET', 'POST'])
def update_customer(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    form = CustomerUpdateForm(request.POST or None, instance=customer)
    if request.method == 'GET':
        return render(request, 'customers/customer_update.html', {'customer': customer, 'form': form})
    if request.method == 'POST':
        if form.is_valid():
            customer = form.save()
            return HttpResponseRedirect(reverse('customers:customer-update', args=[pk]))
        return render(request, 'customers/customer_update.html', {'customer': customer, 'form': form})



@require_http_methods(['GET', 'POST'])
def add_customer(request):
    form = CustomerCreateForm(request.POST or None)
    if request.method == 'GET':
        return add_customer_get(request, form)
    if request.method == 'POST':
        return add_customer_post(request, form)


def add_customer_get(request, form):
    return render(request, 'customers/customer_add.html', {'form': form})


def add_customer_post(request, form):
    if form.is_valid():
        customer = form.save()
        # normally send user as well but it's not set up
        model_saved.send(Customer, instance=customer, action='created')  # Sends the model_saved signal
        return HttpResponseRedirect(reverse('customers:customer-update', args=[customer.pk]))
    return render(request, 'customers/customer_add.html', {'form': form})
