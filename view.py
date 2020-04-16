from  django.https import HttpRonse



def login(request,num):


	num += 1
	return num



def index(request):



	return HttpResponse('index')
