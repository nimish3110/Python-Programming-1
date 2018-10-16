


from easygui import *
import sys
while 1:
    msgbox("online shopping")
    msg ="choose ypur site"
    title = "shop online"
    choices = ["amazon", "filpkart", "Snapdeal", "myntra","jabong"]
    choice = choicebox(msg, title, choices)
    msgbox("You chose: " + str(choice), "shopping")
    if choices=="amazon":
       msgbox("amazon shopping")
       msg1 ="what type of shops do you want to shop"
       title1 = "amazon shop"
       choices1 = ["electronics", "fashion", "shoes", "groceries"]
       choice1 = choicebox(msg1, title1, choices1)
       msgbox("You chose: " +str(choice1),"amazon"
       title1 = "Please Confirm"
       if choices1=="electronics":
           msgbox("electronics")
           msg2 ="what type of elctronic do you want to shop"
           title3 = "amazon shop"
           choices2 = ["mobiles"]
           choice2 = choicebox(msg2, title3, choices2)
           msgbox("You chose: " +str(choice2),"elctronic sale" 
           if choices2=="mobiles":
               msgbox("mobiles")
               msg3 ="which mobile do you want"
               title4= "amazon mobile shop"
               choices3 = ["MI", "samsung"]
               choice3 = choicebox(msg3, title4, choices3)
               msgbox("You chose: " +str(choice3),"phone sale" 
               if choices3=="MI":
                  msgbox("mobiles")
                  msg4 ="which MI phone do you want"
                  title5= "amazon mobile shop"
                  choices4 = ["pocof1", "note pro"]
                  choice4 = choicebox(msg4, title5, choices4)
                  msgbox("You chose: " +str(choice4),"MI sale"
                  if choices4=="pocof1":
                     msgbox("mobiles")
                     msg5 ="which vender do you want"
                     title6= "amazon mobile shop"
                     choices5 = ["lotus elex=21000", "empress elex=21100"]
                     choice5 = choicebox(msg5, title6, choices5)
                     msgbox("You chose: " +str(choice5),"MI poco sale"
                  elif choices4=="note pro":
                     msgbox("mobiles")
                     msg5 ="which vender do you want"
                     title6= "amazon mobile shop"
                     choices5 = ["lotus elex=15000", "empress elex=15100"]
                     choice5 = choicebox(msg5, title6, choices5)
                     msgbox("You chose: " +str(choice5),"MI note pro sale"
                  else:
                      title6 = "Please Confirm"  
                         msg = "Do you want to continue?"
                         title = "Please Confirm"
                        if ccbox(msg, title)
                          pass
                        else:
                           sys.exit(0)
 
               else :
                  msgbox("mobiles")
                  msg4 ="which samsung phone do you want"
                  title5= "amazon mobile shop"
                  choices4 = ["A6", "A8"]
                  choice4 = choicebox(msg4, title5, choices4)
                  msgbox("You chose: " +str(choice4),"samsung sale"
                   if  choices4=="A6":
                     msgbox("mobiles")
                     msg5 ="which vender do you want"
                     title6= "amazon mobile shop"
                     choices5 = ["lotus elex=20000", "empress elex=20100"]
                     choice5 = choicebox(msg5, title6, choices5)
                     msgbox("You chose: " +str(choice5),"samsung a8 sale"
                   elif choices4=="A8":
                     msgbox("mobiles")
                     msg5 ="which vender do you want"
                     title6= "amazon mobile shop"
                     choices5 = ["lotus elex=21000", "empress elex=20100"]
                     choice5 = choicebox(msg5, title6, choices5)
                     msgbox("You chose: " +str(choice5),"samsung a6 sale" 
                   else :
                      title6 = "Please Confirm"  
                     msg = "Do you want to continue?"
                     title = "Please Confirm"
                     if ccbox(msg, title)
                         pass
                     else:
                        sys.exit(0)
           

            else :
       title2 = "Please Confirm"  
    msg = "Do you want to continue?"
    title = "Please Confirm"
    if ccbox(msg, title)
        pass
    else:
        sys.exit(0)


