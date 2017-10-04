from django.shortcuts import render
from django.views import generic
from django.utils import timezone

from .models import Expense


class IndexView(generic.ListView):
    """
    представление главной страницы
    1. необходимо переопределить template_name
    2. context_object_name - с ним мы потом будем в шаблоне работать
    3. Define IndexView.model, IndexView.queryset,
       or override IndexView.get_queryset().
    про это тоже не стоит забывать
    """
    template_name = 'budget/index.html'
    context_object_name = 'expenses_list'
    model = Expense


class NewExpenseView(generic.CreateView):
    """
    представление для создания новой записи
    """
    model = Expense
    template_name = 'budget/new_expense.html'
    fields = ['date', 'cost', 'category', 'comment']