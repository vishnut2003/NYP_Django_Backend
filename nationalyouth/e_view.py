from django.db.models import Max
from rest_framework.views import APIView
from nationalyouth.e_serializers import (
    E_Office_Queue_Serializer,
    E_Employee_Record_Serializer,
    E_employee_daily_work_statement_Serializer,
    E_employee_live_status_Serializer,
    E_employee_leave_status_Serializer,
    Staff_work_allotment_Serializer,
    E_Office_Account_Serializer,
    E_Office_File_Sanction_Serializer,
    Application_for_Affliation_Serializer,
    VTC_Course_Admission_Registration_Serializer,
    Admission_Registration_Serializer,
    Mark_List_Registration_Serializer,
    Exam_Registration_Serializer,
    E_Employee_Record_Contribution_Serializer,
    Affiliated_Vocational_Training_College_Kerla_Serializer
)
from rest_framework.response import Response
from rest_framework import status
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
    Mark_List_Registration,
    Exam_Registration,
    E_Employee_Record_Contribution,
    Affiliated_Vocational_Training_College_Kerla

)
from rest_framework.permissions import IsAuthenticated






class E_Office_Queue_View(APIView):
    # permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = E_Office_Queue_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        e_office_queue = E_Office_Queue.objects.all()
        serializer = E_Office_Queue_Serializer(e_office_queue, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


class E_Office_Queue_Detail_View(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request, id):
        try:
            e_office_queue = E_Office_Queue.objects.get(id=id)
            serializer = E_Office_Queue_Serializer(e_office_queue)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except E_Office_Queue.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data=f"{id} not valid")

    def delete(self, request, id):
        try:
            e_office_queue = E_Office_Queue.objects.get(id=id)
            e_office_queue.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except E_Office_Queue.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data=f"{id} not valid")

    def patch(self, request, id):
        try:
            e_office_queue = E_Office_Queue.objects.get(id=id)
            serializer = E_Office_Queue_Serializer(e_office_queue, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except E_Office_Queue.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data=f"{id} not valid")


class E_Employee_Record_View(APIView):
    # permission_classes = [IsAuthenticated]
    
    def post(self, request):
        serializer = E_Employee_Record_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        e_employee_record = E_Employee_Record.objects.all()
        serializer = E_Employee_Record_Serializer(e_employee_record, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


class E_Employee_Record_Detail_View(APIView):
    # permission_classes = [IsAuthenticated]
    
    def get(self, request, id):
        try:
            e_employee_record = E_Employee_Record.objects.get(id=id)
            serializer = E_Employee_Record_Serializer(e_employee_record)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except E_Employee_Record.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data=f"{id} not valid")

    def delete(self, request, id):
        try:
            e_employee_record = E_Employee_Record.objects.get(id=id)
            e_employee_record.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except E_Employee_Record.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data=f"{id} not valid")

    def patch(self, request, id):
        try:
            e_employee_record = E_Employee_Record.objects.get(id=id)
            serializer = E_Employee_Record_Serializer(e_employee_record, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except E_Employee_Record.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data=f"{id} not valid")


class E_Employee_Record_Contribution_View(APIView):
    def get(self, request, id):
        try:
            record = E_Employee_Record.objects.get(id=id)
            contribution = E_Employee_Record_Contribution.objects.filter(record=record)
            serializer = E_Employee_Record_Contribution_Serializer(contribution, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except E_Employee_Record.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data=f"{id} not valid")
        
    def post(self, request, id):
        try:
            record = E_Employee_Record.objects.get(id=id)
            contribution, created = E_Employee_Record_Contribution.objects.get_or_create(record=record,month=request.data.get('month'), year=request.data.get('year'), defaults=request.data)
            if not created:
                serializer = E_Employee_Record_Contribution_Serializer(contribution, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                serializer = E_Employee_Record_Contribution_Serializer(contribution, many=False)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except E_Employee_Record.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data=f"{id} not valid")


class E_Employee_Record_Contribution_Edit_View(APIView):
    def patch(self, request, record_id, contribution_id):
        try:
            record = E_Employee_Record.objects.get(id=record_id)
            contribution = E_Employee_Record_Contribution.objects.get(id=contribution_id, record=record)
            serializer = E_Employee_Record_Contribution_Serializer(contribution, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except E_Employee_Record.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data=f"{record_id} not valid")
        except E_Employee_Record_Contribution.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data=f"{contribution_id} not valid")
    
    def delete(self, request, record_id, contribution_id):
        try:
            record = E_Employee_Record.objects.get(id=record_id)
            contribution = E_Employee_Record_Contribution.objects.get(id=contribution_id, record=record)
            contribution.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except E_Employee_Record.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data=f"{record_id} not valid")
        except E_Employee_Record_Contribution.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data=f"{contribution_id} not valid")


class E_employee_daily_work_statement_View(APIView):
    # permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = E_employee_daily_work_statement_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        e_employee_daily_work_statement = E_employee_daily_work_statement.objects.all()
        serializer = E_employee_daily_work_statement_Serializer(e_employee_daily_work_statement, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


class E_employee_daily_work_statement_Detail_View(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request, id):
        try:
            e_employee_daily_work_statement = E_employee_daily_work_statement.objects.get(id=id)
            serializer = E_employee_daily_work_statement_Serializer(e_employee_daily_work_statement)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except E_employee_daily_work_statement.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data=f"{id} not valid")

    def delete(self, request, id):
        try:
            e_employee_daily_work_statement = E_employee_daily_work_statement.objects.get(id=id)
            e_employee_daily_work_statement.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except E_employee_daily_work_statement.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data=f"{id} not valid")

    def patch(self, request, id):
        try:
            e_employee_daily_work_statement = E_employee_daily_work_statement.objects.get(id=id)
            serializer = E_employee_daily_work_statement_Serializer(e_employee_daily_work_statement, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except E_employee_daily_work_statement.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data=f"{id} not valid")


class E_employee_live_status_View(APIView):
    # permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = E_employee_live_status_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        e_employee_live_status = E_employee_live_status.objects.all()
        serializer = E_employee_live_status_Serializer(e_employee_live_status, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


class E_employee_live_status_Detail_View(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request, id):
        try:
            e_employee_live_status = E_employee_live_status.objects.get(id=id)
            serializer = E_employee_live_status_Serializer(e_employee_live_status)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except E_employee_live_status.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data=f"{id} not valid")

    def delete(self, request, id):
        try:
            e_employee_live_status = E_employee_live_status.objects.get(id=id)
            e_employee_live_status.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except E_employee_live_status.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data=f"{id} not valid")

    def patch(self, request, id):
        try:
            e_employee_live_status = E_employee_live_status.objects.get(id=id)
            serializer = E_employee_live_status_Serializer(e_employee_live_status, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except E_employee_live_status.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data=f"{id} not valid")


class E_employee_leave_status_View(APIView):
    # permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = E_employee_leave_status_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        e_employee_leave_status = E_employee_leave_status.objects.all()
        serializer = E_employee_leave_status_Serializer(e_employee_leave_status, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


class E_employee_leave_status_Detail_View(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request, id):
        try:
            e_employee_leave_status = E_employee_leave_status.objects.get(id=id)
            serializer = E_employee_leave_status_Serializer(e_employee_leave_status)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except E_employee_leave_status.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data=f"{id} not valid")

    def delete(self, request, id):
        try:
            e_employee_leave_status = E_employee_leave_status.objects.get(id=id)
            e_employee_leave_status.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except E_employee_leave_status.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data=f"{id} not valid")

    def patch(self, request, id):
        try:
            e_employee_leave_status = E_employee_leave_status.objects.get(id=id)
            serializer = E_employee_leave_status_Serializer(e_employee_leave_status, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except E_employee_leave_status.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data=f"{id} not valid")


class Staff_work_allotment_View(APIView):
    # permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = Staff_work_allotment_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        staff_work_allotment = Staff_work_allotment.objects.all()
        serializer = Staff_work_allotment_Serializer(staff_work_allotment, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


class Staff_work_allotment_Detail_View(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request, id):
        try:
            staff_work_allotment = Staff_work_allotment.objects.get(id=id)
            serializer = Staff_work_allotment_Serializer(staff_work_allotment)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Staff_work_allotment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data=f"{id} not valid")

    def delete(self, request, id):
        try:
            staff_work_allotment = Staff_work_allotment.objects.get(id=id)
            staff_work_allotment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Staff_work_allotment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data=f"{id} not valid")

    def patch(self, request, id):
        try:
            staff_work_allotment = Staff_work_allotment.objects.get(id=id)
            serializer = Staff_work_allotment_Serializer(staff_work_allotment, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Staff_work_allotment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data=f"{id} not valid")


class E_Office_Account_Id_generate_View(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self, request):
        max_id = E_Office_Account.objects.aggregate(max_id=Max('id'))['max_id'] or 0
        next_id = max_id + 1
        return Response({'next_id': next_id}, status=status.HTTP_200_OK)


class E_Office_Account_View(APIView):
    # permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = E_Office_Account_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        e_office_account = E_Office_Account.objects.all()
        serializer = E_Office_Account_Serializer(e_office_account, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


class E_Office_Account_Detail_View(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request, id):
        try:
            e_office_account = E_Office_Account.objects.get(id=id)
            serializer = E_Office_Account_Serializer(e_office_account)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except E_Office_Account.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data=f"{id} not valid")

    def delete(self, request, id):
        try:
            e_office_account = E_Office_Account.objects.get(id=id)
            e_office_account.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except E_Office_Account.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data=f"{id} not valid")

    def patch(self, request, id):
        try:
            e_office_account = E_Office_Account.objects.get(id=id)
            serializer = E_Office_Account_Serializer(e_office_account, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except E_Office_Account.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data=f"{id} not valid")


class E_Office_File_Sanction_View(APIView):
    # permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = E_Office_File_Sanction_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        e_office_file_sanction = E_Office_File_Sanction.objects.all()
        serializer = E_Office_File_Sanction_Serializer(e_office_file_sanction, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


class E_Office_File_Sanction_Detail_View(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request, id):
        try:
            e_office_file_sanction = E_Office_File_Sanction.objects.get(id=id)
            serializer = E_Office_File_Sanction_Serializer(e_office_file_sanction)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except E_Office_File_Sanction.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data=f"{id} not valid")

    def delete(self, request, id):
        try:
            e_office_file_sanction = E_Office_File_Sanction.objects.get(id=id)
            e_office_file_sanction.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except E_Office_File_Sanction.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data=f"{id} not valid")

    def patch(self, request, id):
        try:
            e_office_file_sanction = E_Office_File_Sanction.objects.get(id=id)
            serializer = E_Office_File_Sanction_Serializer(e_office_file_sanction, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except E_Office_File_Sanction.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data=f"{id} not valid")


class Application_for_Affliation_View(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self, request):
        college = request.query_params.get('college', None)  
        if not college:
            return Response(data="Affliation college name is required", status=status.HTTP_400_BAD_REQUEST)
        college = Affiliated_Vocational_Training_College_Kerla.objects.filter(id=college).first()
        if college:
            serializer = Affiliated_Vocational_Training_College_Kerla_Serializer(college)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND, data=f"{college} not valid")

    def patch(self, request):
        college = request.data.get('college_id', None)  
        if not college:
            return Response(data="Affliation college_id is required", status=status.HTTP_400_BAD_REQUEST)
        try:
            college = Affiliated_Vocational_Training_College_Kerla.objects.get(id=college)
            serializer = Affiliated_Vocational_Training_College_Kerla_Serializer(college, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Affiliated_Vocational_Training_College_Kerla.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data=f"{college} not valid")


class Student_Certificate_Verification(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        registration_number = request.query_params.get('registration_number', None)  # Use query_params for GET

        if not registration_number:
            return Response(data="Registration number is required", status=status.HTTP_400_BAD_REQUEST)

        try:
            # Check in VTC_Course_Admission_Registration
            btc_query = VTC_Course_Admission_Registration.objects.get(registration_number=registration_number)
            serializer = VTC_Course_Admission_Registration_Serializer(btc_query)
        except VTC_Course_Admission_Registration.DoesNotExist:
            try:
                # Check in Admission_Registration
                add_on_query = Admission_Registration.objects.get(registration_number=registration_number)
                serializer = Admission_Registration_Serializer(add_on_query)
            except Admission_Registration.DoesNotExist:
                # Both queries failed
                return Response(data=f"{registration_number} not valid", status=status.HTTP_404_NOT_FOUND)

        # Fetch marklist and exam data
        marklist_query = Mark_List_Registration.objects.filter(registration_number=registration_number)
        marklist_serializer = Mark_List_Registration_Serializer(marklist_query, many=True)

        exam_query = Exam_Registration.objects.filter(registration_number=registration_number)
        exam_serializer = Exam_Registration_Serializer(exam_query, many=True)

        # Add additional data to the response
        response_data = serializer.data
        response_data['marklist'] = marklist_serializer.data
        response_data['exam'] = exam_serializer.data

        return Response(data=response_data, status=status.HTTP_200_OK)


class Student_Certificate_Verification_Detail_View(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request, id):
        try:
            # Check in VTC_Course_Admission_Registration
            btc_query = VTC_Course_Admission_Registration.objects.get(id=id)
            serializer = VTC_Course_Admission_Registration_Serializer(btc_query)
        except VTC_Course_Admission_Registration.DoesNotExist:
            try:
                # Check in Admission_Registration
                add_on_query = Admission_Registration.objects.get(id=id)
                serializer = Admission_Registration_Serializer(add_on_query)
            except Admission_Registration.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND, data=f"{id} not valid")

        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, id):
        try:
            # Check in VTC_Course_Admission_Registration
            btc_query = VTC_Course_Admission_Registration.objects.get(id=id)
            btc_query.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except VTC_Course_Admission_Registration.DoesNotExist:
            try:
                # Check in Admission_Registration
                add_on_query = Admission_Registration.objects.get(id=id)
                add_on_query.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            except Admission_Registration.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND, data=f"{id} not valid")

    def patch(self, request, id):
        try:
            # Check in VTC_Course_Admission_Registration
            btc_query = VTC_Course_Admission_Registration.objects.get(id=id)
            serializer = VTC_Course_Admission_Registration_Serializer(btc_query, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except VTC_Course_Admission_Registration.DoesNotExist:
            try:
                # Check in Admission_Registration
                add_on_query = Admission_Registration.objects.get(id=id)
                serializer = Admission_Registration_Serializer(add_on_query, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except Admission_Registration.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND, data=f"{id} not valid")



