API using django
1.What is API 
API - Application Programming Interface
Interface that allows two programs/software to talk  to each other 
Ex- We want some data from youtube(Or any other site) for our website so we create a new
api works to get data in JSON format and send it to us.

2.Why use Django Rest Framework?
1.Django Rest Framework is a powerful and flexible toolkit for building Web APIs.
   It makes it easy to create beautiful, standards-driven Web APIs.
   It's designed for speed, and makes it easy to compose APIs from smaller components.

3.HTTP methods

1.GET - To get data from server (Read)
2.POST - To send data to server (Create)
3.PUT - To update data on server (Update)
4.PATCH - Partial Update of data on server (Update)
5.DELETE - To delete data from server (Delete)

(NOT so Important for now)
6.HEAD - Used to ask for just the HTTP headers of a resource without the response body.
7.OPTIONS - Used to ask for the HTTP methods that the server supports for a given URL.
8.TRACE - The TRACE method performs a message loop-back test along the path to the target resource. An HTTP/1.1 server MUST respond
with the complete request message received in the request. This can be used by the client if it wants to determine the

4.END POINTS of projects

1.Company 
End point                   HTTP method         Description
/companies                    GET                  Get all companies
/companies/{id}               GET                  Get a single company by id
/companies/{id}               PUT                  Update a company by id
/companies/{id}             DELETE               Delete a company by id
/companies                   POST                 Create a new company
/companies/{id}/employess    GET                  Get all employess of a company id

2.Employess
End Point                     HTTP Method          Description
/employess                     GET                  Get all employess
/employess/{id}                GET                  Get a single employess by id
/employess/{id}                PUT                  Update a employess by id
/employess/{id}              DELETE               Delete a employess by id
/employess                    POST                 Create a new employess

5.Six Step to have fully working APIs

1.Install Python,Django and Django Rest Framework
2.Set up Django Models(Company,Employess)
3.Create Serializers for models (What is Serializers- It is used to convert python objects to JSON and vice-versa)
4.Create ViewSets for models (What is ViewSets- It is used to provide a way of automatically determining the set of HTTP actions to use for a given model)
5.set up urls(What are urls - It is used to map URLs to views)
6.Test your api


1.Install Python,Django and Django Rest Framework

1.Install Python from https://www.python.org/downloads/
2.Open CMD or Terminal and type python --version , if it shows python version then you have installed python successfully
3.Open CMD or Terminal and type pip --version , if it shows pip version then you have installed pip successfully
4.Create a folder from your project directory 
5.create environment (py -m venv env)
6.CALL environment (call env\Scripts\activate.bat)
7.Install django (pip install django)
8.create project (>django-admin startproject companyapi )
9.Install django rest framework (pip install djangorestframework)
10.settings -> Installed app -> rest_framework

11.Create app (django-admin startapp companyapiapp     )
12.Create model company in models.py ()
13.Create serializer.py (what is serializer- It is used to convert python objects to JSON and vice-versa)
14.Create viewsets.py (what is viewsets- It is used to provide a way of automatically determining the set of HTTP actions to use for a given model)
15.set up urls.py (what are urls - It is used to map URLs to views)
16.urls in companyapi/urls.py (add path to viewsets)
16.IMport from rest_framework import routers
router = routers.DefaultRouter()
18.register app in settings (INSTALLED_APPS)
19.import urls in main project from app
20.Then make migrations (python manage.py makemigrations)
21.Then migrate (python manage.py migrate)
22.Open db browser to check  database 
23.runserver (py manage.py runserver)
24.path(http://127.0.0.1:8000/companyapiapp/v1/companies/)
25.Open postman  or any other tool for testing API's
26.Create a new company (POST)
27.Get all companies (GET)
28.Get a single company (GET)
29.Update a company (PUT)
30.Delete a company (DELETE )
31.create model employess in models.py
32.create serializer for employess in serializer.py
33.Add the following code in url
.py (from .views import EmployeeViewSet)
.add this line router.register(r'employess', EmployeeViewSet)
from .views import EmployeeViewSet
EmployeeViewSet(viewsets.ModelViewset):
    queryset = Employee.objects.all()  
    serializer_class = EmployeeSerializer
34.Create Employee view set in views.py

Creating Custom api 
companies/{id}/employess
http://127.0.0.1:8000/companyapiapp/v1/companies/1/employees/

35.Create function in views.py companyviewset
 to get all employees of a company
@action(detail=True, methods=['get'])
 def employees(self, request,pk=None):
        try:
            company = Company.objects.get(pk=pk)
            emp = Employee.objects.filter(company=company)
            emp_serializer = EmployeeSerializer(emp, many=True, context={'request': request})
            return Response(emp_serializer.data)
        except Exception as e:
            print(e)
            return Response({'error': 'Company not found'}, status=404)

36.Create our apis Readonly
1.Go to settings  and add
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}
Its used restrict unauthenticated user to create,update ,delete api only they can read and update
2.Disabling browsable api-.to stop browsable api  from django admin panel go to settings-> rest framework
 and add
 'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ]

3. add the following in settings-> rest framework

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
     'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ]

}
37.workingon django admin module for communicating with api

1. Create admin.py in companyapiapp
2. Register models in admin.py 
from .models import Company, Employee
from django.contrib import admin
admin.site.register([Company,Employee])

3.create superuser-(py manage.py createsuperuser)   
4.login to admin panel (http://127.0.0.1:8000/admin/)
5.add objects in admin panel(company,employess)

6.check api response in postman
   http://localhost:8000/companyapiapp/v1/companies/
   http://localhost:8000/companyapiapp/v1/employees/





