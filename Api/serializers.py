from rest_framework import serializers
from .models import Expense,Income


class ExpenseSerializer(serializers.ModelSerializer):

    class Meta:
        model=Expense
        fields=['id', 'item','amount']
        read_only_field=['user']


class IncomeSerializer(serializers.ModelSerializer):

    class Meta:
        model=Income
        fields=['income_amount']
        read_only_field=['user']