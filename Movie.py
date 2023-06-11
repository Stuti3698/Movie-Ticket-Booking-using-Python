##################SOURCE CODE FOR MOVIE TICKET
BOOKING##################
import mysql.connector as sql
print ("$$$$$$$$$$$$ CARNIVAL CINEMA BOOKING $$$$$$$$$$$$$$")
# this theater function is used to select screen
def theater():
 print("which screen do you want to watch movie: ")
 print("1,SCREEN 1")
 print("2,SCREEN 2")
 print("3,SCREEN 3")
 a = int(input("choose your screen: "))
 timing(a)
# this timing function is used to select timing for movie
def timing(a):
 time1 = {
 "1": "10.00-1.00",
 "2": "1.10-4.10",
 "3": "4.20-7.20",
 "4": "7.30-10.30"
 }
 time2 = {
 "1": "10.15-1.15",
 "2": "1.25-4.25",
 "3": "4.35-7.35",
 "4": "7.45-10.45"
 }
 time3 = {
 "1": "10.30-1.30",
12
 "2": "1.40-4.40",
 "3": "4.50-7.50",
 "4": "8.00-10.45"
 }
 if a == 1:
 print("choose your time:")
 print(time1)
 t = input("select your time:")
 x = time1[t]
 print("successfull!, enjoy movie at "+x)
 elif a == 2:
 print("choose your time:")
 print(time2)
 t = input("select your time:")
 x = time2[t]
 print("successful!, enjoy movie at "+x)
 elif a == 3:
 print("choose your time:")
 print(time3)
 t = input("select your time:")
 x = time3[t]
 print("successful!, enjoy movie at "+x)
 return 0

f=0
#this t_movie function is used to select movie name
def movie():
 global f
 f = f+1
 print("which movie do you want to watch?")
 print("1,JURASSIC PARK ")
 print("2,HARRY POTTER AND CURSE CHILD ")
 print("3,AVENGERS END GAME")
 print("4,TANHAJI:THE UNSUNG WARRIOR")
13
 print("5,DIL BECHARA")
 print("6,PANGA")
 print("7,GUNJAN SAXENA")
 print("8,FAST AND FURIOUS")
 print("9,back") #to move to previous menu
 movie = int(input("choose your movie: "))
 if movie == 9:
 city()
 return 0
 if f == 1:
 theater()
# this function is used to select city
def city():
 print("where you want to watch movie?:")
 print("1,HYDERABAD")
 print("2,MUMBAI")
 print("3,BANGALORE")
 print("4,CHENNAI")
 print("5,AHEMDABAD")
 print("6,CHANDIGARH")
 print("7,PUNE")
 print("8,KOLKATA")
 print("9,DELHI")
 print("10,KOCHI")
 print("11,OTHER") #to choose your desired city
 place = int(input("choose your option: "))
 if place == 1:
 movie()
 elif place == 2:
 movie()
 elif place == 3:
 movie()
 elif place ==4:
14
 movie()
 elif place ==5:
 movie()
 elif place ==6:
 movie()
 elif place ==7:
 movie()
 elif place ==8:
 movie()
 elif place ==9:
 movie()
 elif place ==10:
 movie()
 else:
 x=input("TYPE YOUR DESIRED PLACE, IF NOT IN OPTION:")
 movie()
city()
print("1,FIRST CLASS SEATS")
print("2,SECOND CLASS SEATS")
ch=int(input("Enter your choice :"))
conn=sql.connect(host =
'localhost',user='root',passwd='stuti123',database='stuti1db')
c1=conn.cursor()
if conn.is_connected():
 print(" ")
else:
 print("error in connecting")
if ch==1:
 print("WELCOME TO FIRST CLASS BOOKING")
 mname = input("Enter the movie name :")
 phno = input("Enter phone number :")
 tic = int(input("Enter total tickets :" ))
15
 sex = input ("Enter your sex :" )
 fname = input ("Enter your first name :")
 lname = input ("Enter your last name :")
 passwd =int( input ("Enter your passwd :"))
 userID = input ("Enter your userID :")
 snacks = input ("Order your snacks :")
 ins="insert into cinema1 values(
'{}','{}',{},'{}','{}','{}',{},'{}','{}')".format(mname,phno,tic,sex,fname,lname,pa
sswd,userID,snacks)
 c1.execute(ins)
 conn.commit()
 sql = "SELECT sum(tic) FROM cinema1 HAVING sum(tic)<100"
 c1.execute(sql)
 x=c1.fetchall()
 print (" ticket booked congrats")
 total =500 * tic
 print('TOTAL AMOUNT:',total)
 print ("THANK YOU FOR VISITING CARNIVAL CINEMAS")
 print ("ratings:-")
 rate=input("HOW WAS YOUR
EXPERIENCE?(POOR/GOOD/EXCELLENT):")
 if rate=='POOR':
 print("We deeply regret for the inconvenience")
 elif rate=='GOOD':
 print("Do share your suggestions how could we improve our
policies")
 else :
 print("THANKS!!DO VISIT AGAIN")
elif ch ==2:
 print ("WELCOME TO SECOND CLASS BOOKING")
 c = input ("Enter your movie name :")
 a = input ("Enter your name :")
 d = input ("Enter total tickets :")
16
 b = input ("Enter your ph_no :")
 pswd= input("Enter the password :")
 sks = input("Order your snacks :")
 ins="insert into cinema2 values(
'{}','{}','{}','{}','{}','{}')".format(c,a,d,b,pswd,sks)
 c1.execute(ins)
 conn.commit()
 print ("*********************TICKET BOOKED***********************")
 tot=250*int(d)
 print('TOTAL AMOUNT:',tot)
else:
 y=input("do you want to cancel the booking?(YES/NO):")
 if y=='yes':
 print("BOOKING CANCELLED")
 else:
 print("CONTINUE")
print ("///////////////ENJOY THE MOVIE AND HAVE FUN/////////////////")
