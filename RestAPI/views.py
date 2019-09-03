from __future__ import unicode_literals
# from django.shortcuts import render
from .models import Trade, User
from rest_framework import viewsets
from .serializers import UserSerializer, TradeSerializer
from rest_framework.decorators import action


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def destroy(self, request, *args, **kwargs):
        return super(UserViewSet, self).destroy(request, *args, **kwargs)

    def dispatch(self, *args, **kwargs):
        return super(UserViewSet, self).dispatch(*args, **kwargs)


class TradeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Trades to be viewed or edited.
    """
    queryset = Trade.objects.all()
    serializer_class = TradeSerializer

    @action(methods=['delete'], detail=False)
    def erase(self, request):
        Trade.objects.all().delete

    def dispatch(self, *args, **kwargs):
        return super(TradeViewSet, self).dispatch(*args, **kwargs)