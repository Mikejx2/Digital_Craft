Bill = float(input("The total bill amount? "))

service = input("The level of service? ")

if service.lower() == "good":
    tip = .20


elif service.lower() == "fair":    
    tip = .15


elif service.lower() == "bad":
    tip = .10
    
    
result = Bill * tip

total = result + Bill

print("Tip Amount:$%.2f" % result)
print("Total Amount:$%.2f" % total)