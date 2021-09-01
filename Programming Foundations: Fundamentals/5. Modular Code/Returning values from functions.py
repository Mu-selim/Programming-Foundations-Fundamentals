# creating Function
def Money_Count(current_amount, will_be_taken):
    if current_amount >= will_be_taken:
        current_amount = current_amount - will_be_taken
    return current_amount

# Calling Function
remain = Money_Count(1000, 950)

print("The remain money is", remain)
if remain <= 100:
    print("Your Balance is low")
else:
    print("Your Balance is good")