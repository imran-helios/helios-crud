from crud.models import Registration
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
import io
from rest_framework.parsers import JSONParser
from .serializers import StudentSerializer
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from rest_framework.generics import CreateAPIView,ListAPIView,UpdateAPIView,RetrieveAPIView, DestroyAPIView


class StudentList(ListAPIView):
    serializer_class = StudentSerializer
    queryset = Registration.objects.all()

class StudentDetails(RetrieveAPIView):
    serializer_class = StudentSerializer
    queryset = Registration.objects.all()
    lookup_field = 'pk'

class CreateStudent(CreateAPIView):
    serializer_class = StudentSerializer
    queryset = Registration.objects.all()

class UpdateStudent(UpdateAPIView):
    serializer_class = StudentSerializer
    queryset = Registration.objects.all()
    lookup_field = 'pk'


class DeleteStudent(DestroyAPIView):
    serializer_class = StudentSerializer
    queryset = Registration.objects.all()
    lookup_field = 'pk'

# def student_detail(request, pk):
#     stu = Registration.objects.get(id = pk)
#     serialazer = StudentSerializer(stu)
#     # json_data = JSONRenderer().render(serialazer.data)
#     # return HttpResponse(json_data, {'msg': 'Data Created'}, content_type = 'application/json')
#     return JsonResponse(serialazer.data)

## Queryset ALl Student Data
# def student_list(request):
#     stu = Registration.objects.all()
#     serialazer = StudentSerializer(stu, many=True)
#     # json_data = JSONRenderer().render(serialazer.data)
#     # return HttpResponse(json_data, content_type = 'application/json')
#     return JsonResponse(serialazer.data, safe = False)

## Create Function
# @csrf_exempt
# def create_student(request):
#     if request.method == "POST":
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         serializer = StudentSerializer(data = pythondata)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg': 'Data Created'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type = 'application/json')
#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data, content_type = 'application/json')

# ## Update Function
# def update_student(request):
#     if request.method == "POST":
#         json_data = request.body
#         strem = io.BytesIO(json_data)
#         pythodata = JSONParser().parse(strem)
#         id = pythodata.get('id')
#         stu = Registration.objects.get(id = id)
#         serializer = StudentSerializer(stu, partial = True)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg':'Data Updated !!'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type = 'application/json')
#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data, content_type = 'application/json')

# ## Delete Function
# def delete_student(request):
#     if request.method == "DELETE":
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         id = pythondata.get('id')
#         stu = Registration.objects.get(id = id)
#         stu.delete()
#         res = {'msg': 'Data Deleted !!'}
#         # json_data = JSONRenderer().render(res)
#         # return HttpResponse(json_data, content_type = 'application/json')
#         return JsonResponse(res, safe = False)
