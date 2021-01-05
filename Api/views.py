from rest_framework import generics,mixins,permissions
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Sum,Avg,Count
from rest_framework.authentication import SessionAuthentication

from .models import Expense,Income
from .serializers import ExpenseSerializer,IncomeSerializer
from rest_framework.views import APIView

class ExpenseListView(generics.ListAPIView,mixins.CreateModelMixin):
    serializer_class = ExpenseSerializer
    def get_queryset(self):
        qs = Expense.objects.all().recent()
        return qs
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ExpenseByWeek(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [SessionAuthentication]
    def get(self,request):
        qs=Expense.objects.all().recent().by_weeks_range(weeks_ago=10,numbers_of_weeks=10)
        qs_exp=qs.filter(user=request.user)
        serializer=ExpenseSerializer(qs_exp,many=True)
        week_sum=qs_exp.aggregate(Sum('amount'))['amount__sum']
        return Response({'weekly_sum':week_sum if week_sum else 0,'objects':serializer.data})

#get the day expenses
class ExpenseByDay(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [SessionAuthentication]
    def get(self,request):
        qs=Expense.objects.all().recent()
        qs_exp = qs.filter(user=request.user).by_date()
        serializer = ExpenseSerializer(qs_exp, many=True)
        day_sum=qs_exp.aggregate(Sum('amount'))['amount__sum']
        return Response({'daily_sum':day_sum if day_sum else 0,'objects':serializer.data})

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class IncomeListView(APIView):
    def get(self,request):
        qs=Income.objects.all()
        income_qs = qs.filter(user=request.user)
        serializer=IncomeSerializer(income_qs,many=True)
        return Response(serializer.data)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)