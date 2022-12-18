import datetime 
hr = datetime.datetime.now().hour 
if hr<=12:
  print("Good Morning") 
elif hr<=12>=18:
  print("Good Afternoon")
else:
  print("Good night")