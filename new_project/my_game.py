
    #     Hello everyone !!!             
     # My name is Khurshid Ruziev  
       # This is my first Pyhton game     
         # Please slack me if you have any suggestions about this game
          # Also, I would be thankfull if you could share with me your opinion
           #     Thank you


print()
print()
print("   #####################################################################")
print("   # This game is about your morning after a Party night  !!!!         #")
print("   # Here you will try to wake up early in the morning to go to work   #")
print("   # Or you will keep sleeping and will get FIRED !!!  GOOD LUCK ))    #")
print("   #####################################################################")
print()
print()

player_name = ""

# ----------------- STARTING ------------------------

while(player_name == ""):
    player_name = input(" Before starting the game, tell me your name, so I could call your name, when I will be laughing once, you get FIRED!! ")

print()
print(" OK " + player_name +", its 7:45 am, Monday, yes!! your lovelly day right? You have to be at work at 9:00am, you dont wanna be late ")
print(" because, you remember, how last time your boss was barking at you like : ""YOU WILL GET FIRED IF YOU WILL BE LATE ONE MORE TIME!!")
print(" Yesterday you were drinking tooo tooo much with your friends and came home at about 3am")
print(" Now you will have to make a right choice to get to work on time ...")
print()
print()
print()
print()
print(" Its 7:45 am, your phone is ringing because you set an alarm every 15 minutes after 7:30 am ")
print(" You will have to drive to work about 20 minutes, so, you have a time to sleep, you can turn off this alarm and get up at next alarm")
print(" which will be at 8:00 am, but its up to you ...")
print()
print()
print(" 1. Turn off an alarm for this time ")
print(" 2. Try to get up ")
decision = ""
while( decision == ""):
    decision = input(" Please pick a number: ")
    if ( decision == "1"):
        print()
        print()
        print()
        print()
        print(" You keep sleeping ")
        print()
        print()
        print()
        print()
        print( player_name + " Its 8:00 am, your phone is ringing, now you realize that you need to take a shower, it will take up to 30 minutes and you could make a cofee and head to work at about 8:40")
        print(" 1. Turn off an alarm for this time ")
        print(" 2. Try to get up ")
        decision2 = ""
        while( decision2 == ""):
            decision2 = input(" Please pick a number: ")
            if ( decision2 == "1"):
                print()
                print()
                print()
                print()
                print(" Ohh "+ player_name +", really??? You wanna lose your job? ")
                print()
                print()
                print()
                print()
                print( " Its 8:15 am, your phone is ringing, now you realize that, you dont have a time to take a shower and you realize that yesterday your friends have spilled a COKE on your head")
                print( " You can not go to work like this, and if you will take a shower you will be late to you job and get FIRED anyways")
                print( " GAME OVER " + player_name +", YOU HAVE BEEN FIRED ")
            elif (decision2 == "2"):
                print( " Good " + player_name +", you can take a shower and be at work on time")
            else:
                print(" Please choose 1 or 2")
    elif ( decision == "2"):
        print()
        print()
        print()
        print()
        print( " You can take a shower to wake up, and make yourself a breakfast ")
        print()
        print()
        print()
        print()
        print()
        print( " Its 8:40, you are driving to work, and you hit the really bad traffic, you spent over 35 minutes to get to work, your boss saw you came late and FIRED YOU!!")
        print( " GAME OVER, YOU HAVE BEEN FIRED")
    else:
        print(" PLEASE CHOOSE 1 OR 2")