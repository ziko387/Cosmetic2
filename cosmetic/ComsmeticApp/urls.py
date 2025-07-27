from django.urls import path
from.import views

urlpatterns = [
    path('',views.intro, name='intro'),
    path('dashboard/', views.Dashboard, name='dashboard'),
    path('adminDashboard/', views.AdminDashboard, name='adminDashboard'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('addCart/', views.addCart, name='addCart'),
    path('confirmPayment/', views.confirPayment, name='confirmPayment'),
    path('processedPayment/', views.processedPayment, name='processedPayment'),
    path('failedPayment/', views.failledPayment, name='failedPayment'),
    path('paymentMethod/', views.paymentMethod, name='paymentMethod'),
    path('forgotPassword/', views.forgotPassword, name='forgotPassword'),
    path('resetPassword/', views.resetPassword, name='resetPassword'),
    path('processedEmail/', views.processedEmail, name='processedEmail'),
]