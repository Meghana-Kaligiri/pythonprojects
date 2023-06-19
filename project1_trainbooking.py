import mysql.connector as sqlct

import random
def createdb():
    global mycn
    global mycur
    
    mycn=sqlct.connect(host="localhost",user="root",password="Meghana2004@2003",database="trainbooking")
    if mycn.is_connected():
        print("\t\t\t\t WELCOME TO TRAINBOOKING .")
    mycur=mycn.cursor()
    cmd1 = "create table if not exists Train (sno int(100)  primary key,Name varchar(100),from1 varchar(100),TO1 varchar(100),TRAIN_NO varchar(200),TRAIN_NAME varchar(200),train_time varchar(100), SEATS_AVALIABLE varchar(200),cost int(100))"
    mycur.execute(cmd1)
createdb()
def display_ACSeats():
    
    print("====================================================================================================================")
    print("| DESTINATION PLACE  ARRIVAL PLACE  TRAIN NO   TRAIN NAME           TRAIN TIMINGS       TICKET PRICE  SEATS AVALIABLE|")
    print("====================================================================================================================")

    print("       NELLORE        VIJAYAWADA     13352    DhanbadExpress         12:55am-5:15am          200rs           200       ")
    print("     SECUNDERABAD      GUNTUR        17254    GunturExpress          5:15am-9:30pm           250rs           250       ")
    print("      TIRUPATI       CHENNAICENTRAL  16054   ChennaiCentralExpress   10:10am-1:40pm          300rs           150       ")
    print("      GUDUR           BANGALORE      12296    SanghamitraExpress     7:20am-3:54pm           350rs           400       ")
    print("     RAMESWARAM      VISAKHAPATNAM   20895    BhubaneswarExpress     8:40am-10:55am          400rs           350       ")
    print("==================================================================================================================")

def passangers():
    
    cmd2 = "select * from Train"
    mycur.execute(cmd2)
    r2 = mycur.fetchall()
    
    print("====================================================================================================================")
    print("|SNO NAME DESTINATION PLACE  ARRIVAL PLACE  TRAIN NO   TRAIN NAME      TRAIN TIMINGS   SEATS  cost|")
    print("====================================================================================================================")

    for i in range(len(r2)): #range(3)0,1,2 i = 0
        print("| ",end="")
        print(str(r2[i][0]).ljust(15," "),end="") #r2[0][0] =1
        print(r2[i][1].ljust(17," "),end="|")  #r2[0][1] = pooji
        print(r2[i][2].ljust(18," "),end="|")                  
        print(r2[i][3].ljust(14," "),end="|")               
        print(str(r2[i][4]).ljust(15," "),end="|")
        print(r2[i][5].ljust(16," "),end=" ")
        print(r2[i][6].ljust(10," "),end=" |")
        print(str(r2[i][7]).ljust(5," "),end="|")
        print(str(r2[i][8]).ljust(5," "),end="|") 
        print()

    print("==================================================================================================================")

cost1,cost2,cost3,cost4,cost5 = 200,250,300,350,400

def Book_ACSeats():
    global Seats
    global cost
    global name
    sno = int(input("Enter the id: "))
    name = input("Enter the name of the passenger: ")
    DestinationPlace=input("Enter the Destination Place: ")               
    ArrivalPlace=input("Enter the Arrival Place: ")                       
    TrainNumber=int(input("Enter the Train Number: "))
    print("DhanbadExpress,GunturExpress,ChennaiCentralExpress,BhubaneswarExpress,SanghamitraExpress")
    TrainName=input("Enter the Train Name: ")
    if TrainName == "DhanbadExpress":
        cost = cost1
        print(cost," Rs per ticket")
        
    elif TrainName == "GunturExpress":
        cost = cost2
        print(cost," Rs per ticket")
        
    elif TrainName == "ChennaiCentralExpress":
        print(cost3," Rs per ticket")
        cost = cost3
    elif TrainName == "BhubaneswarExpress":
        print(cost5," Rs per ticket")
        cost = cost5
    elif TrainName == "SanghamitraExpress":
        print(cost4," Rs per ticket")
        cost = cost4
    else:
        print("please select the train in given list.")
    Timings=str(input("Enter the Train Timings: "))                     
    
    
    Seats=int(input("Enter the no.of Seats: "))
    #Price=int(input("Enter the Ticket Price displayed above: "))
    cmd3 = "insert into Train values ('"+str(sno)+"','"+name+"','"+DestinationPlace+"','"+ArrivalPlace+"','"+str(TrainNumber)+"','"+TrainName+"','"+str(Timings)+"','"+str(Seats)+"','"+str(cost)+"')"
    mycur.execute(cmd3)
    print("Record has been added successfully")

def AC_Bill():
  cmd4 = "select * from Train"
  mycur.execute(cmd4)
  r3 = mycur.fetchall() 
  print("Your bill")
  name_1 = input("Enter the name of the passenger: ") #renuka
  for i in range(len(r3)): #range(3) i = 1
      a = r3[i][1] #r3[1][1] = renuka
      if name_1 == a: #renuka == renuka 
          seat = int(r3[i][7]) #r3[1][7]
          price = int(r3[i][8]) 
          print("Total number of seats you booked: ",r3[i][7])
          print("your seat numbers are: ")
          
          for i in range(seat): 
              print(random.randrange(1,1000),end = ",")
          print(" ")
          total_amount = price * seat
          print("Total Amount = ",total_amount)

while True:
    print("\n\n-------------DETAILS--------------------")
    print("(1)ACSeats (2)GENERALSeats  (3)Exit")
    choice=int(input("Please enter your choice:")) #1
    if(choice==1): #1==1
        while True:
            print("(1)display_ACSeats (2)Book_ACSeats (3)passenger_details (4)AC_Bill  (5)Exit")
            choice1=int(input("Please enter your choice:")) 
            if(choice1==1): #2==1
                display_ACSeats()

            elif(choice1==2): #2==2
                Book_ACSeats()
            elif(choice1==4):
                AC_Bill()
            elif(choice1==3):
                passangers()
            elif(choice1==5):
                break

    if(choice==3):
        mycn.commit()
        break
