from rest_framework import serializers
from companyapiapp.models import Company, Employee

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    company_id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Company
        fields = ('company_id', 'name', 'location', 'about', 'type', 'added_date', 'active')


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    employee_id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Employee
        fields = ('employee_id', 'name', 'email', 'address', 'phone', 'about', 'position', 'company')