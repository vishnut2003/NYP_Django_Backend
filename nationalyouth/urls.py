from django.contrib import admin
from django.urls import path, include
from nationalyouth.views import *
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from nationalyouth.e_view import *

    
    
router = DefaultRouter()
router.register(r'newscategories', NewsCategoryViewSet)
    
    
urlpatterns = [  
    path('password', PasswordGenerator.as_view(), name='password'),
    path('', include(router.urls)),
    path('',homepage,name='homepage'),
    path('add_new_user', add_new_user,name='add_new_user'),
    path('new_user', AddNewUser.as_view(),name='new_user'),
    path('dologin', Login.as_view(),name='dologin'),
    path('user_logout',LogoutView.as_view(),name='user_logout'),
    path('forgot_password',forgot_password,name='forgot_password'),
    path('about_us',about_us,name='about_us'),
    path('gallery',gallery,name='gallery'),
    path('sector',sector,name='sector'),
    path('contact_us',contact_us,name='contact_us'),
    path('home_contact_us',home_contact_us,name='home_contact_us'),
    path('news',news,name='news'),
    path('news_details',news_details,name='news_details'),


    path('course',course,name='course'),

      # Vocational Course URLs 
    path('vocational-course/create', VocationalCourseCreateView.as_view(), name='vocational_course_create'),
    path('vocational-course/<int:id>', VocationalCourseRetrieveUpdateDeleteView.as_view(), name='vocational_course_update'),

    # Certificate Course URLs
    path('certificate-course/create', CertificateCourseCreateView.as_view(), name='certificate_course_create'),
    path('certificate-course/<int:id>', CertificateCourseRetrieveUpdateDeleteView.as_view(), name='certificate_course_update'),

    # Diploma Programme URLs
    path('diploma-programme/create', DiplomaProgrammeCreateView.as_view(), name='diploma_programme_create'),
    path('diploma-programme/<int:id>', DiplomaProgrammeRetrieveUpdateDeleteView.as_view(), name='diploma_programme_update'),

    # PG Diploma Programme URLs
    path('pg-diploma-programme/create', PGDiplomaProgrammeCreateView.as_view(), name='pg_diploma_programme_create'),
    path('pg-diploma-programme/<int:id>', PGDiplomaProgrammeRetrieveUpdateDeleteView.as_view(), name='pg_diploma_programme_update'),

    path('all-course', allcourse,name='all_course'),
    path('college',college,name='college'),
    path('college/edit',collegeEdit.as_view()),
    path('colleges', ApplicationCollageListView.as_view(), name='college_list'),

    path('affiliated-vocational-training-colleges/create', AffiliatedVocationalTrainingCollegeKerlaCreateView.as_view(), name='affiliated_college_create'),
    
    path('affiliated-vocational-training-college/<int:id>', AffiliatedVocationalTrainingCollegeKerlaRetrieveUpdateDestroyView.as_view(), name='affiliated_college_detail'),
    
    path('add-on-programme-college-affiliation-kerala/create', AddOnProgrammeCollegeAffiliationKerlaCreateView.as_view(), name='add_on_programme_create'),
    
    path('add-on-programme-college-affiliation-kerala/<int:id>', AddOnProgrammeCollegeAffiliationKerlaRetrieveUpdateDestroyView.as_view(), name='add_on_programme_detail'),

    #blog
    path('posts', BlogPostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:id>', BlogPostDetailView.as_view(), name='post-detail'), 

    path('vtc_course_admission',vtc_course_admission,name='vtc_course_admission'),
    path('vtc_course_admissions',vtcCourseAdmission.as_view(),name='vtc_course_admissions'),
    path('admission_registration',admission_registration,name='admission_registration'),
    
    path('registration_data',RegistrationDataView.as_view(), name='registration_data'),
    
    path('exam_registration',exam_registration,name='exam_registration'),
    path('exam_registrations',Exam_Registration_View.as_view(),name='exam_registration'),
    path('exam_registration/<int:pk>',Exam_Registration_Detail_View.as_view(),name='exam_registrations_details'),
    path('mark_registration',mark_registration,name='mark_registration'),
    path('mark_registrations',Mark_List_Registration_View.as_view(),name='mark_registrations'),
    path('mark_registration/<int:pk>',Mark_List_Registration_Detail_View.as_view(),name='mark_registrations'),
    path('add_on_programme',add_on_programme,name='add_on_programme'),
    path('application_for_affiliation',application_for_affiliation,name='application_for_affiliation'),
    path('application_for_affiliation_vtc',ApplicationForAffilicationVtc.as_view(),name='application_for_affiliation_vtc'),
    path('application_for_affiliation/<int:pk>',ApplicationForAffilicationVtcDetails.as_view(),name='application_for_affiliation_details'),
    path('application_for_affiliation_addon',ApplicationForAffilicationAddOn.as_view(),name='application_for_affiliation_addon'),
    path('employee_service_book',employee_service_book,name='employee_service_book'),
    path('pay_online_fees',pay_online_fees,name='pay_online_fees'),
    path('e_office_file_sanction',e_office_file_sanction,name='e_office_file_sanction'),
    path('student_marks',student_marks,name='student_marks'),

    path('e_finance_and_accounts',e_finance_and_accounts,name='se_finance_and_accounts'),
    path('e_office_accounts',e_office_accounts,name='e_office_accounts'),
    path('e_office_student_register',e_office_student_register,name='e_office_student_register'),
    path('e_office_email',e_office_email,name='e_office_email'),
    path('e_office_queue_files',e_office_queue_files,name='e_office_queue_files'),
    path('e_office_files',e_office_files,name='e_office_files'),
    path('e_employee_records',e_employee_records,name='e_employee_records'),
    path('e_employee_live_and_leave_status',e_employee_live_and_leave_status,name='e_employee_live_and_leave_status'),
    path('e_employee_live_status',e_employee_live_status,name='e_employee_live_status'),
    path('e_employee_leave_status',e_employee_leave_status,name='e_employee_leave_status'),
    path('e_employee_daily_work_statement',e_employee_daily_work_statement,name='e_employee_daily_work_statement'),
    path('e_adminstations',e_adminstations,name='e_adminstations'),
    path('e_student_certificate_verification',e_student_certificate_verification,name='e_student_certificate_verification'),

    path('e_office_mark_list_registration',e_office_mark_list_registration,name='e_office_mark_list_registration'),
    path('e_office_student_admisiion_registration',e_office_student_admisiion_registration,name='e_office_student_admisiion_registration'),
    path('e_office_student_add_on_programme',e_office_student_add_on_programme,name='e_office_student_add_on_programme'),

    path('e_office_files_student_mark_list',e_office_files_student_mark_list,name='e_office_files_student_mark_list'),
    path('e_office_files_daily_work_statement',e_office_files_daily_work_statement,name='e_office_files_daily_work_statement'),
    path('e_office_files_employee_live_status',e_office_files_employee_live_status,name='e_office_files_employee_live_status'),
    path('e_office_files_pay_online_fees',e_office_files_pay_online_fees,name='e_office_files_pay_online_fees'),

    path('staff_work_alloted',staff_work_alloted,name='staff_work_alloted'),
    path('student_certificate__verification',student_certificate__verification,name="student_certificate__verification"),
    path('status',ApiStatus,name="student_certificate__verification"),
    path('course-add',course_add, name="course_add"),
    path('show-registered-student',showregistered_number, name='showregistered_number'),
    path('add-on-admission-detail/<int:id>',showregistered_number_detail, name='showregistered_number_detail'),
    path('add-on-admission-edit/<int:id>',showregistered_number_edit, name='showregistered_number_detail'),
    path('add-on-admission-delete/<int:id>',showregistered_number_delete, name='showregistered_number_detail'),
    
    path('vtc-admission',vtc_admission, name="vtc"),
    path('vtc-admission-detail/<int:id>',vtc_admission_detail, name="vtc"),
    
    path('edit-vtc-admission/<int:id>',vtc_admission_edit, name="vtc_edit"),
    path('category-list-news/<int:id>', CategoryListView.as_view(), name='category_list'),
    
    # =====================E-service==================== 
    
    path('E_Office_Queue', E_Office_Queue_View.as_view(), name='E_Office_Queue'),
    path("E_Employee_Record", E_Employee_Record_View.as_view(), name='E_Employee_Record'),
    path("E_Employee_Daily_Work_Statement", E_employee_daily_work_statement_View.as_view(), name='E_Employee_Daily_Work_Statement'),
    path("E_Employee_Live_Status", E_employee_live_status_View.as_view(), name='E_Employee_Live_Status'),
    path("E_Employee_Leave_Status", E_employee_leave_status_View.as_view(), name='E_Employee_Leave_Status'),
    path("Staff_Work_Allotment", Staff_work_allotment_View.as_view(), name='Staff_Work_Allotment'),
    path("E_Office_Account", E_Office_Account_View.as_view(), name='E_Office_Account'),
    path("E_Office_Account_NextId", E_Office_Account_Id_generate_View.as_view(), name='E_Office_Account_nextid'),
    path("E_Office_File_Sanction", E_Office_File_Sanction_View.as_view(), name='E_Office_File_Sanction'),
    path("Application_Afflication_Renewal", Application_for_Affliation_View.as_view(), name='Applicationl'),
    path("Student_Certificate", Student_Certificate_Verification.as_view(), name='Student_Certificate'),

    path('E_Office_Queue/<int:id>', E_Office_Queue_Detail_View.as_view(), name='e_office_queue_detail'),
    path('E_Employee_Record/<int:id>', E_Employee_Record_Detail_View.as_view(), name='e_employee_record_detail'),
    path('E_Employee_Record/<int:id>/contribution', E_Employee_Record_Contribution_View.as_view(), name='e_employee_record_contribution'),
    path('E_Employee_Daily_Work_Statement/<int:id>', E_employee_daily_work_statement_Detail_View.as_view(), name='e_employee_daily_work_statement_detail'),
    path('E_Employee_Live_Status/<int:id>', E_employee_live_status_Detail_View.as_view(), name='e_employee_live_status_detail'),
    path('E_Employee_Leave_Status/<int:id>', E_employee_leave_status_Detail_View.as_view(), name='e_employee_leave_status_detail'),
    path('Staff_Work_Allotment/<int:id>', Staff_work_allotment_Detail_View.as_view(), name='staff_work_allotment_detail'),
    path('E_Office_Account/<int:id>', E_Office_Account_Detail_View.as_view(), name='e_office_account_detail'),
    # path('e_office_file_sanction/<int:id>/', E_Office_File_Sanction_Detail_View.as_view(), name='e_office_file_sanction_detail'),
    # path('student_certificate_verification/<int:id>/', Student_Certificate_Verification_Detail_View.as_view(), name='student_certificate_verification_detail'),


]

