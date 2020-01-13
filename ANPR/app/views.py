from django.shortcuts import render
from django.utils import timezone
from .models import resident

def post_list(request):
	#resident = resident.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'app/post_list.html', {'resident': resident.objects.all})