"""
   Made By -: Techzniczone
   website - :https://www.techzniczone.com/
   email - :techzniczone@gmail.com
   """

from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin


class AdminCustomeuser(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id','username','user_role','first_name', 'last_name','gender','email','dob','mobile_number','address','user_status','decrypt_password','date_and_time']
    search_fields = ['first_name','last_name','email','mobile_number']

class AdminType_of_Account(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id','type_of_account','date_and_time']
    search_fields = ['type_of_accountr']


class AdminParticulars_Head(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id','particular_head','date_and_time']
    search_fields = ['particular_head']


class AdminCollege_Name(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id','college_name','date_and_time']
    search_fields = ['college_name']

class AdminCourse_Name(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id','course_name','date_and_time']
    search_fields = ['course_name']


class AdminStatus(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id','status','date_and_time']
    search_fields = ['status']

class AdminEmployee_Record_Type(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id','employee_record_type','date_and_time']
    search_fields = ['employee_record_type']

class AdminWork_Status(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id','work_status','date_and_time']
    search_fields = ['work_status']


class AdminEmployee_Live_and_Leave_Status(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id','employee_live_and_leave_status','date_and_time']
    search_fields = ['employee_live_and_leave_status']


class AdminWork_Assign_Office(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id','work_assign_office','date_and_time']
    search_fields = ['work_assign_office']

class AdminExam_Fees_Type(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id','exam_fees_type','date_and_time']
    search_fields = ['exam_fees_type']

class AdminMark_Status(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id','mark_status','date_and_time']
    search_fields = ['mark_status']

class AdminResult_Status(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id','result_status','date_and_time']
    search_fields = ['result_status']

class AdminAdd_on_College(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id','add_on_college_name','date_and_time']
    search_fields = ['add_on_college_name']

class AdminMain_Course(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id','main_course_name','date_and_time']
    search_fields = ['main_course_name']

class AdminInstitution_Status(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id','institution_status','date_and_time']
    search_fields = ['institution_status']

class AdminAmount_Status(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id','amount_status','date_and_time']
    search_fields = ['amount_status']

class AdminFee_Type(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id','fee_type','date_and_time']
    search_fields = ['fee_type']

class AdminNature_of_Leave(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id','nature_of_leave','date_and_time']
    search_fields = ['nature_of_leave']

class AdminUser_Role(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id','user_role','date_and_time']
    search_fields = ['user_role']


class AdminContact_us(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id','contact_id','full_name','email','subject','mobile_number','date_and_time']
    search_fields = ['contact_id','full_name','email','subject','mobile_number']


class AdminAdmission_Registration(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id','registration_number','name_of_student','address', 'id_number','date_of_birth','mobile_number',\
                    'college_name','district','course_name','admission_fees','admission_date','principal_approval','date_and_time']
    search_fields = ['registration_number','name_of_student','address', 'id_number','date_of_birth','mobile_number',\
                    'college_name','district','course_name','admission_fees','admission_date','principal_approval']
    

class AdminVTC_Course_Admission_Registration(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id','registration_number','name_of_student','address', 'id_number','date_of_birth','mobile_number',\
                    'college_name','district','course_name','admission_fees','admission_date','principal_approval','date_and_time']
    search_fields = ['registration_number','name_of_student','address', 'id_number','date_of_birth','mobile_number',\
                    'college_name','district','course_name','admission_fees','admission_date','principal_approval']    


class AdminExam_Registration(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id','registration_number','exam_fees','exam_attendance', 'any_fees_concession','date','principal_code',\
                    'principal_name','online_fees','principal_approval','date_and_time']
    search_fields = ['registration_number','exam_fees','exam_attendance', 'any_fees_concession','date','principal_code',\
                    'principal_name','online_fees','principal_approval']
    

class AdminMark_List_Registration(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id','registration_number','date','subject_1','subject_2','subject_3','subject_4','subject_5','subject_6',\
                    'subject_7','subject_8','subject_9','subject_10','subject_11','subject_12','internal_marks_1','internal_marks_2',\
                    'internal_marks_3','internal_marks_4','internal_marks_5','internal_marks_6','internal_marks_7','internal_marks_8',
                    'internal_marks_9','internal_marks_10','internal_marks_11','internal_marks_12','external_marks_1','external_marks_2',\
                    'external_marks_3','external_marks_4','external_marks_5','external_marks_6','external_marks_7','external_marks_8',
                    'external_marks_9','external_marks_10','external_marks_11','external_marks_12','mark_obtained_1','mark_obtained_2',\
                    'mark_obtained_3','mark_obtained_4','mark_obtained_5','mark_obtained_6','mark_obtained_7','mark_obtained_8',
                    'mark_obtained_9','mark_obtained_10','mark_obtained_11','mark_obtained_12','total_1','total_2',\
                    'total_3','total_4','total_5','total_6','total_7','total_8','total_9','total_10','total_11','total_12','grade_1','grade_2',\
                    'grade_3','grade_4','grade_5','grade_6','grade_7','grade_8','grade_9','grade_10','grade_11','grade_12',\
                    'total_mark_1','total_mark_obtained','mark_enter_clerk_name','mark_enter_clerk',\
                    'mark_check_clerk_name','mark_check_clerk','second_verified_officer_name','second_verified_officer',\
                    'final_mark_verified_officer_name','result_status','result_enter_register_book_number','mark_obtained','total_mark_2','date_and_time']
    search_fields = ['registration_number','date','subject_1','subject_2','subject_3','subject_4','subject_5','subject_6',\
                    'subject_7','subject_8','subject_9','subject_10','subject_11','subject_12','internal_marks_1','internal_marks_2',\
                    'internal_marks_3','internal_marks_4','internal_marks_5','internal_marks_6','internal_marks_7','internal_marks_8',
                    'internal_marks_9','internal_marks_10','internal_marks_11','internal_marks_12','external_marks_1','external_marks_2',\
                    'external_marks_3','external_marks_4','external_marks_5','external_marks_6','external_marks_7','external_marks_8',
                    'external_marks_9','external_marks_10','external_marks_11','external_marks_12','mark_obtained_1','mark_obtained_2',\
                    'mark_obtained_3','mark_obtained_4','mark_obtained_5','mark_obtained_6','mark_obtained_7','mark_obtained_8',
                    'mark_obtained_9','mark_obtained_10','mark_obtained_11','mark_obtained_12','total_1','total_2',\
                    'total_3','total_4','total_5','total_6','total_7','total_8','total_9','total_10','total_11','total_12','grade_1','grade_2',\
                    'grade_3','grade_4','grade_5','grade_6','grade_7','grade_8','grade_9','grade_10','grade_11','grade_12',\
                    'total_mark_1','total_mark_obtained','mark_enter_clerk_name','mark_enter_clerk',\
                    'mark_check_clerk_name','mark_check_clerk','second_verified_officer_name','second_verified_officer',\
                    'final_mark_verified_officer_name','result_status','result_enter_register_book_number','mark_obtained','total_mark_2']


class AdminAdd_on_Programme(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id','add_on_College','course_name','course_code', 'student_name','address','id_number',\
                    'contact_number','exam_fees','amount','main_course','college_coordinator_approval','date_and_time']
    search_fields = ['add_on_College','course_name','course_code', 'student_name','address','id_number',\
                    'contact_number','exam_fees','amount','main_course','college_coordinator_approval']
    

class AdminApplication_for_Affliation(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id','name_of_institution','mobile_number','status_of_institution', 'email','status_of_institution_other','year_of_establishment',\
                    'address','pincode','name','education_qualification','date_of_birth','designation','profession_experience','postal_address','date_and_time']
    search_fields = ['name_of_institution','mobile_number','status_of_institution', 'email','status_of_institution_other','year_of_establishment',\
                    'address','pincode','name','education_qualification','date_of_birth','designation','profession_experience','postal_address']


class AdminPay_Online_Fees(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id','college_name','type_of_fees','type_of_other_fees', 'amount','date','remark','transaction_id','date_and_time']
    search_fields = ['college_name','type_of_fees','type_of_other_fees', 'amount','date','remark','transaction_id']


class AdminE_Office_Account(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [
    'id',
    'type_of_account',
    'voucher_number',
    'particular_head',
    'date',
    'amount',
    'bank_name',
    'amount_detail',
    'transaction_number',
    'remark',
    'name',
    'college_name',
    'address',
    'amount2',
    'file_referral_number',
    'office_registration_number',
    'pan_card_number',
    'officer_incharge_name',
    'secretary_name',
    'officer_incharge_status',
    'secretary_status',
    'remark_staff_approval',
    'remark_officer_approval',
    'office_referral_number',
    'description',
    'date_and_time',
]
    
search_fields = ['type_of_account',
    'voucher_number',
    'particular_head',
    'date',
    'amount',
    'bank_name',
    'amount_detail',
    'transaction_number',
    'remark',
    'name',
    'college_name',
    'address',
    'amount2',
    'file_referral_number',
    'office_registration_number',
    'pan_card_number',
    'officer_incharge_name',
    'secretary_name',
    'officer_incharge_status',
    'secretary_status',
    'remark_staff_approval',
    'remark_officer_approval',
    'office_referral_number',
    'description']


class AdminE_Office_Queue(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id','queue_number', 'file_subject', 'remark', 'approval_first_officer', 'approval_second_officer', 'date_and_time']
    search_fields = ['queue_number', 'file_subject', 'remark', 'approval_first_officer', 'approval_second_officer']


class AdminE_Employee_Record(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [
        'id',
        'employee_record_type',
        'name',
        'designation',
        'employee_code',
        'office_address',
        'home_address',
        'contact_number',
        'aadhar_number',
        'husband_or_wife_name',
        'father_name',
        'age_of_father',
        'mother_name',
        'age_of_mother',
        'child_name_1',
        'age_of_child_1',
        'child_name_2',
        'age_of_child_2',
        'child_name_3',
        'age_of_child_3',
        'scale_of_pay',
        'employee_liablity',
        'employee_promotion',
        'employee_grade',
        'salary',
        'advance',
        'bonus',
        'loan',
        'note',
        'remark',
        'suspension',
        'showcase_notice',
        'date_and_time',
    ]

    search_fields = ['employee_record_type',
        'name',
        'designation',
        'employee_code',
        'office_address',
        'home_address',
        'contact_number',
        'aadhar_number',
        'husband_or_wife_name',
        'father_name',
        'age_of_father',
        'mother_name',
        'age_of_mother',
        'child_name_1',
        'age_of_child_1',
        'child_name_2',
        'age_of_child_2',
        'child_name_3',
        'age_of_child_3',
        'scale_of_pay',
        'employee_liablity',
        'employee_promotion',
        'employee_grade',
        'salary',
        'advance',
        'bonus',
        'loan',
        'note',
        'remark',
        'suspension',
        'showcase_notice']

class AdminE_Office_File_Sanction(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [
        'id',
        'docket_number',
        'employee_code',
        'employee_name',
        'file_number',
        'file_name',
        'sanction_clerk',
        'officer_grade_1',
        'officer_grade_2',
        'note_file',
        'general_note_sanction_order',
        'order_number',
        'remark',
        'date_and_time',
    ]

    search_fields = ['docket_number',
        'employee_code',
        'employee_name',
        'file_number',
        'file_name',
        'sanction_clerk',
        'officer_grade_1',
        'officer_grade_2',
        'note_file',
        'general_note_sanction_order',
        'order_number',
        'remark']



class AdminE_employee_daily_work_statement(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id','employee_name', 'work_start_time', 'employee_code', 'work_end_time',
                    'serial_number_1', 'file_number_1', 'work_name_1', 'work_status_1',
                    'serial_number_2', 'file_number_2', 'work_name_2', 'work_status_2',
                    'serial_number_3', 'file_number_3', 'work_name_3', 'work_status_3',
                    'serial_number_4', 'file_number_4', 'work_name_4', 'work_status_4',
                    'serial_number_5', 'file_number_5', 'work_name_5', 'work_status_5',
                    'serial_number_6', 'file_number_6', 'work_name_6', 'work_status_6',
                    'serial_number_7', 'file_number_7', 'work_name_7', 'work_status_7',
                    'serial_number_8', 'file_number_8', 'work_name_8', 'work_status_8',
                    'serial_number_9', 'file_number_9', 'work_name_9', 'work_status_9',
                    'serial_number_10', 'file_number_10', 'work_name_10', 'work_status_10',
                    'date', 'charge_officer_name', 'status_1', 'chief_executive_officer_name',
                    'status_2', 'date_and_time']
    search_fields = [
        'employee_name', 'work_start_time', 'employee_code', 'work_end_time',
                    'serial_number_1', 'file_number_1', 'work_name_1', 'work_status_1',
                    'serial_number_2', 'file_number_2', 'work_name_2', 'work_status_2',
                    'serial_number_3', 'file_number_3', 'work_name_3', 'work_status_3',
                    'serial_number_4', 'file_number_4', 'work_name_4', 'work_status_4',
                    'serial_number_5', 'file_number_5', 'work_name_5', 'work_status_5',
                    'serial_number_6', 'file_number_6', 'work_name_6', 'work_status_6',
                    'serial_number_7', 'file_number_7', 'work_name_7', 'work_status_7',
                    'serial_number_8', 'file_number_8', 'work_name_8', 'work_status_8',
                    'serial_number_9', 'file_number_9', 'work_name_9', 'work_status_9',
                    'serial_number_10', 'file_number_10', 'work_name_10', 'work_status_10',
                    'date', 'charge_officer_name', 'status_1', 'chief_executive_officer_name',
                    'status_2']
    

class AdminEmployee_Status(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id','employee_live_or_leave_status', 'employee_id_number', 'employee_name', 'date_and_time']
    search_fields = ['employee_live_or_leave_status', 'employee_id_number', 'employee_name']


class AdminE_employee_leave_status(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id','employee_live_or_leave_status', 'employee_id_number', 'employee_name',
                    'purpose_1', 'distance_walking_1', 'purpose_2', 'distance_walking_2',
                    'purpose_3', 'distance_walking_3', 'staff_out_time', 'staff_in_time',
                    'status', 'remark', 'date_and_time']
    search_fields = [
        'employee_live_or_leave_status', 'employee_id_number', 'employee_name',
                    'purpose_1', 'distance_walking_1', 'purpose_2', 'distance_walking_2',
                    'purpose_3', 'distance_walking_3', 'staff_out_time', 'staff_in_time',
                    'status', 'remark']



class AdminE_employee_live_status(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ["id","employee_live_or_leave_status", "employee_id_number", "employee_name", "nature_of_leave", "remark", "date", "status", "date_and_time"]
    search_fields = [
        "employee_live_or_leave_status", "employee_id_number", "employee_name", "nature_of_leave", "remark", "date", "status"]


class AdminStaff_work_allotment(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id','work_assign_office', 'name_of_employee', 'work_start_date', 'work_start_time',
                    'work_name', 'upload_work', 'work_finishing_date', 'work_finishing_time',
                    'work_head_name', 'current_status', 'date_and_time']
    search_fields = ['work_assign_office', 'name_of_employee', 'work_start_date', 'work_start_time',
                    'work_name', 'upload_work', 'work_finishing_date', 'work_finishing_time',
                    'work_head_name', 'current_status']
    


class AdminAffiliated_Vocational_Training_College_Kerla(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id','district', 'college_name', 'affiliation_number', 'principal_id', 'current_status', 'college_type', 'date_and_time']
    search_fields = [
        'district', 'college_name', 'affiliation_number', 'principal_id', 'current_status', 'college_type']


class AdminAdd_on_Programme_College_Affiliation_Kerla(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id','state', 'district', 'college_name', 'affiliation_number', 'principal_id', 'date_and_time']
    search_fields = [
        'state', 'district', 'college_name', 'affiliation_number', 'principal_id']


class AdminAdd_on_Programme_College_Affiliation_Bangalore(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id','state', 'district', 'college_name', 'affiliation_number', 'principal_id', 'date_and_time']
    search_fields = [
        'state', 'district', 'college_name', 'affiliation_number', 'principal_id']


class AdminVocational_Course(ImportExportModelAdmin, admin.ModelAdmin):
    list_display  = [
            'id','course_name', 'duration', 'add_on_exam_fees', 'admission_fee_1', 'exam_fee_1',
            'transcript_fee_1', 'total_fee_1', 'admission_fee_2', 'exam_fee_2', 'transcript_fee_2',
            'total_fee_2', 'yearly_exam_fee', 'gst', 'date_and_time'
        ]
    search_fields = [
        'course_name', 'duration', 'add_on_exam_fees', 'admission_fee_1', 'exam_fee_1',
            'transcript_fee_1', 'total_fee_1', 'admission_fee_2', 'exam_fee_2', 'transcript_fee_2',
            'total_fee_2', 'yearly_exam_fee', 'gst']

class AdminCertificate_Course(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id','course_name', 'duration', 'add_on_exam_fees', 'admission_fee_1', 'exam_fee_1',
                    'transcript_fee_1', 'total_fee_1', 'gst', 'remark', 'date_and_time']
    search_fields = [
        'course_name', 'duration', 'add_on_exam_fees', 'admission_fee_1', 'exam_fee_1',
                    'transcript_fee_1', 'total_fee_1', 'gst', 'remark']


class AdminDiploma_Programme(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id','course_name', 'duration', 'add_on_exam_fees', 'admission_fee_1', 'exam_fee_1', 'transcript_fee_1', 'total_fee_1', 'gst', 'remark', 'date_and_time']
    search_fields = [
        'course_name', 'duration', 'add_on_exam_fees', 'admission_fee_1', 'exam_fee_1', 'transcript_fee_1', 'total_fee_1', 'gst', 'remark']


class AdminPG_Diploma_Programme(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id','course_name', 'duration', 'add_on_exam_fees', 'admission_fee_1', 'exam_fee_1', 'transcript_fee_1',
                'total_fee_1', 'admission_fee_2', 'exam_fee_2', 'transcript_fee_2', 'total_fee_2', 'gst', 'remark', 'date_and_time']
    search_fields = [
        'course_name', 'duration', 'add_on_exam_fees', 'admission_fee_1', 'exam_fee_1', 'transcript_fee_1',
                'total_fee_1', 'admission_fee_2', 'exam_fee_2', 'transcript_fee_2', 'total_fee_2', 'gst', 'remark']







admin.site.register(Type_of_Account,AdminType_of_Account)
admin.site.register(Particulars_Head,AdminParticulars_Head)
admin.site.register(College_Name,AdminCollege_Name)
admin.site.register(Course_Name,AdminCourse_Name)
admin.site.register(Status,AdminStatus)
admin.site.register(Employee_Record_Type,AdminEmployee_Record_Type)
admin.site.register(Work_Status,AdminWork_Status)
admin.site.register(Employee_Live_and_Leave_Status,AdminEmployee_Live_and_Leave_Status)
admin.site.register(Work_Assign_Office,AdminWork_Assign_Office)
admin.site.register(Exam_Fees_Type,AdminExam_Fees_Type)
admin.site.register(Mark_Status,AdminMark_Status)
admin.site.register(Result_Status,AdminResult_Status)
admin.site.register(Add_on_College,AdminAdd_on_College)
admin.site.register(Main_Course,AdminMain_Course)
admin.site.register(Institution_Status,AdminInstitution_Status)
admin.site.register(Amount_Status,AdminAmount_Status)
admin.site.register(Fee_Type,AdminFee_Type)
admin.site.register(Nature_of_Leave,AdminNature_of_Leave)
admin.site.register(CustomeUser,AdminCustomeuser)
admin.site.register(User_Role,AdminUser_Role)
admin.site.register(Contact_us,AdminContact_us)





admin.site.register(Admission_Registration,AdminAdmission_Registration)
admin.site.register(VTC_Course_Admission_Registration,AdminVTC_Course_Admission_Registration)
admin.site.register(Exam_Registration,AdminExam_Registration)
admin.site.register(Mark_List_Registration,AdminMark_List_Registration)
admin.site.register(Add_on_Programme,AdminAdd_on_Programme)
admin.site.register(Application_for_Affliation,AdminApplication_for_Affliation)
admin.site.register(Pay_Online_Fees,AdminPay_Online_Fees)
admin.site.register(E_Office_Account,AdminE_Office_Account)
admin.site.register(E_Office_Queue,AdminE_Office_Queue)
admin.site.register(E_Employee_Record,AdminE_Employee_Record)
admin.site.register(E_Office_File_Sanction,AdminE_Office_File_Sanction)
admin.site.register(E_employee_daily_work_statement,AdminE_employee_daily_work_statement)
admin.site.register(Employee_Status,AdminEmployee_Status)
admin.site.register(E_employee_leave_status,AdminE_employee_leave_status)
admin.site.register(E_employee_live_status,AdminE_employee_live_status)
admin.site.register(Staff_work_allotment,AdminStaff_work_allotment)
admin.site.register(Visitor_IP)



admin.site.register(Affiliated_Vocational_Training_College_Kerla,AdminAffiliated_Vocational_Training_College_Kerla)
admin.site.register(Add_on_Programme_College_Affiliation_Kerla,AdminAdd_on_Programme_College_Affiliation_Kerla)
admin.site.register(Add_on_Programme_College_Affiliation_Bangalore,AdminAdd_on_Programme_College_Affiliation_Bangalore)
admin.site.register(Vocational_Course,AdminVocational_Course)
admin.site.register(Certificate_Course,AdminCertificate_Course)
admin.site.register(Diploma_Programme,AdminDiploma_Programme)
admin.site.register(PG_Diploma_Programme,AdminPG_Diploma_Programme)
admin.site.register(News)
admin.site.register(Free_Skill_Training)
admin.site.register(E_Employee_Record_Contribution)
