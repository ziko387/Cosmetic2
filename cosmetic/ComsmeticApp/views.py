from django.shortcuts import render
from.forms import CosmeticItemForm, OrderForm, UserRegistrationForm
from django.contrib import messages



# Create your views here.

def Dashboard(request):
    return render(request, 'cosmeticApp/userDashboard.html')

def AdminDashboard(request):
    return render(request, 'cosmeticApp/Admin.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'cosmeticApp/userDashboard.html')
    else:
        form = UserRegistrationForm()
    return render(request, 'cosmeticApp/regestretion.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Here you would typically check the credentials against the database
        if username and password:  # Simplified check for demonstration
            return render(request, 'cosmeticApp/userDashboard.html')
    else:
        messages.error(request, 'Invalid username or password')
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






    

