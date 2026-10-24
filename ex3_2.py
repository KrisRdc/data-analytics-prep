sh = input("enter Hours: ")
sr = input("Enter Rates: ")
try:
  fh = float(sh)
  fr = float(sr)
except:
  print("Error, please enter numeric input")
  quit()
  
print(fh, fr)
if fh > 40 :
    # print("Overtime")
    print("Overtime")
    reg = fr * fh
    otp =  (fh - 40.0) * (fr * 0.5)
    # print(reg,otp)
    print(reg,otp)
    xp = reg + otp
else:
    # print("Regular")
    print("Regular")
    xp = fh * fr
print("Pay:",xp)