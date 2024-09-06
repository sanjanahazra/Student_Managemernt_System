import random
from random import *
import os
import time

class SMS:
 # Menu
 def menu():
  print("1. Admin")
  print("2. Student")
  c = input("Choose from above: ")
  if c == "1":
   SMS.admin()
  elif c == "2":
   SMS.student()
  else:
   print("Invalid choice")
   SMS.menu() 

 # Student account
 def student():
  print("Student account")
  print("---------------")
  print("1. Login")
  print("2. Register")
  c = input("Choose from above: ")
  if c == "1":
   SMS.studentLoginn()
  elif c == "2":
   SMS.studentRegister()
  else:
   print("Invalid choice")
   SMS.student()

 def studentLoginn():
  print("Login as a student")
  print("------------------")
  fname = input("Firstname: ")
  ID__ = input("ID: ")
  for i in os.listdir("C:"):
   try:
    if str(fname)+"."+str(ID__) in i:
     SMS.studentDashboard()
   except:
    print("Invalid details!")
    SMS.studentLogin()

 # Student Registration
 def studentRegister():
  print("Student registration")
  print("--------------------")
  fname = input("Firstname: ")
  lname = input("Lastname: ")
  age = input("Age: ")
  gender = input("Gender: ")
  ID = randint(1000000, 9000000)
  if fname != "" or lname != "" or age != "" or gender != "":
   with open(str(fname)+"."+str(ID), "a") as f:
    f.write("Firstname: "+str(fname)+"\n")
    f.write("Lastname: "+str(lname)+"\n")
    f.write("Age: "+str(age)+"\n")
    f.write("Gender: "+str(gender)+"\n")
    f.write("ID: "+str(ID)+"\n")
    f.write("\n")
    SMS.studentDashboard()
  else:
   print("All fields are required!")
   SMS.studentRegister()

 # Student Login
 def studentLogin():
  print("Student Login")
  print("-------------")
  name = input("Firstname: ")
  ID = input("ID: ")
  if name == "" or ID == "":
   print("All fields are required!")
  else:
   o = os.listdir("C:")
   for reg in o:
    if str(name)+"."+str(ID) not in reg:
     SMS.studentDashboard()
     
    else:
     print("Account is not registered!")
     SMS.studentLogin()
     
 # Student dashboard
 def studentDashboard():
  print("")
  print("Student dashboard")
  print("---------------")
  print("1. My details")
  print("2. Messages")
  print("3. Logout")
  c = input("Choose from above: ")
  if c == "1":
   try:
    name = input("Firstname: ")
    ID = input("ID: ")
    with open(str(name)+"."+str(ID), "r") as f:
     print(f.read())
     print("")
     SMS.studentDashboard()
   except:
    print("Student could not be found!")
    SMS.studentDashboard()
  elif c == "2":
   SMS.studentMessages()
  elif c == "3":
   SMS.student()
  else:
   print("Invalid entry!")

 def studentMessages():
  print("Messages")
  print("1. Send message")
  print("2. View message")
  c = input("Choose from above: ")
  if c == "1":
   m = input("Message:-->: ")
   fname = input("Firstname: ")
   ID = input("ID: ")
   for i in os.listdir("C:"):
    if str(fname)+"."+str(ID) not in i:
     print("Invalid details")
    else:
     with open(str(fname)+".message", "w") as mess:
      mess.write(m+"\n")
  elif c == "2":
   ID_ = input("ID: ")
   for x in os.listdir("C:"):
    if str(ID_)+"."+"adminMessage" not in x:
     print("No message for you!")
     break
    else:
     try:
      with open(str(ID_)+"."+"adminMessage", "r") as fi:
       print(fi.read())
     except:
      print("No message for you!")
      SMS.studentMessages()
      break
  else:
   print("Invalid choice!")
   SMS.studentMessages()


 # Admin
 def admin():
  print("Admin account")
  print("=============")
  name = input("Username: ")
  password = input("Password: ")
  if name == "Daniel" and password == "5716":
   SMS.adminDashboard()

  else:
   print("Invalid admin details")


 # Admin dashboard
 def adminDashboard():
  print("")
  print("Admin dashboard")
  print("===============")
  print("1. View Student's details")
  print("2. Messages")
  print("3. Remove student")
  print("4. Sign in a new student")
  print("5. Logout")
  c = input("Choose from above: ")
  if c == "1":
   try:
    name = input("Firstname: ")
    IDDD = input("ID: ")
    with open(str(name)+"."+str(IDDD), "r") as f:
     print(f.read())
     SMS.adminDashboard()
   except:
    print("Student could not be found!")
    SMS.adminDashboard()
  elif c == "2":
   SMS.adminMessages()

  elif c == "3":
   fname = input("Firstname: ")
   ID_ = input("ID: ")
   for x in os.listdir("C:"):
    try:
     if str(fname)+"."+str(ID_) in x:
      os.remove(str(fname)+"."+str(ID_))
      print("Deleting account...")
      time.sleep(2)
      print("Account deleted successfully!")
      SMS.admin()
    except:
     print("Account could not be found!")
  elif c == "4":
   print("Sign in a new student")
   print("=====================")
   fname = input("Firstname: ")
   lname = input("Lastname: ")
   age = input("Age: ")
   gender = input("Gender: ")
   ID = randint(1000000, 9000000)
   if fname != "" or lname != "" or age != "" or gender != "":
    with open(str(fname)+"."+str(ID), "a") as f:
     f.write("Firstname: "+str(fname)+"\n")
     f.write("Lastname: "+str(lname)+"\n")
     f.write("Age: "+str(age)+"\n")
     f.write("Gender: "+str(gender)+"\n")
     f.write("ID: "+str(ID)+"\n")
     f.write("\n")
     print("Success! ")
     SMS.adminDashboard()
   else:
    print("All fields are required!")
    SMS.adminDashboard()

  elif c == "5":
   SMS.admin()


 # Admin message center
 def adminMessages():
  print("Messages")
  print("========")
  print("1. View message")
  print("2. Send message")
  c = input("Choose from above: ")
  if c == "1":
   n = input("Firstname: ")
   for i in os.listdir("C:"):
    if str(n)+".message" not in i:
     print("No messages to view!")
     SMS.adminMessages()
     
    else:
     try:
      with open(str(n)+".message", "r") as f:
       print(f.read())
     except:
      print("No message to view!")
      SMS.adminMessages()
  elif c == "2":
   message = input("Message:-->: ")
   _ID = input("Student ID: ")
   with open(str(_ID)+".adminMessage", "w") as adminM:
    adminM.write(str(message)+"\n")
    adminM.close()
    SMS.adminMessages()
SMS.menu()
