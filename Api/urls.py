from django.conf.urls import url
from .views import ExpenseListView,IncomeListView,ExpenseByWeek,ExpenseByDay
urlpatterns = [
    url('list', ExpenseListView.as_view(), name='list-apis'),
    url('day', ExpenseByDay.as_view(), name='day-list-apis'),
    url('week',ExpenseByWeek.as_view(),name='week-list-apis'),
url('income',IncomeListView.as_view(),name='amount-apis'),
 # url(r'updates/(?P<id>[\w-]+)/$', ExpenseUpdate.as_view(), name='update-apis'),

]