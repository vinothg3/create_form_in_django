from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse

# Create your views here.
def studentdetail(request):
    sdo=student()
    d={'stud':sdo}
    if request.method=='POST':
        FD=student(request.POST)
        if FD.is_valid():
            return HttpResponse(str(FD.cleaned_data))
    return render(request,'studentdetail.html',d)