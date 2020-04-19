from django.shortcuts import render,redirect
from django.views.generic import CreateView,DetailView,UpdateView,DeleteView,ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.db.models import Q
# Create your views here.

from main.forms import AdditionForm
from main.models import Asset
import csv


def index(request):
	template_name='base.html'
	return render(request,template_name)

class AssetDetail(LoginRequiredMixin,DetailView):
	model=Asset

class MassAddition(LoginRequiredMixin,CreateView):
	form_class=AdditionForm
	template_name='main/addition.html'

	def get_initial(self):		
		return {'user':self.request.user}
	
	def form_valid(self,request):		

		if self.request.method=='POST':
			form=AdditionForm(self.request.POST)
			if form.is_valid():
				form.save()
				return redirect('/addition')
		else:
			form=AdditionForm()
		return render(request,self.template_name,{'form':form})

class AssetUpdate(LoginRequiredMixin,UpdateView):
	UpdateView.form_class=AdditionForm
	UpdateView.template_name='main/asset_update.html'
	UpdateView.model=Asset

	def get_absolute_url(self):
		return reverse('main:addition')

class DeleteAsset(LoginRequiredMixin,DeleteView):
	model=Asset
	success_url=reverse_lazy('main:index')

@login_required
def statusview(request,pk):
	sc=Asset.objects.get(pk=pk)
	sc.update_status()
	return redirect('/search/')

@login_required
def MassRetirement(request):
	rasset=Asset.objects.filter(status='to_retire')
	return render(request,'main/retirement.html',{'rasset':rasset})
@login_required
def retire_update(request):
	rasset=Asset.objects.filter(status='to_retire')
	for r in rasset:
		r.update_retirement()
	return redirect('/mass-retirement')

@login_required
def depreciateview(request):
	single_asset=Asset.objects.filter(asset_cost__gt=0)
	return render(request,'main/depreciation.html',{'single_asset':single_asset})

@login_required
def depreciate_update(request):
	single_asset=Asset.objects.filter(asset_cost__gt=0)
	for rs in single_asset:
		rs.update_depreciation()
	return HttpResponse("Depreciation performed successfully")
	
@login_required
def SearchView(request):
	template_name='main/asset_search.html'
	if request.method =='GET':
		query=request.GET.get('q')
		submitbutton=request.GET.get('submit')

		if query is not None:
			results=Asset.objects.filter(Q(tag_number__icontains=query)|Q(asset_description__icontains=query))
			return render(request,template_name,{'results':results,'submitbutton':submitbutton}) 		 	
		else:
			return render(request,template_name)
	else:
		return render(request,template_name)

@login_required
def RegisterView(request):
	template_name='main/asser_register.html'
	query=Asset.objects.all()
	return render(request,template_name,{'query':query})

@login_required
def register_download(request):
	response=HttpResponse(content_type='text/csv')
	response['Content-Disposition']='attachment;filename="asset_register.csv"'
	query=Asset.objects.all()

	writer=csv.writer(response)
	writer.writerow(['DESCRIPTION','TAG NUMBER','SERIAL NUMBER','CATEGORY','COST','MONTHLY DEPRECIATION','TOTAL_DEPRECIATION','CURRENT COST','LOCATION','SUPPLIER','DATE_IN_SERVICE','STATUS'])
	
	for rows in query:
		writer.writerow([rows.asset_description,rows.tag_number,rows.serial_number,rows.category,rows.asset_cost,rows.monthly_depreciation,rows.total_depreciation,rows.current_cost,rows.location,rows.supplier,rows.date_in_service,rows.status])
	

	return response

@login_required
def retirement_download(request):
	response=HttpResponse(content_type='text/csv')

	response['Content-Disposition']='attachment;filename="retirement.csv"'
	retired_assets=Asset.objects.filter(current_cost=0)
	writer=csv.writer(response)

	writer.writerow(['DESCRIPTION','TAG NUMBER','SERIAL NUMBER','CATEGORY','COST','CURRENT COST',])

	for rows in retired_assets:
		#writer.writerow(['DESCRIPTION','TAG NUMBER','SERIAL NUMBER','CATEGORY','COST','CURRENT COST'])
		writer.writerow([rows.asset_description,rows.tag_number,rows.serial_number,rows.category,rows.asset_cost,rows.current_cost])
	return response

