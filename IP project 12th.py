#PROJECT
import pandas as pd
import matplotlib.pyplot as mp
print()
def book_MtoD():
    print('1. Mumbai to New Delhi')
    print('2. New Delhi to Mumbai')
    opt1=input('Choose the one among the above [1,2]:')
    if opt1=='1':
        df=pd.read_csv("E:\Projects\Python project\Data for project (12th).csv",skiprows=21,nrows=20,names=['Flight no.','Airline','From-To','Departure Time','Arrival Time','Fare','Seats Available'],sep=',')
        print(df)
        S1=list(df.Airline.unique())
        S2=list(df.Fare.unique())
        opt21=input('Do you want to see the graph for airline vs fare [y/n]:')
        if opt21=='y':
            mp.bar(S1,S2,width=0.4,color='cyan')
            mp.xlabel('Airline')
            mp.ylabel('Fare')
            mp.title('Airline VS Fare')
            mp.show()
        print('Insert the flight no. through which you want to travel: ')
        flt=input('-->')
        a=pd.DataFrame(df[df['Flight no.']==flt])
        print(a)
        s_av=(a.iat[0,6])
        opt2=int(input('How many tickets you want to book: '))
        if ((s_av==opt2) or (s_av>opt2)):
            name=[]
            age=[]
            gender=[]
            phone=[]
            for i in range(1,opt2+1):
                print('Passenger',i,'Name:')
                p_name=input('-->')
                print('Passenger',i,'Age:')
                p_age=int(input('-->'))
                print('Passenger',i,'Gender [M/F/O]:')
                p_gen=input('-->')
                print('Passenger',i,'Phone no.:')
                p_phone=int(input('-->'))
                print()
                name.append(p_name)
                age.append(p_age)
                gender.append(p_gen)
                phone.append(p_phone)
            data={'Passenger Name':name,'Passenger Age':age,'Passenger Gender':gender,'Passenger Phone no.':phone}
            df1=pd.DataFrame(data)
            print(df1)
            df1.to_csv("E:\Projects\Python project\P_info.csv")
            print()
            print()
            print('     Payment Summary')
            print()
            fare_perperson=(a.iat[0,5])
            totalfare=(a.iat[0,5])*opt2
            gst=((18/100)*totalfare)
            data1=[fare_perperson,totalfare,gst,(totalfare+gst)]
            payment_data={'Price':data1}
            df2=pd.DataFrame(payment_data,index=['Fare per person','Base Fare','Taxes','Total Fare'])
            print(df2)
            print()
            print('Payment Options')
            print('1. Credit Card')
            print('2. Debit Card')
            print('3. UPI')
            opt3=input('How do you want to make your payment [1/2/3]:')
            if opt3=='1':
                credit_cardno=input('Enter credit card number:')
                exp_date=input('Enter expiry date of your card [MM/YYYY]:')
                cvv=input('Enter CVV:')
                otp=input('Enter the otp received:')
                print()
                print('Your payment is successful.')
                print('Your tickets are booked.')
            elif opt3=='2':
                debit_cardno=input('Enter debit card number:')
                exp_date_d=input('Enter expiry date of your card [MM/YYYY]:')
                cvv_d=input('Enter CVV:')
                otp_d=input('Enter the otp received:')
                print()
                print('Your payment is successful.')
                print('Your tickets are booked.')
            elif opt3=='3':
                upi=input('Enter UPI:')
                print('Accept the notification received on your UPI to proceed.')
                print()
                print('Your payment is successful.')
                print('Your tickets are booked.')
            else:
                print('Invalid input. Try again.')
            j=input('Do you want to see your ticket[y/n]:')
            if j=='y':
                for i in range(1,opt2+1):
                    t_airline=i*(list(a['Airline']))
                    t_dtime=i*(list(a['Departure Time']))
                    t_atime=i*(list(a['Arrival Time']))
                    t_FT=i*(list(a['From-To']))
                data16={'Passenger Name':name,'Airline':t_airline,'From-To':t_FT,'Arrival':t_atime,'Departure':t_dtime}
                df24=pd.DataFrame(data16)
                print(df24)
            else:
                print('OK')
        else:
            print('Number of seats you want to book are not available')
            print('Try to check in other flights')
    elif opt1=='2':
        df3=pd.read_csv("E:\Projects\Python project\Data for project (12th).csv",nrows=20,skiprows=1,names=['Flight no.','Airline','From-To','Departure Time','Arrival Time','Fare','Seats Available'])
        print(df3)
        S3=list(df3.Airline.unique())
        S4=list(df3.Fare.unique())
        opt22=input('Do you want to see the graph for airline vs fare [y/n]:')
        if opt22=='y':
            mp.bar(S3,S4,width=0.4,color='cyan')
            mp.xlabel('Airline')
            mp.ylabel('Fare')
            mp.title('Airline VS Fare')
            mp.show()
        print('Insert the flight no. through which you want to travel: ')
        flt1=input('-->')
        b=pd.DataFrame(df3[df3['Flight no.']==flt1])
        print(b)
        s_av1=(b.iat[0,6])
        opt4=int(input('How many tickets you want to book: '))
        if ((s_av1==opt4) or (s_av1>opt4)):
            name1=[]
            age1=[]
            gender1=[]
            phone1=[]
            for i in range(1,opt4+1):
                print('Passenger',i,'Name:')
                p_name1=input('-->')
                print('Passenger',i,'Age:')
                p_age1=input('-->')
                print('Passenger',i,'Gender [M/F/O]:')
                p_gen1=input('-->')
                print('Passenger',i,'Phone no.:')
                p_phone1=input('-->')
                print()
                name1.append(p_name1)
                age1.append(p_age1)
                gender1.append(p_gen1)
                phone1.append(p_phone1)
            data2={'Passenger Name':name1,'Passenger Age':age1,'Passenger Gender':gender1,'Passenger Phone no.':phone1}
            df4=pd.DataFrame(data2)
            print(df4)
            df4.to_csv("E:\Projects\Python project\P_info.csv")
            print()
            print()
            print('     Payment Summary')
            print()
            fare_perperson1=(b.iat[0,5])
            totalfare1=(b.iat[0,5])*opt4
            gst1=((18/100)*totalfare1)
            data3=[fare_perperson1,totalfare1,gst1,(totalfare1+gst1)]
            payment_data1={'Price':data3}
            df5=pd.DataFrame(payment_data1,index=['Fare per person','Base Fare','Taxes','Total Fare'])
            print(df5)
            print()
            print('Payment Options')
            print('1. Credit Card')
            print('2. Debit Card')
            print('3. UPI')
            opt5=input('How do you want to make your payment [1/2/3]:')
            if opt5=='1':
                credit_cardno1=input('Enter credit card number:')
                exp_date1=input('Enter expiry date of your card [MM/YYYY]:')
                cvv1=input('Enter CVV:')
                otp1=input('Enter the otp received:')
                print()
                print('Your payment is successful.')
                print('Your tickets are booked.')
            elif opt5=='2':
                debit_cardno1=input('Enter debit card number:')
                exp_date_d1=input('Enter expiry date of your card [MM/YYYY]:')
                cvv_d1=input('Enter CVV:')
                otp_d1=input('Enter the otp received:')
                print()
                print('Your payment is successful.')
                print('Your tickets are booked.')
            elif opt5=='3':
                upi1=input('Enter UPI:')
                print('Accept the notification received on your UPI to proceed.')
                print()
                print('Your payment is successful.')
                print('Your tickets are booked.')
            else:
                print('Invalid input. Try again.')
            k=input('Do you want to see your ticket[y/n]:')
            if k=='y':
                for i in range(1,opt4+1):
                    t_airline1=i*(list(b['Airline']))
                    t_dtime1=i*(list(b['Departure Time']))
                    t_atime1=i*(list(b['Arrival Time']))
                    t_FT1=i*(list(b['From-To']))
                data17={'Passenger Name':name1,'Airline':t_airline1,'From-To':t_FT1,'Arrival':t_atime1,'Departure':t_dtime1}
                df25=pd.DataFrame(data17)
                print(df25)
            else:
                print('OK')
        else:
            print('Number of seats you want to book are not available')
            print('Try to check in other flights')
    else:
        print('Invalid input. Try again.')

def book_BtoK():
    print('1. Bangalore to Kolkata')
    print('2. Kolkata to Bangalore')
    opt6=input('Choose the one among the above [1,2]:')
    if opt6=='1':
        df6=pd.read_csv("E:\Projects\Python project\Data for project (12th).csv",nrows=15,skiprows=41,names=['Flight no.','Airline','From-To','Departure Time','Arrival Time','Fare','Seats Available'])
        print(df6)
        S5=list(df6.Airline.unique())
        S6=list(df6.Fare.unique())
        opt23=input('Do you want to see the graph for airline vs fare [y/n]:')
        if opt23=='y':
            mp.bar(S5,S6,width=0.4,color='cyan')
            mp.xlabel('Airline')
            mp.ylabel('Fare')
            mp.title('Airline VS Fare')
            mp.show()
        print('Insert the flight no. through which you want to travel: ')
        flt2=input('-->')
        c=pd.DataFrame(df6[df6['Flight no.']==flt2])
        print(c)
        s_av2=(c.iat[0,6])
        opt7=int(input('How many tickets you want to book: '))
        if ((s_av2==opt7) or (s_av2>opt7)):
            name2=[]
            age2=[]
            gender2=[]
            phone2=[]
            for i in range(1,opt7+1):
                print('Passenger',i,'Name:')
                p_name2=input('-->')
                print('Passenger',i,'Age:')
                p_age2=int(input('-->'))
                print('Passenger',i,'Gender [M/F/O]:')
                p_gen2=input('-->')
                print('Passenger',i,'Phone no.:')
                p_phone2=int(input('-->'))
                print()
                name2.append(p_name2)
                age2.append(p_age2)
                gender2.append(p_gen2)
                phone2.append(p_phone2)
            data4={'Passenger Name':name2,'Passenger Age':age2,'Passenger Gender':gender2,'Passenger Phone no.':phone2}
            df7=pd.DataFrame(data4)
            print(df7)
            df7.to_csv("E:\Projects\Python project\P_info.csv")
            print()
            print()
            print('     Payment Summary')
            print()
            fare_perperson2=(c.iat[0,5])
            totalfare2=(c.iat[0,5])*opt7
            gst2=((18/100)*totalfare2)
            data5=[fare_perperson2,totalfare2,gst2,(totalfare2+gst2)]
            payment_data2={'Price':data5}
            df8=pd.DataFrame(payment_data2,index=['Fare per person','Base Fare','Taxes','Total Fare'])
            print(df8)
            print()
            print('Payment Options')
            print('1. Credit Card')
            print('2. Debit Card')
            print('3. UPI')
            opt8=input('How do you want to make your payment [1/2/3]:')
            if opt8=='1':
                credit_cardno2=input('Enter credit card number:')
                exp_date2=input('Enter expiry date of your card [MM/YYYY]:')
                cvv2=input('Enter CVV:')
                otp2=input('Enter the otp received:')
                print()
                print('Your payment is successful.')
                print('Your tickets are booked.')
            elif opt8=='2':
                debit_cardno2=input('Enter debit card number:')
                exp_date_d2=input('Enter expiry date of your card [MM/YYYY]:')
                cvv_d2=input('Enter CVV:')
                otp_d2=input('Enter the otp received:')
                print()
                print('Your payment is successful.')
                print('Your tickets are booked.')
            elif opt8=='3':
                upi2=input('Enter UPI:')
                print('Accept the notification received on your UPI to proceed.')
                print()
                print('Your payment is successful.')
                print('Your tickets are booked.')
            else:
                print('Invalid input. Try again.')
            l=input('Do you want to see your ticket[y/n]:')
            if l=='y':
                for i in range(1,opt7+1):
                    t_airline2=i*(list(c['Airline']))
                    t_dtime2=i*(list(c['Departure Time']))
                    t_atime2=i*(list(c['Arrival Time']))
                    t_FT2=i*(list(c['From-To']))
                data18={'Passenger Name':name2,'Airline':t_airline2,'From-To':t_FT2,'Arrival':t_atime2,'Departure':t_dtime2}
                df26=pd.DataFrame(data18)
                print(df26)
            else:
                print('OK')
        else:
            print('Number of seats you want to book are not available')
            print('Try to check in other flights')
    elif opt6=='2':
        df9=pd.read_csv("E:\Projects\Python project\Data for project (12th).csv",nrows=15,skiprows=56,names=['Flight no.','Airline','From-To','Departure Time','Arrival Time','Fare','Seats Available'])
        print(df9)
        S7=list(df9.Airline.unique())
        S8=list(df9.Fare.unique())
        opt24=input('Do you want to see the graph for airline vs fare [y/n]:')
        if opt24=='y':
            mp.bar(S7,S8,width=0.4,color='cyan')
            mp.xlabel('Airline')
            mp.ylabel('Fare')
            mp.title('Airline VS Fare')
            mp.show()
        print('Insert the flight no. through which you want to travel: ')
        flt3=input('-->')
        d=pd.DataFrame(df9[df9['Flight no.']==flt3])
        print(d)
        s_av3=(d.iat[0,6])
        opt9=int(input('How many tickets you want to book: '))
        if ((s_av3==opt9) or (s_av3>opt9)):
            name3=[]
            age3=[]
            gender3=[]
            phone3=[]
            for i in range(1,opt9+1):
                print('Passenger',i,'Name:')
                p_name3=input('-->')
                print('Passenger',i,'Age:')
                p_age3=input('-->')
                print('Passenger',i,'Gender [M/F/O]:')
                p_gen3=input('-->')
                print('Passenger',i,'Phone no.:')
                p_phone3=input('-->')
                print()
                name3.append(p_name3)
                age3.append(p_age3)
                gender3.append(p_gen3)
                phone3.append(p_phone3)
            data6={'Passenger Name':name3,'Passenger Age':age3,'Passenger Gender':gender3,'Passenger Phone no.':phone3}
            df10=pd.DataFrame(data6)
            print(df10)
            df10.to_csv("E:\Projects\Python project\P_info.csv")
            print()
            print()
            print('     Payment Summary')
            print()
            fare_perperson3=(d.iat[0,5])
            totalfare3=(d.iat[0,5])*opt9
            gst3=((18/100)*totalfare3)
            data7=[fare_perperson3,totalfare3,gst3,(totalfare3+gst3)]
            payment_data3={'Price':data7}
            df11=pd.DataFrame(payment_data3,index=['Fare per person','Base Fare','Taxes','Total Fare'])
            print(df11)
            print()
            print('Payment Options')
            print('1. Credit Card')
            print('2. Debit Card')
            print('3. UPI')
            opt10=input('How do you want to make your payment [1/2/3]:')
            if opt10=='1':
                credit_cardno3=input('Enter credit card number:')
                exp_date3=input('Enter expiry date of your card [MM/YYYY]:')
                cvv3=input('Enter CVV:')
                otp3=input('Enter the otp received:')
                print()
                print('Your payment is successful.')
                print('Your tickets are booked.')
            elif opt10=='2':
                debit_cardno3=input('Enter debit card number:')
                exp_date_d3=input('Enter expiry date of your card [MM/YYYY]:')
                cvv_d3=input('Enter CVV:')
                otp_d3=input('Enter the otp received:')
                print()
                print('Your payment is successful.')
                print('Your tickets are booked.')
            elif opt10=='3':
                upi3=input('Enter UPI:')
                print('Accept the notification received on your UPI to proceed.')
                print()
                print('Your payment is successful.')
                print('Your tickets are booked.')
            else:
                print('Invalid input. Try again.')
            m=input('Do you want to see your ticket[y/n]:')
            if m=='y':
                for i in range(1,opt9+1):
                    t_airline3=i*(list(d['Airline']))
                    t_dtime3=i*(list(d['Departure Time']))
                    t_atime3=i*(list(d['Arrival Time']))
                    t_FT3=i*(list(d['From-To']))
                data19={'Passenger Name':name3,'Airline':t_airline3,'From-To':t_FT3,'Arrival':t_atime3,'Departure':t_dtime3}
                df27=pd.DataFrame(data19)
                print(df27)
            else:
                print('OK')
        else:
            print('Number of seats you want to book are not available')
            print('Try to check in other flights')
    else:
        print('Invalid input.Try again.')
            
def book_StoJ():
    print('1. Srinagar to Jaipur')
    print('2. Jaipur to Srinagar')
    opt11=input('Choose the one among the above [1,2]:')
    if opt11=='1':
        df12=pd.read_csv("E:\Projects\Python project\Data for project (12th).csv",nrows=15,skiprows=71,names=['Flight no.','Airline','From-To','Departure Time','Arrival Time','Fare','Seats Available'])
        print(df12)
        S9=list(df12.Airline.unique())
        S10=list(df12.Fare.unique())
        opt25=input('Do you want to see the graph for airline vs fare [y/n]:')
        if opt25=='y':
            mp.bar(S9,S10,width=0.4,color='cyan')
            mp.xlabel('Airline')
            mp.ylabel('Fare')
            mp.title('Airline VS Fare')
            mp.show()
        print('Insert the flight no. through which you want to travel: ')
        flt4=input('-->')
        e=pd.DataFrame(df12[df12['Flight no.']==flt4])
        print(e)
        s_av4=(e.iat[0,6])
        opt12=int(input('How many tickets you want to book: '))
        if ((s_av4==opt12) or (s_av4>opt12)):
            name4=[]
            age4=[]
            gender4=[]
            phone4=[]
            for i in range(1,opt12+1):
                print('Passenger',i,'Name:')
                p_name4=input('-->')
                print('Passenger',i,'Age:')
                p_age4=int(input('-->'))
                print('Passenger',i,'Gender [M/F/O]:')
                p_gen4=input('-->')
                print('Passenger',i,'Phone no.:')
                p_phone4=int(input('-->'))
                print()
                name4.append(p_name4)
                age4.append(p_age4)
                gender4.append(p_gen4)
                phone4.append(p_phone4)
            data8={'Passenger Name':name4,'Passenger Age':age4,'Passenger Gender':gender4,'Passenger Phone no.':phone4}
            df13=pd.DataFrame(data8)
            print(df13)
            df13.to_csv("E:\Projects\Python project\P_info.csv")
            print()
            print()
            print('     Payment Summary')
            print()
            fare_perperson4=(e.iat[0,5])
            totalfare4=(e.iat[0,5])*opt12
            gst4=((18/100)*totalfare4)
            data9=[fare_perperson4,totalfare4,gst4,(totalfare4+gst4)]
            payment_data4={'Price':data9}
            df14=pd.DataFrame(payment_data4,index=['Fare per person','Base Fare','Taxes','Total Fare'])
            print(df14)
            print()
            print('Payment Options')
            print('1. Credit Card')
            print('2. Debit Card')
            print('3. UPI')
            opt13=input('How do you want to make your payment [1/2/3]:')
            if opt13=='1':
                credit_cardno4=input('Enter credit card number:')
                exp_date4=input('Enter expiry date of your card [MM/YYYY]:')
                cvv4=input('Enter CVV:')
                otp4=input('Enter the otp received:')
                print()
                print('Your payment is successful.')
                print('Your tickets are booked.')
            elif opt13=='2':
                debit_cardno4=input('Enter debit card number:')
                exp_date_d4=input('Enter expiry date of your card [MM/YYYY]:')
                cvv_d4=input('Enter CVV:')
                otp_d4=input('Enter the otp received:')
                print()
                print('Your payment is successful.')
                print('Your tickets are booked.')
            elif opt13=='3':
                upi4=input('Enter UPI:')
                print('Accept the notification received on your UPI to proceed.')
                print()
                print('Your payment is successful.')
                print('Your tickets are booked.')
            else:
                print('Invalid input. Try again.')
            n=input('Do you want to see your ticket[y/n]:')
            if n=='y':
                for i in range(1,opt12+1):
                    t_airline4=i*(list(e['Airline']))
                    t_dtime4=i*(list(e['Departure Time']))
                    t_atime4=i*(list(e['Arrival Time']))
                    t_FT4=i*(list(e['From-To']))
                data20={'Passenger Name':name4,'Airline':t_airline4,'From-To':t_FT4,'Arrival':t_atime4,'Departure':t_dtime4}
                df28=pd.DataFrame(data20)
                print(df28)
            else:
                print('OK')
        else:
            print('Number of seats you want to book are not available')
            print('Try to check in other flights')
    elif opt11=='2':
        df15=pd.read_csv("E:\Projects\Python project\Data for project (12th).csv",nrows=15,skiprows=86,names=['Flight no.','Airline','From-To','Departure Time','Arrival Time','Fare','Seats Available'])
        print(df15)
        S11=list(df15.Airline.unique())
        S12=list(df15.Fare.unique())
        opt26=input('Do you want to see the graph for airline vs fare [y/n]:')
        if opt26=='y':
            mp.bar(S11,S12,width=0.4,color='cyan')
            mp.xlabel('Airline')
            mp.ylabel('Fare')
            mp.title('Airline VS Fare')
            mp.show()
        print('Insert the flight no. through which you want to travel: ')
        flt5=input('-->')
        f=pd.DataFrame(df15[df15['Flight no.']==flt5])
        print(f)
        s_av5=(f.iat[0,6])
        opt14=int(input('How many tickets you want to book: '))
        if ((s_av5==opt14) or (s_av5>opt14)):
            name5=[]
            age5=[]
            gender5=[]
            phone5=[]
            for i in range(1,opt14+1):
                print('Passenger',i,'Name:')
                p_name5=input('-->')
                print('Passenger',i,'Age:')
                p_age5=input('-->')
                print('Passenger',i,'Gender [M/F/O]:')
                p_gen5=input('-->')
                print('Passenger',i,'Phone no.:')
                p_phone5=input('-->')
                print()
                name5.append(p_name5)
                age5.append(p_age5)
                gender5.append(p_gen5)
                phone5.append(p_phone5)
            data10={'Passenger Name':name5,'Passenger Age':age5,'Passenger Gender':gender5,'Passenger Phone no.':phone5}
            df16=pd.DataFrame(data10)
            print(df16)
            df16.to_csv("E:\Projects\Python project\P_info.csv")
            print()
            print()
            print('     Payment Summary')
            print()
            fare_perperson5=(f.iat[0,5])
            totalfare5=(f.iat[0,5])*opt14
            gst5=((18/100)*totalfare5)
            data11=[fare_perperson5,totalfare5,gst5,(totalfare5+gst5)]
            payment_data5={'Price':data11}
            df17=pd.DataFrame(payment_data5,index=['Fare per person','Base Fare','Taxes','Total Fare'])
            print(df17)
            print()
            print('Payment Options')
            print('1. Credit Card')
            print('2. Debit Card')
            print('3. UPI')
            opt15=input('How do you want to make your payment [1/2/3]:')
            if opt15=='1':
                credit_cardn5=input('Enter credit card number:')
                exp_date5=input('Enter expiry date of your card [MM/YYYY]:')
                cvv5=input('Enter CVV:')
                otp5=input('Enter the otp received:')
                print()
                print('Your payment is successful.')
                print('Your tickets are booked.')
            elif opt15=='2':
                debit_cardno5=input('Enter debit card number:')
                exp_date_d5=input('Enter expiry date of your card [MM/YYYY]:')
                cvv_d5=input('Enter CVV:')
                otp_d5=input('Enter the otp received:')
                print()
                print('Your payment is successful.')
                print('Your tickets are booked.')
            elif opt15=='3':
                upi5=input('Enter UPI:')
                print('Accept the notification received on your UPI to proceed.')
                print()
                print('Your payment is successful.')
                print('Your tickets are booked.')
            else:
                print('Invalid input. Try again.')
            o=input('Do you want to see your ticket[y/n]:')
            if o=='y':
                for i in range(1,opt14+1):
                    t_airline5=i*(list(f['Airline']))
                    t_dtime5=i*(list(f['Departure Time']))
                    t_atime5=i*(list(f['Arrival Time']))
                    t_FT5=i*(list(f['From-To']))
                data21={'Passenger Name':name5,'Airline':t_airline5,'From-To':t_FT5,'Arrival':t_atime5,'Departure':t_dtime5}
                df29=pd.DataFrame(data21)
                print(df29)
            else:
                print('OK')
        else:
            print('Number of seats you want to book are not available')
            print('Try to check in other flights')
    else:
        print('Invalid input. Try again.')
        
def book_HtoP():
    print('1. Hyderabad to Patna')
    print('2. Patna to Hyderabad')
    opt16=input('Choose the one among the above [1,2]:')
    if opt16=='1':
        df18=pd.read_csv("E:\Projects\Python project\Data for project (12th).csv",nrows=15,skiprows=101,names=['Flight no.','Airline','From-To','Departure Time','Arrival Time','Fare','Seats Available'])
        print(df18)
        S13=list(df18.Airline.unique())
        S14=list(df18.Fare.unique())
        opt27=input('Do you want to see the graph for airline vs fare [y/n]:')
        if opt27=='y':
            mp.bar(S13,S14,width=0.4,color='cyan')
            mp.xlabel('Airline')
            mp.ylabel('Fare')
            mp.title('Airline VS Fare')
            mp.show()
        print('Insert the flight no. through which you want to travel: ')
        flt6=input('-->')
        g=pd.DataFrame(df18[df18['Flight no.']==flt6])
        print(g)
        s_av6=(g.iat[0,6])
        opt17=int(input('How many tickets you want to book: '))
        if ((s_av6==opt17) or (s_av6>opt17)):
            name6=[]
            age6=[]
            gender6=[]
            phone6=[]
            for i in range(1,opt17+1):
                print('Passenger',i,'Name:')
                p_name6=input('-->')
                print('Passenger',i,'Age:')
                p_age6=int(input('-->'))
                print('Passenger',i,'Gender [M/F/O]:')
                p_gen6=input('-->')
                print('Passenger',i,'Phone no.:')
                p_phone6=int(input('-->'))
                print()
                name6.append(p_name6)
                age6.append(p_age6)
                gender6.append(p_gen6)
                phone6.append(p_phone6)
            data12={'Passenger Name':name6,'Passenger Age':age6,'Passenger Gender':gender6,'Passenger Phone no.':phone6}
            df19=pd.DataFrame(data12)
            print(df19)
            df19.to_csv("E:\Projects\Python project\P_info.csv")
            print()
            print()
            print('     Payment Summary')
            print()
            fare_perperson6=(g.iat[0,5])
            totalfare6=(g.iat[0,5])*opt17
            gst6=((18/100)*totalfare6)
            data13=[fare_perperson6,totalfare6,gst6,(totalfare6+gst6)]
            payment_data6={'Price':data13}
            df20=pd.DataFrame(payment_data6,index=['Fare per person','Base Fare','Taxes','Total Fare'])
            print(df20)
            print()
            print('Payment Options')
            print('1. Credit Card')
            print('2. Debit Card')
            print('3. UPI')
            opt18=input('How do you want to make your payment [1/2/3]:')
            if opt18=='1':
                credit_cardno6=input('Enter credit card number:')
                exp_date6=input('Enter expiry date of your card [MM/YYYY]:')
                cvv6=input('Enter CVV:')
                otp6=input('Enter the otp received:')
                print()
                print('Your payment is successful.')
                print('Your tickets are booked.')
            elif opt18=='2':
                debit_cardno6=input('Enter debit card number:')
                exp_date_d6=input('Enter expiry date of your card [MM/YYYY]:')
                cvv_d6=input('Enter CVV:')
                otp_d6=input('Enter the otp received:')
                print()
                print('Your payment is successful.')
                print('Your tickets are booked.')
            elif opt18=='3':
                upi6=input('Enter UPI:')
                print('Accept the notification received on your UPI to proceed.')
                print()
                print('Your payment is successful.')
                print('Your tickets are booked.')
            else:
                print('Invalid input. Try again.')
            p=input('Do you want to see your ticket[y/n]:')
            if p=='y':
                for i in range(1,opt17+1):
                    t_airline6=i*(list(g['Airline']))
                    t_dtime6=i*(list(g['Departure Time']))
                    t_atime6=i*(list(g['Arrival Time']))
                    t_FT6=i*(list(g['From-To']))
                data22={'Passenger Name':name6,'Airline':t_airline6,'From-To':t_FT6,'Arrival':t_atime6,'Departure':t_dtime6}
                df30=pd.DataFrame(data22)
                print(df30)
            else:
                print('OK')
        else:
            print('Number of seats you want to book are not available')
            print('Try to check in other flights')
    elif opt16=='2':
        df21=pd.read_csv("E:\Projects\Python project\Data for project (12th).csv",nrows=15,skiprows=116,names=['Flight no.','Airline','From-To','Departure Time','Arrival Time','Fare','Seats Available'])
        print(df21)
        S15=list(df21.Airline.unique())
        S16=list(df21.Fare.unique())
        opt28=input('Do you want to see the graph for airline vs fare [y/n]:')
        if opt28=='y':
            mp.bar(S15,S16,width=0.4,color='cyan')
            mp.xlabel('Airline')
            mp.ylabel('Fare')
            mp.title('Airline VS Fare')
            mp.show()
        print('Insert the flight no. through which you want to travel: ')
        flt7=input('-->')
        h=pd.DataFrame(df21[df21['Flight no.']==flt7])
        print(h)
        s_av7=(h.iat[0,6])
        opt19=int(input('How many tickets you want to book: '))
        if ((s_av7==opt19) or (s_av7>opt19)):
            name7=[]
            age7=[]
            gender7=[]
            phone7=[]
            for i in range(1,opt19+1):
                print('Passenger',i,'Name:')
                p_name7=input('-->')
                print('Passenger',i,'Age:')
                p_age7=input('-->')
                print('Passenger',i,'Gender [M/F/O]:')
                p_gen7=input('-->')
                print('Passenger',i,'Phone no.:')
                p_phone7=input('-->')
                print()
                name7.append(p_name7)
                age7.append(p_age7)
                gender7.append(p_gen7)
                phone7.append(p_phone7)
            data14={'Passenger Name':name7,'Passenger Age':age7,'Passenger Gender':gender7,'Passenger Phone no.':phone7}
            df22=pd.DataFrame(data14)
            print(df22)
            df22.to_csv("E:\Projects\Python project\P_info.csv")
            print()
            print()
            print('     Payment Summary')
            print()
            fare_perperson7=(h.iat[0,5])
            totalfare7=(h.iat[0,5])*opt19
            gst7=((18/100)*totalfare7)
            data15=[fare_perperson7,totalfare7,gst7,(totalfare7+gst7)]
            payment_data7={'Price':data15}
            df23=pd.DataFrame(payment_data7,index=['Fare per person','Base Fare','Taxes','Total Fare'])
            print(df23)
            print()
            print('Payment Options')
            print('1. Credit Card')
            print('2. Debit Card')
            print('3. UPI')
            opt20=input('How do you want to make your payment [1/2/3]:')
            if opt20=='1':
                credit_cardn7=input('Enter credit card number:')
                exp_date7=input('Enter expiry date of your card [MM/YYYY]:')
                cvv7=input('Enter CVV:')
                otp7=input('Enter the otp received:')
                print()
                print('Your payment is successful.')
                print('Your tickets are booked.')
            elif opt20=='2':
                debit_cardno7=input('Enter debit card number:')
                exp_date_d7=input('Enter expiry date of your card [MM/YYYY]:')
                cvv_d7=input('Enter CVV:')
                otp_d7=input('Enter the otp received:')
                print()
                print('Your payment is successful.')
                print('Your tickets are booked.')
            elif opt20=='3':
                upi7=input('Enter UPI:')
                print('Accept the notification received on your UPI to proceed.')
                print()
                print('Your payment is successful.')
                print('Your tickets are booked.')
            else:
                 print('Invalid input. Try again.')
            q=input('Do you want to see your ticket[y/n]:')
            if q=='y':
                for i in range(1,opt19+1):
                    t_airline7=i*(list(h['Airline']))
                    t_dtime7=i*(list(h['Departure Time']))
                    t_atime7=i*(list(h['Arrival Time']))
                    t_FT7=i*(list(h['From-To']))
                data23={'Passenger Name':name7,'Airline':t_airline7,'From-To':t_FT7,'Arrival':t_atime7,'Departure':t_dtime7}
                df31=pd.DataFrame(data23)
                print(df31)
            else:
                print('OK')
        else:
            print('Number of seats you want to book are not available')
            print('Try to check in other flights')
    else:
        print('Invalid input. Try again.')
    

ch='y'
while ch=='y':
    print('                                 MAKE MY TOUR')
    print()
    print('                           Flight Booking Available')
    opt=input('                     Do you want to book flight [y/n]:')
    if opt=='y':
        print('                   1. MUMBAI TO NEW-DELHI or vice-versa')
        print('                   2. BANGALORE TO KOLKATA or vice-versa')
        print('                   3. SRINAGAR TO JAIPUR or vice-versa')
        print('                   4. HYDERABAD TO PATNA or vice-versa')
        print()
        choice=int(input('Enter your choice[1,2,3,4]:'))
        if choice==1:
            mumbai_delhi=book_MtoD()
        elif choice==2:
            bangalore_kolkata=book_BtoK()
        elif choice==3:
            srinagar_jaipur=book_StoJ()
        elif choice==4:
            hyderabad_patna=book_HtoP()
        else:
            print()
            print('Kindly select from the above given option.')
            print("Currently, we are serving only for the above mentioned routes.")
    else:
        print()
        print('                         Thank you for visiting us.')
        print()
    ch=input('Do you want to continue booking more tickets[y/n]:')
    if ch=='y':
        continue
    else:
        break
