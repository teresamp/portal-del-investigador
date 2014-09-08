# -*- encoding: UTF-8 -*-

from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    context = {}
    return render(request, 'accounting/base.html', context)
