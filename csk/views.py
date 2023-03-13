from django.shortcuts import render

# Create your views here.
def dhoni(request):
    d={'NAME':'Vinod','age':20}
    return render(request,'dhoni.html',context=d)
