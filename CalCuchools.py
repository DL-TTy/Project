# Programmed By DL-TTy (A.M. Ispare)
# https://www.github.com/DL-TTy/Project
# via Python 3.4.4 ~ 3.7.4
# Beta
# Version 2.0.4.36
# Telegram : T.me/DarkLord_TTy
# AM7@hackermail.com


def main():
      welcome()
      
def welcome():
      q = input("""Hello, I`m CalCuchools.
A Calculator For Formuls And Hard Activitys.
>>>My Programmer Is A.M. Ispare<<<
I`m Always Have Update That`s Can Help You.
Press ENTER Key For Start Our Work.""")#Welcame Message
      work_find()
      
def work_find():
      print("""Good. Now, Please Insert Number Of Your Work:
Diameters: 1
Addition: 2
Subtraction: 3
Multiplication: 4
Division: 5
Power: 6
Average: 7
Sum and Count: 8
Multipcation Table: 9
""")
      activity = input("Witch One ??  _")# Select Activity
      activity = int(activity)# Update
      if (activity == int("1")):
            dia_frml()
      elif (activity == int("2")):
            add_frml()
      elif (activity == int("3")):
            sub_frml()
      elif (activity == int("4")):
            mul_frml()
      elif (activity == int("5")):
            div_frml()
      elif (activity == int("6")):
            pow_frml()
      elif (activity == int("7")):
            avg_frml()
      elif (activity == int("8")):
            cum_frml()
      elif (activity == int("9")):
            mul_tpl()
      else:
            errorMessage_1 = input("You Inserted A Invalid Number. Do You Want To Try Again?[y/n]")#Error
            if (errorMessage_1 == "y"):
                  work_find()
            elif (errorMessage_1 == "Y"):
                  work_find()
            else:
                  end_workMessage = input("You Want To Do It, Again?[y/n]")#Try Again Message
                  if (end_workMessage == "y"):#Select Try Again
                        work_find()
                  elif (end_workMessage == "n"):#Select Exit
                        input("Good Luck! _")
                        exit()
                  else:#Exit
                        input("Good Luck! _")
                        exit()

def dia_frml():
      sides_str = input('Now, Insert Sides And Get Diameters: ')#Get Sides From User
      opr_1_dia = int(sides_str)
      opr_2_dia = int(sides_str) - 3
      opr_3_dia = int(opr_1_dia) * opr_2_dia
      opr_4_dia = 2
      awn_dia = opr_3_dia // opr_4_dia#Activitys
      diameters = awn_dia#Awnser
      if (int(sides_str) < 4):#Verifying Input
            errorMessage = input("""Erorr: Your Shape Does`nt Have Any diameters.
If You Want To Try Other Numbers, Write RESET  And Press ENTER Key.
Or Press Enter For Exit.""")
            if (errorMessage == 'RESET'):#Reseting
                  dia_frml()
            if (errorMessage == 'Reset'):#Reseting
                  dia_frml()
            if (errorMessage == 'reset'):#Reseting
                  dia_frml()      
            else:
                  exit()
      else:#OutPut
            print("You Inserted ",int(sides_str),""", That Is A Valid Number For Claculate The Diameters.
We Calculated That The Number Of Diameters In A """,int(sides_str),"""
Sided Shape Is """,diameters,"Diameters.")#printing OutPut
            end_workMessage = input("You Want To Do It, Again?[y/n]")#Try Again Message
            if (end_workMessage == "y"):#Select Try Again
                  work_find()
            elif (end_workMessage == "n"):#Select Exit
                  input("Good Luck! _")
                  exit()
            else:#Exit
                  input("Good Luck! _")
                  exit()

def add_frml():
      opr_1_add = int(input("Ok, Insert Your First Number"))
      opr_2_add = int(input("Ok, Insert Your Secend Number"))#Get Number
      message = input("Do You Want Use Third Number?[y/n]")
      if (message == 'y'):
            opr_3_add = int(input("Ok, Insert Your Secend Number"))
            opr_4_add = opr_1_add + opr_2_add
            awn_add = opr_4_add + opr_3_add
            addition = awn_add
            print("Ok, We Add ",opr_1_add," To ",opr_2_add," And ",opr_3_add,""" And Get A Number.
That`s Is Your Awnser. """,addition)#output
            end_workMessage = input("You Want To Do It, Again?[y/n]")#Try Again Message
            if (end_workMessage == "y"):#Select Try Again
                  work_find()
            elif (end_workMessage == "n"):#Select Exit
                  input("Good Luck! _")
                  exit()
            else:#Exit
                  input("Good Luck! _")
                  exit()
      else:
            awn_add = opr_1_add + opr_2_add
            addition = awn_add
            print("Ok, We Add ",opr_1_add," To ",opr_2_add,""" And Get A Number.
That`s Is Your Awnser. """,addition)
            end_workMessage = input("You Want To Do It, Again?[y/n]")#Try Again Message
            if (end_workMessage == "y"):#Select Try Again
                  work_find()
            elif (end_workMessage == "n"):#Select Exit
                  input("Good Luck! _")
                  exit()
            else:#Exit
                  input("Good Luck! _")
                  exit()

def avg_frml():
      opr_1_avg = int(input("Now, Insert Your 1th Number. "))
      opr_2_avg = int(input("Now, Insert Your 2nd Number. "))
      message_1 = input("Do You Want Use An Other Number?[y/n]")
      if (message_1 == "y"):
            opr_3_avg = int(input("Now, Insert Your 3rd Number. "))
            message_2 = input("Do You Want Use An Other Number?[y/n]")
            if (message_2 == 'y'):
                  opr_4_avg = int(input("Now, Insert Your 4th Number. "))
                  message_3 = input("Do You Want Use An Other Number?[y/n]")
                  if (message_3 == 'y'):
                        opr_5_avg = int(input("Now, Insert Your 5th Number. "))
                        opr_4_1_avg = opr_1_avg + opr_2_avg
                        opr_4_2_avg = opr_4_1_avg + opr_3_avg
                        opr_4_3_avg = opr_4_2_avg + opr_4_avg
                        opr_4_4_avg = opr_4_3_avg + opr_5_avg 
                        awn_avg = opr_4_4_avg // 5
                        averag = awn_avg#Frml
                        average = int(average)
                        print("We Calculate Average Of ",opr_1_avg," And " ,opr_2_avg," , ",opr_3_avg," , ",opr_4_avg," , ",opr_5_avg ,""" Then From That Get A Number,
""",average)
                        end_workMessage = input("You Want To Do It, Again?[y/n]")#Try Again Message
                        if (end_workMessage == "y"):#Select Try Again
                              work_find()
                        elif (end_workMessage == "n"):#Select Exit
                              input("Good Luck! _")
                              exit()
                        else:#Exit
                              input("Good Luck! _")
                              exit()
                  else:
                        opr_3_1_avg = opr_1_avg + opr_2_avg
                        opr_3_2_avg = opr_3_1_avg + opr_3_avg
                        opr_3_3_avg = opr_3_2_avg + opr_4_avg
                        awn_avg = opr_3_3_avg // 4
                        average = awn_avg
                        print("We Calculate Average Of ",opr_1_avg,"""
And """ ,opr_2_avg," , ",opr_3_avg,"""
""",opr_4_avg,""" Then From That Get A Number,
""",average)
                        end_workMessage = input("You Want To Do It, Again?[y/n]")#Try Again Message
                        if (end_workMessage == "y"):#Select Try Again
                              work_find()
                        elif (end_workMessage == "n"):#Select Exit
                              input("Good Luck! _")
                              exit()
                        else:#Exit
                              input("Good Luck! _")
                              exit()
            else:
                  opr_2_1_avg = opr_1_avg + opr_2_avg
                  opr_2_2_avg = opr_2_1_avg + opr_3_avg
                  awn_avg = opr_2_2_avg // 3
                  average = awn_avg
                  print("We Calculate Average Of ",opr_1_avg," And " ,opr_2_avg," , ",opr_3_avg,""" Then From That Get A Number,
""",average)
            end_workMessage = input("You Want To Do It, Again?[y/n]")#Try Again Message
            if (end_workMessage == "y"):#Select Try Again
                  work_find()
            elif (end_workMessage == "n"):#Select Exit
                  input("Good Luck! _")
                  exit()
            else:#Exit
                  input("Good Luck! _")
                  exit()
      else:
            opr_1_1_avg = opr_1_avg + opr_2_avg
            opr_1_2_avg = opr_1_1_avg // 2
            awn_avg = opr_1_2_avg
            average = awn_avg
            print("We Calculate Average Of ",opr_1_avg," And " ,opr_2_avg, """ Then From That Get A Number,
""",average)
            end_workMessage = input("You Want To Do It, Again?[y/n]")#Try Again Message
            if (end_workMessage == "y"):#Select Try Again
                  work_find()
            elif (end_workMessage == "n"):#Select Exit
                  input("Good Luck! _")
                  exit()
            else:#Exit
                  input("Good Luck! _")
                  exit()
def sub_frml():
      opr_1_sub = int(input("Ok. Now, Insert First Number. _"))
      opr_2_sub = int(input("Now, Insert Secend Number. _"))
      message_sub = input("Do You Want To Ao Add A Third Number? _[y/n]")
      if (message_sub == 'y'):
            opr_3_sub = int(input("""OK, Insert Third Number.
(First - Secend - Third = Awnser) _"""))
            message_sub_2 = input("Do You Want To Ao Add A Third Number? _[y/n]")
            if (message_sub == 'y'):
                   opr_4_sub = int(input("""OK, Insert Fourth Number.
(First - Secend - Third - Fourth= Awnser) _"""))
                   opr_5_1_sub = opr_1_sub - opr_2_sub
                   opr_5_2_sub = opr_5_1_sub - opr_3_sub
                   awn_sub = opr_5_2_sub - opr_4_sub
                   subtraction = awn_sub
                   print("""Ummm, This Work So Eazy! I Do It.
""",subtraction," Is Your Awnser.")
                   end_workMessage = input("You Want To Do It, Again?[y/n]")#Try Again Message
                   if (end_workMessage == "y"):#Select Try Again
                         work_find()
                   elif (end_workMessage == "n"):#Select Exit
                         input("Good Luck! _")
                         exit()
                   else:#Exit
                         input("Good Luck! _")
                         exit()
            else:
                   opr_5_1_sub = opr_1_sub - opr_2_sub
                   awn_sub = opr_5_1_sub - opr_3_sub
                   Subtraction = awn_sub
                   print("""Ummm, This Work So Eazy! I Do It.
""",subtraction," Is Your Awnser.")
                   end_workMessage = input("You Want To Do It, Again?[y/n]")#Try Again Message
                   if (end_workMessage == "y"):#Select Try Again
                         work_find()
                   elif (end_workMessage == "n"):#Select Exit
                         input("Good Luck! _")
                         exit()
                   else:#Exit
                         input("Good Luck! _")
                         exit()
      else:
            opr_5_1_sub = opr_1_sub - opr_2_sub
            Subtraction = awn_sub
            print("""Ummm, This Work So Eazy! I Do It.
""",subtraction," Is Your Awnser.")
            end_workMessage = input("You Want To Do It, Again?[y/n]")#Try Again Message
            if (end_workMessage == "y"):#Select Try Again
                  work_find()
            elif (end_workMessage == "n"):#Select Exit
                  input("Good Luck! _")
                  exit()
            else:#Exit
                  input("Good Luck! _")
                  exit()
                  
def mul_frml():
      opr_1_mul = int(input("Right. Now, Insert 1th Numbet"))
      opr_2_mul = int(input("Right. Now, Insert 2nd Numbet"))
      message_mul = input("Do You Want Use An Other Number?[y/n]")
      if (message_mul == 'y'):
            opr_3_mul = int(input("Right. Now, Insert 3rd Numbet"))
            message_mul = input("Do You Want Use An Other Number?[y/n]")
            if (message_mul == 'y'):
                  opr_4_mul = int(input("Right. Now, Insert 4th Numbet"))
                  message_mul = input("Do You Want Use An Other Number?[y/n]")
                  if (message_mul == 'y'):
                        opr_5_mul = int(input("Right. Now, Insert 5th Numbet"))
                        opr_1_1_mul = opr_1_mul * opr_2_mul
                        opr_1_2_mul = opr_1_1_mul * opr_3_mul
                        opr_1_3_mul = opr_1_2_mul * opr_4_mul
                        awn_mul = opr_1_3_mul * opr_5_mul
                        multiplication = awn_mul
                        print("""We Do It :)
Your Awnser Is """,multiplication)
                        end_workMessage = input("You Want To Do It, Again?[y/n]")#Try Again Message
                        if (end_workMessage == "y"):#Select Try Again
                              work_find()
                        elif (end_workMessage == "n"):#Select Exit
                              input("Good Luck! _")
                              exit()
                        else:#Exit
                              input("Good Luck! _")
                              exit()
                  else:
                        opr_5_mul = int(input("Right. Now, Insert 5th Numbet"))
                        opr_1_1_mul = opr_1_mul * opr_2_mul
                        opr_1_2_mul = opr_1_1_mul * opr_3_mul
                        awn_mul = opr_1_2_mul * opr_4_mul
                        multiplication = awn_mul
                        print("""We Do It :)
Your Awnser Is """,multiplication)
                        end_workMessage = input("You Want To Do It, Again?[y/n]")#Try Again Message
                        if (end_workMessage == "y"):#Select Try Again
                              work_find()
                        elif (end_workMessage == "n"):#Select Exit
                              input("Good Luck! _")
                              exit()
                        else:#Exit
                              input("Good Luck! _")
                              exit()
            else:
                  opr_1_1_mul = opr_1_mul * opr_2_mul
                  awn_mul = opr_1_1_mul * opr_3_mul
                  multiplication = awn_mul
                  print("""We Do It :)
Your Awnser Is """,multiplication)
                  end_workMessage = input("You Want To Do It, Again?[y/n]")#Try Again Message
                  if (end_workMessage == "y"):#Select Try Again
                        work_find()
                  elif (end_workMessage == "n"):#Select Exit
                        input("Good Luck! _")
                        exit()
                  else:#Exit
                        input("Good Luck! _")
                        exit()
      else:
            awn_mul = opr_1_mul * opr_2_mul
            multiplication = awn_mul
            print("""We Do It :)
Your Awnser Is """,multiplication)
            end_workMessage = input("You Want To Do It, Again?[y/n]")#Try Again Message
            if (end_workMessage == "y"):#Select Try Again
                  work_find()
            elif (end_workMessage == "n"):#Select Exit
                  input("Good Luck! _")
                  exit()
            else:#Exit
                  input("Good Luck! _")
                  exit()

def power_select_mode(): # Withot Use
      print("Choose Mode To You Want: _")
      sec_pow_mess = input("Power(p) Or Power In Power(pip)")
      if (sec_pow_mess == 'p'):
            pow_frml()
      elif (sec_pow_mess == 'pip'):
            pip_frml()
      else:
            print("You Inserted A Invalid Awnser, Please Jast Write 'p' or ' pip'")
            spm_2 = input("Retry It?[y/n]")
            if (spm_2 == 'y'):
                  power_select_mode()
            else:
                  end_workMessage = input("You Want To Back To Home?[y/n]")#Try Again Message
                  if (end_workMessage == "y"):#Select Try Again
                        work_find()
                  elif (end_workMessage == "n"):#Select Exit
                        input("Good Luck! _")
                        exit()
                  else:#Exit
                        input("Good Luck! _")
                        exit()

def pow_frml():
        opr_1_pow = int(input("Good. Now, Insert A Number That Want To Use For Number"))
        opr_1_pow = int(input("Good. Now, Insert A Number That Want To Use For Power"))
        awn_pow = opr_1_pow ** opr_1_pow
        power = awn_pow
        print("""We CalCulate This :-)
Your Awnser Is  """,power)
        end_workMessage = input("You Want To Do It, Again?[y/n]")#Try Again Message
        if (end_workMessage == "y"):#Select Try Again
              work_find()
        elif (end_workMessage == "n"):#Select Exit
              input("Good Luck! _")
              exit()
        else:#Exit
              input("Good Luck! _")
              exit()

def pip_frml(): # Withot Use
      print("Shit. Ok, Insert Couple Numbers. (Number ** Power ** Power`s Power)")
      opr_1_pip = int(input("Number _"))
      opr_2_pip = int(input("Power _"))
      opr_3_pip = int(input("Power`s Power _"))
      opr_56_3_pip = opr_2_pip ** opr_3_pip
      awn_pip = opr_1_pip ** opr_56_3_pip
      power_in_power = awn_pip
      print("""We CalCulate This =))))
Your Awnser Is  """,power_in_power)
      end_workMessage = input("You Want To Do It, Again?[y/n]")#Try Again Message
      if (end_workMessage == "y"):#Select Try Again
            work_find()
      elif (end_workMessage == "n"):#Select Exit
            input("Good Luck! _")
            exit()
      else:#Exit
            input("Good Luck! _")
            exit()
      
def div_frml():
      div_mess = input("Ummm, You Want To I Count Exactly?[y/n]")
      if (div_mess == 'y'):
            opr_1_div = int(input("Insert Divisive: _"))
            opr_2_div = int(input("Insert Divisor: _"))
            awn_div = opr_1_div / opr_2_div
            division = awn_div
            print("""Wow, We Did it =)))
""",division,"  Is Your Awnser")
            end_workMessage = input("You Want To Do It, Again?[y/n]")#Try Again Message
            if (end_workMessage == "y"):#Select Try Again
                  work_find()
            elif (end_workMessage == "n"):#Select Exit
                  input("Good Luck! _")
                  exit()
            else:#Exit
                  input("Good Luck! _")
                  exit()
      else:
            opr_1_div = int(input("Insert Divisive: _"))
            opr_2_div = int(input("Insert Divisor: _"))
            awn_div = opr_1_div // opr_2_div
            division = awn_div
            print("""Wow, We Did it =)))
""",division,"  Is Your Awnser")
            end_workMessage = input("You Want To Do It, Again?[y/n]")#Try Again Message
            if (end_workMessage == "y"):#Select Try Again
                  work_find()
            elif (end_workMessage == "n"):#Select Exit
                  input("Good Luck! _")
                  exit()
            else:#Exit
                  input("Good Luck! _")
                  exit()

def cum_frml():
      opr_1_cum = int(input("OK. Insert Starter Number."))
      opr_2_cum = int(input("OK. Insert Stoped Number."))
      opr_3_cum = int(input("OK. Insert Step."))
      count = 0
      sum = 0
      print("Please With...")
      print("Just A Moment")
      for i in range(opr_1_cum, opr_2_cum, opr_3_cum):
            count = count + 1
            sum = sum + i
      count = count + 1
      print("""We Calculate This, Again $)))
Count : """,count,"""
Sum : """,sum)
      end_workMessage = input("You Want To Do It, Again?[y/n]")#Try Again Message
      if (end_workMessage == "y"):#Select Try Again
            work_find()
      elif (end_workMessage == "n"):#Select Exit
            input("Good Luck! _")
            exit()
      else:#Exit
            input("Good Luck! _")
            exit()

def mul_tpl():
      for x in range(1, 11, 1):
            x1 = x * 1
            x2 = x * 2
            x3 = x * 3
            x4 = x * 4
            x5 = x * 5
            x6 = x * 6
            x7 = x * 7
            x8 = x * 8
            x9 = x * 9
            x10 = x * 10
            print(x1,x2,x3,x4,x5,x6,x7,x8,x9,x10)

      end_workMessage = input("You Want To Do It, Again?[y/n]")#Try Again Message
      if (end_workMessage == "y"):#Select Try Again
            work_find()
      elif (end_workMessage == "n"):#Select Exit
            input("Good Luck! _")
            exit()
      else:#Exit
            input("Good Luck! _")
            exit()

            

                  
if __name__ == "__main__":main()


#Programmed By DL-TTy (A.M. Ispare)
