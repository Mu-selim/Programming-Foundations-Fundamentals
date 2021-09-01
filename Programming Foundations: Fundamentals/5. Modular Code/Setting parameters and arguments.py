# define function
def Amount_Of_Taxes(income): # income is called parameter
    if income >= 5000:
        print("taxes =", income*0.27)
    
    if income < 5000:
        print("taxes =", income*0.22)

# calling function
Amount_Of_Taxes(7000) # 7000 is called argument
print()
Amount_Of_Taxes(3500) # 3500 is called argument