from django.http import HttpResponse
from django.shortcuts import render
from .forms import Myform


# Create your views here.
def people(request):
    if request.method == "POST":
        myform = Myform(request.POST)
        print("in post",myform)
        # myform.y = request.GET.get("hidden")
        if myform.is_valid():
            print("valid-------------------------")
        # print("this is the hidden input", request.POST["hidden"])
        return HttpResponse("sdff")
    else:
        myform = Myform(data=request.GET)
        print("--------------------",myform)
        return render(request, "peopel.html",context={"form":myform})
