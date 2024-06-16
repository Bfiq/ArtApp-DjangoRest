from .serializers import UserSerializer, BoardSerializer, PinSerializer, BoardPinSerializer, TagSerializer, PinTagSerializer
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .models import Board, Pin, BoardPin, Tag, PinTag

# Create your views here.
class UserRegistration(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class BoardsView(APIView):
    def get(self, request):
        boards = Board.objects.all()
        serializer = BoardSerializer(boards, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BoardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk):
        board = get_object_or_404(Board, pk=pk)
        serializer = BoardSerializer(board, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        board = get_object_or_404(Board, pk=pk)
        serializer = BoardSerializer(board, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        board = get_object_or_404(Board, pk=pk)
        board.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PinView(APIView):
    def get(self, request):
        pins = Pin.objects.all()
        serializer = PinSerializer(pins, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PinSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        pin = get_object_or_404(Pin, pk=pk)
        serializer = PinSerializer(pin, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        pin = get_object_or_404(Pin, pk=pk)
        serializer = PinSerializer(pin, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
class BoardPinView(APIView):
    def get(self, request):
        boardPin = BoardPin.objects.all()
        serializer = BoardPinSerializer(boardPin, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = BoardPinSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk):
        boardPin = get_object_or_404(BoardPin, pk=pk)
        serializer = BoardPinSerializer(boardPin, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        boardPin = get_object_or_404(BoardPin, pk=pk)
        serializer = BoardPinSerializer(boardPin, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

#Creado por lista generica
class TagView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class PinTagView(generics.ListCreateAPIView):
    queryset = PinTag.objects.all()
    serializer_class = PinTagSerializer
