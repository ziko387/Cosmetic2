from django.shortcuts import render

# Create your views here.

def Dashboard(request):
    return render(request, 'cosmeticApp/userDashboard.html')

def AdminDashboard(request):
    return render(request, 'cosmeticApp/Admin.html')

def register(request):
    return render(request, 'cosmeticApp/regestretion.html')

def login(request):
    return render(request, 'cosmeticApp/loginpage.html')

def addCart(request):
    return render(request, 'cosmeticApp/addcart.html')

def confirPayment(request):
    return render(request, 'cosmeticApp/confirmedpayment.html') 

def processedPayment(request):
    return render(request, 'cosmeticApp/processedpayment.html') 

def failledPayment(request):
    return render(request, 'cosmeticApp/faiiledpayment.html')

def intro(request):
    return render(request, 'cosmeticApp/intro.html')

def paymentMethod(request):
    return render(request, 'cosmeticApp/paymentMethod.html')

def forgotPassword(request):
    return render(request, 'cosmeticApp/forgotpassword.html')

def resetPassword(request):
    return render(request, 'cosmeticApp/changepassword.html')

def processedEmail(request):
    return render(request, 'cosmeticApp/processedEmail.html')






    

