from rest_framework import serializers
from nationalyouth.models import (
    E_Office_Queue,
    E_Employee_Record,
    E_employee_daily_work_statement,
    E_employee_live_status,
    E_employee_leave_status,
    Staff_work_allotment,
    E_Office_Account,
    E_Office_File_Sanction,
    Application_for_Affliation,
    VTC_Course_Admission_Registration,
    Admission_Registration,
    Exam_Registration,
    Mark_List_Registration,
    College_Name,
    E_Employee_Record_Contribution,
    Affiliated_Vocational_Training_College_Kerla
)



class E_Office_Queue_Serializer(serializers.ModelSerializer):
    class Meta:
        model = E_Office_Queue
        fields = '__all__'


class E_Employee_Record_Serializer(serializers.ModelSerializer):
    class Meta:
        model = E_Employee_Record
        fields = '__all__'


class E_Employee_Record_Contribution_Serializer(serializers.ModelSerializer):
    class Meta:
        model = E_Employee_Record_Contribution
        fields = '__all__'


class E_employee_daily_work_statement_Serializer(serializers.ModelSerializer):
    class Meta:
        model = E_employee_daily_work_statement
        fields = '__all__'


class E_employee_live_status_Serializer(serializers.ModelSerializer):
    class Meta:
        model = E_employee_live_status
        fields = '__all__'


class E_employee_leave_status_Serializer(serializers.ModelSerializer):
    class Meta:
        model = E_employee_leave_status
        fields = '__all__'


class Staff_work_allotment_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Staff_work_allotment
        fields = '__all__'


class E_Office_Account_Serializer(serializers.ModelSerializer):
    particular_head = serializers.SerializerMethodField()
    class Meta:
        model = E_Office_Account
        fields = '__all__'

    def get_particular_head(self, obj):
        return obj.particular_head.particular_head


class E_Office_File_Sanction_Serializer(serializers.ModelSerializer):
    class Meta:
        model = E_Office_File_Sanction
        fields = '__all__'




class Application_for_Affliation_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Application_for_Affliation
        fields = '__all__'



class Affiliated_Vocational_Training_College_Kerla_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Affiliated_Vocational_Training_College_Kerla
        fields = '__all__'



class Admission_Registration_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Admission_Registration
        fields = '__all__'


class VTC_Course_Admission_Registration_Serializer(serializers.ModelSerializer):
    course_name = serializers.SerializerMethodField()
    college_name = serializers.SerializerMethodField()
    class Meta:
        model = VTC_Course_Admission_Registration
        fields = '__all__'

    def get_course_name(self, obj):
        return obj.course_name.course_name
    
    def get_college_name(self, obj):
        return obj.college_name.college_name


class Mark_List_Registration_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Mark_List_Registration
        fields = '__all__'

class Exam_Registration_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Exam_Registration
        fields = '__all__'
