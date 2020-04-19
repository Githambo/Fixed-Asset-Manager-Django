from django.urls import path
from main import views

app_name='main'

urlpatterns=[

	path('',views.index,name='index'),
	path('addition',views.MassAddition.as_view(),name='addition'),
	path('asset/<int:pk>',views.AssetDetail.as_view(),name='AssetDetail'),	
	path('depreciation',views.depreciateview,name='depreciation'),
	path('depreciated',views.depreciate_update,name="d-update"),
	path('search/',views.SearchView,name='search'),
	path('asset/<int:pk>/update',views.UpdateView.as_view(),name='update'),
	path('asset/<int:pk>/delete',views.DeleteAsset.as_view(),name='delete'),	
	path('register',views.RegisterView,name='register'),
	path('asset/<int:pk>/',views.statusview,name='statuschange'),
	path('mass-retirement',views.MassRetirement,name="retire"),
	path('retired',views.retire_update,name="retire-update"),
	path('download-register',views.register_download,name='download-register'),
	path('retirement-download',views.retirement_download,name='retire_report'),
	
	
]