# the server scalar program
# current_users=int(input("enter number of current users:"))
# new_users=50
# minutes=2
# total_users=current_users + (new_users * minutes)
# if total_users>3000:
#     print("launch new server instance")
# else:
#     print("server stable")

# uptime = 97.5
# bill = 50000
# if uptime >= 99.9:
#     refund = 0
#     print("refund amount :",refund)
# elif uptime >= 98:
#     refund = bill*0.10
# else:    
#     refund = bill*0.25
#     print("refund amount :",refund)

weight = float(input("enter weight in kg :"))
height = float(input("enter height in metres:"))
bmi = weight / (height**2)
if bmi < 18.5:
    category = "under weight"
elif bmi < 25:
    category = "normal"
elif bmi < 30:
    category = "over weight"
else:
    category = "obese"
    print("BMI:",bmi)
    print("category:",category)        