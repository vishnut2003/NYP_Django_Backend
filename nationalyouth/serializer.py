from rest_framework import serializers
from .models import *


class NewsCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsCategory
        fields = "__all__"
class NewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"



class ApplicationForAffilicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application_for_Affliation
        fields = [
            'name_of_institution',
            'mobile_number',
            'email',
            'address',
            'district',
            'registration_fee',
            'payment_mode',
            'manager_name',
            'principal_name',
            'manager_address',
            'principal_address',
        ]


class ApplicationForAffilicationListSerializer(serializers.ModelSerializer):
    status_of_institution = serializers.SerializerMethodField()
    class Meta:
        model = Application_for_Affliation
        fields = "__all__"
    
    def get_status_of_institution(self, obj):
        if obj.status_of_institution:
            return obj.status_of_institution.institution_status
        return None



class ApplicationForAffiliationCoursesSerializer(serializers.Serializer):
    class Meta:
        model = Application_for_Affliation_Course
        fields = ['course','application']

        
        
class Exam_Registration_serializer(serializers.ModelSerializer):
    college_name = serializers.SerializerMethodField()
    course_name = serializers.SerializerMethodField()
    class Meta:
        model = Exam_Registration
        fields = "__all__"
        
    def get_college_name(self,obj):
        if obj.college_name:
            return obj.college_name.college_name
        return None
    
    
    def get_course_name(self,obj):
        if obj.course_name:
            return obj.course_name.course_name
        return None


class Exam_Registration_List_Serializer(serializers.ModelSerializer):
    college_name = serializers.SerializerMethodField()
    exam_fees = serializers.SerializerMethodField()
    class Meta:
        model = Exam_Registration
        fields = "__all__"
        
    def get_college_name(self, obj):
        if obj.college_name:
            return obj.college_name.college_name
        return None

    def get_exam_fees(self, obj):
        if obj.exam_fees:
            return obj.exam_fees.exam_fees_type
        return None



class Mark_List_Registration_serializer(serializers.ModelSerializer):
    college_name = serializers.SerializerMethodField()
    course_name = serializers.SerializerMethodField()
    principal_approval = serializers.SerializerMethodField()
    exam_fees = serializers.SerializerMethodField()
    mark_enter_clerk = serializers.SerializerMethodField()
    mark_check_clerk = serializers.SerializerMethodField()
    second_verified_officer = serializers.SerializerMethodField()
    class Meta:
        model = Mark_List_Registration
        fields = '__all__'

    def get_college_name(self, obj):
        if obj.college_name:
            return obj.college_name.college_name
        return None

    def get_course_name(self, obj):
        if obj.course_name:
            return obj.course_name.course_name
        return None
    
    def get_principal_approval(self, obj):
        if obj.principal_approval:
            return obj.principal_approval.status
        return None
    
    def get_exam_fees(self, obj):
        if obj.exam_fees:
            return obj.exam_fees.exam_fees_type
        return None
    
    def get_mark_enter_clerk(self, obj):
        if obj.mark_enter_clerk:
            return obj.mark_enter_clerk.mark_status
        return None
    
    def get_mark_check_clerk(self, obj):
        if obj.mark_check_clerk:
            return obj.mark_check_clerk.mark_status
        return None
    
    def get_second_verified_officer(self, obj):
        if obj.second_verified_officer:
            return obj.second_verified_officer.mark_status
        return None
    




        
class VTC_Course_Admission_Registration_serializer(serializers.ModelSerializer):        
    class Meta:
        model = VTC_Course_Admission_Registration
        fields = "__all__"
        
        
    
    def to_representation(self, instance):
        data =  super().to_representation(instance)
        data['college_name'] =instance.college_name.college_name if instance.college_name else None
        data['course_name'] = instance.course_name.course_name if instance.course_name else None
        return data

class Admission_Registration_serializer(serializers.ModelSerializer):
    college_name = serializers.SerializerMethodField()
    course_name = serializers.SerializerMethodField()
    class Meta:
        model = Admission_Registration
        fields = "__all__"
    def get_college_name(self,obj):
        return obj.college_name.college_name
    def get_course_name(self,obj):
        return obj.course_name.course_name

class CustomeUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomeUser
        fields = "__all__"
        
        
        
class Free_Skill_TrainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Free_Skill_Training
        fields = "__all__"
        
        




class User_RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Role
        fields = "__all__"
        
        





class Vocational_CourseSerializer(serializers.ModelSerializer):
    course_name_display = serializers.SerializerMethodField()
    course_name = serializers.PrimaryKeyRelatedField(queryset=Course_Name.objects.all(), allow_null=True)

    class Meta:
        model = Vocational_Course
        fields = "__all__"
    
    def get_course_name_display(self, obj):
        if obj.course_name:
            return obj.course_name.course_name
        return None

    def update(self, instance, validated_data):
        course_name = validated_data.pop('course_name', None)
        if course_name:
            instance.course_name = course_name
        return super().update(instance, validated_data)

            
        





class Certificate_CourseseSerializer(serializers.ModelSerializer):
    course_name_display = serializers.SerializerMethodField()
    course_name = serializers.PrimaryKeyRelatedField(queryset=Course_Name.objects.all(), allow_null=True)
    class Meta:
        model = Certificate_Course
        fields = "__all__"
        
       
    def get_course_name_display(self, obj):
        if obj.course_name:
            return obj.course_name.course_name
        return None

    def update(self, instance, validated_data):
        course_name = validated_data.pop('course_name', None)
        if course_name:
            instance.course_name = course_name
        return super().update(instance, validated_data)

            

class Diploma_ProgrammeSerializer(serializers.ModelSerializer):
    course_name_display = serializers.SerializerMethodField()
    course_name = serializers.PrimaryKeyRelatedField(queryset=Course_Name.objects.all(), allow_null=True)    
    class Meta:
        model = Diploma_Programme
        fields = "__all__"
        
    
    def get_course_name_display(self, obj):
        if obj.course_name:
            return obj.course_name.course_name
        return None

    def update(self, instance, validated_data):
        course_name = validated_data.pop('course_name', None)
        if course_name:
            instance.course_name = course_name
        return super().update(instance, validated_data)


class PG_Diploma_ProgrammeSerializer(serializers.ModelSerializer):
    course_name_display = serializers.SerializerMethodField()
    course_name = serializers.PrimaryKeyRelatedField(queryset=Course_Name.objects.all(), allow_null=True)       
    class Meta:
        model = PG_Diploma_Programme
        fields = "__all__"
        
       
    def get_course_name_display(self, obj):
        if obj.course_name:
            return obj.course_name.course_name
        return None

    def update(self, instance, validated_data):
        course_name = validated_data.pop('course_name', None)
        if course_name:
            instance.course_name = course_name
        return super().update(instance, validated_data)

from rest_framework.exceptions import ValidationError
class Affiliated_Vocational_Training_College_KerlaSerializer(serializers.ModelSerializer):
    college_name_display = serializers.CharField(source='college_name.college_name', read_only=True)

    class Meta:
        model = Affiliated_Vocational_Training_College_Kerla
        fields = "__all__"
    
    def update(self, instance, validated_data):
        # Handle the update logic
        college_name_data = validated_data.pop('college_name', None)
        if college_name_data:
            instance.college_name = College_Name.objects.get(id=college_name_data.id)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
            
    # def create(self, validated_data):
    #     print("sss")
    #     college_name_data = validated_data.pop('college_name', None)
        
    #     if college_name_data:
    #         # Get or create the college name object based on its attributes
    #         college_name_obj, created = College_Name.objects.get_or_create(
    #             id=college_name_data.id,
    #             defaults={'college_name': college_name_data.college_name}
    #         )
    #         validated_data['college_name'] = college_name_obj
    #     else:
    #         raise serializers.ValidationError({"college_name": "This field is required."})

    #     # Create the Affiliated_Vocational_Training_College_Kerla object
    #     return super().create(validated_data)




class Course_NameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course_Name
        fields = "__all__"



#
class Add_on_Programme_College_Affiliation_KerlaSerializer(serializers.ModelSerializer):
    college_name_display = serializers.CharField(source='college_name.college_name', read_only=True)

    class Meta:
        model = Add_on_Programme_College_Affiliation_Kerla
        fields = "__all__"
        
    def update(self, instance, validated_data):
        college_name_data = validated_data.pop('college_name', None).id
        if college_name_data:
            instance.college_name = College_Name.objects.get(id=college_name_data)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance   
    
    def perform_create(self, serializer):
        college_name_data = self.request.data.get('college_name')
        
        if college_name_data:
            college_name_obj, created = College_Name.objects.get_or_create(college_name=college_name_data)
            serializer.save(college_name=college_name_obj)
        else:
            raise ValidationError({"college_name": "This field is required."})
        
    



class College_NameSerializer(serializers.ModelSerializer):
    class Meta:
        model = College_Name
        fields = "__all__"
        
        




class Course_NameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course_Name
        fields = "__all__"
        
        
        



class Exam_Fees_TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam_Fees_Type
        fields = "__all__"
        




class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = "__all__"



class Mark_StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mark_Status
        fields = "__all__"
        

class Result_StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result_Status
        fields = "__all__"
        



class Add_on_CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Add_on_College
        fields = "__all__"
        
        




class Main_CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Main_Course
        fields = "__all__"
        




class Institution_StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institution_Status
        fields = "__all__"
        
        

    
class Amount_StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Amount_Status
        fields = "__all__"
        
        


class Fee_TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fee_Type
        fields = "__all__"
        
        



class E_Office_AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = E_Office_Account
        fields = "__all__"
        


class Type_of_AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type_of_Account
        fields = "__all__"
Particulars_Head
class Particulars_HeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Particulars_Head
        fields = "__all__"
        
        
        



class Employee_Record_TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee_Record_Type
        fields = "__all__"
        
        




class Work_StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work_Status
        fields = "__all__"
        
        



class Employee_Live_and_Leave_StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee_Live_and_Leave_Status
        fields = "__all__"
        


class Nature_of_LeaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nature_of_Leave
        fields = "__all__"
        
        




class Work_Assign_OfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work_Assign_Office
        fields = "__all__"


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'
        
        
    def to_representation(self, instance):
        data =  super().to_representation(instance)
        data['category_name'] =instance.category.category_name if instance.category else None
        return data
