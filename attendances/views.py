# coding: utf-8

# ////////////////////////////////////////////////////////////////////////// #
#
#  モジュールインポート
#
# ////////////////////////////////////////////////////////////////////////// #
import sys, os
sys.path.append(os.path.join('..', 'rakudasu_project'))
# ------------------------------
#  オリジナルモジュール
# ------------------------------
sys.path.append(os.path.join('..', 'lib'))
from lib import rakudasu_db
# ////////////////////////////////////////////////////////////////////////// #
#
#  Django モジュールインポート
#
# ////////////////////////////////////////////////////////////////////////// #
from rest_framework import generics, viewsets
from .models import Attendance
from .serializers import AttendanceSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view

# class AttendanceViewSet(viewsets.ModelViewSet):
class AttendanceList(generics.ListCreateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

    # GET
    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        employee_id = request.user.get_employee_id()
        user_fullname = request.user.get_full_name()
        queryset = self.get_queryset().filter(employee_id=employee_id)
        serializer = AttendanceSerializer(queryset, many=True)
        return Response(serializer.data)

    # POST
    def create(self, request):
        print('-'*60, 'POST request.','-'*60)
        employee_id = request.user.get_employee_id()
        if employee_id:
            to_RAKUDASU_flag = False
            # ========================================================================== #
            #  本家RAKUDASUに対する処理
            # ========================================================================== #
            try:
                rakudasu = rakudasu_db.Rakudasu(request)
                user_fullname = request.user.get_full_name()
                assert not rakudasu.get_userInfo()
                assert not rakudasu.check_info(user_fullname)
                assert not rakudasu.get_latestAttendanceId()
                assert not rakudasu.calculate_working_hours()
                assert not rakudasu.commit_data()
                to_RAKUDASU_flag = True
            except Exception as e:
                pass
            # ========================================================================== #
            #  Django Modelに対する処理
            # ========================================================================== #
            if to_RAKUDASU_flag:
                request_data = dict(request.data)
                request_data['employee_id'] = employee_id
                serializer = self.get_serializer(data=request_data)
                if serializer.is_valid():
                    self.object = serializer.save()
                    headers = self.get_success_headers(serializer.data)
                    return Response({
                        'result': 'Successed',
                        'message': 'Registration to the RAKUDASU and Django models are complete.',
                        'data': serializer.data
                    }, status=200, headers=headers)
                else:
                    return Response({
                        'result': 'Failed',
                        'message': 'Registration to RAKUDASU failed.',
                        'reason': serializer.errors
                    }, status=400)
            else:
                return Response({
                    'result': 'Failed',
                    'message': 'Your fullname is not registered. Please try after registering your first name and last name.',
                }, status=400)
        # ---------------------
        # employee_id 未登録
        # ---------------------
        else:
            return Response({
                'result': 'Failed',
                'message': 'Employee ID is not registered. Please try after registering your Employee ID.',
            }, status=400)

# class AttendanceViewSet(viewsets.ModelViewSet):
class AttendanceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

    # GET
    # def retrieve(self, request, pk):
    #     pass

    # PUT
    def update(self, request, pk):
        request_data = request.data
        request_data['user_id'] = request.user.id
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request_data)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response({
                'result': 'Successed',
                'message': 'The update of attendance information has been completed.',
                'data': serializer.data
            }, status=200)
        except:
            return Response({
                'result': 'Failed',
                'message': 'Failed to update attendance information.',
                'reason': serializer.errors
            }, status=400)

    # PATCH
    def partial_update(self, request, pk):
        return self.update(request, pk)

    # DELETE
    def destroy(self, request, pk):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            self.perform_destroy(instance)
            return Response({
                'result': 'Successed',
                'message': 'The deletion of attendance information has been completed.',
                'data': serializer.data
            }, status=200)
        except:
            return Response({
                'result': 'Failed',
                'message': 'Failed to delete attendance information.',
                'data': serializer.data
            }, status=400)
