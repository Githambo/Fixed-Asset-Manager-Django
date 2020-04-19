from django.db import models
from django.conf import settings
from django.urls import reverse
import datetime

# Create your models here.
class Asset(models.Model):
	CATEGORY=(
		('COMPUTERS','COMPUTER'),
		('FURNITURES','FURNITURE'),
		('OFFICE_EQUIPMENT','OFFICE EQUIPMENT'),
		('LINK_EQUIPMENT','LINK EQUIPMENT'),
		('SERVERS','SERVERS'),
		)
	BRANCH=(
		('BRANCH_1','BRANCH 1'),
		('BRANCH_2','BRANCH 2'),
		('BRANCH_3','BRANCH 3'),
		('BRANCH_4','BRANCH 5'),
		('BRANCH_5','BRANCH 5'),
		)
	supplier=models.ForeignKey(
		to='Supplier',
		related_name='supplied_by',
		on_delete=models.CASCADE,		
		)
	asset_description=models.TextField(max_length=100)
	tag_number=models.TextField(unique=True)
	asset_cost=models.DecimalField(default=0,max_digits=50,decimal_places=2)
	monthly_depreciation=models.DecimalField(default=0,max_digits=50,decimal_places=2)
	total_depreciation=models.DecimalField(default=0,max_digits=50,decimal_places=2)
	current_cost=models.DecimalField(default=0,max_digits=50,decimal_places=2)	
	user=models.ForeignKey(
		to=settings.AUTH_USER_MODEL,
		on_delete=models.CASCADE
		)
	serial_number=models.TextField()
	category=models.TextField(choices=CATEGORY)
	location=models.TextField(choices=BRANCH)
	date_in_service=models.DateField(default=datetime.date.today)
	status=models.TextField(max_length=100,default='IN USE')

	class Meta:
		ordering=('id',)
	

	def __str__(self):
		return self.asset_description

	
	def get_monthly_depreciation(self):
		if self.category=="COMPUTERS":
			self.monthly_depreciation=(self.asset_cost/3)/12
		elif self.category=="FURNITURES":
			self.monthly_depreciation=(self.asset_cost/8)/12
		elif self.category=="OFFICE_EQUIPMENT":
			self.monthly_depreciation=(self.asset_cost/8)/12
		elif self.category=="SERVERS":
			self.monthly_depreciation=(self.asset_cost/5)/12
		elif self.category=="LINK_EQUIPMENT":
			self.monthly_depreciation=(self.asset_cost/5)/12
		return self.monthly_depreciation
	
	def get_total_depreciation(self):
		self.total_depreciation=self.total_depreciation+self.monthly_depreciation
		return self.total_depreciation
	
	def get_current_cost(self):
		self.current_Cost=self.asset_cost- self.total_depreciation
		return self.current_cost		
	
	def update_depreciation(self):
		self.monthly_depreciation=self.get_monthly_depreciation()
		self.total_depreciation=self.get_total_depreciation()
		self.current_cost=self.get_current_cost()
		self.save()

	def update_status(self):
		self.status='to_retire'
		self.save()

	def update_retirement(self):
		self.asset_cost=0
		self.status='retired'
		self.save()

	def get_absolute_url(self):
		return reverse('main:AssetDetail',kwargs={'pk':self.id})
class Supplier(models.Model):
	supplier_name=models.TextField()
	supplier_location=models.TextField()
	supplier_Phonenumber=models.TextField()
	supplier_email=models.EmailField()
	supplier_website=models.URLField()



	def __str__(self):
		return self.supplier_name
