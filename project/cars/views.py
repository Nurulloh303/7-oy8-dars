from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status, generics, permissions, viewsets
from .permissions import MyPermission
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication



from .models import Car, Owner, Color
from .serializers import CarSerializer, OwnerSerializer, ColorSerializer


class CarApiView(viewsets.ModelViewSet):
    # queryset = Car.objects.order_by('-id')

    serializer_class = CarSerializer

    permission_classes = [permissions.IsAuthenticated]

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['name', 'color']
    search_fields = ['name', 'brand']
    ordering_fields = ['name', 'price']

    def get_queryset(self):
        return Car.objects.all()





# class CarDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Car.objects.all()
#     serializer_class = CarSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly, permissions.IsAdminUser)


class OwnerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    # queryset = Owner.objects.all()

    serializer_class = OwnerSerializer

    # permission_classes = (permissions.IsAdminUser)
    
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    django_filters = ['first_name']
    search_fields = ['first_name', 'phone_number']
    ordering_fields = ['first_name', 'age']




    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Owner.objects.all()
        else:
            return Owner.objects.filter(user=user)

class ColorDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
    permission_classes = (permissions.IsAdminUser)
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    django_filters = ['name']
    search_fields = ['name']
    ordering_fields = ['name']



#
# class CarAPIView(APIView):
#     def get(self, request:Request, pk: int = None):
#         if not pk:
#             cars = Car.objects.all()
#             serializer = CarSerializer(cars, many=True)
#             return Response(serializer.data)
#         else:
#             try:
#                 car = Car.objects.get(pk=pk)
#                 serializer = CarSerializer(car, many=False)
#                 return Response(serializer.data)
#             except Exception as e:
#                 return Response({"mesages": "Car not found"}, status=status.HTTP_404_NOT_FOUND)
#
#     def post(self, request:Request, pk: int = None):
#         if pk:
#             return Response({"messages": "Method POST not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
#         else:
#             serializer = CarSerializer(data=request.data)
#             serializer.is_valid(raise_exception=True)
#             car = serializer.save()
#             return Response(CarSerializer(car).data, status=status.HTTP_201_CREATED)
#
#     def put(self, request:Request, pk: int = None):
#         if pk:
#             return Response({"messages": f"Method {request.method} not alloowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
#         else:
#             try:
#                 car = Car.objects.get(pk=pk)
#             except Exception as e:
#                 return Response({"mesages": "Car not found"}, status=status.HTTP_404_NOT_FOUND)
#
#             serializer = CarSerializer(car, data=request.data, partial=True if request.method == 'PATCH' else False)
#             serializer.is_valid(raise_exception=True)
#             car = serializer.save()
#             return Response(CarSerializer(car).data, status=status.HTTP_200_OK)
#
#     def patch(self, request:Request, pk: int = None):
#         return self.put(request, pk)
#
#     def delete(self, request:Request, pk: int = None):
#         if not pk:
#             return Response({"messages": f"Method DELETE not alloowed"},
#                             status=status.HTTP_405_METHOD_NOT_ALLOWED)
#         else:
#             try:
#                 car = Car.objects.get(pk=pk)
#             except Exception as e:
#                 return Response({"mesages": "Car not found"}, status=status.HTTP_404_NOT_FOUND)
#
#             car.delete()
#             return Response({"messages": "Cars delete"}, status=status.HTTP_200_OK)
#
#
# class OwnerAPIView(APIView):
#     def get(self, requset:Request, pk: int = None):
#         if not pk:
#             owners = Owner.objects.all()
#             serializer = OwnerSerializer(owners, many=True)
#             return Response(serializer.data)
#         else:
#             try:
#                 owner = Owner.objects.get(pk=pk)
#                 serializer = OwnerSerializer(owner, many=False)
#                 return Response(serializer.data)
#             except Exception as e:
#                 return Response({"mesages": "Owner not found"}, status=status.HTTP_404_NOT_FOUND)
#
#     def post(self, request:Request, pk: int = None):
#         if pk:
#             return Response({"messages": "Method POST not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
#         else:
#             serializer = OwnerSerializer(data=request.data)
#             serializer.is_valid(raise_exception=True)
#             owner = serializer.save()
#             return Response(OwnerSerializer(owner).data, status=status.HTTP_201_CREATED)
#
#     def put(self, request:Request, pk: int = None):
#         if pk:
#             return Response({"messages": f"Method {request.method} not alloowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
#         else:
#             try:
#                 owner = Owner.objects.get(pk=pk)
#             except Exception as e:
#                 return Response({"mesages": "Owner not found"}, status=status.HTTP_404_NOT_FOUND)
#
#             serializer = OwnerSerializer(owner, data=request.data, partial=True if request.method == 'PATCH' else False)
#             serializer.is_valid(raise_exception=True)
#             owner = serializer.save()
#             return Response(OwnerSerializer(owner).data, status=status.HTTP_200_OK)
#
#     def patch(self, request:Request, pk: int = None):
#         return self.put(request, pk)
#
#     def delete(self, request:Request, pk: int = None):
#         if not pk:
#             return Response({"messages": f"Method DELETE not alloowed"},
#                             status=status.HTTP_405_METHOD_NOT_ALLOWED)
#         else:
#             try:
#                 owner = Owner.objects.get(pk=pk)
#             except Exception as e:
#                 return Response({"mesages": "Owner not found"}, status=status.HTTP_404_NOT_FOUND)
#
#             owner.delete()
#             return Response({"messages": "Owner delete"}, status=status.HTTP_200_OK)
#
#
# class CarCreateAPIView(generics.CreateAPIView):
#     queryset = Car.objects.all()
#     serializer_class = CarSerializer
#
# class OwnerCreateAPIView(generics.CreateAPIView):
#     queryset = Owner.objects.all()
#     serializer_class = OwnerSerializer