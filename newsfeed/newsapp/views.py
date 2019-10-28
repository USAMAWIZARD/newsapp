from django.shortcuts import render,redirect
from .models import user,admin
from django.shortcuts import render_to_response
from django.template import RequestContext
import os
def getUserIntrustedPage(requser):
	#obj = user.objects.filter(name=requser)
	listofuserinterst=user.objects.values_list('selectedfields', flat=True).get(name=requser)
	print(listofuserinterst)
	listofuserinterst=res = listofuserinterst.strip("']['").split(', ') 
	allintrestedpagedic={}
	for interst in listofuserinterst:		
		allintrestedpagedic[interst]=os.listdir("C:/Users/USAMAWIZARD/Desktop/New folder/newsfeed/newsapp/templates/"+ interst.replace("'",""))
	print(allintrestedpagedic)
	return allintrestedpagedic
def getallcatfunc():
	adminobj=admin()
	getallcat=list(admin.objects.values_list('availablecat',flat=True))
	return getallcat
def signup(request):
	return render(request,"signup.html",{'allcat':getallcatfunc()})
def signin(request):
	return render(request,"signin.html")
def signupdata(request):
	userobj=user()
	#print(request.POST.getlist('selectedfields'))
	userobj.name=request.POST['name']
	userobj.selectedfields=request.POST.getlist('selectedfields') 
	userobj.save()
	userintrustedpages=getUserIntrustedPage(request.POST['name'])
	print("last me ho mai")
	return render(request,'UserIntrustedPage.html/',{'userintrustedpages':userintrustedpages})
def admincontroll(request):
	return render(request,"admincontroll.html",{'allcat':getallcatfunc()})
def addcat(request):
	adminobj=admin()
	#list(admin.objects.values_list('availablecat',flat=True))
	#lis.append(request.POST['addcat'])
	adminobj.availablecat=request.POST['addcat']
	os.mkdir("C:\\Users\\USAMAWIZARD\\Desktop\\New folder\\newsfeed\\newsapp\\templates\\"+ request.POST['addcat'])
	adminobj.save()
	#print(lis)
	return render(request,"admincontroll.html")