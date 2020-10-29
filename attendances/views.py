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
        queryset = self.get_queryset().filter(user_id=request.user.id)
        serializer = AttendanceSerializer(queryset, many=True)
        return Response(serializer.data)

    # POST
    def create(self, request):
        request_data = request.data
        request_data['user_id'] = request.user.id
        serializer = self.get_serializer(data=request_data)
        if serializer.is_valid():
            self.object = serializer.save()
            headers = self.get_success_headers(serializer.data)
            return Response({
                'result': 'Successed',
                'message': 'Registration to the RAKUDASU is complete.',
                'data': serializer.data
            }, status=200, headers=headers)
        else:
            return Response({
                'result': 'Failed',
                'message': 'Registration to RAKUDASU failed.',
                'Reason': serializer.errors
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
                'Reason': serializer.errors
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
