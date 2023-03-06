from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import LimitOffsetPagination

from .serializers import *
from .models import Thread, Message
from django.contrib.auth.models import User


class CreateThread(APIView):

    """Create a new message thread"""

    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        try:
            thread = Thread.objects.get(participants=request.data.get('participants'))
            serializer = ThreadSerializer(thread)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Thread.DoesNotExist:
            serializer = ThreadSerializer(data=request.data)
            if serializer.is_valid():
                thread_instance = serializer.save()
                for participant in request.data.get('participants'):
                    user_id = User.objects.get(id=int(participant))
                    thread_instance.participants.add(user_id)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class DeleteThread(APIView):

    """Delete a message thread"""

    permission_classes = (IsAuthenticated,)

    def delete(self, request, pk, format=None):
        thread = get_object_or_404(Thread.objects.all(), pk=pk)
        thread.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class GetAllThreadByUser(APIView, LimitOffsetPagination):

    """Get all threads for a user"""

    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        try:
            threads = Thread.objects.filter(participants=request.user)
            result_page = self.paginate_queryset(threads, request)
            serializer = GetAllThreadSerializer(result_page, many=True)
            return self.get_paginated_response(serializer.data)
        except User.DoesNotExist:
            return Response({'detail': 'User does not exist!'})


class CreateNewMessage(APIView):

    """Create a new message to send"""

    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetMessageForThread(APIView, LimitOffsetPagination):

    """Get all messages for a specific thread"""

    permission_classes = (IsAuthenticated,)

    def get(self, request, pk, format=None):
        try:

            thread_instance = Thread.objects.get(pk=pk)
            messages = Message.objects.filter(thread=thread_instance)
            result = self.paginate_queryset(messages, request)
            serializer = MessageSerializer(result, many=True)
            return self.get_paginated_response(serializer.data)
        except Thread.DoesNotExist:
            return Response({'detail': 'Thread does not exist!'})
        

class GetCountUnreadMessageForUser(APIView):

    """Get the number of unread messages by user"""

    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        thread = Thread.objects.filter(participants=request.user)
        messages = Message.objects.filter(thread__in=thread, is_read=False)
        return Response({'count_unread_messages': messages.count()})


class MarkReadMessage(APIView):

    """Mark read sms or several sms"""

    permission_classes = (IsAuthenticated,)

    def put(self, request, pk, format=None):
        try:
            message = Message.objects.get(pk=pk, sender=request.user.id)
            message.is_read = request.data.get('is_read', message.is_read)
            message.save()
            serializer = MessageSerializer(message)
            return Response(serializer.data)
        except Message.DoesNotExist:
            return Response({'detail': 'Message does not exist'})

