from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from .models import Model
from datetime import datetime,date
from dateutil import relativedelta

# Create your views here.


def cal(request,rate=None,data=False):
    if request.method == 'POST':
        data = request.POST
        print("*****************************************")
        start =data['start']
        end= data['end']
        y1,m1,d1=list(map(int,start.split("-")))
        y,m,d=list(map(int,end.split("-")))
        print(y1,m1,d1)
        print(y,m,d)

        date_1 = date(y1,m1,d1)
        date_2 = date(y,m,d)
        # total_days between two years
        Total_days = (date_2 - date_1).days
        # Get the interval between two dates
        diff = relativedelta.relativedelta(date_2, date_1)
        print('Difference between dates in years: ', diff.years)
        print(f"Complete Difference between two dates: \n {diff.years}  years , {diff.months} months and  {diff.days}  days")

        year = int(diff.years)
        months = int(diff.months)
        days = int(diff.days)
        principal=int(data['Principal']) 
        print(request.POST)  

        r =request.POST.get('rate')
        rate_ = 2 if principal > 5000 else 3
        rate = rate_ if r=='0' else int(r)
        print(data,type(r))
        print("----------------",rate,type(rate))
        if Total_days <= 360:
            if principal <= 4999:                  
                Interest_Rate_Per_Month = (principal/100)*rate
                print(Interest_Rate_Per_Month,"----------------",rate)
                Interest_Rate_for_Months = Interest_Rate_Per_Month * months
                print(Interest_Rate_for_Months)
                Interest_Rate_for_Days = (Interest_Rate_Per_Month/30) * days                    
                print(Interest_Rate_for_Days)

                Interest_amount=Interest_Rate_for_Months+Interest_Rate_for_Days
                print(Interest_amount)
                print(Interest_amount+principal,"lesss than 5")
            else:                              
                Interest_Rate_Per_Month = (principal/100)*rate
                print(Interest_Rate_Per_Month,"----------------",rate)
                Interest_Rate_for_Months = Interest_Rate_Per_Month * months
                print(Interest_Rate_for_Months)
                Interest_Rate_for_Days = (Interest_Rate_Per_Month/30) * days
                print(Interest_Rate_for_Days)

                Interest_amount=Interest_Rate_for_Months+Interest_Rate_for_Days
                print(Interest_amount+principal,"gretr than 5")
        else:
            
            if principal >= 5000:  
                print("____",rate,"eeeeeeeeeeee",principal)
                Interest_Rate_Per_Month = (principal/100) * rate 
                print(Interest_Rate_Per_Month)
                Interest_Rate_of_Month = Interest_Rate_Per_Month * (year*12)
                print(Interest_Rate_of_Month)
                new_principle_Per_Year = principal + Interest_Rate_of_Month
                print(new_principle_Per_Year)
                # total of rest year
                Interest_Rate_Per_Month_2 = (new_principle_Per_Year/100)*rate
                print(Interest_Rate_Per_Month_2)
                Interest_Rate_of_Month_2 = Interest_Rate_Per_Month_2 * months
                print(Interest_Rate_of_Month_2)
                Interest_Rate_for_Days = (Interest_Rate_Per_Month_2/30) * days                    
                print(Interest_Rate_for_Days)                

                Interest_amount =  Interest_Rate_of_Month_2 +Interest_Rate_for_Days
                total =principal+Interest_amount
                
                print("Interest_amount", Interest_amount,'---------comp /less than 5")----------------',total)
            else:
                print("____",rate,"hhhhhhhhhhhhhhhh")
                Interest_Rate_Per_Month = (principal/100) * rate 
                print(Interest_Rate_Per_Month)
                Interest_Rate_of_Month = Interest_Rate_Per_Month * (year*12)
                print(Interest_Rate_of_Month)
                new_principle_Per_Year = principal + Interest_Rate_of_Month
                print(new_principle_Per_Year)
                # total of rest year
                Interest_Rate_Per_Month_2 = (new_principle_Per_Year/100)*rate
                print(Interest_Rate_Per_Month_2)
                Interest_Rate_of_Month_2 = Interest_Rate_Per_Month_2 * months
                print(Interest_Rate_of_Month_2)
                Interest_Rate_for_Days = (Interest_Rate_Per_Month_2/30) * days                    
                print(Interest_Rate_for_Days)                

                Interest_amount =  Interest_Rate_of_Month_2 +Interest_Rate_for_Days
                total =principal+Interest_amount                
                print("Interest_amount", Interest_amount,total)
                print(Interest_amount+principal,"lesss than 5",'------------------------------comp/grtr ',type(Interest_amount))
        # except:
        #     pass 
        model = Model.objects.create(start_date=data['start'],end_date=data['end'],principal=data['Principal'],interest=Interest_amount)
        model.save()
        data = True
        obj=Model.objects.all().order_by('-id')
        print(obj)
        context ={'model':obj,'data':data}
        return render(request,'cal.html',context )
    return render(request,'cal.html',{'data':data})
