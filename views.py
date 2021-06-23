from django.shortcuts import render
from . import ml_predict


def welcome(request):
    return render(request,'front.html')


def home(request):
    return render(request,'index.html')

def result(request):
    Present_Price=float(request.GET['Present_Price'])
    Kms_Driven=int(request.GET['Kms_Driven'])
    Owner=int(request.GET['Owner'])
    no_year=int(request.GET['no_year'])
    Fuel_Type_Petrol=request.GET['Fuel_Type_Petrol']
    Seller_Type_Individual=request.GET['Seller_Type_Individual']
    Transmission_Mannual=request.GET['Transmission_Mannual']

    no_year=2021-no_year 

    if (Fuel_Type_Petrol=='petrol'):
        Fuel_Type_Petrol=1
        Fuel_Type_Diesel=0
    else:
        Fuel_Type_Petrol=0
        Fuel_Type_Diesel=1


    if Seller_Type_Individual=='individual':
        Seller_Type_Individual=1
        Seller_Type_Dealer=0
    else:
        Seller_Type_Individual=0
        Seller_Type_Dealer=1

    if Transmission_Mannual=='Mannual':
        Transmission_Mannual=0
        Transmission_Automatic=1
    else:
        Transmission_Mannual=0
        Transmission_Automatic=1


    pred1=ml_predict.prediction(Present_Price,Kms_Driven,Owner,no_year,Fuel_Type_Diesel,Fuel_Type_Petrol,Seller_Type_Dealer,Seller_Type_Individual,Transmission_Automatic,Transmission_Mannual)
    return render(request,'result.html',{"pred1":pred1})