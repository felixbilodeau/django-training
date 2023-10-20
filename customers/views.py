from django.shortcuts import render

from .models import Customer


# Create your views here.
def index(request):
    customers = Customer.objects.select_related('user').all()
    return render(request, 'customers/index.html', {'customers': customers})
