from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from .models import Ask


@login_required
def ask_list(request):
    asks = Ask.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'diary/ask_list.html', {'asks': asks})
