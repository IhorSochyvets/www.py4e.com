hours = input("Enter Hours: ")
rate = input("Enter Rate: ")
type(hours)
type(rate)

try: 
    hoursInt = int(hours)
    rateInt = int(rate)
except:
    print("Error, please enter numeric input")
    exit()

if hoursInt <= 40:
    pay = hoursInt * rateInt
else:
    pay = (40 * rateInt) + ( (hoursInt - 40) * rateInt * 1.5 )

print("Pay: ", pay)
