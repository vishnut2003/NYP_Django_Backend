"""
   Made By -: Techzniczone
   website - :https://www.techzniczone.com/
   email - :techzniczone@gmail.com
   """

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.utils.text import slugify


#====================================== Contact Model ============================================
class Contact_us(models.Model):
    contact_id = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=255)
    message = models.TextField(max_length=250)
    date_and_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.full_name
    
    class Meta:
        verbose_name = 'Contact Us'

#==================================================================================================
#==================================================================================================



#====================================== User Role Model ==========================================
class User_Role(models.Model):
    user_role = models.CharField(max_length=250)
    date_and_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user_role
    
    class Meta:
        verbose_name = 'User Role'

#==================================================================================================
#==================================================================================================



#====================================== User Model ================================================
class CustomeUser(AbstractUser):
    STATUS = (
          ('1','ACTIVE'),
          ('2','INACTIVE'),
          )
    ##
    # USER_ROLE = (
    #       ('1','ACTIVE'),
    #       ('2','INACTIVE'),
    #       )
    profile_image = models.ImageField(upload_to='image/download/uploads/user_image/',null=True,blank=True)
    dob = models.CharField(max_length=50,null=True,blank=True)
    mobile_number = models.CharField(max_length=50,null=True,blank=True)
    address = models.TextField(max_length=500,null=True,blank=True)
    gender = models.CharField(max_length=50,null=True,blank=True)
    user_status = models.CharField(max_length=25,choices=STATUS,default=2)
    decrypt_password = models.CharField(max_length=25)
    user_role = models.ForeignKey(User_Role, on_delete = models.CASCADE,null=True,blank=True) #select option filed
    date_and_time = models.DateTimeField(auto_now_add=True)
        
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'Custome User'
#==================================================================================================
#==================================================================================================




#===================================== Drop down Models =============================================================

#====================================== Type of Accounts Model ====================================
class Type_of_Account(models.Model):
    type_of_account = models.CharField(max_length=250)
    date_and_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.type_of_account
    class Meta:
        verbose_name = 'Type of Account'
#==================================================================================================
#==================================================================================================


#====================================== Particulars Head Model ====================================
class Particulars_Head(models.Model):
    particular_head = models.CharField(max_length=250)
    date_and_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.particular_head
    class Meta:
        verbose_name = 'Particulars Head'
#==================================================================================================
#==================================================================================================


#====================================== Collage Name Model ========================================
class College_Name(models.Model):
    college_name = models.CharField(max_length=250)
    date_and_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.college_name
    class Meta:
        verbose_name = 'College Name'
#==================================================================================================
#==================================================================================================


#====================================== Course Name Model ========================================
class Course_Name(models.Model):
    course_name = models.CharField(max_length=250)
    date_and_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.course_name
    
    class Meta:
        verbose_name = 'Course Name'
    
#==================================================================================================
#==================================================================================================



#====================================== Status Model ==============================================
class Status(models.Model):
    status = models.CharField(max_length=250)
    date_and_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.status
    
    class Meta:
        verbose_name = 'Status'
#==================================================================================================
#==================================================================================================


#====================================== Employee Record Type Model ================================
class Employee_Record_Type(models.Model):
    employee_record_type = models.CharField(max_length=250)
    date_and_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.employee_record_type
    class Meta:
        verbose_name = 'Employee Record Type'
#==================================================================================================
#==================================================================================================


#====================================== Work Status Model =========================================
class Work_Status(models.Model):
    work_status = models.CharField(max_length=250)
    date_and_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.work_status

    class Meta:
        verbose_name = 'Work Status'
#==================================================================================================
#==================================================================================================


#====================================== Employee Live / Leave Model ================================
class Employee_Live_and_Leave_Status(models.Model):
    employee_live_and_leave_status = models.CharField(max_length=250)
    date_and_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.employee_live_and_leave_status

    class Meta:
        verbose_name = 'Employee Live And Leave Status'
#==================================================================================================
#==================================================================================================


#====================================== Work Assign Office Model ==================================
class Work_Assign_Office(models.Model):
    work_assign_office = models.CharField(max_length=250)
    date_and_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.work_assign_office
    class Meta:
        verbose_name = 'Work Assign Office'    
#==================================================================================================
#==================================================================================================



#====================================== Exam Fees Type Model ======================================
class Exam_Fees_Type(models.Model):
    exam_fees_type = models.CharField(max_length=250)
    date_and_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.exam_fees_type
    class Meta:
        verbose_name = 'Exam Fees Type'   
#==================================================================================================
#==================================================================================================


#====================================== Mark Enter Clerk Model ====================================
class Mark_Status(models.Model):
    mark_status = models.CharField(max_length=250)
    date_and_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.mark_status

    class Meta:
        verbose_name = 'Mark Status'  
#==================================================================================================
#==================================================================================================



#====================================== Result Status Model =======================================
class Result_Status(models.Model):
    result_status = models.CharField(max_length=250)
    date_and_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.result_status
    class Meta:
        verbose_name = 'Result Status'  
#==================================================================================================
#==================================================================================================


#====================================== Add-on Colleges Model =====================================
class Add_on_College(models.Model):
    add_on_college_name = models.CharField(max_length=250)
    date_and_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.add_on_college_name
    class Meta:
        verbose_name = 'Add On College'  
#==================================================================================================
#==================================================================================================



#====================================== Main Courses Model ========================================
class Main_Course(models.Model):
    main_course_name = models.CharField(max_length=250)
    date_and_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.main_course_name
    class Meta:
        verbose_name = 'Main Course'  
#==================================================================================================
#==================================================================================================


#====================================== Status of the Institution Model ===========================
class Institution_Status(models.Model):
    institution_status = models.CharField(max_length=250)
    date_and_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.institution_status
    class Meta:
        verbose_name = 'Institution Status'  
    
#==================================================================================================
#==================================================================================================



#====================================== Amount Status Model =======================================
class Amount_Status(models.Model):
    amount_status = models.CharField(max_length=250)
    date_and_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.amount_status
    class Meta:
        verbose_name = 'Amount Status'  
#==================================================================================================
#==================================================================================================



#====================================== Types of Fees Model =======================================
class Fee_Type(models.Model):
    fee_type = models.CharField(max_length=250)
    date_and_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.fee_type

    class Meta:
        verbose_name = 'Fee Type'
#==================================================================================================
#==================================================================================================


#====================================== Nature  Of Leave Model ====================================
class Nature_of_Leave(models.Model):
    nature_of_leave = models.CharField(max_length=250)
    date_and_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.nature_of_leave
    class Meta:
        verbose_name = 'Nature of Leave'
#==================================================================================================
#==================================================================================================



#===================================== End Dropdown Model==========================================
#==================================================================================================







#====================================== VTC Course Admission Registration Model =================
class VTC_Course_Admission_Registration(models.Model):
    registration_number = models.IntegerField(unique=True)
    name_of_student = models.CharField(max_length=250)
    address = models.TextField(max_length=250,default='',null=True,blank=True)
    id_number = models.CharField(max_length=250)
    date_of_birth = models.CharField(max_length=250)
    mobile_number = models.CharField(max_length=250)
    college_name = models.ForeignKey(College_Name, on_delete = models.CASCADE,null=True,blank=True) #select option filed
    district = models.CharField(max_length=250)     
    course_name = models.ForeignKey(Course_Name, on_delete = models.CASCADE,null=True,blank=True) #select option filed
    admission_fees = models.CharField(max_length=250)
    admission_date = models.CharField(max_length=250)
    principal_approval = models.ForeignKey(Status, on_delete = models.CASCADE,null=True,blank=True) #select option filed
    date_and_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'VTC Course Admission Registration'
#==================================================================================================
#==================================================================================================



#====================================== Admission Registration Model ==============================
class Admission_Registration(models.Model):
    registration_number = models.IntegerField(unique=True)
    name_of_student = models.CharField(max_length=250)
    address = models.TextField(max_length=250,default='',null=True,blank=True)
    id_number = models.CharField(max_length=250)
    date_of_birth = models.CharField(max_length=250)
    mobile_number = models.CharField(max_length=250)
    college_name = models.ForeignKey(College_Name, on_delete = models.CASCADE,null=True,blank=True) #select option filed
    district = models.CharField(max_length=250)     
    course_name = models.ForeignKey(Course_Name, on_delete = models.CASCADE,null=True,blank=True) #select option filed
    admission_fees = models.CharField(max_length=250)
    admission_date = models.CharField(max_length=250)
    principal_approval = models.ForeignKey(Status, on_delete = models.CASCADE,null=True,blank=True) #select option filed
    date_and_time = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = 'Admission Registration'
#==================================================================================================
#==================================================================================================




#====================================== Exam Registration Model ====================================
class Exam_Registration(models.Model):
    registration_number = models.CharField(max_length=250)
    #registered_student = models.ForeignKey(Admission_Registration, on_delete = models.CASCADE,null=True,blank=True) #select option filed

    name_of_student = models.CharField(max_length=250,null=True,blank=True)
    address = models.TextField(max_length=250,default='',null=True,blank=True)
    id_number = models.CharField(max_length=250,null=True,blank=True)
    date_of_birth = models.CharField(max_length=250,null=True,blank=True)
    mobile_number = models.CharField(max_length=250,null=True,blank=True)
    college_name = models.ForeignKey(College_Name, on_delete = models.CASCADE,null=True,blank=True) #select option filed
    district = models.CharField(max_length=250,null=True,blank=True)     
    course_name = models.ForeignKey(Course_Name, on_delete = models.CASCADE,null=True,blank=True) #select option filed
    admission_fees = models.CharField(max_length=250,null=True,blank=True)
    admission_date = models.CharField(max_length=250,null=True,blank=True)
    principal_approval = models.ForeignKey(Status, on_delete = models.CASCADE,null=True,blank=True)


    exam_fees = models.ForeignKey(Exam_Fees_Type, on_delete = models.CASCADE,null=True,blank=True)     #select option filed
    exam_attendance = models.CharField(max_length=250)
    any_fees_concession = models.CharField(max_length=250)
    date = models.CharField(max_length=250)
    principal_code = models.CharField(max_length=250)   
    principal_name = models.CharField(max_length=250)     
    online_fees = models.IntegerField(default=0)
    remark = models.TextField(max_length=250)
    principal_approval = models.ForeignKey(Status, on_delete = models.CASCADE,null=True,blank=True) #select option filed
    date_and_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.registration_number

    
    class Meta:
        verbose_name = 'Exam Registration'
#==================================================================================================
#==================================================================================================



#====================================== Mark List Registration Model ==============================
class Mark_List_Registration(models.Model):
    RESULT_STATUS = (
            ('pass','Passed'),
            ('fail','Failed'),
        )
    registration_number = models.CharField(max_length=250)
    name_of_student = models.CharField(max_length=250,null=True,blank=True)
    address = models.TextField(max_length=250,default='',null=True,blank=True)
    id_number = models.CharField(max_length=250,null=True,blank=True)
    date_of_birth = models.CharField(max_length=250,null=True,blank=True)
    mobile_number = models.CharField(max_length=250,null=True,blank=True)
    college_name = models.ForeignKey(College_Name, on_delete = models.CASCADE,null=True,blank=True) #select option filed
    district = models.CharField(max_length=250,null=True,blank=True)     
    course_name = models.ForeignKey(Course_Name, on_delete = models.CASCADE,null=True,blank=True) #select option filed
    admission_fees = models.CharField(max_length=250,null=True,blank=True)
    admission_date = models.CharField(max_length=250,null=True,blank=True)
    principal_approval = models.ForeignKey(Status, on_delete = models.CASCADE,null=True,blank=True)

    exam_fees = models.ForeignKey(Exam_Fees_Type, on_delete = models.CASCADE,null=True,blank=True)     #select option filed
    exam_attendance = models.CharField(max_length=250,null=True,blank=True)
    any_fees_concession = models.CharField(max_length=250,null=True,blank=True)
    date = models.CharField(max_length=250,null=True,blank=True)
    principal_code = models.CharField(max_length=250,null=True,blank=True)   
    principal_name = models.CharField(max_length=250,null=True,blank=True)     
    online_fees = models.IntegerField(default=0,null=True,blank=True)
    remark = models.TextField(max_length=250,null=True,blank=True)
    principal_approval = models.ForeignKey(Status, on_delete = models.CASCADE,null=True,blank=True) #select option filed




    date = models.CharField(max_length=250)
    subject_1 = models.CharField(max_length=250,default='',null=True,blank=True)
    subject_2 = models.CharField(max_length=250,default='',null=True,blank=True)   
    subject_3 = models.CharField(max_length=250,default='',null=True,blank=True)
    subject_4 = models.CharField(max_length=250,default='',null=True,blank=True)
    subject_5 = models.CharField(max_length=250,default='',null=True,blank=True)
    subject_6 = models.CharField(max_length=250,default='',null=True,blank=True)   
    subject_7 = models.CharField(max_length=250,default='',null=True,blank=True)
    subject_8 = models.CharField(max_length=250,default='',null=True,blank=True)
    subject_9 = models.CharField(max_length=250,default='',null=True,blank=True)
    subject_10 = models.CharField(max_length=250,default='',null=True,blank=True)   
    subject_11 = models.CharField(max_length=250,default='',null=True,blank=True)
    subject_12 = models.CharField(max_length=250,default='',null=True,blank=True)
    internal_marks_1 = models.IntegerField(default=0,null=True,blank=True)
    internal_marks_2 = models.IntegerField(default=0,null=True,blank=True)
    internal_marks_3 = models.IntegerField(default=0,null=True,blank=True)
    internal_marks_4 = models.IntegerField(default=0,null=True,blank=True)
    internal_marks_5 = models.IntegerField(default=0,null=True,blank=True)
    internal_marks_6 = models.IntegerField(default=0,null=True,blank=True)
    internal_marks_7 = models.IntegerField(default=0,null=True,blank=True)
    internal_marks_8 = models.IntegerField(default=0,null=True,blank=True)
    internal_marks_9 = models.IntegerField(default=0,null=True,blank=True)
    internal_marks_10 = models.IntegerField(default=0,null=True,blank=True)
    internal_marks_11 = models.IntegerField(default=0,null=True,blank=True)
    internal_marks_12 = models.IntegerField(default=0,null=True,blank=True)
    internal_marks_13 = models.IntegerField(default=0,null=True,blank=True)
    internal_marks_14 = models.IntegerField(default=0,null=True,blank=True)
    external_marks_1 = models.IntegerField(default=0,null=True,blank=True)
    external_marks_2 = models.IntegerField(default=0,null=True,blank=True)
    external_marks_3 = models.IntegerField(default=0,null=True,blank=True)
    external_marks_4 = models.IntegerField(default=0,null=True,blank=True)
    external_marks_5 = models.IntegerField(default=0,null=True,blank=True)
    external_marks_6 = models.IntegerField(default=0,null=True,blank=True)
    external_marks_7 = models.IntegerField(default=0,null=True,blank=True)
    external_marks_8 = models.IntegerField(default=0,null=True,blank=True)
    external_marks_9 = models.IntegerField(default=0,null=True,blank=True)
    external_marks_10 = models.IntegerField(default=0,null=True,blank=True)
    external_marks_11 = models.IntegerField(default=0,null=True,blank=True)
    external_marks_12 = models.IntegerField(default=0,null=True,blank=True)
    external_marks_13 = models.IntegerField(default=0,null=True,blank=True)
    external_marks_14 = models.IntegerField(default=0,null=True,blank=True)

    mark_obtained_1 = models.IntegerField(default=0,null=True,blank=True)
    mark_obtained_2 = models.IntegerField(default=0,null=True,blank=True)
    mark_obtained_3 = models.IntegerField(default=0,null=True,blank=True)
    mark_obtained_4 = models.IntegerField(default=0,null=True,blank=True)
    mark_obtained_5 = models.IntegerField(default=0,null=True,blank=True)
    mark_obtained_6 = models.IntegerField(default=0,null=True,blank=True)
    mark_obtained_7 = models.IntegerField(default=0,null=True,blank=True)
    mark_obtained_8 = models.IntegerField(default=0,null=True,blank=True)
    mark_obtained_9 = models.IntegerField(default=0,null=True,blank=True)
    mark_obtained_10 = models.IntegerField(default=0,null=True,blank=True)
    mark_obtained_11 = models.IntegerField(default=0,null=True,blank=True)
    mark_obtained_12 = models.IntegerField(default=0,null=True,blank=True)
    mark_obtained_13 = models.IntegerField(default=0,null=True,blank=True)
    mark_obtained_14 = models.IntegerField(default=0,null=True,blank=True)
    total_1 = models.IntegerField(default=0,null=True,blank=True)
    total_2 = models.IntegerField(default=0,null=True,blank=True)
    total_3 = models.IntegerField(default=0,null=True,blank=True)
    total_4 = models.IntegerField(default=0,null=True,blank=True)
    total_5 = models.IntegerField(default=0,null=True,blank=True)
    total_6 = models.IntegerField(default=0,null=True,blank=True)
    total_7 = models.IntegerField(default=0,null=True,blank=True)
    total_8 = models.IntegerField(default=0,null=True,blank=True)
    total_9 = models.IntegerField(default=0,null=True,blank=True)
    total_10 = models.IntegerField(default=0,null=True,blank=True)
    total_11 = models.IntegerField(default=0,null=True,blank=True)
    total_12 = models.IntegerField(default=0,null=True,blank=True)
    total_13 = models.IntegerField(default=0,null=True,blank=True)
    total_14 = models.IntegerField(default=0,null=True,blank=True)
    grade_1 = models.CharField(max_length=250,default='',null=True,blank=True)
    grade_2 = models.CharField(max_length=250,default='',null=True,blank=True)
    grade_3 = models.CharField(max_length=250,default='',null=True,blank=True)
    grade_4 = models.CharField(max_length=250,default='',null=True,blank=True)
    grade_5 = models.CharField(max_length=250,default='',null=True,blank=True)
    grade_6 = models.CharField(max_length=250,default='',null=True,blank=True)
    grade_7 = models.CharField(max_length=250,default='',null=True,blank=True)
    grade_8 = models.CharField(max_length=250,default='',null=True,blank=True)
    grade_9 = models.CharField(max_length=250,default='',null=True,blank=True)
    grade_10 = models.CharField(max_length=250,default='',null=True,blank=True)
    grade_11 = models.CharField(max_length=250,default='',null=True,blank=True)
    grade_12 = models.CharField(max_length=250,default='',null=True,blank=True)
    grade_13 = models.CharField(max_length=250,default='',null=True,blank=True)
    grade_14 = models.CharField(max_length=250,default='',null=True,blank=True)
    total_mark_1 = models.IntegerField(default=0)
    total_mark_obtained = models.IntegerField(default=0)
    result = models.CharField(max_length=25,choices=RESULT_STATUS,null=True,blank=True)

    certificate_image = models.ImageField(upload_to='image/download/uploads/certificate_image/',null=True,blank=True)
    marklist_image = models.ImageField(upload_to='image/download/uploads/marklist_image/',null=True,blank=True)
    

    #========================Office use=================
    mark_enter_clerk_name = models.CharField(max_length=250,default='',null=True,blank=True)   
    mark_enter_clerk = models.ForeignKey(Mark_Status, on_delete = models.CASCADE,null=True,blank=True) #select option filed
    mark_check_clerk_name = models.CharField(max_length=250,default='',null=True,blank=True)
    mark_check_clerk = models.ForeignKey(Mark_Status, on_delete = models.CASCADE,null=True,blank=True,related_name='mark_check_cleark_status') #select option filed
    second_verified_officer_name = models.CharField(max_length=250,default='',null=True,blank=True)   
    second_verified_officer = models.ForeignKey(Mark_Status, on_delete = models.CASCADE,null=True,blank=True,related_name='second_verified_officer_status') #select option filed
    final_mark_verified_officer_name = models.CharField(max_length=250,default='',null=True,blank=True)   
    result_status = models.ForeignKey(Result_Status, on_delete = models.CASCADE,null=True,blank=True) #select option filed
    result_enter_register_book_number = models.CharField(max_length=250,default='',null=True,blank=True)
    mark_obtained = models.IntegerField(default=0,null=True,blank=True)
    total_mark_2 = models.IntegerField(default=0,null=True,blank=True)
    date_and_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.registration_number
    

    class Meta:
        verbose_name = 'Mark List Registration'
#==================================================================================================
#==================================================================================================



#====================================== Add On Programme(College) Model ============================
class Add_on_Programme(models.Model):
    add_on_College = models.ForeignKey(Add_on_College, on_delete = models.CASCADE,null=True,blank=True) #select option filed
    course_name = models.ForeignKey(Course_Name, on_delete = models.CASCADE,null=True,blank=True) #select option filed
    course_code = models.CharField(max_length=250,default='')
    student_name = models.CharField(max_length=250,default='')
    address = models.TextField(max_length=250,default='',null=True,blank=True)
    id_number = models.CharField(max_length=250,default='')
    contact_number = models.CharField(max_length=250,default='')   
    exam_fees = models.IntegerField(default=0,null=True,blank=True)   
    amount = models.IntegerField(default=0,null=True,blank=True)
    main_course = models.ForeignKey(Main_Course, on_delete = models.CASCADE,null=True,blank=True) #select option filed
    college_coordinator_approval = models.ForeignKey(Status, on_delete = models.CASCADE,null=True,blank=True) #select option filed
    date_and_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.id)
    
    class Meta:
        verbose_name = 'Add on Programme'
#==================================================================================================
#==================================================================================================



#====================================== Application for affliation Model ==========================

class Application_for_Affliation(models.Model):
    name_of_institution = models.CharField(max_length=250)
    mobile_number = models.CharField(max_length=250)
    status_of_institution = models.ForeignKey(Institution_Status, on_delete = models.CASCADE,null=True,blank=True) #select option filed
    email = models.CharField(max_length=250)
    status_of_institution_other = models.CharField(max_length=250)
    year_of_establishment = models.CharField(max_length=250)
    address = models.TextField(max_length=250,default='',null=True,blank=True)
    pincode = models.IntegerField(null=True,blank=True)
    
    #===========Information about management =============
    name = models.CharField(max_length=250)
    education_qualification = models.CharField(max_length=250)
    date_of_birth = models.CharField(max_length=250)
    designation = models.CharField(max_length=250)
    profession_experience = models.CharField(max_length=250)
    postal_address = models.CharField(max_length=250,default='',null=True,blank=True)

    #===========Infrastructure Facility =================
    number_of_room_1 = models.CharField(max_length=250,default='',null=True,blank=True)
    seating_capacity_1 = models.CharField(max_length=250,default='',null=True,blank=True)
    total_area_1 = models.CharField(max_length=250,default='',null=True,blank=True)
    number_of_room_2 = models.CharField(max_length=250,default='',null=True,blank=True)
    seating_capacity_2 = models.CharField(max_length=250,default='',null=True,blank=True)
    total_area_2 = models.CharField(max_length=250,default='',null=True,blank=True)
    number_of_room_3 = models.CharField(max_length=250,default='',null=True,blank=True)
    seating_capacity_3 = models.CharField(max_length=250,default='',null=True,blank=True)
    total_area_3 = models.CharField(max_length=250,default='',null=True,blank=True)
    number_of_room_4 = models.CharField(max_length=250,default='',null=True,blank=True)
    seating_capacity_4 = models.CharField(max_length=250,default='',null=True,blank=True)
    total_area_4 = models.CharField(max_length=250,default='',null=True,blank=True)
    number_of_room_5 = models.CharField(max_length=250,default='',null=True,blank=True)
    seating_capacity_5 = models.CharField(max_length=250,default='',null=True,blank=True)
    total_area_5 = models.CharField(max_length=250,default='',null=True,blank=True)
    number_of_room_6 = models.CharField(max_length=250,default='',null=True,blank=True)
    seating_capacity_6 = models.CharField(max_length=250,default='',null=True,blank=True)
    total_area_6 = models.CharField(max_length=250,default='',null=True,blank=True)
    
    #===========Computer Facility =================
    serial_number_1 = models.CharField(max_length=250,default='',null=True,blank=True)
    type_of_computer_1 = models.CharField(max_length=250,default='',null=True,blank=True)
    number_terminal_1 = models.CharField(max_length=250,default='',null=True,blank=True)
    year_of_purchase_1 = models.CharField(max_length=250,default='',null=True,blank=True)
    cost_1 = models.CharField(max_length=250,default='',null=True,blank=True)
    software_facility_1 = models.CharField(max_length=250,default='',null=True,blank=True)
    other_facility_1 = models.CharField(max_length=250,default='',null=True,blank=True)

    serial_number_2 = models.CharField(max_length=250,default='',null=True,blank=True)
    type_of_computer_2 = models.CharField(max_length=250,default='',null=True,blank=True)
    number_terminal_2 = models.CharField(max_length=250,default='',null=True,blank=True)
    year_of_purchase_2 = models.CharField(max_length=250,default='',null=True,blank=True)
    cost_2 = models.CharField(max_length=250,default='',null=True,blank=True)
    software_facility_2 = models.CharField(max_length=250,default='',null=True,blank=True)
    other_facility_2 = models.CharField(max_length=250,default='',null=True,blank=True)

    serial_number_3 = models.CharField(max_length=250,default='',null=True,blank=True)
    type_of_computer_3 = models.CharField(max_length=250,default='',null=True,blank=True)
    number_terminal_3 = models.CharField(max_length=250,default='',null=True,blank=True)
    year_of_purchase_3 = models.CharField(max_length=250,default='',null=True,blank=True)
    cost_3 = models.CharField(max_length=250,default='',null=True,blank=True)
    software_facility_3 = models.CharField(max_length=250,default='',null=True,blank=True)
    other_facility_3 = models.CharField(max_length=250,default='',null=True,blank=True)

    serial_number_4 = models.CharField(max_length=250,default='',null=True,blank=True)
    type_of_computer_4 = models.CharField(max_length=250,default='',null=True,blank=True)
    number_terminal_4 = models.CharField(max_length=250,default='',null=True,blank=True)
    year_of_purchase_4 = models.CharField(max_length=250,default='',null=True,blank=True)
    cost_4 = models.CharField(max_length=250,default='',null=True,blank=True)
    software_facility_4 = models.CharField(max_length=250,default='',null=True,blank=True)
    other_facility_4 = models.CharField(max_length=250,default='',null=True,blank=True)

    serial_number_5 = models.CharField(max_length=250,default='',null=True,blank=True)
    type_of_computer_5 = models.CharField(max_length=250,default='',null=True,blank=True)
    number_terminal_5 = models.CharField(max_length=250,default='',null=True,blank=True)
    year_of_purchase_5 = models.CharField(max_length=250,default='',null=True,blank=True)
    cost_5 = models.CharField(max_length=250,default='',null=True,blank=True)
    software_facility_5 = models.CharField(max_length=250,default='',null=True,blank=True)
    other_facility_5 = models.CharField(max_length=250,default='',null=True,blank=True)

    serial_number_6 = models.CharField(max_length=250,default='',null=True,blank=True)
    type_of_computer_6 = models.CharField(max_length=250,default='',null=True,blank=True)
    number_terminal_6 = models.CharField(max_length=250,default='',null=True,blank=True)
    year_of_purchase_6 = models.CharField(max_length=250,default='',null=True,blank=True)
    cost_6 = models.CharField(max_length=250,default='',null=True,blank=True)
    software_facility_6 = models.CharField(max_length=250,default='',null=True,blank=True)
    other_facility_6 = models.CharField(max_length=250,default='',null=True,blank=True)

    #===========Information about Facility =================
    information_serial_number_1 = models.CharField(max_length=250,default='',null=True,blank=True)
    name_1 = models.CharField(max_length=250,default='',null=True,blank=True)
    designation_1 = models.CharField(max_length=250,default='',null=True,blank=True)
    qualification_1 = models.CharField(max_length=250,default='',null=True,blank=True)
    teaching_experience_1 = models.CharField(max_length=250,default='',null=True,blank=True)
    date_of_appointment_1 = models.CharField(max_length=250,default='',null=True,blank=True)
    status_1 = models.CharField(max_length=250,default='',null=True,blank=True)

    information_serial_number_2 = models.CharField(max_length=250,default='',null=True,blank=True)
    name_2 = models.CharField(max_length=250,default='',null=True,blank=True)
    designation_2 = models.CharField(max_length=250,default='',null=True,blank=True)
    qualification_2 = models.CharField(max_length=250,default='',null=True,blank=True)
    teaching_experience_2 = models.CharField(max_length=250,default='',null=True,blank=True)
    date_of_appointment_2 = models.CharField(max_length=250,default='',null=True,blank=True)
    status_2 = models.CharField(max_length=250,default='',null=True,blank=True)

    information_serial_number_3 = models.CharField(max_length=250,default='',null=True,blank=True)
    name_3 = models.CharField(max_length=250,default='',null=True,blank=True)
    designation_3 = models.CharField(max_length=250,default='',null=True,blank=True)
    qualification_3 = models.CharField(max_length=250,default='',null=True,blank=True)
    teaching_experience_3 = models.CharField(max_length=250,default='',null=True,blank=True)
    date_of_appointment_3 = models.CharField(max_length=250,default='',null=True,blank=True)
    status_3 = models.CharField(max_length=250,default='',null=True,blank=True)

    information_serial_number_4 = models.CharField(max_length=250,default='',null=True,blank=True)
    name_4 = models.CharField(max_length=250,default='',null=True,blank=True)
    designation_4 = models.CharField(max_length=250,default='',null=True,blank=True)
    qualification_4 = models.CharField(max_length=250,default='',null=True,blank=True)
    teaching_experience_4 = models.CharField(max_length=250,default='',null=True,blank=True)
    date_of_appointment_4 = models.CharField(max_length=250,default='',null=True,blank=True)
    status_4 = models.CharField(max_length=250,default='',null=True,blank=True)

    center_address = models.TextField(max_length=250,default='',null=True,blank=True)
    residential_address = models.TextField(max_length=250,default='',null=True,blank=True)
    signature = models.CharField(max_length=250,default='',null=True,blank=True)

    #===========Head Office use ===============
    form_receive_date = models.CharField(max_length=250,default='',null=True,blank=True)
    affliation_number = models.CharField(max_length=250,default='',null=True,blank=True)
    total_affliation_fee = models.CharField(max_length=250,default='',null=True,blank=True)
    registration_fee = models.CharField(max_length=250,default='',null=True,blank=True)
    amount_status = models.ForeignKey(Amount_Status, on_delete = models.CASCADE,null=True,blank=True) #select option filed
    bank_name = models.CharField(max_length=250,default='',null=True,blank=True)
    receipt_number = models.CharField(max_length=250,default='',null=True,blank=True)
    date = models.CharField(max_length=250,default='',null=True,blank=True)
    education_institution_type = models.CharField(max_length=250,default='',null=True,blank=True)
    affliation_from_date = models.CharField(max_length=250,default='',null=True,blank=True)
    affliation_to_date = models.CharField(max_length=250,default='',null=True,blank=True)
    date_and_time = models.DateTimeField(auto_now_add=True)

    # #============Addition Data===============
    district = models.CharField(max_length=50, null=True, blank=True)
    payment_mode = models.CharField(max_length=50,null=True, blank=True)
    manager_name = models.CharField(max_length=50,null=True, blank=True)
    principal_name = models.CharField(max_length=50, null=True, blank=True)
    manager_address = models.TextField(null=True, blank=True)
    principal_address = models.TextField(null=True, blank=True)
    type = models.CharField(max_length=20, choices=[('addon','addon'),('vtc','vtc')], default='vtc', null=True, blank=True)


    class Meta:
        verbose_name = 'Application for Affliation'
        

class Application_for_Affliation_Course(models.Model):
    course = models.ForeignKey(Course_Name, on_delete=models.CASCADE, null=True, blank=True)
    application = models.ForeignKey(Application_for_Affliation, on_delete=models.CASCADE, null=True, blank=True)

    
# =========================================================================================
#==================================================================================================



#====================================== Pay Online Fees Model =====================================
class Pay_Online_Fees(models.Model):
    college_name = models.CharField(max_length=250)
    type_of_fees =models.ForeignKey(Fee_Type, on_delete = models.CASCADE,null=True,blank=True) #select option filed
    type_of_other_fees = models.CharField(max_length=250)
    amount = models.IntegerField(default=0)
    date = models.CharField(max_length=250)   
    remark = models.TextField(max_length=250)  
    transaction_id = models.CharField(max_length=250)
    date_and_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.id)
    
    
    class Meta:
        verbose_name = 'Pay Online Fees'

#==================================================================================================
#==================================================================================================















#====================================== Official and Administration ===============================
#==================================================================================================

#====================================== E Office Account Model ====================================
class E_Office_Account(models.Model):
    type_of_account = models.ForeignKey(Type_of_Account, on_delete = models.CASCADE,null=True,blank=True) #select option filed
    voucher_number = models.CharField(max_length=250)
    particular_head = models.ForeignKey(Particulars_Head, on_delete = models.CASCADE,null=True,blank=True) #select option filed
    date = models.CharField(max_length=250)
    amount = models.CharField(max_length=250)

    #===========Online Payment Details ===============
    payment_type = models.CharField(max_length=25, choices=[('online','Online'),('offline','Offline')],default='online')
    amount2 = models.CharField(max_length=250, )   
    gst = models.CharField(max_length=25,null=True, blank=True)  
    bank_name = models.CharField(max_length=250,null=True, blank=True)  
    purpose = models.CharField(max_length=250,null=True, blank=True) 
    remitter_name = models.CharField(max_length=250,null=True, blank=True)
    amount_detail = models.CharField(max_length=250,null=True, blank=True)     
    transaction_number = models.CharField(max_length=250,null=True, blank=True)   
    remark = models.CharField(max_length=250,null=True, blank=True)   
    name = models.CharField(max_length=250,null=True, blank=True)   
    college_name = models.ForeignKey(College_Name, on_delete = models.CASCADE,null=True,blank=True) #select option filed
    address = models.CharField(max_length=250,null=True, blank=True)   
    file_referral_number = models.CharField(max_length=250,null=True, blank=True)
    office_registration_number = models.CharField(max_length=250,null=True, blank=True)     
    pan_card_number = models.CharField(max_length=250,null=True, blank=True)
    cashbook_registration_page_number = models.CharField(max_length=25,null=True, blank=True)
    cashbook_file_number = models.CharField(max_length=25,null=True, blank=True)
    finance_registration_book_number = models.CharField(max_length=25,null=True, blank=True)

    #===========Approval ======================
    officer_incharge_name = models.CharField(max_length=250, null=True, blank=True)   
    secretary_name = models.CharField(max_length=250, null=True, blank=True)     
    officer_incharge_status = models.ForeignKey(Status, on_delete = models.CASCADE,null=True,blank=True,related_name='officer_incharge_status') #select option filed
    secretary_status = models.ForeignKey(Status, on_delete = models.CASCADE,null=True,blank=True,related_name='secretry_status') #select option filed
    remark_staff_approval = models.CharField(max_length=250, null=True, blank=True)   
    remark_officer_approval = models.CharField(max_length=250, null=True, blank=True)
    administrate_officer_approval = models.CharField(max_length=50, null=True, blank=True)
    administrate_director_approval = models.CharField(max_length=50, null=True, blank=True)
    staff_approval = models.CharField(max_length=250, null=True, blank=True)
    officer_approval = models.CharField(max_length=250, null=True, blank=True)
    administrate_officer_approval_remarks = models.CharField(max_length=250, null=True, blank=True)
    administrate_director_remarks = models.CharField(max_length=250, null=True, blank=True)
    staff_approval_status = models.ForeignKey(Status, on_delete = models.CASCADE,null=True,blank=True,related_name='staff_approval_status') #select option filed
    officer_approval_status = models.ForeignKey(Status, on_delete = models.CASCADE,null=True,blank=True,related_name='officer_approval_status') #select option filed
    administrate_officer_status = models.ForeignKey(Status, on_delete = models.CASCADE,null=True,blank=True,related_name='administrate_officer_status') #select option filed
    administrate_director_status = models.ForeignKey(Status, on_delete = models.CASCADE,null=True,blank=True,related_name='administrate_director_status') #select option filed
    
    office_referral_number = models.CharField(max_length=250, null=True, blank=True) 
    description = models.TextField(max_length=250,null=True)   # Doubt in field
    date_and_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.id)
    
    class Meta:
        verbose_name = 'E Office Account'
#==================================================================================================
#==================================================================================================



#====================================== E Office Queue Model ======================================
class E_Office_Queue(models.Model):
    queue_number = models.CharField(max_length=250)
    file_subject = models.CharField(max_length=250)
    remark = models.CharField(max_length=250)
    approval_first_officer = models.ForeignKey(Status, on_delete = models.CASCADE,null=True,blank=True,related_name='approval_first_officer') #select option filed
    approval_second_officer = models.ForeignKey(Status, on_delete = models.CASCADE,null=True,blank=True,related_name='approval_second_officer') #select option filed 
    date_and_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.id)
    
    class Meta:
        verbose_name = 'E Office Queue'
#==================================================================================================
#==================================================================================================



#====================================== E Employee Record Model ===================================
class E_Employee_Record(models.Model):
    employee_record_type = models.ForeignKey(Employee_Record_Type, on_delete = models.CASCADE,null=True,blank=True) #select option filed 
    name = models.CharField(max_length=250)
    designation = models.CharField(max_length=250)
    employee_code = models.CharField(max_length=250)
    office_address = models.TextField(max_length=250)
    home_address = models.TextField(max_length=250)
    contact_number = models.CharField(max_length=250)
    aadhar_number = models.CharField(max_length=250)
    husband_or_wife_name = models.CharField(max_length=250)
    father_name = models.CharField(max_length=250)
    age_of_father = models.CharField(max_length=250)
    mother_name = models.CharField(max_length=250)
    age_of_mother = models.CharField(max_length=250)
    child_name_1 = models.CharField(max_length=250)
    age_of_child_1 = models.CharField(max_length=250)
    child_name_2 = models.CharField(max_length=250,default='',null=True,blank=True)
    age_of_child_2 = models.CharField(max_length=250,default='',null=True,blank=True)
    child_name_3 = models.CharField(max_length=250,default='',null=True,blank=True)
    age_of_child_3 = models.CharField(max_length=250,default='',null=True,blank=True)
    scale_of_pay = models.CharField(max_length=250,default='',null=True,blank=True)
    employee_liablity = models.CharField(max_length=250,default='',null=True,blank=True)
    employee_promotion = models.CharField(max_length=250,default='',null=True,blank=True)
    employee_grade = models.CharField(max_length=250,default='',null=True,blank=True)
    salary = models.CharField(max_length=250,default='',null=True,blank=True)
    advance = models.CharField(max_length=250,default='',null=True,blank=True)
    bonus = models.CharField(max_length=250,default='',null=True,blank=True)
    loan = models.CharField(max_length=250,default='',null=True,blank=True)
    note = models.TextField(max_length=250,default='',null=True,blank=True)
    remark = models.TextField(max_length=250,default='',null=True,blank=True)
    suspension = models.CharField(max_length=250,default='',null=True,blank=True)
    showcase_notice = models.CharField(max_length=250,default='',null=True,blank=True)
    date_and_time = models.DateTimeField(auto_now_add=True)
    pf_id = models.CharField(max_length=250,null=True,blank=True)
    head_office = models.CharField(max_length=250,null=True,blank=True)

 
    def __str__(self):
        return str(self.id)
    class Meta:
        verbose_name = 'E Employee Record'

class E_Employee_Record_Contribution(models.Model):
    
    month = models.CharField(max_length=25, null=True, blank=True)
    year = models.CharField(max_length=25, null=True, blank=True)
    amount = models.CharField(max_length=25, null=True, blank=True)
    
    clerk = models.CharField(
        max_length=250, 
        choices=[
            ('approved', 'Approved'),
            ('pending', 'Pending'),
            ('not_approved', 'Not Approved')
        ]
    )
    
    fo = models.CharField(
        max_length=250, 
        choices=[
            ('approved', 'Approved'),
            ('pending', 'Pending'),
            ('not_approved', 'Not Approved')
        ]
    )
    
    executive_officer = models.CharField(
        max_length=250, 
        choices=[
            ('approved', 'Approved'),
            ('pending', 'Pending'),
            ('not_approved', 'Not Approved')
        ]
    )
    
    record = models.ForeignKey(E_Employee_Record, on_delete=models.CASCADE, null=True, blank=True) 



#==================================================================================================
#==================================================================================================


#====================================== E Office File Sanction Model ==============================
class E_Office_File_Sanction(models.Model):
    docket_number = models.CharField(max_length=250)
    employee_code = models.CharField(max_length=250)
    employee_name = models.CharField(max_length=250)
    file_number = models.CharField(max_length=250)
    file_name = models.CharField(max_length=250)
    sanction_clerk = models.ForeignKey(Status, on_delete = models.CASCADE,null=True,blank=True,related_name='sanction_clerk_status') #select option filed 
    officer_grade_1 = models.ForeignKey(Status, on_delete = models.CASCADE,null=True,blank=True,related_name='officer_grade_1_status') #select option filed 
    officer_grade_2 = models.ForeignKey(Status, on_delete = models.CASCADE,null=True,blank=True,related_name='officer_grade_2_status') #select option filed 
    note_file = models.TextField(max_length=250)
    general_note_sanction_order = models.TextField(max_length=250)
    order_number = models.CharField(max_length=250)
    remark = models.CharField(max_length=250,default='',null=True,blank=True)   
    date_and_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.id)
    
    class Meta:
        verbose_name = 'E Office File Sanction'
#==================================================================================================
#==================================================================================================



#====================================== E Employee Daily Work Statement Model =====================
class E_employee_daily_work_statement(models.Model):
    employee_name = models.CharField(max_length=250)  
    work_start_time = models.CharField(max_length=250)
    employee_code = models.CharField(max_length=250)
    work_end_time = models.CharField(max_length=250)
    serial_number_1 = models.CharField(max_length=250)
    file_number_1 = models.CharField(max_length=250)
    work_name_1 = models.CharField(max_length=250)
    work_status_1 = models.ForeignKey(Work_Status, on_delete = models.CASCADE,null=True,blank=True,related_name='work_status_1') #select option filed 
    serial_number_2 = models.CharField(max_length=250,default='',null=True,blank=True)
    file_number_2 = models.CharField(max_length=250,default='',null=True,blank=True)
    work_name_2 = models.CharField(max_length=250,default='',null=True,blank=True)
    work_status_2 = models.ForeignKey(Work_Status, on_delete = models.CASCADE,null=True,blank=True,related_name='work_status_2') #select option filed 
    serial_number_3 = models.CharField(max_length=250,default='',null=True,blank=True)
    file_number_3 = models.CharField(max_length=250,default='',null=True,blank=True)
    work_name_3 = models.CharField(max_length=250,default='',null=True,blank=True)
    work_status_3 = models.ForeignKey(Work_Status, on_delete = models.CASCADE,null=True,blank=True,related_name='work_status_3') #select option filed 
    serial_number_4 = models.CharField(max_length=250,default='',null=True,blank=True)
    file_number_4 = models.CharField(max_length=250,default='',null=True,blank=True)
    work_name_4 = models.CharField(max_length=250,default='',null=True,blank=True)
    work_status_4 = models.ForeignKey(Work_Status, on_delete = models.CASCADE,null=True,blank=True,related_name='work_status_4') #select option filed 
    serial_number_5 = models.CharField(max_length=250,default='',null=True,blank=True)
    file_number_5 = models.CharField(max_length=250,default='',null=True,blank=True)
    work_name_5 = models.CharField(max_length=250,default='',null=True,blank=True)
    work_status_5 = models.ForeignKey(Work_Status, on_delete = models.CASCADE,null=True,blank=True,related_name='work_status_5') #select option filed 
    serial_number_6 = models.CharField(max_length=250,default='',null=True,blank=True)
    file_number_6 = models.CharField(max_length=250,default='',null=True,blank=True)
    work_name_6 = models.CharField(max_length=250,default='',null=True,blank=True)
    work_status_6 = models.ForeignKey(Work_Status, on_delete = models.CASCADE,null=True,blank=True,related_name='work_status_6') #select option filed 
    serial_number_7 = models.CharField(max_length=250,default='',null=True,blank=True)
    file_number_7 = models.CharField(max_length=250,default='',null=True,blank=True)
    work_name_7 = models.CharField(max_length=250,default='',null=True,blank=True)
    work_status_7 = models.ForeignKey(Work_Status, on_delete = models.CASCADE,null=True,blank=True,related_name='work_status_7') #select option filed 
    serial_number_8 = models.CharField(max_length=250,default='',null=True,blank=True)
    file_number_8 = models.CharField(max_length=250,default='',null=True,blank=True)
    work_name_8 = models.CharField(max_length=250,default='',null=True,blank=True)
    work_status_8 = models.ForeignKey(Work_Status, on_delete = models.CASCADE,null=True,blank=True,related_name='work_status_8') #select option filed 
    serial_number_9 = models.CharField(max_length=250,default='',null=True,blank=True)
    file_number_9 = models.CharField(max_length=250,default='',null=True,blank=True)
    work_name_9 = models.CharField(max_length=250,default='',null=True,blank=True)
    work_status_9 = models.ForeignKey(Work_Status, on_delete = models.CASCADE,null=True,blank=True,related_name='work_status_9') #select option filed 
    serial_number_10 = models.CharField(max_length=250,default='',null=True,blank=True)
    file_number_10 = models.CharField(max_length=250,default='',null=True,blank=True)
    work_name_10 = models.CharField(max_length=250,default='',null=True,blank=True)
    work_status_10 = models.ForeignKey(Work_Status, on_delete = models.CASCADE,null=True,blank=True,related_name='work_status_10') #select option filed 
    date = models.CharField(max_length=250,default='',null=True,blank=True)
    charge_officer_name = models.CharField(max_length=250)
    status_1 = models.ForeignKey(Status, on_delete = models.CASCADE,null=True,blank=True,related_name='status_1') #select option filed 
    chief_executive_officer_name = models.CharField(max_length=250)  
    status_2 = models.ForeignKey(Status, on_delete = models.CASCADE,null=True,blank=True,related_name='status_2') #select option filed 
    date_and_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.id)
    class Meta:
        verbose_name = 'E Employee Daily Work Statement'
    
#==================================================================================================
#==================================================================================================


#====================================== E Employee Live and Live Status Model =====================
class Employee_Status(models.Model):
    employee_live_or_leave_status = models.ForeignKey(Employee_Live_and_Leave_Status, on_delete = models.CASCADE,null=True,blank=True) #select option filed 
    employee_id_number = models.CharField(max_length=250)
    employee_name = models.CharField(max_length=250)
    date_and_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.id)
    class Meta:
        verbose_name = 'Employee Status'
    
#==================================================================================================
#==================================================================================================



#====================================== E Employee Leave Status Model ==============================
class E_employee_leave_status(models.Model):
    employee_live_or_leave_status = models.ForeignKey(Employee_Live_and_Leave_Status, on_delete = models.CASCADE,null=True,blank=True) #select option filed 
    employee_id_number = models.CharField(max_length=250)
    employee_name = models.CharField(max_length=250)
    purpose_1 = models.TextField(max_length=250)
    distance_walking_1 = models.CharField(max_length=250)
    purpose_2 = models.TextField(max_length=250,default='',null=True,blank=True)
    distance_walking_2 = models.CharField(max_length=250,default='',null=True,blank=True)
    purpose_3 = models.TextField(max_length=250,default='',null=True,blank=True)
    distance_walking_3 = models.CharField(max_length=250,default='',null=True,blank=True)
    staff_out_time = models.CharField(max_length=250)
    staff_in_time = models.CharField(max_length=250)
    status = models.ForeignKey(Status, on_delete = models.CASCADE,null=True,blank=True) #select option filed 
    remark = models.TextField(max_length=250,default='',null=True,blank=True)
    date_and_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.id)
    class Meta:
        verbose_name = 'E Employee Leave Status'
#==================================================================================================
#==================================================================================================



#====================================== E Employee Live Status Model ==============================
class E_employee_live_status(models.Model):
    employee_live_or_leave_status = models.ForeignKey(Employee_Live_and_Leave_Status, on_delete = models.CASCADE,null=True,blank=True) #select option filed 
    employee_id_number = models.CharField(max_length=250)
    employee_name = models.CharField(max_length=250)
    nature_of_leave = models.ForeignKey(Nature_of_Leave, on_delete = models.CASCADE,null=True,blank=True) #select option filed
    remark = models.TextField(max_length=250)
    date = models.CharField(max_length=250)
    status = models.ForeignKey(Status, on_delete = models.CASCADE,null=True,blank=True) #select option filed 
    date_and_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.id)
    class Meta:
        verbose_name = 'E Employee Live Status'
#==================================================================================================
#==================================================================================================




#====================================== Staff Work Allotment Model ================================
class Staff_work_allotment(models.Model):
    work_assign_office = models.ForeignKey(Work_Assign_Office, on_delete = models.CASCADE,null=True,blank=True) #select option filed 
    name_of_employee = models.CharField(max_length=250)
    work_start_date = models.CharField(max_length=250)
    work_start_time = models.CharField(max_length=250)
    work_name = models.CharField(max_length=250)
    upload_work = models.ImageField(upload_to='image/download/uploads/upload_work_image/',null=True,blank=True)
    work_finishing_date = models.CharField(max_length=250)
    work_finishing_time= models.CharField(max_length=250)
    work_head_name = models.CharField(max_length=250)
    current_status = models.ForeignKey(Work_Status, on_delete = models.CASCADE,null=True,blank=True) #select option filed 
    date_and_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.id)
    class Meta:
        verbose_name = 'Staff Work Allotment'
#==================================================================================================
#==================================================================================================




#====================================== Visitor Model ==============================================
class Visitor_IP(models.Model):
    visitor_ip = models.CharField(max_length=250)
    date_and_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.id)
    class Meta:
        verbose_name = 'Visitor IP'
#==================================================================================================
#==================================================================================================







#====================================== Tables Models =============================================
#==================================================================================================

#====================================== AFFILIATED VOCATIONAL TRAINING COLLEGES KERALA ============
class Affiliated_Vocational_Training_College_Kerla(models.Model):
    Table_Status = (
          ('1','ACTIVE'),
          ('2','INACTIVE'),
          )
    College_Type = (
          ('1','AIDED'),
          ('2','UN-AIDED'),
          )
    district = models.CharField(max_length=250,null=True,blank=True,default='')
    college_name = models.ForeignKey(College_Name, on_delete = models.CASCADE,null=True,blank=True,default='') #select option filed
    affiliation_number = models.CharField(max_length=250,null=True,blank=True,default='')
    principal_id = models.CharField(max_length=250,null=True,blank=True,default='')   
    current_status = models.CharField(max_length=25,choices=Table_Status,null=True,blank=True,default='')
    college_type = models.CharField(max_length=25,choices=College_Type,null=True,blank=True,default='')
    date_and_time = models.DateTimeField(auto_now_add=True)
    from_date = models.CharField(max_length=20, null=True, blank=True)
    to_date = models.CharField(max_length=20, null=True, blank=True)
    fee = models.CharField(max_length=10, null=True, blank=True)
    status = models.ForeignKey(Status, on_delete = models.SET_NULL, null=True,blank=True)


    def __str__(self):
        return str(self.id)
    class Meta:
        verbose_name = 'Affiliated Vocational Training College Kerla'
#==================================================================================================
#==================================================================================================



#====================================== ADD -ON PROGRAMME COLLEGE AFFILIATION ( Kerala ) ===========
class Add_on_Programme_College_Affiliation_Kerla(models.Model):
    state = models.CharField(max_length=250,null=True,blank=True,default='')
    district = models.CharField(max_length=250,null=True,blank=True,default='')
    college_name = models.ForeignKey(College_Name, on_delete = models.CASCADE,null=True,blank=True) #select option filed
    affiliation_number = models.CharField(max_length=250,null=True,blank=True,default='')
    principal_id = models.CharField(max_length=250,null=True,blank=True,default='')   
    date_and_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.id)
    class Meta:
        verbose_name = 'Add On Programme College Affiliation Kerla'
    
#==================================================================================================
#==================================================================================================



#====================================== ADD -ON PROGRAMME COLLEGE AFFILIATION ( Bangalore ) ===========
class Add_on_Programme_College_Affiliation_Bangalore(models.Model):
    state = models.CharField(max_length=250,null=True,blank=True,default='')
    district = models.CharField(max_length=250,null=True,blank=True,default='')
    college_name = models.ForeignKey(College_Name, on_delete = models.CASCADE,null=True,blank=True) #select option filed
    affiliation_number = models.CharField(max_length=250,null=True,blank=True,default='')
    principal_id = models.CharField(max_length=250,null=True,blank=True,default='')   
    date_and_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.id)
    class Meta:
        verbose_name = 'Add On Programme College Affiliation Bangalore'
#==================================================================================================
#==================================================================================================



#====================================== VOCATIONAL COURSES =========================================
class Vocational_Course(models.Model):
    course_name = models.ForeignKey(Course_Name, on_delete = models.CASCADE,null=True,blank=True) #select option filed
    duration = models.CharField(max_length=250,null=True,blank=True,default='')
    add_on_exam_fees = models.IntegerField(default=0)
    admission_fee_1 = models.IntegerField(default=0)
    exam_fee_1 = models.IntegerField(default=0)
    transcript_fee_1 = models.IntegerField(default=0)
    total_fee_1 = models.IntegerField(default=0)
    admission_fee_2 = models.IntegerField(default=0)
    exam_fee_2 = models.IntegerField(default=0)
    transcript_fee_2 = models.IntegerField(default=0)
    total_fee_2 = models.IntegerField(default=0)
    yearly_exam_fee = models.IntegerField(default=0)
    gst = models.CharField(max_length=250,null=True,blank=True,default='')
    date_and_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.id)
    class Meta:
        verbose_name = 'Vocational Course'
#==================================================================================================
#==================================================================================================


#====================================== CERTIFICATE COURSE =======================================
class Certificate_Course(models.Model):
    course_name = models.ForeignKey(Course_Name, on_delete = models.CASCADE,null=True,blank=True) #select option filed
    duration = models.CharField(max_length=250,null=True,blank=True,default='')
    add_on_exam_fees = models.IntegerField(default=0)
    admission_fee_1 = models.IntegerField(default=0)
    exam_fee_1 = models.IntegerField(default=0)
    transcript_fee_1 = models.IntegerField(default=0)
    total_fee_1 = models.IntegerField(default=0)
    gst = models.CharField(max_length=250,null=True,blank=True,default='')
    remark = models.TextField(max_length=250,null=True,blank=True,default='')
    date_and_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.id)
    class Meta:
        verbose_name = 'Certificate Course'
#==================================================================================================
#==================================================================================================



#====================================== DIPLOMA PROGRAME ==========================================
class Diploma_Programme(models.Model):
    course_name = models.ForeignKey(Course_Name, on_delete = models.CASCADE,null=True,blank=True) #select option filed
    duration = models.CharField(max_length=250,null=True,blank=True,default='')
    add_on_exam_fees = models.IntegerField(default=0)
    admission_fee_1 = models.IntegerField(default=0)
    exam_fee_1 = models.IntegerField(default=0)
    transcript_fee_1 = models.IntegerField(default=0)
    total_fee_1 = models.IntegerField(default=0)
    gst = models.CharField(max_length=250,null=True,blank=True,default='')
    remark = models.TextField(max_length=250,null=True,blank=True,default='')
    date_and_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.id)
    class Meta:
        verbose_name = 'Diploma Programme'
#==================================================================================================
#==================================================================================================



#====================================== PG DIPLOMA PROGRAMME =======================================
class PG_Diploma_Programme(models.Model):
    course_name = models.ForeignKey(Course_Name, on_delete = models.CASCADE,null=True,blank=True) #select option filed
    duration = models.CharField(max_length=250,null=True,blank=True,default='')
    add_on_exam_fees = models.IntegerField(default=0)
    admission_fee_1 = models.IntegerField(default=0)
    exam_fee_1 = models.IntegerField(default=0)
    transcript_fee_1 = models.IntegerField(default=0)
    total_fee_1 = models.IntegerField(default=0)
    admission_fee_2 = models.IntegerField(default=0)
    exam_fee_2 = models.IntegerField(default=0)
    transcript_fee_2 = models.IntegerField(default=0)
    total_fee_2 = models.IntegerField(default=0)
    gst = models.CharField(max_length=250,null=True,blank=True,default='')
    remark = models.TextField(max_length=250,null=True,blank=True,default='')
    date_and_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.id)
    class Meta:
        verbose_name = 'PG Diploma Programme'
#==================================================================================================
#==================================================================================================



#====================================== News ======================================================
class NewsCategory(models.Model):
    category_name = models.CharField(max_length=250)
class News(models.Model):
    news_title = models.CharField(max_length=250)
    news_image = models.ImageField(upload_to='image/download/uploads/news_image/',null=True,blank=True)
    news_description = models.TextField()
    news_date = models.DateField(auto_now_add=True)
    category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return str(self.news_title)
    class Meta:
        verbose_name = 'News'
#==================================================================================================
#==================================================================================================



#====================================== Free Skill Training =======================================
class Free_Skill_Training(models.Model):
    skill_image = models.ImageField(upload_to='image/download/uploads/skill_image/')
    skill_date = models.DateField(auto_now_add=True)
    def __str__(self):
        return str(self.id)
    class Meta:
        verbose_name = 'Free Skill Training'
#==================================================================================================
#==================================================================================================

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(null=True, max_length=200)
    meta_title = models.CharField(max_length=70, blank=True, null=True)  
    meta_description = models.CharField(max_length=160, blank=True, null=True)  
    meta_keywords = models.CharField(max_length=255, blank=True, null=True) 
    blog_image = models.ImageField(upload_to='image/download/uploads/blog_image/')
    category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE,null=True,blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)  
        super(BlogPost, self).save(*args, **kwargs)

    def _str_(self):
        return self.title
    


