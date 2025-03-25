from rest_framework import viewsets, permissions
from .models import Item
from .serializers import ItemSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

# tests.py
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Item