Year = int(input("Enter the Year: "))
if Year%4==0 or Year%400==0:
    print(Year,"Is a Leap year")
else:
    print(Year,"Is Not a Leap Year")