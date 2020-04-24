# Django-Asset-Manager-
Fixed Asset app to track asset movement,depreciation and retirements

# Django-Asset-Manager-
Erp for Assets
=====
Erp for assets is a simple django app that maintains company or firm based assets.
It takes new assets ,runs depreciations using straight line method,and being able 
to retire the assest.Its a pretty exiting webapp much related to assetworkbench for Oracle.
Detailed documentation is in the "docs" directory.
Simple Django app to track asset movement,depreciation and retirements


fork the folder,
Navigate to the directory containing the app
manage.py runserver
manage.py migrate

# For app installation
pip install django-asset-manager
=====


Quick start
-----------
1. Add "Erp" to your INSTALLED_APPS setting like this::
INSTALLED_APPS = [
...
'Erp',
]

2. Include the Erp URLconf in your project urls.py like this::
path('Erp/', include('Erp.urls')),

3. Run `python manage.py migrate` to create the Erp models.

4. Start the development server and visit http://127.0.0.1:8000/admin/to Add assets and perfom the operations (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/Erp/ to Enjoy various actions

##any lookup for assets is performed under search Asset
