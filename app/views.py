from django.shortcuts import render, redirect
from django.db.models import Sum
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.views.generic import CreateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
# Create your views here.
from .forms import  PISubModelForm, RegistrationForm, PIModelForm
from .decorators import unauthenticated_user
import time

@login_required(login_url="login")
def home(request):
    orders = 10
    # customers = Customer.objects.all()
    pimodel = PIModel.objects.values('model_pk', 'model_name', 'description', 'tags', 'insourcing_or_not', 'insourcing_code')
    print(pimodel)

    # total_orders = orders.count()
    # total_customers = customers.count()

    # total_iphone_sold = Order.objects.filter(product__name='Iphone').count()

    # total_sales = Order.objects.aggregate(Sum('product__price'))['product__price__sum']

    context = {
        'total_models_explored' : pimodel.count(),
        'total_deployed' : 0,
        'total_model_insourced' : pimodel.filter(insourcing_or_not='Yes').count(),
        'pimodel' : pimodel,
        'pimodel_insourced' : pimodel.filter(insourcing_or_not='Yes')
    }
    return render(request, 'app/dashboard.html',context)
    # return HttpResponse('Hello World.')

@unauthenticated_user
def app_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect.')
    return render(request, 'app/authentication/login.html')

def app_logout(request):
	logout(request)
	return redirect('login')

@unauthenticated_user
def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            messages.success(request, 'Account was created for '+username+'.')
            return  redirect('login')
    
    context = {'form':form}
    return render(request, 'app/authentication/register.html', context)


def create_PIModel(request):
    form = PIModelForm()
    if request.method == 'POST':
        form = PIModelForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.last_updated_by = request.user
            obj.save()
            return redirect('/pimodel/show')
    
    context = {'form':form}
    return render(request, 'app/content/PIModel/create_PIModel.html',context)

def update_PIModel(request, model_pk):
    mod = PIModel.objects.get(model_pk=model_pk)
    form = PIModelForm(instance=mod)
    if request.method == 'POST':
        form = PIModelForm(request.POST, instance=mod)
        if form.is_valid():
            form.save()
            return redirect('/pimodel/show')

    context = {'form':form}
    return render(request, 'app/content/PIModel/update_PIModel.html', context)

def delete_PIModel(request, model_pk):
    PIModel.objects.filter(model_pk=model_pk).delete()
    return redirect('/pimodel/show')

def create_PISubModel(request, pk):
    form = PISubModelForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            obj = form.save(commit=False)
            obj.model_pk = PIModel(model_pk=pk)
            obj.last_updated_by = request.user
            obj.save()
            return redirect(f'/pisubmodel/show/{pk}')
    
    context = {'form':form}
    return render(request, 'app/content/PISubModel/create_PISubModel.html',context)

def show_PIModel(request):
    PIModel_rec = PIModel.objects.all()
    # PISubModel_recs = PISubModel.objects.filter(model_pk=model_pk)
    context = {
        # 'pisubmodel' : PISubModel_recs,
        'pimodel' : PIModel_rec
    }
    return render(request, 'app/content/PIModel/show_PIModel.html', context)


def show_PISubModel(request, model_pk):
    PIModel_rec = PIModel.objects.get(model_pk=model_pk)
    PISubModel_recs = PISubModel.objects.filter(model_pk=model_pk)
    context = {
        'pisubmodel' : PISubModel_recs,
        'pimodel' : PIModel_rec
    }
    return render(request, 'app/content/PISubModel/show_PISubModel.html', context)

def update_PISubModel(request, sub_model_pk):
    mod = PISubModel.objects.get(sub_model_pk=sub_model_pk)
    model_pk = PISubModel.objects.filter(sub_model_pk=sub_model_pk).values_list('model_pk_id', flat=True).first()
    form = PISubModelForm(instance=mod)
    if request.method == 'POST':
        form = PISubModelForm(request.POST, instance=mod)
        if form.is_valid():
            form.save()
            return redirect(f"/pisubmodel/show/{model_pk}")

    context = {'form':form}
    return render(request, 'app/content/PISubModel/update_PISubModel.html', context)

def delete_PISubModel(request, model_pk, sub_model_pk):
    PISubModel.objects.filter(sub_model_pk=sub_model_pk).delete()
    return redirect(f'/pisubmodel/show/{model_pk}')


def open_PISubModel(request, sub_model_pk):
    pisubmodel = PISubModel.objects.filter(sub_model_pk=sub_model_pk)
    pimodel = PIModel.objects.filter(model_pk=pisubmodel.first().model_pk_id)
    context = {'pisubmodel':pisubmodel.first(), 'pimodel' : pimodel.first()}
    if pimodel.values_list('insourcing_or_not', flat=True).first() == 'Yes':
        return render(request, 'app/content/PISubModel/insourcing_open_PISubModel.html', context)
    else:
        return render(request, 'app/content/PISubModel/open_PISubModel.html', context)

import os

def generateExcel(request):
    path = './abc.xlsx' # this should live elsewhere, definitely
    if os.path.exists(path):
        with open(path, "rb") as excel:
            data = excel.read()
        id = 'my_file'
        response = HttpResponse(data,content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=%s_Report.xlsx' % id
        return response

# Rest Framework Views

from .serializer import *
from rest_framework import viewsets

from rest_framework import generics
from rest_framework.response import Response
from rest_framework_datatables import pagination as dt_pagination


# class OrderDetailViewSet(viewsets.ModelViewSet):
#     queryset = OrderDetail.objects.all().order_by('order_detail_pk')
#     serializer_class = OrderDetailSerializer
#     pagination_class = dt_pagination.DatatablesLimitOffsetPagination
#     http_method_names = ['get', 'head']
#     # class Meta:
#     #     datatables_extra_json = ('get_options', )

# # class OrderDetailListView(generics.ListAPIView):
# #     queryset = OrderDetail.objects.all().order_by('order_detail_pk')
# #     serializer_class = OrderDetailSerializer
# #     pagination_class = dt_pagination.DatatablesLimitOffsetPagination

# #     def post(self, request, *args, **kwargs):
# #         return self.list(request, *args, **kwargs)

# class FtyTableViewSet(viewsets.ModelViewSet):
#     queryset = FtyTable.objects.all()
#     serializer_class = FtyTableSerializer
#     pagination_class = dt_pagination.DatatablesLimitOffsetPagination
#     http_method_names = ['get', 'head']


# class OrderViewSet(viewsets.ModelViewSet):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer
#     pagination_class = dt_pagination.DatatablesLimitOffsetPagination
#     http_method_names = ['get', 'head']


# class ProductViewSet(viewsets.ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     pagination_class = dt_pagination.DatatablesLimitOffsetPagination
#     http_method_names = ['get', 'head']