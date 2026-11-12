# units=int(input("enter the number units used"))
# if units <=100:
#     bill = unit*1
# elif units <= 200:
#     bill = 100*1 +(units-100)*2
# else:
#     bill = 100*1 + 100*2 + (units-200)*5
# print("electricity bill:",bill)

#triangles program :- angles 50,50,80
# a=int(input("enter the first angle:"))
# b=int(input("enter the second angle:"))
# c=int(input("enter the third angle:"))
# if a==b and b==c and c==a:
#     print("equilateral triangle")
# elif a==b or b==c or a==c:
#     print("isoceles triangle" )
# else:
#     print("scalene triangle")

# nested if else

age=20
has_id = False
if age >=18:
 if has_id:
    print("entry allowed")
 else:
    print("show your id card")
else:
     print("too young for entry")