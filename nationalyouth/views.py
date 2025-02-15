"""
Made By -: Techzniczone
website - :https://www.techzniczone.com/
email - :techzniczone@gmail.com
"""

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
from django.shortcuts import render, redirect, HttpResponse
from nationalyouth.models import *
from rest_framework.viewsets import ModelViewSet
from django.views import View
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
import random
import time
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.permissions import AllowAny  # or other permissions
from rest_framework.authentication import (
    BasicAuthentication,
)  # or other authentication classes
from rest_framework.response import Response
from rest_framework.decorators import (
    api_view,
    permission_classes,
    authentication_classes,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import (
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
    ListCreateAPIView
    
)
from .serializer import *
from django.db import transaction



class PasswordGenerator(APIView):
    def get(self, request):
        password = request.data.get('password', None)
        hash_password = make_password(password)
        return Response(hash_password)
    
    
# application_for_affiliation
class ApplicationForAffilicationVtc(APIView):
    def get(self, request):
        queryset = Application_for_Affliation.objects.all().order_by("-date_and_time")
        serializer_obj = ApplicationForAffilicationListSerializer(queryset, many=True)
        return Response(serializer_obj.data, status=status.HTTP_200_OK)
        
    
    def post(self, request):
        serializer_obj = ApplicationForAffilicationSerializer(data=request.data)
        if serializer_obj.is_valid():
            serializer_obj.save(type='vtc')
            return Response(serializer_obj.data, status=status.HTTP_200_OK)
        print(serializer_obj.errors)
        return Response(status=status.HTTP_400_BAD_REQUEST, data='One or field do not have a value')



class ApplicationForAffilicationVtcDetails(APIView):
    def get(self, request, pk):
        application_queryset = Application_for_Affliation.objects.filter(id=pk).first()
        if application_queryset is None:
            return Response(status=status.HTTP_400_BAD_REQUEST, data='Id is not exist')
        application_serializer_obj = ApplicationForAffilicationListSerializer(application_queryset, many=False)
        return Response(status=status.HTTP_200_OK,data=application_serializer_obj.data)
    
    
    def patch(self, request, pk):
        application_queryset = Application_for_Affliation.objects.filter(id=pk).first()
        if application_queryset is None:
            return Response(status=status.HTTP_400_BAD_REQUEST, data='Id is not exist')
        application_serializer_obj = ApplicationForAffilicationListSerializer(application_queryset, data=request.data, partial=True)
        if application_serializer_obj.is_valid():
            application_affiliation = application_serializer_obj.save()

            # Ensure the college name is correctly referenced
            college, created = College_Name.objects.get_or_create(
                college_name=application_affiliation.name_of_institution
            )
            
            if application_affiliation.type == 'vtc':
                Affiliated_Vocational_Training_College_Kerla.objects.update_or_create(
                    college_name=college,
                    defaults={
                        "current_status":application_affiliation.status_of_institution_other,
                        'district': application_affiliation.district,
                        'affiliation_number': application_affiliation.affliation_number,
                        'principal_id': '',
                    }
                )
            else:

                 # Handle the creation or update of the Add_on_Programme_College_Affiliation_Kerla record
                Add_on_Programme_College_Affiliation_Kerla.objects.update_or_create(
                    college_name=college,
                    defaults={
                        'state': application_affiliation.status_of_institution_other,
                        'district': application_affiliation.district,
                        'affiliation_number': application_affiliation.affliation_number,
                        'principal_id': '',
                    }
                )
            return Response(status=status.HTTP_200_OK,data=application_serializer_obj.data)
        return Response(status=status.HTTP_400_BAD_REQUEST,data=application_serializer_obj.errors)


    def delete(self, request, pk):
        type = request.query_params.get('type')
        if type == 'affiliated_vocational_training_college_Kerla':
            query = Affiliated_Vocational_Training_College_Kerla.objects.filter(id=pk).first()
        elif type == 'add_on_programme_college_affiliation_kerla':
            query = Add_on_Programme_College_Affiliation_Kerla.objects.filter(id=pk).first()
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data='Invalid type')

        if query:
            query.delete()
            return Response(status=status.HTTP_200_OK, data='Data Deleted Successfully')
        else:
            return Response(status=status.HTTP_404_NOT_FOUND, data='Record not found')


# application_for_affiliation
class ApplicationForAffilicationAddOn(APIView):
    def post(self, request):
        serializer_obj = ApplicationForAffilicationSerializer(data=request.data)
        if serializer_obj.is_valid():
            serializer_obj.save(type='addon')
            return Response(serializer_obj.data, status=status.HTTP_200_OK)
        print(serializer_obj.errors)
        return Response(status=status.HTTP_400_BAD_REQUEST, data='One or field do not have a value')



def common_data():
    # ======= 1 Command =======================================
    all_admission_data = Admission_Registration.objects.all()
    for ad in all_admission_data:
        filter_exam_data = Exam_Registration.objects.filter(
            registration_number=ad.registration_number
        ).first()
        if filter_exam_data:
            filter_exam_data.name_of_student = ad.name_of_student
            filter_exam_data.address = ad.address
            filter_exam_data.id_number = ad.id_number
            filter_exam_data.date_of_birth = ad.date_of_birth
            filter_exam_data.mobile_number = ad.mobile_number
            filter_exam_data.college_name = ad.college_name
            filter_exam_data.district = ad.district
            filter_exam_data.course_name = ad.course_name
            filter_exam_data.admission_fees = ad.admission_fees
            filter_exam_data.admission_date = ad.admission_date
            filter_exam_data.principal_approval = (
                ad.principal_approval
            )  # Assuming principal_approval is a ForeignKey field
            filter_exam_data.save()
            print("All Admission Data Done in Exam Data")

    # =========================================================================

    # =============== 2 Command ================================================

    all_vtc_admission = VTC_Course_Admission_Registration.objects.all()
    for vt in all_vtc_admission:
        put_exam = Exam_Registration.objects.filter(
            registration_number=vt.registration_number
        ).first()
        if put_exam:
            put_exam.name_of_student = vt.name_of_student
            put_exam.address = vt.address
            put_exam.id_number = vt.id_number
            put_exam.date_of_birth = vt.date_of_birth
            put_exam.mobile_number = vt.mobile_number
            put_exam.college_name = vt.college_name
            put_exam.district = vt.district
            put_exam.course_name = vt.course_name
            put_exam.admission_fees = vt.admission_fees
            put_exam.admission_date = vt.admission_date
            put_exam.principal_approval = vt.principal_approval
            put_exam.save()
            print("All VTC Data Done in Exam Data")
    # =============================================================================

    # ================= 3 Command =================================================
    all_admission_data2 = Admission_Registration.objects.all()
    for ad2 in all_admission_data2:
        get_exam_data = Exam_Registration.objects.filter(
            registration_number=ad2.registration_number
        ).first()
        get_mark_data = Mark_List_Registration.objects.filter(
            registration_number=ad2.registration_number
        ).first()
        if get_mark_data:
            get_mark_data.name_of_student = ad2.name_of_student
            get_mark_data.address = ad2.address
            get_mark_data.id_number = ad2.id_number
            get_mark_data.date_of_birth = ad2.date_of_birth
            get_mark_data.mobile_number = ad2.mobile_number
            get_mark_data.college_name = ad2.college_name
            get_mark_data.district = ad2.district
            get_mark_data.course_name = ad2.course_name
            get_mark_data.admission_fees = ad2.admission_fees
            get_mark_data.admission_date = ad2.admission_date
            get_mark_data.principal_approval = ad2.principal_approval

            get_mark_data.exam_fees = get_exam_data.exam_fees
            get_mark_data.exam_attendance = get_exam_data.exam_attendance
            get_mark_data.any_fees_concession = get_exam_data.any_fees_concession
            get_mark_data.date = get_exam_data.date
            get_mark_data.principal_code = get_exam_data.principal_code
            get_mark_data.principal_name = get_exam_data.principal_name
            get_mark_data.online_fees = get_exam_data.online_fees
            get_mark_data.remark = get_exam_data.remark
            get_mark_data.principal_approval = get_exam_data.principal_approval
            get_mark_data.save()
        if get_exam_data:
            get_exam_data.name_of_student = ad2.name_of_student
            get_exam_data.address = ad2.address
            get_exam_data.id_number = ad2.id_number
            get_exam_data.date_of_birth = ad2.date_of_birth
            get_exam_data.mobile_number = ad2.mobile_number
            get_exam_data.college_name = ad2.college_name
            get_exam_data.district = ad2.district
            get_exam_data.course_name = ad2.course_name
            get_exam_data.admission_fees = ad2.admission_fees
            get_exam_data.admission_date = ad2.admission_date
            get_exam_data.principal_approval = ad2.principal_approval
            get_exam_data.save()
            print("All Admission & Exam Data Done in Mark Data")

    # ==============================================================================

    # =====================4 Command ===============================================
    get_vtc_admission = VTC_Course_Admission_Registration.objects.all()
    for a in get_vtc_admission:
        marks = Mark_List_Registration.objects.filter(
            registration_number=a.registration_number
        ).first()
        if marks:
            marks.name_of_student = a.name_of_student
            marks.address = a.address
            marks.id_number = a.id_number
            marks.date_of_birth = a.date_of_birth
            marks.mobile_number = a.mobile_number
            marks.college_name = a.college_name
            marks.district = a.district
            marks.course_name = a.course_name
            marks.admission_fees = a.admission_fees
            marks.admission_date = a.admission_date
            marks.principal_approval = a.principal_approval
            marks.save()
            print("Only VTC Data Done in Mark Data")

            # Exam data is pending in Mark data


# ===================================================================================================
# ======================================= Homepage Page =============================================
def homepage(request):
    user_pwd = CustomeUserSerializer(CustomeUser.objects.all(), many=True).data
    get_all_news = NewsSerializers(News.objects.all(), many=True).data
    get_all_free_skill_image = Free_Skill_TrainingSerializer(
        Free_Skill_Training.objects.all(), many=True
    ).data

    count = None

    def get_ip(request):
        address = request.META.get("HTTP_X_FORWAREDED_FOR")
        if address:
            ip = address.split(",")[-1].strip()
        else:
            ip = request.META.get("REMOTE_ADDR")
        return ip

    ip = get_ip(request)
    u = Visitor_IP(visitor_ip=ip)
    result = Visitor_IP.objects.filter(Q(visitor_ip__contains=ip))
    if len(result) == 1:
        print("User Exist")
    elif len(result) > 1:
        print("User Exist more....")
    else:
        u.save()
        print("user is unqiue")
    count = Visitor_IP.objects.all().count() + 437070

    data = {
        "count": count,
        "get_all_news": get_all_news,
        "get_all_free_skill_image": get_all_free_skill_image,
    }

    return Response(data, status=status.HTTP_200_OK)


# ===================================================================================================
# ===================================================================================================


# ====================================================================================================
# ======================================= Add New User Page ==========================================

@api_view(['POST'])
def add_new_user(request):
    error_message = None
    value = None
    all_user_role = User_RoleSerializer(User_Role.objects.all(), many=True).data
    if request.method == "POST":
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        get_username = request.POST.get("username")
        get_password = request.POST.get("password")

        get_user_role_id = request.POST.get("user_role")
        get_user_group = request.POST.get("user_group")
        hash_password = make_password(get_password)

        get_user_role = User_Role.objects.get(id=get_user_role_id)

        # user = CustomeUser.objects.get(username=get_username)

        value = {
            "fname": fname,
            "lname": lname,
            "email": email,
            "username": get_username,
        }
        add_user = CustomeUser(
            username=get_username,
            first_name=fname,
            last_name=lname,
            email=email,
            password=hash_password,
            decrypt_password=get_password,
            user_status="1",
            user_role=get_user_role,
            is_staff=True,
        )
        if not fname:
            error_message = "User First Name is Required !!"
        elif not lname:
            error_message = "User Last Name is Required !!"
        elif not email:
            error_message = "User Email is Required !!"
        elif not get_username:
            error_message = "Username is Required !!"
        elif not get_password:
            error_message = "User Password is Required !!"
        elif CustomeUser.objects.filter(email=email).exists():
            error_message = "Email Already Exists !!!"
        elif CustomeUser.objects.filter(username=get_username).exists():
            error_message = "Username Already Exists !!!"
        if not error_message:
            add_user.save()
            # add_user.groups.set(user_group)
            messages.success(request, "User Registered Successfully ")
            return redirect("add_new_user")
    data = {
        "user_role": all_user_role,
        "error": error_message,
        "value": value,
    }
    return Response(data, status=status.HTTP_200_OK)


class AddNewUser(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        error_message = None
        value = None
        all_user_role = User_RoleSerializer(User_Role.objects.all(), many=True).data
        fname = request.data.get("fname")
        lname = request.data.get("lname")
        email = request.data.get("email")
        get_username = request.data.get("username")
        get_password = request.data.get("password")

        get_user_role_id = request.data.get("user_role")
        get_user_group = request.data.get("user_group")
        hash_password = make_password(get_password)

        try:
            get_user_role = User_Role.objects.get(id=get_user_role_id)
        except User_Role.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST, data='id is not valid')

        # user = CustomeUser.objects.get(username=get_username)

        value = {
            "fname": fname,
            "lname": lname,
            "email": email,
            "username": get_username,
        }
        add_user = CustomeUser(
            username=get_username,
            first_name=fname,
            last_name=lname,
            email=email,
            password=hash_password,
            decrypt_password=get_password,
            user_status="1",
            user_role=get_user_role,
            is_staff=True,
        )
        if not fname:
            error_message = "User First Name is Required !!"
        elif not lname:
            error_message = "User Last Name is Required !!"
        elif not email:
            error_message = "User Email is Required !!"
        elif not get_username:
            error_message = "Username is Required !!"
        elif not get_password:
            error_message = "User Password is Required !!"
        elif CustomeUser.objects.filter(email=email).exists():
            error_message = "Email Already Exists !!!"
        elif CustomeUser.objects.filter(username=get_username).exists():
            error_message = "Username Already Exists !!!"
        if not error_message:
            add_user.save()
            # add_user.groups.set(user_group)
            messages.success(request, "User Registered Successfully ")
            return redirect("add_new_user")
        data = {
            "user_role": all_user_role,
            "error": error_message,
            "value": value,
        }
        return Response(data, status=status.HTTP_200_OK)

# ====================================================================================================


# ====================================================================================================
# ======================================= Login Page =================================================
from rest_framework_simplejwt.tokens import RefreshToken


class Login(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []

    def post(self, request):
        try:
            if not request.data:
                return Response(
                    {"message": "Request body is empty."},
                    status=status.HTTP_400_BAD_REQUEST
                )

            username = request.data.get("username")
            get_password = request.data.get("password")

            if not username or not get_password:
                return Response(
                    {"message": "Both username and password are required."},
                    status=status.HTTP_400_BAD_REQUEST
                )

            get_user = CustomeUser.objects.filter(username=username).first()
            if not get_user:
                return Response(
                    {"message": "Invalid username or password."},
                    status=status.HTTP_401_UNAUTHORIZED,
                )

            if not check_password(get_password, get_user.password):
                return Response(
                    {"message": "Invalid username or password."},
                    status=status.HTTP_401_UNAUTHORIZED,
                )

            user_data = self.get_tokens_for_user(get_user)
            return Response(
                {
                    "message": "Login successful.",
                    "id": get_user.id,
                    "email": get_user.email,
                    "role": get_user.user_role.user_role,
                    "token": user_data,
                },
                status=status.HTTP_200_OK,
            )

        except KeyError as e:
            return Response(
                {"message": f"Missing field: {e.args[0]}"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        except Exception as e:
            return Response(
                {"message": f"An error occurred: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }



# ==================================================================================================================================================
# ==================================================================================================================================================


# ======================================== Logout Page ==============================================================================================
class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# =====================================================================================================================================================


# ==================================================================================================
# ======================================= Forgot Password Page =====================================
def forgot_password(request):
    return render(request, "Main/forgot_password.html")


# =================================================================================================
# =================================================================================================


# ==================================================================================================
# ======================================= About Page ===============================================
@api_view(["GET"])
@permission_classes([AllowAny])
@authentication_classes([BasicAuthentication])
def about_us(request):

    def get_ip(request):
        address = request.META.get("HTTP_X_FORWARDED_FOR")
        if address:
            ip = address.split(",")[-1].strip()
        else:
            ip = request.META.get("REMOTE_ADDR")
        return ip

    ip = get_ip(request)  # Get the user's IP address

    result = Visitor_IP.objects.filter(Q(visitor_ip__contains=ip))

    if len(result) == 1:
        print("User Exists")
    elif len(result) > 1:
        print("User Exists more....")
    else:

        Visitor_IP.objects.create(visitor_ip=ip)
        print("User is unique")

    count = Visitor_IP.objects.all().count()

    data = {
        "count": count,
    }

    return Response(data, status=status.HTTP_200_OK)


# =================================================================================================
# =================================================================================================


# ===================================================================================================
# ======================================= Gallery Page ==============================================


@api_view(["GET"])
@permission_classes([AllowAny])
@authentication_classes([BasicAuthentication])
def gallery(request):
    def get_ip(request):
        address = request.META.get("HTTP_X_FORWAREDED_FOR")
        if address:
            ip = address.split(",")[-1].strip()
        else:
            ip = request.META.get("REMOTE_ADDR")
        return ip

    ip = get_ip(request)
    u = Visitor_IP(visitor_ip=ip)
    result = Visitor_IP.objects.filter(Q(visitor_ip__contains=ip))
    if len(result) == 1:
        print("User Exist")
    elif len(result) > 1:
        print("User Exist more....")
    else:
        u.save()
        print("user is unqiue")
    count = Visitor_IP.objects.all().count()

    data = {
        "count": count,
    }
    return Response(data, status=status.HTTP_200_OK)


# =================================================================================================
# =================================================================================================


# ===================================================================================================
# ======================================= Sector Page ===============================================


@api_view(["GET", "POST"])
@permission_classes([AllowAny])
@authentication_classes([BasicAuthentication])
def sector(request):
    def get_ip(request):
        address = request.META.get("HTTP_X_FORWAREDED_FOR")
        if address:
            ip = address.split(",")[-1].strip()
        else:
            ip = request.META.get("REMOTE_ADDR")
        return ip

    ip = get_ip(request)
    u = Visitor_IP(visitor_ip=ip)
    result = Visitor_IP.objects.filter(Q(visitor_ip__contains=ip))
    if len(result) == 1:
        print("User Exist")
    elif len(result) > 1:
        print("User Exist more....")
    else:
        u.save()
        print("user is unqiue")
    count = Visitor_IP.objects.all().count()

    data = {
        "count": count,
    }
    return Response(data, status=status.HTTP_200_OK)


# ===================================================================================================
# ===================================================================================================


# ===================================================================================================
# ======================================= Contact Page ==============================================


@api_view(["GET", "POST"])
@permission_classes([AllowAny])
@authentication_classes([BasicAuthentication])
def contact_us(request):
    def get_ip(request):
        address = request.META.get("HTTP_X_FORWAREDED_FOR")
        if address:
            ip = address.split(",")[-1].strip()
        else:
            ip = request.META.get("REMOTE_ADDR")
        return ip

    ip = get_ip(request)
    u = Visitor_IP(visitor_ip=ip)
    result = Visitor_IP.objects.filter(Q(visitor_ip__contains=ip))
    if len(result) == 1:
        print("User Exist")
    elif len(result) > 1:
        print("User Exist more....")
    else:
        u.save()
        print("user is unqiue")
    count = Visitor_IP.objects.all().count()
    error_message = None
    value = None
    print(request.method)
    if request.method == "POST":
        full_name = request.data.get("full_name")
        email = request.data.get("email")
        mobile_number = request.data.get("mobile_number")
        subject = request.data.get("subject")
        message = request.data.get("message")
        contact_id = random.randint(00000000, 99999999)
        value = {
            "full_name": full_name,
            "email": email,
            "mobile_number": mobile_number,
            "subject": subject,
            "message": message,
        }
        save_data = Contact_us(
            contact_id=contact_id,
            full_name=full_name,
            email=email,
            mobile_number=mobile_number,
            subject=subject,
            message=message,
        )
        if not full_name:
            error_message = "Full Name is Required !!"
        elif not email:
            error_message = "Email is Required !!"
        elif not mobile_number:
            error_message = "Mobile No. is Required !!"
        elif not subject:
            error_message = "Subject is Required !!"
        elif not message:
            error_message = "Write some Message !!"
        if not error_message:
            save_data.save()
            messages.success(request, "Your Response Submitted Successfully")
            return Response({"message": "success"}, status=status.HTTP_200_OK)
        else:
            return Response(
                {"error": error_message}, status=status.HTTP_400_BAD_REQUEST
            )

    data = {
        "count": count,
        "value": value,
        "error": error_message,
    }
    return Response(data, status=status.HTTP_200_OK)


# ===================================================================================================
# ===================================================================================================


# ===================================================================================================
# ======================================= Home Contact Page =========================================
@api_view(["GET", "POST"])
@permission_classes([AllowAny])
@authentication_classes([BasicAuthentication])
def home_contact_us(request):
    error_message = None
    value = None
    if request.method == "POST":
        full_name = request.data.get("full_name")
        email = request.data.get("email")
        mobile_number = request.data.get("mobile_number")
        subject = request.data.get("subject")
        message = request.data.get("message")
        contact_id = random.randint(00000000, 99999999)
        value = {
            "full_name": full_name,
            "email": email,
            "mobile_number": mobile_number,
            "subject": subject,
            "message": message,
        }
        save_data = Contact_us(
            contact_id=contact_id,
            full_name=full_name,
            email=email,
            mobile_number=mobile_number,
            subject=subject,
            message=message,
        )
        if not full_name:
            error_message = "Full Name is Required !!"
        elif not email:
            error_message = "Email is Required !!"
        elif not mobile_number:
            error_message = "Mobile No. is Required !!"
        elif not subject:
            error_message = "Subject is Required !!"
        elif not message:
            error_message = "Write some Message !!"
        if not error_message:
            save_data.save()
            return Response(
                {"message": "Your Response Submitted Successfully"},
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {"error": error_message}, status=status.HTTP_400_BAD_REQUEST
            )
    data = {
        "value": value,
        "error": error_message,
    }
    return Response(data, status=status.HTTP_200_OK)


# ===================================================================================================
# ===================================================================================================


# ===================================================================================================
# ======================================= News Page =================================================


class NewsCategoryViewSet(ModelViewSet):
    queryset = NewsCategory.objects.all()
    permission_classes = [AllowAny]
    authentication_classes = [BasicAuthentication]
    serializer_class = NewsCategorySerializer


    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "News category deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()

@api_view(["GET"])
@permission_classes([AllowAny])
@authentication_classes([BasicAuthentication])
def news(request):
    get_all_news = News.objects.all()
    get_all_news = NewsSerializers(get_all_news, many=True).data

    def get_ip(request):
        address = request.META.get("HTTP_X_FORWAREDED_FOR")
        if address:
            ip = address.split(",")[-1].strip()
        else:
            ip = request.META.get("REMOTE_ADDR")
        return ip

    ip = get_ip(request)
    u = Visitor_IP(visitor_ip=ip)
    result = Visitor_IP.objects.filter(Q(visitor_ip__contains=ip))
    if len(result) == 1:
        print("User Exist")
    elif len(result) > 1:
        print("User Exist more....")
    else:
        u.save()
        print("user is unqiue")
    count = Visitor_IP.objects.all().count()

    data = {
        "count": count,
        "get_all_news": get_all_news,
    }
    return Response(data, status=status.HTTP_200_OK)


# ===================================================================================================
# ===================================================================================================


# ===================================================================================================
# ======================================= News Detail Page ==========================================
@api_view(["GET"])
@permission_classes([AllowAny])
@authentication_classes([BasicAuthentication])
def news_details(request):
    def get_ip(request):
        address = request.META.get("HTTP_X_FORWAREDED_FOR")
        if address:
            ip = address.split(",")[-1].strip()
        else:
            ip = request.META.get("REMOTE_ADDR")
        return ip

    ip = get_ip(request)
    u = Visitor_IP(visitor_ip=ip)
    result = Visitor_IP.objects.filter(Q(visitor_ip__contains=ip))
    if len(result) == 1:
        print("User Exist")
    elif len(result) > 1:
        print("User Exist more....")
    else:
        u.save()
        print("user is unqiue")
    count = Visitor_IP.objects.all().count()

    data = {
        "count": count,
    }
    return Response(data, status=status.HTTP_200_OK)


# ===================================================================================================
# ===================================================================================================


# ===================================================================================================
# ======================================= Internal Functions (1) ====================================

# ===================================================================================================
# ======================================= Course and college Page ===================================


@api_view(["GET"])
@permission_classes([AllowAny])
@authentication_classes([BasicAuthentication])
def course(request):
    vocational_course = Vocational_CourseSerializer(
        Vocational_Course.objects.all(), many=True
    ).data
    certificate_course = Certificate_CourseseSerializer(
        Certificate_Course.objects.all(), many=True
    ).data
    diploma_programme = Diploma_ProgrammeSerializer(
        Diploma_Programme.objects.all(), many=True
    ).data
    pg_diploma_programme = PG_Diploma_ProgrammeSerializer(
        PG_Diploma_Programme.objects.all(), many=True
    ).data

    data = {
        "vocational_course": vocational_course,
        "certificate_course": certificate_course,
        "diploma_programme": diploma_programme,
        "pg_diploma_programmes": pg_diploma_programme,
    }
    return Response(data, status=status.HTTP_200_OK)


# class based view

"""vocational course"""


class VocationalCourseCreateView(CreateAPIView):
    permission_classes = [AllowAny]
    authentication_classes = [BasicAuthentication]
    queryset = Vocational_Course.objects.all()
    serializer_class = Vocational_CourseSerializer


class VocationalCourseRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    authentication_classes = [BasicAuthentication]
    queryset = Vocational_Course.objects.all()
    serializer_class = Vocational_CourseSerializer
    lookup_field = "id"
    
    def patch(self, request, *args, **kwargs):
        print("patch")
        course_name = self.request.data.get('course_name',None)
        if course_name:
           course, created = Course_Name.objects.get_or_create(course_name=course_name)
           request.data['course_name'] = course.id
        return self.partial_update(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {"message": "Vocational course deleted successfully."},
            status=status.HTTP_200_OK,
        )


"""Certificate_Course"""


class CertificateCourseCreateView(CreateAPIView):
    permission_classes = [AllowAny]
    authentication_classes = [BasicAuthentication]
    queryset = Certificate_Course.objects.all()
    serializer_class = Certificate_CourseseSerializer


class CertificateCourseRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    authentication_classes = [BasicAuthentication]
    queryset = Certificate_Course.objects.all()
    serializer_class = Certificate_CourseseSerializer
    lookup_field = "id"
    def patch(self, request, *args, **kwargs):
        print("patch")
        course_name = self.request.data.get('course_name',None)
        if course_name:
           course, created = Course_Name.objects.get_or_create(course_name=course_name)
           request.data['course_name'] = course.id
        return self.partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {"message": "Certificate course deleted successfully."},
            status=status.HTTP_200_OK,
        )


"""Diploma_Programme"""


class DiplomaProgrammeCreateView(CreateAPIView):
    permission_classes = [AllowAny]
    authentication_classes = [BasicAuthentication]
    queryset = Diploma_Programme.objects.all()
    serializer_class = Diploma_ProgrammeSerializer


class DiplomaProgrammeRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    authentication_classes = [BasicAuthentication]
    queryset = Diploma_Programme.objects.all()
    serializer_class = Diploma_ProgrammeSerializer
    lookup_field = "id"
    
    
    def patch(self, request, *args, **kwargs):
        print("patch")
        course_name = self.request.data.get('course_name',None)
        if course_name:
           course, created = Course_Name.objects.get_or_create(course_name=course_name)
           request.data['course_name'] = course.id
        return self.partial_update(request, *args, **kwargs)
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {"message": "Diploma programme deleted successfully."},
            status=status.HTTP_200_OK,
        )


"""PG_Diploma_Programme"""


class PGDiplomaProgrammeCreateView(CreateAPIView):
    permission_classes = [AllowAny]
    authentication_classes = [BasicAuthentication]
    queryset = PG_Diploma_Programme.objects.all()
    serializer_class = PG_Diploma_ProgrammeSerializer


class PGDiplomaProgrammeRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    authentication_classes = [BasicAuthentication]
    queryset = PG_Diploma_Programme.objects.all()
    serializer_class = PG_Diploma_ProgrammeSerializer
    lookup_field = "id"
    
    def patch(self, request, *args, **kwargs):
        print("patch")
        course_name = self.request.data.get('course_name',None)
        if course_name:
           course, created = Course_Name.objects.get_or_create(course_name=course_name)
           request.data['course_name'] = course.id
        return self.partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {"message": "PG Diploma programme deleted successfully."},
            status=status.HTTP_200_OK,
        )


@api_view(["GET"])
@permission_classes([AllowAny])
@authentication_classes([BasicAuthentication])
def college(request):
    affiliated_vocational_training_college_Kerla = (
        Affiliated_Vocational_Training_College_KerlaSerializer(
            Affiliated_Vocational_Training_College_Kerla.objects.all(), many=True
        ).data
    )
    add_on_programme_college_affiliation_kerla = (
        Add_on_Programme_College_Affiliation_KerlaSerializer(
            Add_on_Programme_College_Affiliation_Kerla.objects.all(), many=True
        ).data
    )
    collage = College_Name.objects.all()
    college_name = College_NameSerializer(collage, many=True).data
    data = {
        "affiliated_vocational_training_college_Kerla": affiliated_vocational_training_college_Kerla,
        "add_on_programme_college_affiliation_kerla": add_on_programme_college_affiliation_kerla,
        "college_name": college_name,
    }
    return Response(data, status=status.HTTP_200_OK)

# from django.db.models import Q, F


class collegeEdit(APIView):
    def patch(self, request):
        type = request.data.get("type")
        if type and type == 'vtc':
            college = Affiliated_Vocational_Training_College_Kerla.objects.get(id=request.data.get("id"))
            # college.college_name = request.data.get("college_name")
            college.district = request.data.get("district")
            college.affiliation_number = request.data.get("affiliation_number")
            college.principal_id = request.data.get("principal_id")
            college.current_status = request.data.get("current_status")
            college.college_type = request.data.get("college_type")
            # college.date_and_time = request.data.get("date_and_time")
            college.save()
            return Response({"message": "Vocational college updated successfully."}, status=status.HTTP_200_OK)
        elif type and type == 'addon':
            college = Add_on_Programme_College_Affiliation_Kerla.objects.get(id=request.data.get("id"))
            # college.college_name = request.data.get("college_name")
            college.state = request.data.get("state")
            college.district = request.data.get("district")
            college.affiliation_number = request.data.get("affiliation_number")
            college.principal_id = request.data.get("principal_id")
            # college.date_and_time = request.data.get("date_and_time")
            college.save()
            return Response({"message": "Add on programme college updated successfully."}, status=status.HTTP_200_OK)
        return Response({"message": "Invalid type."}, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request):
        type = request.data.get("type")
        if type and type == 'vtc':
            college = Affiliated_Vocational_Training_College_Kerla.objects.get(id=request.data.get("id"))
            college.delete()
            return Response({"message": "Vocational college deleted successfully."}, status=status.HTTP_200_OK)
        elif type and type == 'addon':
            college = Add_on_Programme_College_Affiliation_Kerla.objects.get(id=request.data.get("id"))
            college.delete()
            return Response({"message": "Add on programme college deleted successfully."}, status=status.HTTP_200_OK)
        return Response({"message": "Invalid type."}, status=status.HTTP_400_BAD_REQUEST)



class ApplicationCollageListView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        vocational_colleges = Affiliated_Vocational_Training_College_Kerla.objects.all()
        addon_colleges = Add_on_Programme_College_Affiliation_Kerla.objects.all()
        applications = Application_for_Affliation.objects.all()

        vocational_data = []
        addon_data = []

        for college in vocational_colleges:
            application = applications.filter(name_of_institution=college.college_name).first()
            affliation_to_date = application.affliation_to_date if application else None
            vocational_data.append({
                'id': college.id,
                'college_name_display': college.college_name.college_name,
                'district': college.district,
                'affiliation_number': college.affiliation_number,
                'principal_id': college.principal_id,
                'current_status': college.current_status,
                'college_type': college.college_type,
                'date_and_time': college.date_and_time,
                'college_name': college.college_name,
                'affliation_to_date': affliation_to_date,
            })

        for college in addon_colleges:
            application = applications.filter(name_of_institution=college.college_name).first()
            affliation_to_date = application.affliation_to_date if application else None
            addon_data.append({
                'id': college.id,
                'college_name_display': college.college_name.college_name,
                'state': college.state,
                'district': college.district,
                'affiliation_number': college.affiliation_number,
                'principal_id': college.principal_id,
                'date_and_time': college.date_and_time,
                'college_name': college.college_name,
                'affliation_to_date': affliation_to_date,

            })
        collage = College_Name.objects.all()
        college_name = College_NameSerializer(collage, many=True).data

        return Response({
            'affiliated_vocational_training_college_Kerla': vocational_data,
            'add_on_programme_college_affiliation_kerla': addon_data,
            "college_name": college_name,
        })





class AffiliatedVocationalTrainingCollegeKerlaCreateView(CreateAPIView):
    queryset = Affiliated_Vocational_Training_College_Kerla.objects.all()
    serializer_class = Affiliated_Vocational_Training_College_KerlaSerializer
    permission_classes = [AllowAny]
    authentication_classes = [BasicAuthentication]

    def post(self, request, *args, **kwargs):
        college_name = request.data["college_name"]
        print("reaching here")
        try:
            college_name = College_Name.objects.get(id=int(college_name)).id
            
        except:
            obj = College_Name.objects.create(college_name=college_name)
            college_name = obj.id
            print("colleage_name:", college_name)
        request.data["college_name"] = college_name
        return self.create(request, *args, **kwargs)


class AffiliatedVocationalTrainingCollegeKerlaRetrieveUpdateDestroyView(
    RetrieveUpdateDestroyAPIView
):
    queryset = Affiliated_Vocational_Training_College_Kerla.objects.all()
    serializer_class = Affiliated_Vocational_Training_College_KerlaSerializer
    permission_classes = [AllowAny]
    authentication_classes = [BasicAuthentication]
    lookup_field = "id"

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {"message": "Affiliated vocational training college deleted successfully."},
            status=status.HTTP_200_OK,
        )


class AddOnProgrammeCollegeAffiliationKerlaCreateView(CreateAPIView):
    queryset = Add_on_Programme_College_Affiliation_Kerla.objects.all()
    serializer_class = Add_on_Programme_College_Affiliation_KerlaSerializer
    permission_classes = [AllowAny]
    authentication_classes = [BasicAuthentication]

    def post(self, request, *args, **kwargs):
        college_name = request.data["college_name"]
        try:
            college_name = College_Name.objects.get(id=int(college_name)).id
        except:
            obj = College_Name.objects.create(college_name=college_name)
            college_name = obj.id
        request.data["college_name"] = college_name
        return self.create(request, *args, **kwargs)


class AddOnProgrammeCollegeAffiliationKerlaRetrieveUpdateDestroyView(
    RetrieveUpdateDestroyAPIView
):
    queryset = Add_on_Programme_College_Affiliation_Kerla.objects.all()
    serializer_class = Add_on_Programme_College_Affiliation_KerlaSerializer
    permission_classes = [AllowAny]
    authentication_classes = [BasicAuthentication]
    lookup_field = "id"

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {"message": "Add on programme college affiliation deleted successfully."},
            status=status.HTTP_200_OK,
        )


# ===================================================================================================
# ===================================================================================================


@api_view(["GET"])
@permission_classes([AllowAny])
@authentication_classes([BasicAuthentication])
def allcourse(request):
    course_name = Course_Name.objects.all()
    course_serializer = Course_NameSerializer(course_name, many=True)
    data = {"course_names": course_serializer.data}
    return Response(data, status=status.HTTP_200_OK)


def generate_admission_roll_number():
    last_roll_number = Admission_Registration.objects.order_by("-id").first()
    print(last_roll_number.registration_number)
    if last_roll_number:
        last_roll_number = int(last_roll_number.registration_number)
        new_roll_number = str(last_roll_number + 1)
    else:
        new_roll_number = "555501038"
    return new_roll_number


def generate_vtc_roll_number():
    last_roll_number = VTC_Course_Admission_Registration.objects.order_by("-id").first()
    if last_roll_number:
        last_roll_number = int(last_roll_number.registration_number)
        new_roll_number = str(last_roll_number + 1)
    else:
        new_roll_number = "900363385"
    return new_roll_number


# ===================================================================================================
# ======================================= Admission Registration Page ===============================
from rest_framework_simplejwt.authentication import JWTAuthentication


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def vtc_course_admission(request):
    
    all_college_name = College_NameSerializer(
        College_Name.objects.all(), many=True
    ).data
    all_course_name = Course_NameSerializer(Course_Name.objects.all(), many=True).data
    all_status = StatusSerializer(Status.objects.all(), many=True).data
    reg_id = random.randint(00000000, 99999999)
    while Admission_Registration.objects.filter(registration_number=reg_id).exists():
        reg_id = random.randint(00000000, 99999999)

    print("---------")
    registrationNum = request.data.get("registrationNum")
    nameOfStudent = request.data.get("nameOfStudent")
    address = request.data.get("address")
    idNumber = request.data.get("idNumber")
    date = request.data.get("date")
    mobileNumber = request.data.get("mobileNumber")
    collegeName = request.data.get("collegeName")
    district = request.data.get("district")
    courseName = request.data.get("courseName")
    admissionFees = request.data.get("admissionFees")
    admission_date = request.data.get("admission_date")
    principalApproval = request.data.get("principalApproval")
    print("---")
    if (
        registrationNum is not None
        and nameOfStudent is not None
        and address is not None
        and idNumber is not None
        and date is not None
        and mobileNumber is not None
        and collegeName is not None
        and district is not None
        and courseName is not None
        and admissionFees is not None
        and admission_date is not None
        and principalApproval is not None
    ):
        college_name_id = College_Name.objects.get(id=collegeName)
        course_name_id = Course_Name.objects.get(id=courseName)
        principal_approval_id = Status.objects.get(id=principalApproval)

        add_vtc_course_admission_registration = VTC_Course_Admission_Registration(
            registration_number=generate_vtc_roll_number(),
            name_of_student=nameOfStudent,
            address=address,
            id_number=idNumber,
            date_of_birth=date,
            mobile_number=mobileNumber,
            college_name=college_name_id,
            district=district,
            course_name=course_name_id,
            admission_fees=admissionFees,
            admission_date=admission_date,
            principal_approval=principal_approval_id,
        )

        print("----")
        add_vtc_course_admission_registration.save()
        return Response({"message": "saved successfully"}, status=status.HTTP_200_OK)
    data = {
        "all_college_name": all_college_name,
        "all_course_name": all_course_name,
        "all_status": all_status,
        "reg_id": generate_vtc_roll_number(),
    }
    print(data)
    return Response(data, status=status.HTTP_200_OK)



class vtcCourseAdmission(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):

        nameOfStudent = request.data.get("nameOfStudent")
        address = request.data.get("address")
        idNumber = request.data.get("idNumber")
        date = request.data.get("date")
        mobileNumber = request.data.get("mobileNumber")
        collegeName = request.data.get("collegeName")
        district = request.data.get("district")
        courseName = request.data.get("courseName")
        admissionFees = request.data.get("admissionFees")
        admission_date = request.data.get("admission_date")
        principalApproval = request.data.get("principalApproval")

        college_name_id = College_Name.objects.get(id=collegeName)
        course_name_id = Course_Name.objects.get(id=courseName)
        principal_approval_id = Status.objects.get(id=principalApproval)
        add_vtc_course_admission_registration = VTC_Course_Admission_Registration(
            registration_number=generate_vtc_roll_number(),
            name_of_student=nameOfStudent,
            address=address,
            id_number=idNumber,
            date_of_birth=date,
            mobile_number=mobileNumber,
            college_name=college_name_id,
            district=district,
            course_name=course_name_id,
            admission_fees=admissionFees,
            admission_date=admission_date,
            principal_approval=principal_approval_id,
        )

        add_vtc_course_admission_registration.save()
        return Response({"message": "saved successfully"}, status=status.HTTP_200_OK)    



# ===================================================================================================
# ===================================================================================================


# ===================================================================================================
# ======================================= Admission Registration Page ===============================
@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def admission_registration(request):
    all_college_name = College_NameSerializer(
        College_Name.objects.all(), many=True
    ).data
    all_course_name = Course_NameSerializer(Course_Name.objects.all(), many=True).data
    all_status = StatusSerializer(Status.objects.all(), many=True).data
    reg_id = random.randint(00000000, 99999999)
    while Admission_Registration.objects.filter(registration_number=reg_id).exists():
        reg_id = random.randint(00000000, 99999999)

    if request.method == "GET":
        data = {
            "all_college_name": all_college_name,
            "all_course_name": all_course_name,
            "all_status": all_status,
            "reg_id": generate_admission_roll_number(),
        }
        return Response(data, status=status.HTTP_200_OK)
    else:
        registrationNum = request.data["registrationNum"]
        nameOfStudent = request.data["nameOfStudent"]
        address = request.data["address"]
        idNumber = request.data["idNumber"]
        date = request.data["date"]
        mobileNumber = request.data["mobileNumber"]
        collegeName = request.data["collegeName"]
        district = request.data["district"]
        courseName = request.data["courseName"]
        admissionFees = request.data["admissionFees"]
        admission_date = request.data["admission_date"]
        principalApproval = request.data["principalApproval"]

        college_name_id = College_Name.objects.get(id=collegeName)
        course_name_id = Course_Name.objects.get(id=courseName)
        principal_approval_id = Status.objects.get(id=principalApproval)

        add_admission_registration = Admission_Registration(
            registration_number=registrationNum,
            name_of_student=nameOfStudent,
            address=address,
            id_number=idNumber,
            date_of_birth=date,
            mobile_number=mobileNumber,
            college_name=college_name_id,
            district=district,
            course_name=course_name_id,
            admission_fees=admissionFees,
            admission_date=admission_date,
            principal_approval=principal_approval_id,
        )

        add_admission_registration.save()
        return Response({"message": "saved successfully"}, status=status.HTTP_200_OK)


# ===================================================================================================
# ===================================================================================================


# ===================================================================================================
# ======================================= Exam Registration Page ====================================


class Exam_Registration_View(APIView):
    def get(self, request):
        query_set = Exam_Registration.objects.all().order_by('-id')
        serializer_obj = Exam_Registration_List_Serializer(query_set,many=True)
        return Response(
            {'message': 'registration data list','data':serializer_obj.data},
            status=status.HTTP_200_OK
        )


class Exam_Registration_Detail_View(APIView):
    def get(self, request, pk):
        try:
            query_set = Exam_Registration.objects.get(id=pk)
            exam_registration_serializer = Exam_Registration_List_Serializer(query_set, many=False)
            return Response(exam_registration_serializer.data, status=status.HTTP_200_OK)
        except Exam_Registration.DoesNotExist:
            return Response({'message': 'Exam Registration Id is not valid'}, status=status.HTTP_400_BAD_REQUEST)


    def patch(self, request, pk):
        try:
            query_set = Exam_Registration.objects.get(id=pk)
            data = Admission_Registration.objects.filter(registration_number=query_set.registration_number).first() if Admission_Registration.objects.filter(registration_number=query_set.registration_number).exists() else VTC_Course_Admission_Registration.objects.filter(registration_number=query_set.registration_number).first()

            query_set.name_of_student = data.name_of_student
            query_set.address = data.address
            query_set.id_number = data.id_number
            query_set.date_of_birth = data.date_of_birth
            query_set.mobile_number = data.mobile_number
            query_set.college_name = data.college_name
            query_set.district = data.district
            query_set.course_name = data.course_name
            query_set.admission_fees = data.admission_fees
            query_set.admission_date = data.admission_date
            query_set.principal_approval = data.principal_approval
            query_set.date_and_time = data.date_and_time
            
            exam_registration_serializer = Exam_Registration_List_Serializer(query_set, data=request.data, partial=True)
            if exam_registration_serializer.is_valid():
                exam_registration_serializer.save()
                query_set.save()
                return Response({'message': 'Registration updated successfully'}, status=status.HTTP_200_OK)
            return Response(data=exam_registration_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exam_Registration.DoesNotExist:
            return Response({'message': 'Exam Registration Id is not valid'}, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request, pk):
        try:
            query_set = Exam_Registration.objects.get(id=pk)
            query_set.delete()
            return Response({'message': 'Exam Registration deleted successfully'}, status=status.HTTP_200_OK)
        except Exam_Registration.DoesNotExist:
            return Response({'message': 'Exam Registration Id is not valid'}, status=status.HTTP_400_BAD_REQUEST)


class Mark_List_Registration_View(APIView):
    def get(self, request):
        mark_list_queryset = Mark_List_Registration.objects.all().order_by('-id')
        serializer_obj = Mark_List_Registration_serializer(mark_list_queryset,many=True)
        return Response(
            {'message':"List Successfully", 'data':serializer_obj.data},
            status=status.HTTP_200_OK            
        )
    


    def post(self, request):
        registration_number = request.data.get("registration_number")
        admissions = Admission_Registration.objects.filter(registration_number=registration_number).first()
        vtc_admissions = VTC_Course_Admission_Registration.objects.filter(registration_number=registration_number).first()
        get_exam = Exam_Registration.objects.filter(registration_number=registration_number).first()
    
        if admissions:
            search_student_data = admissions
            search_get_exam = get_exam
            mark_list_registration_serializer = Mark_List_Registration_serializer(data=request.data)
            if mark_list_registration_serializer.is_valid():
                mark_list_registration_serializer.save(
                    name_of_student = search_student_data.name_of_student,
                    address = search_student_data.address,
                    id_number = search_student_data.id_number,
                    date_of_birth = search_student_data.date_of_birth,
                    mobile_number = search_student_data.mobile_number,
                    college_name = search_student_data.college_name,
                    district = search_student_data.district,
                    course_name = search_student_data.course_name,
                    admission_fees = search_student_data.admission_fees,
                    admission_date = search_student_data.admission_date,
                    principal_approval = search_student_data.principal_approval,
                )
                return Response({'message': 'Mark List Registration saved successfully'}, status=status.HTTP_200_OK)
            return Response(data=mark_list_registration_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        elif vtc_admissions:
            search_student_data = vtc_admissions
            search_get_exam = get_exam
            mark_list_registration_serializer = Mark_List_Registration_serializer(data=request.data)
            if mark_list_registration_serializer.is_valid():
                mark_list_registration_serializer.save(
                    name_of_student = search_student_data.name_of_student,
                    address = search_student_data.address,
                    id_number = search_student_data.id_number,
                    date_of_birth = search_student_data.date_of_birth,
                    mobile_number = search_student_data.mobile_number,
                    college_name = search_student_data.college_name,
                    district = search_student_data.district,
                    course_name = search_student_data.course_name,
                    admission_fees = search_student_data.admission_fees,
                    admission_date = search_student_data.admission_date,
                    principal_approval = search_student_data.principal_approval,
                )
                return Response({'message': 'Mark List Registration saved successfully'}, status=status.HTTP_200_OK)
            return Response(data=mark_list_registration_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response({'message': 'Registration Number is not valid'}, status=status.HTTP_400_BAD_REQUEST)

class Mark_List_Registration_Detail_View(APIView):
    def get(self, request, pk):
        try:
            mark_list_queryset = Mark_List_Registration.objects.get(id=pk)

            serializer_obj = Mark_List_Registration_serializer(mark_list_queryset, many=False)
            return Response(serializer_obj.data, status=status.HTTP_200_OK)
        except Mark_List_Registration.DoesNotExist:
            return Response({'message': 'Mark List Registration Id is not valid'}, status=status.HTTP_400_BAD_REQUEST)
        
    def patch(self, request, pk):
        try:
            mark_list_queryset = Mark_List_Registration.objects.get(id=pk)
            exam_queryset = Exam_Registration.objects.filter(registration_number=mark_list_queryset.registration_number).first()
            data = Admission_Registration.objects.filter(registration_number=mark_list_queryset.registration_number).first() if Admission_Registration.objects.filter(registration_number=mark_list_queryset.registration_number).exists() else VTC_Course_Admission_Registration.objects.filter(registration_number=mark_list_queryset.registration_number).first()

            mark_list_queryset.name_of_student = data.name_of_student
            mark_list_queryset.address = data.address
            mark_list_queryset.id_number = data.id_number
            mark_list_queryset.date_of_birth = data.date_of_birth
            mark_list_queryset.mobile_number = data.mobile_number
            mark_list_queryset.college_name = data.college_name
            mark_list_queryset.district = data.district
            mark_list_queryset.course_name = data.course_name
            mark_list_queryset.admission_fees = data.admission_fees
            mark_list_queryset.admission_date = data.admission_date
            mark_list_queryset.principal_approval = data.principal_approval
            mark_list_queryset.date_and_time = data.date_and_time
            mark_list_queryset.exam_fees = exam_queryset.exam_fees
            mark_list_queryset.any_fees_concession = exam_queryset.any_fees_concession
            mark_list_queryset.exam_attendance = exam_queryset.exam_attendance
            mark_list_queryset.date = exam_queryset.date
            mark_list_queryset.principal_code = exam_queryset.principal_code
            mark_list_queryset.principal_name = exam_queryset.principal_name
            mark_list_queryset.online_fees = exam_queryset.online_fees
            mark_list_queryset.remark = exam_queryset.remark

            serializer_obj = Mark_List_Registration_serializer(mark_list_queryset, data=request.data, partial=True)
            if serializer_obj.is_valid():
                serializer_obj.save()
                mark_list_queryset.save()
                return Response({'message': 'Mark List Registration updated successfully'}, status=status.HTTP_200_OK)
            return Response(data=serializer_obj.errors, status=status.HTTP_400_BAD_REQUEST)
        except Mark_List_Registration.DoesNotExist:
            return Response({'message': 'Mark List Registration Id is not valid'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            mark_list_queryset = Mark_List_Registration.objects.get(id=pk)
            mark_list_queryset.delete()
            return Response({'message': 'Mark List Registration deleted successfully'}, status=status.HTTP_200_OK)
        except Mark_List_Registration.DoesNotExist:
            return Response({'message': 'Mark List Registration Id is not valid'}, status=status.HTTP_400_BAD_REQUEST)




import logging

logger = logging.getLogger(__name__)

class RegistrationDataView(APIView):
    def get(self, request, *args, **kwargs):
        get_search_registration_number = request.GET.get("search_registration_number")
        logger.debug(f"Searching for registration number: {get_search_registration_number}")
        
        all_status = StatusSerializer(Status.objects.all(), many=True).data
        all_exam_fee = Exam_Fees_TypeSerializer(
            Exam_Fees_Type.objects.all(), many=True
        ).data
        search_student_data = ""
        search_student_data_error = ""
        register_number_allready = ""
        
        exam_registeration = Exam_Registration.objects.filter(
            registration_number=get_search_registration_number
        )
        vtx_registeration = VTC_Course_Admission_Registration.objects.filter(
            registration_number=get_search_registration_number
        )
        
        if exam_registeration and len(exam_registeration) != 0:
            exmd = Exam_Registration_serializer(exam_registeration.first()).data
        else:
            exmd = VTC_Course_Admission_Registration_serializer(
                vtx_registeration.first()
            ).data

        logger.debug(f"Exam registration data: {exmd}")

        if exmd:
            register_number_allready = (
                f"Registration Number already exist in Mark Registration !{exmd}! get_search_registration_number={get_search_registration_number}"
            )
        
        data = {
            "all_status": all_status,
            "all_exam_fee": all_exam_fee,
            "search_student_data": search_student_data,
            "search_student_data_error": search_student_data_error,
            "get_search_registration_number": get_search_registration_number,
            "register_number_allready": register_number_allready,
            "exmd": exmd,
        }
        
        logger.debug(f"Response data: {data}")
        
        return Response(data, status=status.HTTP_200_OK)


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def exam_registration(request):
    if request.method == "GET":
        all_status = StatusSerializer(Status.objects.all(), many=True).data
        all_exam_fee = Exam_Fees_TypeSerializer(
            Exam_Fees_Type.objects.all(), many=True
        ).data
        search_student_data = ""
        search_student_data_error = ""
        register_number_allready = ""
        get_search_registration_number = request.GET.get("search_registration_number")
        exmd = None

        if get_search_registration_number:
            admissions = Admission_Registration_serializer(
                Admission_Registration.objects.filter(
                    registration_number=get_search_registration_number
                ).first()
            ).data
            vtc_admissions = VTC_Course_Admission_Registration_serializer(
                VTC_Course_Admission_Registration.objects.filter(
                    registration_number=get_search_registration_number
                ).first()
            ).data
            exam_registeration = Exam_Registration.objects.filter(
                registration_number=get_search_registration_number
            )
            vtx_registeration = VTC_Course_Admission_Registration.objects.filter(
                registration_number=get_search_registration_number
            )
            if exam_registeration and len(exam_registeration) != 0:
                exmd = Exam_Registration_serializer(exam_registeration.first()).data
            else:
                exmd = VTC_Course_Admission_Registration_serializer(
                    vtx_registeration.first()
                ).data

            if exmd:
                register_number_allready = (
                    f"Registration Number already exist in Mark Registration !{exmd}! get_search_registration_number={get_search_registration_number}"
                )

            if admissions.get('registration_number'):
                search_student_data = admissions
            elif vtc_admissions.get("registration_number"):
                search_student_data = vtc_admissions
            else:
                search_student_data_error = "Invalid Registration Number!"

        data = {
            "all_status": all_status,
            "all_exam_fee": all_exam_fee,
            "search_student_data": search_student_data,
            "search_student_data_error": search_student_data_error,
            "get_search_registration_number": get_search_registration_number,
            "register_number_allready": register_number_allready,
            "exmd": exmd,
        }
        return Response(data, status=status.HTTP_200_OK)

    elif request.method == "POST":
        registration_number = request.data.get("send_registration_number")
        exam_fees = request.data.get("send_exam_fees")
        exam_attendance = request.data.get("send_exam_attendance")
        any_fees_concession = request.data.get("send_any_fees_concession")
        date = request.data.get("send_date")
        principal_code = request.data.get("send_principal_code")
        principal_name = request.data.get("send_principal_name")
        online_fees = request.data.get("send_online_fees")
        remark = request.data.get("send_remark")
        principal_approval = request.data.get("send_principal_approval")
        
        vtc = VTC_Course_Admission_Registration.objects.filter(
                    registration_number=registration_number
                ).first()
        addon = Admission_Registration.objects.filter(
                    registration_number=registration_number
                ).first()
        if vtc:
            data = vtc
        elif addon:
            data = addon

        if (
            registration_number is not None
            and exam_fees is not None
            and exam_attendance is not None
            and any_fees_concession is not None
            and date is not None
            and principal_code is not None
            and principal_name is not None
            and online_fees is not None
            and remark is not None
            and principal_approval is not None
        ):
            exam_fee_id = Exam_Fees_Type.objects.get(id=exam_fees)
            principal_approval_id = Status.objects.get(id=principal_approval)
            regiter_number_checking = Exam_Registration.objects.filter(
                registration_number=registration_number
            ).first()

            if regiter_number_checking:
                regiter_number_checking.registration_number = registration_number
                regiter_number_checking.exam_fees = exam_fee_id
                regiter_number_checking.exam_attendance = exam_attendance
                regiter_number_checking.any_fees_concession = any_fees_concession
                regiter_number_checking.date = date
                regiter_number_checking.principal_code = principal_code
                regiter_number_checking.principal_name = principal_name
                regiter_number_checking.online_fees = online_fees
                regiter_number_checking.remark = remark
                regiter_number_checking.principal_approval = principal_approval_id
                regiter_number_checking.name_of_student = regiter_number_checking.name_of_student if regiter_number_checking.name_of_student else data.name_of_student
                regiter_number_checking.address = regiter_number_checking.address if regiter_number_checking.address else data.address
                regiter_number_checking.id_number = regiter_number_checking.id_number if regiter_number_checking.id_number else data.id_number
                regiter_number_checking.date_of_birth = regiter_number_checking.date_of_birth if regiter_number_checking.date_of_birth else data.date_of_birth
                regiter_number_checking.mobile_number = regiter_number_checking.mobile_number if regiter_number_checking.mobile_number else data.mobile_number
                regiter_number_checking.college_name = regiter_number_checking.college_name if regiter_number_checking.college_name else data.college_name
                regiter_number_checking.district = regiter_number_checking.district if regiter_number_checking.district else data.district
                regiter_number_checking.course_name = regiter_number_checking.course_name if regiter_number_checking.course_name else data.course_name
                regiter_number_checking.admission_fees = regiter_number_checking.admission_fees if regiter_number_checking.admission_fees else data.admission_fees
                regiter_number_checking.admission_date = regiter_number_checking.admission_date if regiter_number_checking.admission_date else data.admission_date
                
                regiter_number_checking.save()
                return Response(
                    {"message": "saved successfully"}, status=status.HTTP_200_OK
                )
            else:
                add_exam_registration = Exam_Registration(
                    registration_number=registration_number,
                    exam_fees=exam_fee_id,
                    exam_attendance=exam_attendance,
                    any_fees_concession=any_fees_concession,
                    date=date,
                    principal_code=principal_code,
                    principal_name=principal_name,
                    online_fees=online_fees,
                    remark=remark,
                    principal_approval=principal_approval_id,

                    name_of_student=data.name_of_student,
                    address=data.address,
                    id_number = data.id_number,
                    date_of_birth = data.date_of_birth,
                    mobile_number = data.mobile_number,
                    college_name = data.college_name,
                    district = data.district,
                    course_name = data.course_name,
                    admission_fees = data.admission_fees,
                    admission_date = data.admission_date,

                )

                add_exam_registration.save()
                return Response(
                    {"message": "saved successfully"}, status=status.HTTP_200_OK
                )

        return Response(
            {"message": "Missing required fields"}, status=status.HTTP_400_BAD_REQUEST
        )

# ===================================================================================================
# ===================================================================================================


# ===================================================================================================
# ======================================= Mark Registration Page ====================================
@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def mark_registration(request):
    all_mark_enter_clerk = Mark_StatusSerializer(
        Mark_Status.objects.all(), many=True
    ).data
    all_result_status = Result_StatusSerializer(
        Result_Status.objects.all(), many=True
    ).data
    search_student_data = ""
    search_get_exam = ""
    search_student_data_error = ""
    admissionsFormdata = None
    register_number_allready = ""
    get_search_registration_number = request.GET.get("search_registration_number")
    if get_search_registration_number:
        admissions = Admission_Registration.objects.filter(
            registration_number=get_search_registration_number
        ).first()
        vtc_admissions = VTC_Course_Admission_Registration.objects.filter(
            registration_number=get_search_registration_number
        ).first()
        get_exam = Exam_Registration.objects.filter(
            registration_number=get_search_registration_number
        ).first()
        admissionsFormdata = Mark_List_Registration.objects.filter(
            registration_number=get_search_registration_number
        ).first()


        if admissionsFormdata:
            register_number_allready = (
                "Registration Number already exist in Mark Registration !!"
            )
        if admissions:
            search_student_data = admissions
            search_get_exam = get_exam
        elif vtc_admissions:
            search_student_data = vtc_admissions
            search_get_exam = get_exam
        else:
            search_student_data_error = "Invalid Registration Number!"

    get_registration_number_offix = request.data.get("get_registration_number_offix")
    send_total_mark_2 = request.data.get("send_total_mark_2")
    mark_enter_clerk_name = request.data.get("send_mark_enter_clerk_name")
    mark_enter_clerk = request.data.get("send_mark_enter_clerk")
    mark_check_clerk_name = request.data.get("send_mark_check_clerk_name")
    send_mark_check_clerk0 = request.data.get("send_mark_check_clerk0")
    second_verified_officer_name = request.data.get("send_second_verified_officer_name")
    second_verified_officer = request.data.get("send_second_verified_officer")
    final_mark_verified_officer_name = request.data.get(
        "send_final_mark_verified_officer_name"
    )
    result_status = request.data.get("send_result_status")
    result_enter_register_book_number = request.data.get(
        "send_result_enter_register_book_number"
    )
    mark_obtained = request.data.get("send_mark_obtained")
    total_mark_2 = request.data.get("send_total_mark_2")

    if (
        get_registration_number_offix
        and send_total_mark_2
        and mark_enter_clerk_name
        and mark_enter_clerk
        and mark_check_clerk_name
        and send_mark_check_clerk0
        and second_verified_officer_name
        and second_verified_officer
        and final_mark_verified_officer_name
        and result_status
        and result_enter_register_book_number
        and mark_obtained
        and total_mark_2
    ):

        geting_number_rnd = Mark_List_Registration.objects.get(
            registration_number=get_registration_number_offix
        )
        if geting_number_rnd:
            mark_enter_clerk = Mark_Status.objects.get(
                id=mark_enter_clerk
            )  # select option filed
            mark_check_clerk = Mark_Status.objects.get(id=send_mark_check_clerk0)
            second_verified_officer = Mark_Status.objects.get(
                id=second_verified_officer
            )
            result_status = Result_Status.objects.get(id=result_status)
            # Update the fields
            geting_number_rnd.total_mark_1 = send_total_mark_2
            geting_number_rnd.mark_enter_clerk_name = mark_enter_clerk_name
            geting_number_rnd.mark_enter_clerk = mark_enter_clerk
            geting_number_rnd.mark_check_clerk_name = mark_check_clerk_name
            geting_number_rnd.mark_check_clerk = mark_check_clerk
            geting_number_rnd.second_verified_officer_name = (
                second_verified_officer_name
            )
            geting_number_rnd.second_verified_officer = second_verified_officer
            geting_number_rnd.final_mark_verified_officer_name = (
                final_mark_verified_officer_name
            )
            geting_number_rnd.result_status = result_status
            geting_number_rnd.result_enter_register_book_number = (
                result_enter_register_book_number
            )
            geting_number_rnd.mark_obtained = mark_obtained
            geting_number_rnd.total_mark_2 = total_mark_2

            # Save the changes
            geting_number_rnd.save()
            return Response(
                {"message": "saved successfully"}, status=status.HTTP_200_OK
            )
        else:
            new_user = Mark_List_Registration(
                total_mark_1=send_total_mark_2,
                mark_enter_clerk_name=mark_enter_clerk_name,
                mark_enter_clerk=mark_enter_clerk,
                mark_check_clerk_name=mark_check_clerk_name,
                mark_check_clerk=mark_check_clerk,
                second_verified_officer_name=second_verified_officer_name,
                second_verified_officer=second_verified_officer,
                final_mark_verified_officer_name=final_mark_verified_officer_name,
                result_status=result_status,
                result_enter_register_book_number=result_enter_register_book_number,
                mark_obtained=mark_obtained,
                total_mark_2=total_mark_2,

                registration_number = search_student_data.registration_number,
                name_of_student = search_student_data.name_of_student,
                address = search_student_data.address,
                id_number = search_student_data.id_number,
                date_of_birth = search_student_data.date_of_birth,
                mobile_number = search_student_data.mobile_number,
                college_name = search_student_data.college_name,
                district = search_student_data.district,
                course_name = search_student_data.course_name,
                admission_fees = search_student_data.admission_fees,
                admission_date = search_student_data.admission_date,
                principal_approval = search_student_data.principal_approval,

                exam_fees = get_exam.exam_fees,
                any_fees_concession = get_exam.any_fees_concession,
                exam_attendance = get_exam.exam_attendance,
                date = get_exam.date,
                principal_code = get_exam.principal_code,
                principal_name = get_exam.principal_name,
                online_fees = get_exam.online_fees,
                remark = get_exam.remark,

            )
            new_user.save, ()
            return Response(
                {"message": "saved successfully"}, status=status.HTTP_200_OK
            )

    registration_number = request.data.get("send_registration_number")
    date = request.data.get("send_date")
    subject_1 = request.data.get("send_subject_1")
    subject_2 = request.data.get("send_subject_2")
    subject_3 = request.data.get("send_subject_3")
    subject_4 = request.data.get("send_subject_4")
    subject_5 = request.data.get("send_subject_5")
    subject_6 = request.data.get("send_subject_6")
    subject_7 = request.data.get("send_subject_7")
    subject_8 = request.data.get("send_subject_8")
    subject_9 = request.data.get("send_subject_9")
    subject_10 = request.data.get("send_subject_10")
    subject_11 = request.data.get("send_subject_11")
    subject_12 = request.data.get("send_subject_12")
    internal_marks_1 = request.data.get("send_internal_marks_1")
    internal_marks_2 = request.data.get("send_internal_marks_2")
    internal_marks_3 = request.data.get("send_internal_marks_3")
    internal_marks_4 = request.data.get("send_internal_marks_4")
    internal_marks_5 = request.data.get("send_internal_marks_5")
    internal_marks_6 = request.data.get("send_internal_marks_6")
    internal_marks_7 = request.data.get("send_internal_marks_7")
    internal_marks_8 = request.data.get("send_internal_marks_8")
    internal_marks_9 = request.data.get("send_internal_marks_9")
    internal_marks_10 = request.data.get("send_internal_marks_10")
    internal_marks_11 = request.data.get("send_internal_marks_11")
    internal_marks_12 = request.data.get("send_internal_marks_12")
    internal_marks_13 = request.data.get("send_internal_marks_13")
    internal_marks_14 = request.data.get("send_internal_marks_14")
    external_marks_1 = request.data.get("send_external_marks_1")
    external_marks_2 = request.data.get("send_external_marks_2")
    external_marks_3 = request.data.get("send_external_marks_3")
    external_marks_4 = request.data.get("send_external_marks_4")
    external_marks_5 = request.data.get("send_external_marks_5")
    external_marks_6 = request.data.get("send_external_marks_6")
    external_marks_7 = request.data.get("send_external_marks_7")
    external_marks_8 = request.data.get("send_external_marks_8")
    external_marks_9 = request.data.get("send_external_marks_9")
    external_marks_10 = request.data.get("send_external_marks_10")
    external_marks_11 = request.data.get("send_external_marks_11")
    external_marks_12 = request.data.get("send_external_marks_12")
    external_marks_13 = request.data.get("send_external_marks_13")
    external_marks_14 = request.data.get("send_external_marks_14")
    mark_obtained_1 = request.data.get("send_mark_obtained_1")
    mark_obtained_2 = request.data.get("send_mark_obtained_2")
    mark_obtained_3 = request.data.get("send_mark_obtained_3")
    mark_obtained_4 = request.data.get("send_mark_obtained_4")
    mark_obtained_5 = request.data.get("send_mark_obtained_5")
    mark_obtained_6 = request.data.get("send_mark_obtained_6")
    mark_obtained_7 = request.data.get("send_mark_obtained_7")
    mark_obtained_8 = request.data.get("send_mark_obtained_8")
    mark_obtained_9 = request.data.get("send_mark_obtained_9")
    mark_obtained_10 = request.data.get("send_mark_obtained_10")
    mark_obtained_11 = request.data.get("send_mark_obtained_11")
    mark_obtained_12 = request.data.get("send_mark_obtained_12")
    mark_obtained_13 = request.data.get("send_mark_obtained_13")
    mark_obtained_14 = request.data.get("send_mark_obtained_14")
    total_1 = request.data.get("send_total_1")
    total_2 = request.data.get("send_total_2")
    total_3 = request.data.get("send_total_3")
    total_4 = request.data.get("send_total_4")
    total_5 = request.data.get("send_total_5")
    total_6 = request.data.get("send_total_6")
    total_7 = request.data.get("send_total_7")
    total_8 = request.data.get("send_total_8")
    total_9 = request.data.get("send_total_9")
    total_10 = request.data.get("send_total_10")
    total_11 = request.data.get("send_total_11")
    total_12 = request.data.get("send_total_12")
    total_13 = request.data.get("send_total_13")
    total_14 = request.data.get("send_total_14")
    total_mark_1 = request.data.get("send_total_mark_1")
    total_mark_obtained = request.data.get("send_total_mark_obtained")
    result_status_pass_and_failed_new = request.data.get(
        "send_result_status_pass_and_failed"
    )
    print(result_status_pass_and_failed_new, "********")
    if result_status_pass_and_failed_new == "1":
        save_result = "1"
    else:
        save_result = "2"

    grade_1 = request.data.get("send_grade_1")
    grade_2 = request.data.get("send_grade_2")
    grade_3 = request.data.get("send_grade_3")
    grade_4 = request.data.get("send_grade_4")
    grade_5 = request.data.get("send_grade_5")
    grade_6 = request.data.get("send_grade_6")
    grade_7 = request.data.get("send_grade_7")
    grade_8 = request.data.get("send_grade_8")
    grade_9 = request.data.get("send_grade_9")
    grade_10 = request.data.get("send_grade_10")
    grade_11 = request.data.get("send_grade_11")
    grade_12 = request.data.get("send_grade_12")
    grade_13 = request.data.get("send_grade_13")
    grade_14 = request.data.get("send_grade_14")

    admissions = Admission_Registration.objects.filter(registration_number=registration_number).first()
    vtc_admissions = VTC_Course_Admission_Registration.objects.filter(registration_number=registration_number).first()
    get_exam = Exam_Registration.objects.filter(registration_number=registration_number).first()
    
    if admissions:
        search_student_data = admissions
        search_get_exam = get_exam
    elif vtc_admissions:
        search_student_data = vtc_admissions
        search_get_exam = get_exam
    else:
        search_student_data_error = "Invalid Registration Number!"
    if (
        registration_number
        and date
        and subject_1
        and internal_marks_1
        and external_marks_1
        and mark_obtained_1
        and total_1
        and grade_1
    ):
        pc_geting_number_rnd = Mark_List_Registration.objects.filter(
            registration_number=registration_number
        ).first()

        if pc_geting_number_rnd:
            pc_geting_number_rnd.date = date
            pc_geting_number_rnd.subject_1 = subject_1
            pc_geting_number_rnd.subject_2 = subject_2
            pc_geting_number_rnd.subject_3 = subject_3
            pc_geting_number_rnd.subject_4 = subject_4
            pc_geting_number_rnd.subject_5 = subject_5
            pc_geting_number_rnd.subject_6 = subject_6
            pc_geting_number_rnd.subject_7 = subject_7
            pc_geting_number_rnd.subject_8 = subject_8
            pc_geting_number_rnd.subject_9 = subject_9
            pc_geting_number_rnd.subject_10 = subject_10
            pc_geting_number_rnd.subject_11 = subject_11
            pc_geting_number_rnd.subject_12 = subject_12
            pc_geting_number_rnd.internal_marks_1 = internal_marks_1
            pc_geting_number_rnd.internal_marks_2 = internal_marks_2
            pc_geting_number_rnd.internal_marks_3 = internal_marks_3
            pc_geting_number_rnd.internal_marks_4 = internal_marks_4
            pc_geting_number_rnd.internal_marks_5 = internal_marks_5
            pc_geting_number_rnd.internal_marks_6 = internal_marks_6
            pc_geting_number_rnd.internal_marks_7 = internal_marks_7
            pc_geting_number_rnd.internal_marks_8 = internal_marks_8
            pc_geting_number_rnd.internal_marks_9 = internal_marks_9
            pc_geting_number_rnd.internal_marks_10 = internal_marks_10
            pc_geting_number_rnd.internal_marks_11 = internal_marks_11
            pc_geting_number_rnd.internal_marks_12 = internal_marks_12
            pc_geting_number_rnd.internal_marks_13 = internal_marks_13
            pc_geting_number_rnd.internal_marks_14 = internal_marks_14
            pc_geting_number_rnd.external_marks_1 = external_marks_1
            pc_geting_number_rnd.external_marks_2 = external_marks_2
            pc_geting_number_rnd.external_marks_3 = external_marks_3
            pc_geting_number_rnd.external_marks_4 = external_marks_4
            pc_geting_number_rnd.external_marks_5 = external_marks_5
            pc_geting_number_rnd.external_marks_6 = external_marks_6
            pc_geting_number_rnd.external_marks_7 = external_marks_7
            pc_geting_number_rnd.external_marks_8 = external_marks_8
            pc_geting_number_rnd.external_marks_9 = external_marks_9
            pc_geting_number_rnd.external_marks_10 = external_marks_10
            pc_geting_number_rnd.external_marks_11 = external_marks_11
            pc_geting_number_rnd.external_marks_12 = external_marks_12
            pc_geting_number_rnd.external_marks_13 = external_marks_13
            pc_geting_number_rnd.external_marks_14 = external_marks_14
            pc_geting_number_rnd.mark_obtained_1 = mark_obtained_1
            pc_geting_number_rnd.mark_obtained_2 = mark_obtained_2
            pc_geting_number_rnd.mark_obtained_3 = mark_obtained_3
            pc_geting_number_rnd.mark_obtained_4 = mark_obtained_4
            pc_geting_number_rnd.mark_obtained_5 = mark_obtained_5
            pc_geting_number_rnd.mark_obtained_6 = mark_obtained_6
            pc_geting_number_rnd.mark_obtained_7 = mark_obtained_7
            pc_geting_number_rnd.mark_obtained_8 = mark_obtained_8
            pc_geting_number_rnd.mark_obtained_9 = mark_obtained_9
            pc_geting_number_rnd.mark_obtained_10 = mark_obtained_10
            pc_geting_number_rnd.mark_obtained_11 = mark_obtained_11
            pc_geting_number_rnd.mark_obtained_12 = mark_obtained_12
            pc_geting_number_rnd.mark_obtained_13 = mark_obtained_13
            pc_geting_number_rnd.mark_obtained_14 = mark_obtained_14
            pc_geting_number_rnd.total_1 = total_1
            pc_geting_number_rnd.total_2 = total_2
            pc_geting_number_rnd.total_3 = total_3
            pc_geting_number_rnd.total_4 = total_4
            pc_geting_number_rnd.total_5 = total_5
            pc_geting_number_rnd.total_6 = total_6
            pc_geting_number_rnd.total_7 = total_7
            pc_geting_number_rnd.total_8 = total_8
            pc_geting_number_rnd.total_9 = total_9
            pc_geting_number_rnd.total_10 = total_10
            pc_geting_number_rnd.total_11 = total_11
            pc_geting_number_rnd.total_12 = total_12
            pc_geting_number_rnd.total_13 = total_13
            pc_geting_number_rnd.total_14 = total_14

            pc_geting_number_rnd.total_mark_1 = total_mark_1
            pc_geting_number_rnd.total_mark_obtained = total_mark_obtained
            pc_geting_number_rnd.result = save_result

            pc_geting_number_rnd.grade_1 = grade_1
            pc_geting_number_rnd.grade_2 = grade_2
            pc_geting_number_rnd.grade_3 = grade_3
            pc_geting_number_rnd.grade_4 = grade_4
            pc_geting_number_rnd.grade_5 = grade_5
            pc_geting_number_rnd.grade_6 = grade_6
            pc_geting_number_rnd.grade_7 = grade_7
            pc_geting_number_rnd.grade_8 = grade_8
            pc_geting_number_rnd.grade_9 = grade_9
            pc_geting_number_rnd.grade_10 = grade_10
            pc_geting_number_rnd.grade_11 = grade_11
            pc_geting_number_rnd.grade_12 = grade_12
            pc_geting_number_rnd.grade_13 = grade_13
            pc_geting_number_rnd.grade_14 = grade_14
            pc_geting_number_rnd.save()
            return Response(
                {"message": "saved successfully"}, status=status.HTTP_200_OK
            )

        else:
            add_mark_registration = Mark_List_Registration(
                registration_number=registration_number,
                date=date,
                subject_1=subject_1,
                subject_2=subject_2,
                subject_3=subject_3,
                subject_4=subject_4,
                subject_5=subject_5,
                subject_6=subject_6,
                subject_7=subject_7,
                subject_8=subject_8,
                subject_9=subject_9,
                subject_10=subject_10,
                subject_11=subject_11,
                subject_12=subject_12,
                internal_marks_1=internal_marks_1 if internal_marks_1 else 0,
                internal_marks_2=internal_marks_2 if internal_marks_2 else 0,
                internal_marks_3=internal_marks_3 if internal_marks_3 else 0,
                internal_marks_4=internal_marks_4 if internal_marks_4 else 0,
                internal_marks_5=internal_marks_5 if internal_marks_5 else 0,
                internal_marks_6=internal_marks_6 if internal_marks_6 else 0,
                internal_marks_7=internal_marks_7 if internal_marks_7 else 0,
                internal_marks_8=internal_marks_8 if internal_marks_8 else 0,
                internal_marks_9=internal_marks_9 if internal_marks_9 else 0,
                internal_marks_10=internal_marks_10 if internal_marks_10 else 0,
                internal_marks_11=internal_marks_11 if internal_marks_11 else 0,
                internal_marks_12=internal_marks_12 if internal_marks_12 else 0,
                internal_marks_13=internal_marks_13 if internal_marks_13 else 0,
                internal_marks_14=internal_marks_14 if internal_marks_14 else 0,
                external_marks_1=external_marks_1 if external_marks_1 else 0,
                external_marks_2=external_marks_2 if external_marks_2 else 0,
                external_marks_3=external_marks_3 if external_marks_3 else 0,
                external_marks_4=external_marks_4 if external_marks_4 else 0,
                external_marks_5=external_marks_5 if external_marks_5 else 0,
                external_marks_6=external_marks_6 if external_marks_6 else 0,
                external_marks_7=external_marks_7 if external_marks_7 else 0,
                external_marks_8=external_marks_8 if external_marks_8 else 0,
                external_marks_9=external_marks_9 if external_marks_9 else 0,
                external_marks_10=external_marks_10 if external_marks_10 else 0,
                external_marks_11=external_marks_11 if external_marks_11 else 0,
                external_marks_12=external_marks_12 if external_marks_12 else 0,
                external_marks_13=external_marks_13 if external_marks_13 else 0,
                external_marks_14=external_marks_14 if external_marks_14 else 0,
                mark_obtained_1=mark_obtained_1 if mark_obtained_1 else 0,
                mark_obtained_2=mark_obtained_2 if mark_obtained_2 else 0,
                mark_obtained_3=mark_obtained_3 if mark_obtained_3 else 0,
                mark_obtained_4=mark_obtained_4 if mark_obtained_4 else 0,
                mark_obtained_5=mark_obtained_5 if mark_obtained_5 else 0,
                mark_obtained_6=mark_obtained_6 if mark_obtained_6 else 0,
                mark_obtained_7=mark_obtained_7 if mark_obtained_7 else 0,
                mark_obtained_8=mark_obtained_8 if mark_obtained_8 else 0,
                mark_obtained_9=mark_obtained_9 if mark_obtained_9 else 0,
                mark_obtained_10=mark_obtained_10 if mark_obtained_10 else 0,
                mark_obtained_11=mark_obtained_11 if mark_obtained_11 else 0,
                mark_obtained_12=mark_obtained_12 if mark_obtained_12 else 0,
                mark_obtained_13=mark_obtained_13 if mark_obtained_13 else 0,
                mark_obtained_14=mark_obtained_14 if mark_obtained_14 else 0,
                total_1=total_1 if total_1 else 0,
                total_2=total_2 if total_2 else 0,
                total_3=total_3 if total_3 else 0,
                total_4=total_4 if total_4 else 0,
                total_5=total_5 if total_5 else 0,
                total_6=total_6 if total_6 else 0,
                total_7=total_7 if total_7 else 0,
                total_8=total_8 if total_8 else 0,
                total_9=total_9 if total_9 else 0,
                total_10=total_10 if total_10 else 0,
                total_11=total_11 if total_11 else 0,
                total_12=total_12 if total_12 else 0,
                total_13=total_13 if total_13 else 0,
                total_14=total_14 if total_14 else 0,
                total_mark_1=total_mark_1 if total_mark_1 else 0,
                total_mark_obtained=total_mark_obtained if total_mark_obtained else 0,
                result=save_result,
                grade_1=grade_1,
                grade_2=grade_2,
                grade_3=grade_3,
                grade_4=grade_4,
                grade_5=grade_5,
                grade_6=grade_6,
                grade_7=grade_7,
                grade_8=grade_8,
                grade_9=grade_9,
                grade_10=grade_10,
                grade_11=grade_11,
                grade_12=grade_12,
                grade_13=grade_13,
                grade_14=grade_14,

                name_of_student = search_student_data.name_of_student,
                address = search_student_data.address,
                id_number = search_student_data.id_number,
                date_of_birth = search_student_data.date_of_birth,
                mobile_number = search_student_data.mobile_number,
                college_name = search_student_data.college_name,
                district = search_student_data.district,
                course_name = search_student_data.course_name,
                admission_fees = search_student_data.admission_fees,
                admission_date = search_student_data.admission_date,
                principal_approval = search_student_data.principal_approval,

                exam_fees = get_exam.exam_fees,
                any_fees_concession = get_exam.any_fees_concession,
                exam_attendance = get_exam.exam_attendance,
                principal_code = get_exam.principal_code,
                principal_name = get_exam.principal_name,
                online_fees = get_exam.online_fees,
                remark = get_exam.remark,
            )
            add_mark_registration.save()
            return Response(
                {"message": "saved successfully"}, status=status.HTTP_200_OK
            )

    data = {
        "all_mark_enter_clerk": all_mark_enter_clerk,
        "all_result_status": all_result_status,
        "search_student_data": search_student_data,
        "search_get_exam": search_get_exam,
        "search_student_data_error": search_student_data_error,
        "get_search_registration_number": get_search_registration_number,
        "admissionsFormdata": admissionsFormdata,
        "register_number_allready": register_number_allready,
    }
    return Response(data, status=status.HTTP_200_OK)


# ===================================================================================================
# ===================================================================================================


# ===================================================================================================
# ======================================= Add on Programme Page =====================================
@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def add_on_programme(request):
    all_college_name = Add_on_CollegeSerializer(
        Add_on_College.objects.all(), many=True
    ).data
    all_course_name = Course_NameSerializer(Course_Name.objects.all(), many=True).data
    all_status = StatusSerializer(Status.objects.all(), many=True).data
    all_main_course = Main_CourseSerializer(Main_Course.objects.all(), many=True).data

    college_id = request.data.get("collegeId0")
    course_id = request.data.get("courseId0")
    course_code = request.data.get("courseCode0")
    student_name = request.data.get("studentName0")
    address = request.data.get("address0")
    id_number = request.data.get("idNumber0")
    contact_number = request.data.get("contactNumber0")
    exam_fees = request.data.get("examFees0")
    amount = request.data.get("amount0")
    main_course_id = request.data.get("mainCourseId0")
    college_status_id = request.data.get("collegeStatusId0")

    if (
        college_id
        and course_id
        and course_code
        and student_name
        and address
        and id_number
        and contact_number
        and exam_fees
        and amount
        and main_course_id
        and college_status_id
    ):
        add_on_college0 = Add_on_College.objects.get(id=college_id)
        course_name = Course_Name.objects.get(id=course_id)
        main_course = Main_Course.objects.get(id=main_course_id)
        college_coordinator_approval = Status.objects.get(id=college_status_id)

        add_on_programme = Add_on_Programme(
            add_on_College=add_on_college0,
            course_name=course_name,
            course_code=course_code,
            student_name=student_name,
            address=address,
            id_number=id_number,
            contact_number=contact_number,
            exam_fees=exam_fees,
            amount=amount,
            main_course=main_course,
            college_coordinator_approval=college_coordinator_approval,
        )
        add_on_programme.save()
        return Response({"message": "saved successfully"}, status=status.HTTP_200_OK)

    data = {
        "all_college_name": all_college_name,
        "all_course_name": all_course_name,
        "all_status": all_status,
        "all_main_course": all_main_course,
    }

    return Response(data, status=status.HTTP_200_OK)


# ===================================================================================================

# ===================================================================================================


# ===================================================================================================
# ======================================= Application For Affiliation Page ==========================
@api_view(["GET", "POST"])
# @permission_classes([IsAuthenticated])
# @authentication_classes([JWTAuthentication])
def application_for_affiliation(request):
    all_institution_status = Institution_StatusSerializer(
        Institution_Status.objects.all(), many=True
    ).data
    payment_status = Amount_StatusSerializer(
        Amount_Status.objects.all(), many=True
    ).data

    name_of_institution = request.data.get("name_of_institution")
    mobile_number = request.data.get("mobile_number")
    status_of_institution = request.data.get("status_of_institution")
    email = request.data.get("email")
    status_of_institution_other = request.data.get("status_of_institution_other")
    year_of_establishment = request.data.get("year_of_establishment")
    address = request.data.get("address")
    pincode = request.data.get("pincode")
    name_mpd = request.data.get("name_mpd")
    education_qualification = request.data.get("education_qualification")
    date_of_birth = request.data.get("date_of_birth")
    designation = request.data.get("designation")
    profession_experience = request.data.get("profession_experience")
    postal_address = request.data.get("postal_address")
    number_of_room_1 = request.data.get("number_of_room_1")
    seating_capacity_1 = request.data.get("seating_capacity_1")
    total_area_1 = request.data.get("total_area_1")
    number_of_room_2 = request.data.get("number_of_room_2")
    seating_capacity_2 = request.data.get("seating_capacity_2")
    total_area_2 = request.data.get("total_area_2")
    number_of_room_3 = request.data.get("number_of_room_3")
    seating_capacity_3 = request.data.get("seating_capacity_3")
    total_area_3 = request.data.get("total_area_3")
    number_of_room_4 = request.data.get("number_of_room_4")
    seating_capacity_4 = request.data.get("seating_capacity_4")
    total_area_4 = request.data.get("total_area_4")
    number_of_room_5 = request.data.get("number_of_room_5")
    seating_capacity_5 = request.data.get("seating_capacity_5")
    total_area_5 = request.data.get("total_area_5")
    number_of_room_6 = request.data.get("number_of_room_6")
    seating_capacity_6 = request.data.get("seating_capacity_6")
    total_area_6 = request.data.get("total_area_6")

    serial_number1 = request.data.get("serial_number1")
    type_of_computer_1 = request.data.get("type_of_computer_1")
    number_terminal_1 = request.data.get("number_terminal_1")
    year_of_purchase_1 = request.data.get("year_of_purchase_1")
    cost_1 = request.data.get("cost_1")
    software_facility_1 = request.data.get("software_facility_1")
    other_facility_1 = request.data.get("other_facility_1")
    serial_number2 = request.data.get("serial_number2")
    type_of_computer_2 = request.data.get("type_of_computer_2")
    number_terminal_2 = request.data.get("number_terminal_2")
    year_of_purchase_2 = request.data.get("year_of_purchase_2")
    cost_2 = request.data.get("cost_2")
    software_facility_2 = request.data.get("software_facility_2")
    other_facility_2 = request.data.get("other_facility_2")
    serial_number3 = request.data.get("serial_number3")
    type_of_computer_3 = request.data.get("type_of_computer_3")
    number_terminal_3 = request.data.get("number_terminal_3")
    year_of_purchase_3 = request.data.get("year_of_purchase_3")
    cost_3 = request.data.get("cost_3")
    software_facility_3 = request.data.get("software_facility_3")
    other_facility_3 = request.data.get("other_facility_3")
    serial_number4 = request.data.get("serial_number4")
    type_of_computer_4 = request.data.get("type_of_computer_4")
    number_terminal_4 = request.data.get("number_terminal_4")
    year_of_purchase_4 = request.data.get("year_of_purchase_4")
    cost_4 = request.data.get("cost_4")
    software_facility_4 = request.data.get("software_facility_4")
    other_facility_4 = request.data.get("other_facility_4")
    serial_number5 = request.data.get("serial_number_5")
    type_of_computer_5 = request.data.get("type_of_computer_5")
    number_terminal_5 = request.data.get("number_terminal_5")
    year_of_purchase_5 = request.data.get("year_of_purchase_5")
    cost_5 = request.data.get("cost_5")
    software_facility_5 = request.data.get("software_facility_5")
    other_facility_5 = request.data.get("other_facility_5")
    serial_number6 = request.data.get("serial_number_6")
    type_of_computer_6 = request.data.get("type_of_computer_6")
    number_terminal_6 = request.data.get("number_terminal_6")
    year_of_purchase_6 = request.data.get("year_of_purchase_6")
    cost_6 = request.data.get("cost_6")
    software_facility_6 = request.data.get("software_facility_6")
    other_facility_6 = request.data.get("other_facility_6")

    information_serial_number_1 = request.data.get("information_serial_number_1")
    name_1 = request.data.get("name_1")
    designation_1 = request.data.get("designation_1")
    qualification_1 = request.data.get("qualification_1")
    teaching_experience_1 = request.data.get("teaching_experience_1")
    date_of_appointment_1 = request.data.get("date_of_appointment_1")
    status_1 = request.data.get("status_1")
    information_serial_number_2 = request.data.get("information_serial_number_2")
    name_2 = request.data.get("name_2")
    designation_2 = request.data.get("designation_2")
    qualification_2 = request.data.get("qualification_2")
    teaching_experience_2 = request.data.get("teaching_experience_2")
    date_of_appointment_2 = request.data.get("date_of_appointment_2")
    status_2 = request.data.get("status_2")
    information_serial_number_3 = request.data.get("information_serial_number_3")
    name_3 = request.data.get("name_3")
    designation_3 = request.data.get("designation_3")
    qualification_3 = request.data.get("qualification_3")
    teaching_experience_3 = request.data.get("teaching_experience_3")
    date_of_appointment_3 = request.data.get("date_of_appointment_3")
    status_3 = request.data.get("status_3")
    information_serial_number_4 = request.data.get("information_serial_number_4")
    name_4 = request.data.get("name_4")
    designation_4 = request.data.get("designation_4")
    qualification_4 = request.data.get("qualification_4")
    teaching_experience_4 = request.data.get("teaching_experience_4")
    date_of_appointment_4 = request.data.get("date_of_appointment_4")
    status_4 = request.data.get("status_4")
    center_address = request.data.get("center_address")
    residential_address = request.data.get("residential_address")
    signature = request.data.get("signature")
    form_receive_date = request.data.get("form_receive_date")
    affliation_number = request.data.get("affliation_number")
    total_affliation_fee = request.data.get("total_affliation_fee")
    registration_fee = request.data.get("registration_fee")
    amount_status = request.data.get("amount_status")
    bank_name = request.data.get("bank_name")
    receipt_number = request.data.get("receipt_number")
    date = request.data.get("date")
    education_institution_type = request.data.get("education_institution_type")
    affliation_from_date = request.data.get("affliation_from_date")
    affliation_to_date = request.data.get("affliation_to_date")
    district = request.data.get("district")
    payment_mode = request.data.get("payment_mode")
    manager_name = request.data.get("manager_name")
    principal_name = request.data.get("principal_name")
    manager_address = request.data.get("manager_address")
    principal_address = request.data.get("principal_address")

    variables = [
        
        manager_address,
        principal_name,
        principal_address,
        manager_name,
        payment_mode,
        district,
        name_of_institution,
        mobile_number,
        status_of_institution,
        email,
        year_of_establishment,
        address,
        pincode,
        name_mpd,
        education_qualification,
        date_of_birth,
        designation,
        profession_experience,
        postal_address,
        number_of_room_1,
        seating_capacity_1,
        total_area_1,
        number_of_room_2,
        seating_capacity_2,
        total_area_2,
        number_of_room_3,
        seating_capacity_3,
        total_area_3,
        number_of_room_4,
        seating_capacity_4,
        total_area_4,
        number_of_room_5,
        seating_capacity_5,
        total_area_5,
        number_of_room_6,
        seating_capacity_6,
        total_area_6,
        serial_number1,
        type_of_computer_1,
        number_terminal_1,
        year_of_purchase_1,
        cost_1,
        software_facility_1,
        other_facility_1,
        information_serial_number_1,
        name_1,
        designation_1,
        qualification_1,
        teaching_experience_1,
        date_of_appointment_1,
        status_1,
        center_address,
        residential_address,
        signature,
        form_receive_date,
        affliation_number,
        total_affliation_fee,
        registration_fee,
        amount_status,
        bank_name,
        receipt_number,
        date,
        education_institution_type,
        affliation_from_date,
        affliation_to_date,
    ]

    all_variables_have_value = all(variables)

    if all_variables_have_value:
        status_of_institution = Institution_Status.objects.get(
            id=status_of_institution
        )  # select option filed
        amount_status = Amount_Status.objects.get(id=amount_status)

        application = Application_for_Affliation(
            name_of_institution=name_of_institution,
            mobile_number=mobile_number,
            status_of_institution=status_of_institution,
            email=email,
            status_of_institution_other=status_of_institution_other,
            year_of_establishment=year_of_establishment,
            address=address,
            pincode=pincode,
            name=name_mpd,
            education_qualification=education_qualification,
            date_of_birth=date_of_birth,
            designation=designation,
            profession_experience=profession_experience,
            postal_address=postal_address,
            number_of_room_1=number_of_room_1,
            seating_capacity_1=seating_capacity_1,
            total_area_1=total_area_1,
            number_of_room_2=number_of_room_2,
            seating_capacity_2=seating_capacity_2,
            total_area_2=total_area_2,
            number_of_room_3=number_of_room_3,
            seating_capacity_3=seating_capacity_3,
            total_area_3=total_area_3,
            number_of_room_4=number_of_room_4,
            seating_capacity_4=seating_capacity_4,
            total_area_4=total_area_4,
            number_of_room_5=number_of_room_5,
            seating_capacity_5=seating_capacity_5,
            total_area_5=total_area_5,
            number_of_room_6=number_of_room_6,
            seating_capacity_6=seating_capacity_6,
            total_area_6=total_area_6,
            serial_number_1=serial_number1,
            type_of_computer_1=type_of_computer_1,
            number_terminal_1=number_terminal_1,
            year_of_purchase_1=year_of_purchase_1,
            cost_1=cost_1,
            software_facility_1=software_facility_1,
            other_facility_1=other_facility_1,
            serial_number_2=serial_number2,
            type_of_computer_2=type_of_computer_2,
            number_terminal_2=number_terminal_2,
            year_of_purchase_2=year_of_purchase_2,
            cost_2=cost_2,
            software_facility_2=software_facility_2,
            other_facility_2=other_facility_2,
            serial_number_3=serial_number3,
            type_of_computer_3=type_of_computer_3,
            number_terminal_3=number_terminal_3,
            year_of_purchase_3=year_of_purchase_3,
            cost_3=cost_3,
            software_facility_3=software_facility_3,
            other_facility_3=other_facility_3,
            serial_number_4=serial_number4,
            type_of_computer_4=type_of_computer_4,
            number_terminal_4=number_terminal_4,
            year_of_purchase_4=year_of_purchase_4,
            cost_4=cost_4,
            software_facility_4=software_facility_4,
            other_facility_4=other_facility_4,
            serial_number_5=serial_number5,
            type_of_computer_5=type_of_computer_5,
            number_terminal_5=number_terminal_5,
            year_of_purchase_5=year_of_purchase_5,
            cost_5=cost_5,
            software_facility_5=software_facility_5,
            other_facility_5=other_facility_5,
            serial_number_6=serial_number6,
            type_of_computer_6=type_of_computer_6,
            number_terminal_6=number_terminal_6,
            year_of_purchase_6=year_of_purchase_6,
            cost_6=cost_6,
            software_facility_6=software_facility_6,
            other_facility_6=other_facility_6,
            information_serial_number_1=information_serial_number_1,
            name_1=name_1,
            designation_1=designation_1,
            qualification_1=qualification_1,
            teaching_experience_1=teaching_experience_1,
            date_of_appointment_1=date_of_appointment_1,
            status_1=status_1,
            information_serial_number_2=information_serial_number_2,
            name_2=name_2,
            designation_2=designation_2,
            qualification_2=qualification_2,
            teaching_experience_2=teaching_experience_2,
            date_of_appointment_2=date_of_appointment_2,
            status_2=status_2,
            information_serial_number_3=information_serial_number_3,
            name_3=name_3,
            designation_3=designation_3,
            qualification_3=qualification_3,
            teaching_experience_3=teaching_experience_3,
            date_of_appointment_3=date_of_appointment_3,
            status_3=status_3,
            information_serial_number_4=information_serial_number_4,
            name_4=name_4,
            designation_4=designation_4,
            qualification_4=qualification_4,
            teaching_experience_4=teaching_experience_4,
            date_of_appointment_4=date_of_appointment_4,
            status_4=status_4,
            center_address=center_address,
            residential_address=residential_address,
            signature=signature,
            form_receive_date=form_receive_date,
            affliation_number=affliation_number,
            total_affliation_fee=total_affliation_fee,
            registration_fee=registration_fee,
            amount_status=amount_status,
            bank_name=bank_name,
            receipt_number=receipt_number,
            date=date,
            education_institution_type=education_institution_type,
            affliation_from_date=affliation_from_date,
            affliation_to_date=affliation_to_date,
            type='addon'
        )
        application.save()
        return Response({"message": "saved successfully"}, status=status.HTTP_200_OK)
    else:
        print("One or more variables do not have a value")

    data = {
        "all_institution_status": all_institution_status,
        "payment_status": payment_status,
    }

    return Response(data, status=status.HTTP_200_OK)


# ===================================================================================================
# ===================================================================================================
# ===================================================================================================
# ===================================================================================================


# ===================================================================================================
# ======================================= Employee Service Book Page ================================
def employee_service_book(request):
    return render(request, "internal/employee_service_book.html")


# ===================================================================================================
# ===================================================================================================


# ===================================================================================================
# ======================================= Pay Online Fees Page ======================================
@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def pay_online_fees(request):
    all_type_fees = Fee_TypeSerializer(Fee_Type.objects.all(), many=True).data

    CollegeName = request.data.get("CollegeName")
    Typeoffee = request.data.get("Typeoffee")
    typeofFeeOther = request.data.get("typeofFeeOther")
    amount = request.data.get("amount")
    datepicker = request.data.get("datepicker")
    remarks = request.data.get("remarks")
    Transactionid = request.data.get("Transactionid")

    if (
        CollegeName
        and Typeoffee
        and amount
        and datepicker
        and remarks
        and Transactionid
    ):
        typeoffee = Fee_Type.objects.get(id=Typeoffee)

        Pay_Online_Fees(
            college_name=CollegeName,
            type_of_fees=typeoffee,
            type_of_other_fees=typeofFeeOther,
            amount=amount,
            date=datepicker,
            remark=remarks,
            transaction_id=Transactionid,
        ).save()
        return Response({"message": "saved successfully"}, status=status.HTTP_200_OK)
    data = {
        "all_type_fees": all_type_fees,
    }

    return Response(data, status=status.HTTP_200_OK)


# ===================================================================================================
# ===================================================================================================


# ===================================================================================================
# ======================================= E Office File Sanction Page ===============================
@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def e_office_file_sanction(request):
    all_status = StatusSerializer(Status.objects.all(), many=True).data
    docket_number = request.data.get("docket_number")
    employee_code = request.data.get("employee_code")
    employee_name = request.data.get("employee_name")
    file_number = request.data.get("file_number")
    file_name = request.data.get("file_name")
    sanction_clerk = request.data.get("sanction_clerk")
    officer_grade_1 = request.data.get("officer_grade_1")
    officer_grade_2 = request.data.get("officer_grade_2")
    note_file = request.data.get("note_file")
    general_note_sanction_order = request.data.get("general_note_sanction_order")
    order_number = request.data.get("order_number")
    remark = request.data.get("remark")

    if (
        docket_number
        and employee_code
        and employee_name
        and file_number
        and file_name
        and sanction_clerk
        and officer_grade_1
        and officer_grade_2
        and note_file
        and general_note_sanction_order
        and order_number
        and remark
    ):
        sanction_clerk_id = Status.objects.get(id=sanction_clerk)
        officer_grade_1_id = Status.objects.get(id=officer_grade_1)
        officer_grade_2_id = Status.objects.get(id=officer_grade_2)

        your_model_instance = E_Office_File_Sanction(
            docket_number=docket_number,
            employee_code=employee_code,
            employee_name=employee_name,
            file_number=file_number,
            file_name=file_name,
            sanction_clerk=sanction_clerk_id,
            officer_grade_1=officer_grade_1_id,
            officer_grade_2=officer_grade_2_id,
            note_file=note_file,
            general_note_sanction_order=general_note_sanction_order,
            order_number=order_number,
            remark=remark,
        )

        your_model_instance.save()
        return Response({"message": "saved successfully"}, status=status.HTTP_200_OK)

    data = {
        "all_status": all_status,
    }
    return Response(data, status=status.HTTP_200_OK)


# ===================================================================================================
# ===================================================================================================


# ===================================================================================================
# ======================================= Student Marks Page ========================================
def student_marks(request):
    return render(request, "internal/student_marks.html")


# ===================================================================================================
# ===================================================================================================


# ===================================================================================================
# ======================================= Internal Functions (2) ====================================


# ===================================================================================================
# ======================================= E-Finance and Accounts Page ===============================
@api_view(["GET"])
@permission_classes([AllowAny])
@authentication_classes([BasicAuthentication])
def e_finance_and_accounts(request):
    all_e_finance_and_accounts = E_Office_AccountSerializer(
        E_Office_Account.objects.all(), many=True
    ).data
    data = {
        "all_e_finance_and_accounts": all_e_finance_and_accounts,
    }
    return Response(data, status=status.HTTP_200_OK)


# ===================================================================================================
# ===================================================================================================


# ===================================================================================================
# ======================================= E-Office Accounts Page ====================================
@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def e_office_accounts(request):
    all_type_account = Type_of_AccountSerializer(
        Type_of_Account.objects.all(), many=True
    ).data
    all_particular_head = Particulars_HeadSerializer(
        Particulars_Head.objects.all(), many=True
    ).data
    all_college_name = College_NameSerializer(
        College_Name.objects.all(), many=True
    ).data
    all_status = StatusSerializer(Status.objects.all(), many=True).data

    voucher_number = request.data.get("voucher_number")

    particular_head = request.data.get("particular_head")

    date = request.data.get("date")

    amount = request.data.get("amount")

    bank_name = request.data.get("bank_name")

    amount_detail = request.data.get("amount_detail")

    transaction_id = request.data.get("transaction_id")

    remark = request.data.get("remark")

    details_name = request.data.get("details_name")

    college_name = request.data.get("college_name")

    address = request.data.get("address")

    amount2 = request.data.get("amount2")

    file_referral_number = request.data.get("file_referral_number")

    o_office_register_number = request.data.get("o_office_register_number")

    pan_card_number = request.data.get("pan_card_number")

    officer_incharge_name = request.data.get("officer_incharge_name")

    secretary_name = request.data.get("secretary_name")

    officer_incharge_status = request.data.get("officer_incharge_status")

    secretary_status = request.data.get("secretary_status")

    remark_staff_approval = request.data.get("remark_staff_approval")

    remark_officer_approval = request.data.get("remark_officer_approval")

    office_referral_number = request.data.get("office_referral_number")

    description = request.data.get("description")
    type_of_account = request.data.get("type_of_account")

    if (
        type_of_account
        and particular_head
        and date
        and voucher_number
        and details_name
        and college_name
        and address
        and file_referral_number
        and o_office_register_number
        and officer_incharge_name
        and secretary_name
        and officer_incharge_status
        and secretary_status
        and remark_staff_approval
        and remark_officer_approval
        and office_referral_number
    ):
        type_of_account = Type_of_Account.objects.get(id=type_of_account)
        particular_head = Particulars_Head.objects.get(id=particular_head)
        college_name = College_Name.objects.get(id=college_name)
        officer_incharge_status = Status.objects.filter(
            id=officer_incharge_status
        ).first()
        secretary_status = Status.objects.filter(id=secretary_status).first()
        e_office_account = E_Office_Account(
            type_of_account=type_of_account,
            voucher_number=voucher_number,
            particular_head=particular_head,
            date=date,
            amount=amount,
            bank_name=bank_name,
            amount_detail=amount_detail,
            transaction_number=transaction_id,
            remark=remark,
            name=details_name,
            college_name=college_name,
            address=address,
            amount2=amount2,
            file_referral_number=file_referral_number,
            office_registration_number=o_office_register_number,
            pan_card_number=pan_card_number,
            officer_incharge_name=officer_incharge_name,
            secretary_name=secretary_name,
            officer_incharge_status=officer_incharge_status,
            secretary_status=secretary_status,
            remark_staff_approval=remark_staff_approval,
            remark_officer_approval=remark_officer_approval,
            office_referral_number=office_referral_number,
            description=description,
        )
        e_office_account.save()
        return Response({"message": "saved successfully"}, status=status.HTTP_200_OK)

    data = {
        "all_type": all_type_account,
        "all_heads": all_particular_head,
        "all_college": all_college_name,
        "all_status": all_status,
    }
    return Response(data, status=status.HTTP_200_OK)


# ===================================================================================================
# ===================================================================================================


# ===================================================================================================
# ======================================= E-Office Student Register Page ============================
def e_office_student_register(request):
    return render(request, "internal/e_office_students_registration.html")


# ===================================================================================================
# ===================================================================================================


# ===================================================================================================
# ======================================= E-Office Email Page =======================================
def e_office_email(request):
    return render(request, "internal/e_office_email.html")


# ===================================================================================================
# ===================================================================================================


# ===================================================================================================
# ======================================= E-Office Queue Files Page =================================
@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def e_office_queue_files(request):
    all_status = StatusSerializer(Status.objects.all(), many=True).data
    queue_number = request.data.get("queue_number")
    file_subject = request.data.get("file_subject")
    remark = request.data.get("remark")
    approval_first_officer = request.data.get("approval_first_officer")
    approval_second_officer = request.data.get("approval_second_officer")

    if queue_number and file_subject:
        get_approval_first_officer = Status.objects.filter(
            id=approval_first_officer
        ).first()
        get_approval_second_officer = Status.objects.filter(
            id=approval_second_officer
        ).first()
        add_e_office_queue_files = E_Office_Queue(
            queue_number=queue_number,
            file_subject=file_subject,
            remark=remark,
            approval_first_officer=get_approval_first_officer,
            approval_second_officer=get_approval_second_officer,
        )

        # Save the instance
        add_e_office_queue_files.save()
        return Response({"message": "saved successfully"}, status=status.HTTP_200_OK)

    data = {
        "all_status": all_status,
    }
    return Response(data, status=status.HTTP_200_OK)


# ===================================================================================================
# ===================================================================================================


# ===================================================================================================
# ======================================= E-Office Files Page =======================================
def e_office_files(request):
    return render(request, "internal/e_office_files.html")


# ===================================================================================================
# ===================================================================================================


# ===================================================================================================
# ======================================= E Employee Records Page ===================================
@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def e_employee_records(request):
    all_employee_record = Employee_Record_TypeSerializer(
        Employee_Record_Type.objects.all(), many=True
    ).data
    employee_record_type = request.data.get("employee_record_type")
    name = request.data.get("name")
    designation = request.data.get("designation")
    employee_code = request.data.get("employee_code")
    office_address = request.data.get("office_address")
    home_address = request.data.get("home_address")
    contact_number = request.data.get("contact_number")
    aadhar_number = request.data.get("aadhar_number")
    husband_or_wife_name = request.data.get("husband_or_wife_name")
    father_name = request.data.get("father_name")
    age_of_father = request.data.get("age_of_father")
    mother_name = request.data.get("mother_name")
    age_of_mother = request.data.get("age_of_mother")
    child_name_1 = request.data.get("child_name_1")
    age_of_child_1 = request.data.get("age_of_child_1")
    child_name_2 = request.data.get("child_name_2")
    age_of_child_2 = request.data.get("age_of_child_2")
    child_name_3 = request.data.get("child_name_3")
    age_of_child_3 = request.data.get("age_of_child_3")
    scale_of_pay = request.data.get("scale_of_pay")
    employee_liablity = request.data.get("employee_liablity")
    employee_promotion = request.data.get("employee_promotion")
    employee_grade = request.data.get("employee_grade")
    salary = request.data.get("salary")
    advance = request.data.get("advance")
    bonus = request.data.get("bonus")
    loan = request.data.get("loan")
    note = request.data.get("note")
    remark = request.data.get("remark")
    suspension = request.data.get("suspension")
    showcase_notice = request.data.get("showcase_notice")

    if (
        employee_record_type
        and name
        and designation
        and employee_code
        and office_address
        and home_address
        and contact_number
        and aadhar_number
        and husband_or_wife_name
        and father_name
        and age_of_father
        and mother_name
        and age_of_mother
        and child_name_1
        and age_of_child_1
        and scale_of_pay
        and employee_liablity
        and employee_promotion
        and employee_grade
        and salary
        and advance
        and bonus
        and loan
        and note
        and remark
        and suspension
        and showcase_notice
    ):
        get_employee_record_type = Employee_Record_Type.objects.get(
            id=employee_record_type
        )
        add_employee_record = E_Employee_Record(
            employee_record_type=get_employee_record_type,
            name=name,
            designation=designation,
            employee_code=employee_code,
            office_address=office_address,
            home_address=home_address,
            contact_number=contact_number,
            aadhar_number=aadhar_number,
            husband_or_wife_name=husband_or_wife_name,
            father_name=father_name,
            age_of_father=age_of_father,
            mother_name=mother_name,
            age_of_mother=age_of_mother,
            child_name_1=child_name_1,
            age_of_child_1=age_of_child_1,
            child_name_2=child_name_2,
            age_of_child_2=age_of_child_2,
            child_name_3=child_name_3,
            age_of_child_3=age_of_child_3,
            scale_of_pay=scale_of_pay,
            employee_liablity=employee_liablity,
            employee_promotion=employee_promotion,
            employee_grade=employee_grade,
            salary=salary,
            advance=advance,
            bonus=bonus,
            loan=loan,
            note=note,
            remark=remark,
            suspension=suspension,
            showcase_notice=showcase_notice,
        )
        return Response({"message": "saved successfully"}, status=status.HTTP_200_OK)

    data = {
        "all_employee_record": all_employee_record,
    }
    return Response(data, status=status.HTTP_200_OK)


# ===================================================================================================
# ===================================================================================================


# ===================================================================================================
# ======================================= E Employee Daily Work Statement Page ======================
@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def e_employee_daily_work_statement(request):
    all_status = StatusSerializer(Status.objects.all(), many=True).data
    all_work_status = Work_StatusSerializer(Work_Status.objects.all(), many=True).data

    employee_name = request.data.get("employee_name")
    work_start_time = request.data.get("work_start_time")
    employee_code = request.data.get("employee_code")
    work_end_time = request.data.get("work_end_time")
    serial_number_1 = request.data.get("serial_number_1")
    file_number_1 = request.data.get("file_number_1")
    work_name_1 = request.data.get("work_name_1")
    work_status_1 = request.data.get("work_status_1")
    serial_number_2 = request.data.get("serial_number_2")
    file_number_2 = request.data.get("file_number_2")
    work_name_2 = request.data.get("work_name_2")
    work_status_2 = request.data.get("work_status_2")
    serial_number_3 = request.data.get("serial_number_3")
    file_number_3 = request.data.get("file_number_3")
    work_name_3 = request.data.get("work_name_3")
    work_status_3 = request.data.get("work_status_3")
    serial_number_4 = request.data.get("serial_number_4")
    file_number_4 = request.data.get("file_number_4")
    work_name_4 = request.data.get("work_name_4")
    work_status_4 = request.data.get("work_status_4")
    serial_number_5 = request.data.get("serial_number_5")
    file_number_5 = request.data.get("file_number_5")
    work_name_5 = request.data.get("work_name_5")
    work_status_5 = request.data.get("work_status_5")
    serial_number_6 = request.data.get("serial_number_6")
    file_number_6 = request.data.get("file_number_6")
    work_name_6 = request.data.get("work_name_6")
    work_status_6 = request.data.get("work_status_6")
    serial_number_7 = request.data.get("serial_number_7")
    file_number_7 = request.data.get("file_number_7")
    work_name_7 = request.data.get("work_name_7")
    work_status_7 = request.data.get("work_status_7")
    serial_number_8 = request.data.get("serial_number_8")
    file_number_8 = request.data.get("file_number_8")
    work_name_8 = request.data.get("work_name_8")
    work_status_8 = request.data.get("work_status_8")
    serial_number_9 = request.data.get("serial_number_9")
    file_number_9 = request.data.get("file_number_9")
    work_name_9 = request.data.get("work_name_9")
    work_status_9 = request.data.get("work_status_9")
    serial_number_10 = request.data.get("serial_number_10")
    file_number_10 = request.data.get("file_number_10")
    work_name_10 = request.data.get("work_name_10")
    work_status_10 = request.data.get("work_status_10")
    date = request.data.get("date")
    charge_officer_name = request.data.get("charge_officer_name")
    status_1 = request.data.get("status_1")
    chief_executive_officer_name = request.data.get("chief_executive_officer_name")
    status_2 = request.data.get("status_2")

    if (
        employee_name
        and work_start_time
        and employee_code
        and work_end_time
        and serial_number_1
        and file_number_1
        and work_name_1
        and work_status_1
    ):
        get_work_status_1 = Work_Status.objects.get(id=work_status_1)
        get_work_status_2 = Work_Status.objects.get(id=work_status_2)
        get_work_status_3 = Work_Status.objects.get(id=work_status_3)
        get_work_status_4 = Work_Status.objects.get(id=work_status_4)
        get_work_status_5 = Work_Status.objects.get(id=work_status_5)
        get_work_status_6 = Work_Status.objects.get(id=work_status_6)
        get_work_status_7 = Work_Status.objects.get(id=work_status_7)
        get_work_status_8 = Work_Status.objects.get(id=work_status_8)
        get_work_status_9 = Work_Status.objects.get(id=work_status_9)
        get_work_status_10 = Work_Status.objects.get(id=work_status_10)
        get_status_1 = Status.objects.get(id=status_1)
        get_status_2 = Status.objects.get(id=status_2)

        add_employee_daily_work_statement = E_employee_daily_work_statement(
            employee_name=employee_name,
            work_start_time=work_start_time,
            employee_code=employee_code,
            work_end_time=work_end_time,
            serial_number_1=serial_number_1,
            file_number_1=file_number_1,
            work_name_1=work_name_1,
            work_status_1=get_work_status_1,
            serial_number_2=serial_number_2,
            file_number_2=file_number_2,
            work_name_2=work_name_2,
            work_status_2=get_work_status_2,
            serial_number_3=serial_number_3,
            file_number_3=file_number_3,
            work_name_3=work_name_3,
            work_status_3=get_work_status_3,
            serial_number_4=serial_number_4,
            file_number_4=file_number_4,
            work_name_4=work_name_4,
            work_status_4=get_work_status_4,
            serial_number_5=serial_number_5,
            file_number_5=file_number_5,
            work_name_5=work_name_5,
            work_status_5=get_work_status_5,
            serial_number_6=serial_number_6,
            file_number_6=file_number_6,
            work_name_6=work_name_6,
            work_status_6=get_work_status_6,
            serial_number_7=serial_number_7,
            file_number_7=file_number_7,
            work_name_7=work_name_7,
            work_status_7=get_work_status_7,
            serial_number_8=serial_number_8,
            file_number_8=file_number_8,
            work_name_8=work_name_8,
            work_status_8=get_work_status_8,
            serial_number_9=serial_number_9,
            file_number_9=file_number_9,
            work_name_9=work_name_9,
            work_status_9=get_work_status_9,
            serial_number_10=serial_number_10,
            file_number_10=file_number_10,
            work_name_10=work_name_10,
            work_status_10=get_work_status_10,
            date=date,
            charge_officer_name=charge_officer_name,
            status_1=get_status_1,
            chief_executive_officer_name=chief_executive_officer_name,
            status_2=get_status_2,
        )
        add_employee_daily_work_statement.save()
        return Response({"message": "saved successfully"}, status=status.HTTP_200_OK)
    data = {
        "all_status": all_status,
        "all_work_status": all_work_status,
    }
    return Response(data, status=status.HTTP_200_OK)


# ===================================================================================================
# ===================================================================================================


# ===================================================================================================
# ======================================= E Employee Live and Leave Status Page =====================
@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def e_employee_live_and_leave_status(request):
    all_employee_live_status = Employee_Live_and_Leave_StatusSerializer(
        Employee_Live_and_Leave_Status.objects.all(), many=True
    ).data
    all_status = StatusSerializer(Status.objects.all(), many=True).data
    all_nature_of_leave = Nature_of_LeaveSerializer(
        Nature_of_Leave.objects.all(), many=True
    ).data

    Employee_Live = request.data.get("Employee_Live")
    Employee_ID_Number = request.data.get("Employee_ID_Number")
    Employee_Namec = request.data.get("Employee_Namec")
    if Employee_Live and Employee_ID_Number and Employee_Namec:
        if Employee_Live == "None":
            Employee_Live_id = None
        else:
            Employee_Live_id = Employee_Live_and_Leave_Status.objects.get(
                id=Employee_Live
            )

        your_module = Employee_Status(
            employee_live_or_leave_status=Employee_Live_id,
            employee_id_number=Employee_ID_Number,
            employee_name=Employee_Namec,
        )
        your_module.save()
        return Response({"message": "saved successfuly"}, status=status.HTTP_200_OK)
    data = {
        "employee_live": all_employee_live_status,
        "all_status": all_status,
        "all_nature_of_leave": all_nature_of_leave,
    }
    return Response(data, status=status.HTTP_200_OK)


# ===================================================================================================
# ===================================================================================================


# ===================================================================================================
# ======================================= E Employee Live Status Page ===============================
@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def e_employee_live_status(request):
    all_employee_live_status = Employee_Live_and_Leave_StatusSerializer(
        Employee_Live_and_Leave_Status.objects.all(), many=True
    ).data
    all_status = StatusSerializer(Status.objects.all(), many=True).data
    all_nature_of_leave = Nature_of_LeaveSerializer(
        Nature_of_Leave.objects.all(), many=True
    ).data

    get_Employee_Live = request.data.get("send_Employee_Live")
    get_Employee_ID_Number = request.data.get("send_Employee_ID_Number")
    get_Employee_Namec = request.data.get("send_Employee_Namec")
    get_nature_of_leave = request.data.get("send_nature_of_leave")
    get_remark2 = request.data.get("send_remark2")
    get_datepicker = request.data.get("send_datepicker")
    get_current_status2 = request.data.get("send_current_status2")

    # Check if all variables have a value
    if (
        get_Employee_Live
        and get_Employee_ID_Number
        and get_Employee_Namec
        and get_nature_of_leave
        and get_remark2
        and get_datepicker
        and get_current_status2
    ):
        status_ = Status.objects.filter(
            id=get_current_status2
        ).first()  # select option filed
        employee_live_or_leave_status = Employee_Live_and_Leave_Status.objects.filter(
            id=2
        ).first()
        nature_of_leave = Nature_of_Leave.objects.filter(id=get_nature_of_leave).first()

        save_live_status_data = E_employee_live_status(
            employee_live_or_leave_status=employee_live_or_leave_status,
            employee_id_number=get_Employee_ID_Number,
            employee_name=get_Employee_Namec,
            nature_of_leave=nature_of_leave,
            remark=get_remark2,
            date=get_datepicker,
            status=status_,
        )
        save_live_status_data.save()
        return Response({"message": "saved successfuly"}, status=status.HTTP_200_OK)
    else:
        print("One or more variables are missing a value.")

    data = {
        "employee_live": all_employee_live_status,
        "all_status": all_status,
        "all_nature_of_leave": all_nature_of_leave,
    }
    return Response(data, status=status.HTTP_200_OK)


# ===================================================================================================
# ===================================================================================================


# ===================================================================================================
# ======================================= E Employee Leave Status Page ==============================
@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def e_employee_leave_status(request):
    all_employee_live_status = Employee_Live_and_Leave_StatusSerializer(
        Employee_Live_and_Leave_Status.objects.all(), many=True
    ).data
    all_status = StatusSerializer(Status.objects.all(), many=True).data
    all_nature_of_leave = Nature_of_LeaveSerializer(
        Nature_of_Leave.objects.all(), many=True
    ).data

    # get_Employee_Live = request.POST.get("Employee_ID_Number2")
    get_Employee_ID_Number = request.data.get("send_Employee_ID_Number2")
    get_Employee_Namec = request.data.get("send_Employee_Name2")
    get_purpose_1 = request.data.get("send_purpose1")
    get_distance_walking_1 = request.data.get("send_walking_distance1")
    get_purpose_2 = request.data.get("send_purpose2")
    get_distance_walking_2 = request.data.get("send_walking_distance2")
    get_purpose_3 = request.data.get("send_purpose3")
    get_distance_walking_3 = request.data.get("send_walking_distance3")
    get_staff_out_time = request.data.get("send_staff_out_time")
    get_staff_in_time = request.data.get("send_staff_in_time")
    get_status3 = request.data.get("send_current_status3")
    get_remark = request.data.get("send_remark")

    if (
        get_Employee_ID_Number
        and get_Employee_Namec
        and get_purpose_1
        and get_distance_walking_1
        and get_staff_out_time
        and get_staff_in_time
        and get_status3
        and get_remark
    ):
        get_Employee_Live_id = Employee_Live_and_Leave_Status.objects.get(id=1)
        status_ = Status.objects.get(id=get_status3)

        save_leave_status_data = E_employee_leave_status(
            employee_live_or_leave_status=get_Employee_Live_id,
            employee_id_number=get_Employee_ID_Number,
            employee_name=get_Employee_Namec,
            purpose_1=get_purpose_1,
            distance_walking_1=get_distance_walking_1,
            purpose_2=get_purpose_2,
            distance_walking_2=get_distance_walking_2,
            purpose_3=get_purpose_3,
            distance_walking_3=get_distance_walking_3,
            staff_out_time=get_staff_out_time,
            staff_in_time=get_staff_in_time,
            status=status_,
            remark=get_remark,
        )
        save_leave_status_data.save()
        return Response({"message": "saved successfuly"}, status=status.HTTP_200_OK)
    data = {
        "employee_live": all_employee_live_status,
        "all_status": all_status,
        "all_nature_of_leave": all_nature_of_leave,
    }
    return Response(data, status=status.HTTP_200_OK)


# ===================================================================================================
# ===================================================================================================


# ===================================================================================================
# ======================================= E Adminstration Page ======================================
def e_adminstations(request):
    return render(request, "internal/e_adminstration.html")


# ===================================================================================================
# ===================================================================================================


# ===================================================================================================
# ======================================= E Student Certificate Verification Page ===================
def e_student_certificate_verification(request):
    return render(request, "internal/e_student_certificate_verification.html")


# ===================================================================================================
# ===================================================================================================


# ============================================ Extra 1 ==============================================


# ===================================================================================================
# ======================================= E Office Student Mark List Registration Page ==============
def e_office_mark_list_registration(request):
    return render(request, "internal/e_office_mark_list_registration.html")


# ===================================================================================================
# ===================================================================================================


# ===================================================================================================
# ======================================= E Office Student Admission Registration Page ==============
def e_office_student_admisiion_registration(request):
    return render(request, "internal/e_office_student_admission_registration.html")


# ===================================================================================================
# ===================================================================================================


# ===================================================================================================
# ======================================= E Office Student Add on Programme Page ====================
def e_office_student_add_on_programme(request):
    return render(request, "internal/e_office_student_add_on_programme.html")


# ===================================================================================================
# ===================================================================================================


# ============================================ Extra 2 ==============================================


# ===================================================================================================
# ======================================= E Office Files Mark List Page =============================
def e_office_files_student_mark_list(request):
    return render(request, "internal/e_office_files_student_mark_list.html")


# ===================================================================================================
# ===================================================================================================


# ===================================================================================================
# ======================================= E Office Files Daily Work Statement Page ==================
def e_office_files_daily_work_statement(request):
    return render(request, "internal/e_office_files_daily_work_statement.html")


# ===================================================================================================
# ===================================================================================================


# ===================================================================================================
# ======================================= E Office Files Employee Live Status Page ==================
def e_office_files_employee_live_status(request):
    return render(request, "internal/e_office_files_employee_live_status.html")


# ===================================================================================================
# ===================================================================================================


# ===================================================================================================
# ======================================= E Office Files Pay Online Fees Page =======================
def e_office_files_pay_online_fees(request):
    return render(request, "internal/e_office_files_pay_online_fees.html")


# ===================================================================================================
# ===================================================================================================


# ============================================ Extra 3 ==============================================


# ===================================================================================================
# ======================================= E Office Files Staff work Allotment Page ==================
@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def staff_work_alloted(request):
    all_work_assign_office = Work_Assign_OfficeSerializer(
        Work_Assign_Office.objects.all(), many=True
    ).data
    all_work_status = Work_StatusSerializer(Work_Status.objects.all(), many=True).data

    work_assign_office = request.POST.get("send_work_assign_office")
    name_of_employee = request.POST.get("send_name_of_employee")
    work_start_date = request.POST.get("send_work_start_date")
    work_start_time = request.POST.get("send_work_start_time")
    work_name = request.POST.get("send_work_name")
    upload_work = request.POST.get("send_myFileInput")
    work_finishing_date = request.POST.get("send_work_finishing_date")
    work_finishing_time = request.POST.get("send_work_finishing_time")
    work_head_name = request.POST.get("send_work_head_name")
    current_status = request.POST.get("send_current_status")

    if (
        work_assign_office
        and name_of_employee
        and work_start_date
        and work_start_time
        and work_name
        and upload_work
        and work_finishing_date
        and work_finishing_time
        and work_head_name
        and current_status
    ):
        get_work_assign_office_id = Work_Assign_Office.objects.get(
            id=work_assign_office
        )
        get_current_status_id = Work_Status.objects.get(id=current_status)
        save_data = Staff_work_allotment(
            work_assign_office=get_work_assign_office_id,
            name_of_employee=name_of_employee,
            work_start_date=work_start_date,
            work_start_time=work_start_time,
            work_name=work_name,
            upload_work=upload_work,
            work_finishing_date=work_finishing_date,
            work_finishing_time=work_finishing_time,
            work_head_name=work_head_name,
            current_status=get_current_status_id,
        )
        save_data.save()
        return HttpResponse("Save")
    data = {
        "all_work_assign_office": all_work_assign_office,
        "all_work_status": all_work_status,
    }
    return Response(data, status=status.HTTP_200_OK)


# ===================================================================================================
# ===================================================================================================
@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def student_certificate__verification(request):
    all_mark_enter_clerk = Mark_StatusSerializer(
        Mark_Status.objects.all(), many=True
    ).data
    all_result_status = Result_StatusSerializer(
        Result_Status.objects.all(), many=True
    ).data
    search_student_data = ""
    search_get_exam = ""
    search_student_data_error = ""
    admissionsFormdata = None
    register_number_allready = ""
    get_search_registration_number = request.GET.get("search_registration_number")
    certificate_image_with_path = None
    marklist_image_with_path = None

    if get_search_registration_number:
        admissions = Admission_Registration.objects.filter(
            registration_number=get_search_registration_number
        ).first()
        get_exam = Exam_Registration.objects.filter(
            registration_number=get_search_registration_number
        ).first()
        admissionsFormdata = Mark_List_Registration.objects.filter(
            registration_number=get_search_registration_number
        ).first()
        vtc_admissions = VTC_Course_Admission_Registration.objects.filter(
            registration_number=get_search_registration_number
        ).first()

        if admissionsFormdata:
            search_student_data = admissionsFormdata
            if search_student_data.certificate_image:
                certificate_image_with_path = search_student_data.certificate_image.url
            if search_student_data.marklist_image:
                marklist_image_with_path = search_student_data.marklist_image.url
        else:
            search_student_data_error = "Invalid Registration Number!"

    data = {
        "all_mark_enter_clerk": all_mark_enter_clerk,
        "all_result_status": all_result_status,
        "search_student_data": search_student_data,
        "search_get_exam": search_get_exam,
        "search_student_data_error": search_student_data_error,
        "get_search_registration_number": get_search_registration_number,
        "admissionsFormdata": admissionsFormdata,
        "register_number_allready": register_number_allready,
        "certificate_image_with_path": certificate_image_with_path,
        "marklist_image_with_path": marklist_image_with_path,
    }
    return Response(data, status=status.HTTP_200_OK)


@api_view(["GET", "POST"])
@permission_classes([])
@authentication_classes([])
def ApiStatus(request):
    collage_name = [
        "Sree narayana college chengannur",
        "Sree narayana college chengannur",
        "Sree narayana college chengannur",
        "Sree narayana college chengannur",
        "Sree narayana college chengannur",
    ]

    for i in collage_name:
        College_Name.objects.create(college_name=i)
    course_name = [
        "ADVANCED DIPLOMA IN HUMAN RESOURCE MANAGEMENT",
        "ADVANCED DIPLOMA IN MEP",
    ]

    for i in course_name:
        Course_Name.objects.create(course_name=i)
    return Response({"message": "api updated"})


@api_view(["GET", "POST"])
@permission_classes([])
@authentication_classes([])
def course_add(request):
    if request.method == "POST":
        try:
            course_name = request.data["course_name"]
        except KeyError as e:
            return Response(
                {"message": f"please pass the {e} in payload"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        created_course = Course_Name.objects.create(course_name=course_name)
        data = {"id": created_course.id, "course_name": created_course.course_name}
        return Response({"message": data}, status=status.HTTP_200_OK)
    else:
        all_courses = Course_Name.objects.all()
        coiurses = Course_NameSerializer(all_courses, many=True).data
        return Response({"data": coiurses})


@api_view(["GET", "POST"])
@permission_classes([])
@authentication_classes([])
def showregistered_number(request):
    obj = Admission_Registration.objects.all().order_by('-id')
    data = Admission_Registration_serializer(obj, many=True).data
    return Response({"data": data})


@api_view(["GET", "POST"])
@permission_classes([])
@authentication_classes([])
def showregistered_number_detail(request,id):
    obj = Admission_Registration.objects.get(id=id)
    data = Admission_Registration_serializer(obj).data
    return Response({"data": data})




@api_view(["PATCH","DELETE"])
@permission_classes([])
@authentication_classes([])
def showregistered_number_edit(request, id):
    try:
        obj = Admission_Registration.objects.get(id=id)
    except Admission_Registration.DoesNotExist:
        return Response({"error": "Object not found"}, status=404)
    
    if request.method == "DELETE":
        obj.delete()
        return Response({"message":"successfully deleted"}, status = status.HTTP_200_OK)

    serializer = Admission_Registration_serializer(obj, data=request.data, partial=True)
    
    if serializer.is_valid():
        serializer.save()
        return Response({"data": serializer.data})
    else:
        return Response(serializer.errors, status=400)



@api_view(["DELETE"])
@permission_classes([])
@authentication_classes([])
def showregistered_number_delete(request, id):
    try:
        obj = Admission_Registration.objects.get(id=id)
    except Admission_Registration.DoesNotExist:
        return Response({"error": "Object not found"}, status=404)
    obj.delete()
    return Response({"message":"success"})

@api_view(["GET", "POST","PATCH","DELETE"])
@permission_classes([])
@authentication_classes([])
def vtc_admission(request):
    obj = VTC_Course_Admission_Registration.objects.all().order_by('-id')
    data = VTC_Course_Admission_Registration_serializer(obj, many=True).data
    return Response({"data": data})

@api_view(["GET", "POST","PATCH","DELETE"])
@permission_classes([])
@authentication_classes([])
def vtc_admission_detail(request,id):
    obj = VTC_Course_Admission_Registration.objects.get(id=id)
    data = VTC_Course_Admission_Registration_serializer(obj).data
    return Response({"data": data})


@api_view(["PATCH","DELETE"])
@permission_classes([])
@authentication_classes([])
def vtc_admission_edit(request,id):
    if request.method == "DELETE":
        obj = VTC_Course_Admission_Registration.objects.get(id=id)
        obj.delete()
        return Response({"message":"successfully deleted"}, status = status.HTTP_200_OK)
    
    obj = VTC_Course_Admission_Registration.objects.get(id=id)
    serializer = VTC_Course_Admission_Registration_serializer(obj, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()  # Save the updated object
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class BlogPostListCreateView(ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [AllowAny]
    authentication_classes = [BasicAuthentication]

class BlogPostDetailView(RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field = 'id'  
    permission_classes = [AllowAny]
    authentication_classes = [BasicAuthentication]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {"message": "Blog post deleted successfully."},
            status=status.HTTP_200_OK,
        )


class CategoryListView(APIView):
    permission_classes = []
    authentication_classes = []
    def get(self,request, id):
        news_obj = News.objects.filter(category_id=id)
        data = NewsSerializers(news_obj, many=True).data
        return Response({"data":data})
