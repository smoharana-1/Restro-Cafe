##we can make here a restro management
menu = { 
'pizza' : 150,
'gupchup' : 40,
'momos' : 70,
'icecream' : 45,
'mojito' : 80,
'paovaji' : 50,
'chholebature' : 60,
'cheessypasta' : 100,
}

print("welcome to our restro cafe !!")
print("pizza : 150\ngupchup : 30\nmomos : 70\nicecream : 45\nmojito : 80\npaovaji : 50\nchole bature : 60\ncheessy pasta : 100  ")

total_order = 0 
item_1 = input("enter your first order =")

if item_1 in menu :
    total_order += menu[item_1]
    print( "please wait few minute for serving your food ")
else :
    print("your order food is not available")

another_item2 = input("Do you want for another order ? (yes/no)")
if another_item2 == "yes" :
    item_3 = input("please tell me what is your next order =")
    if item_3 in menu :

      total_order += menu [item_3]
    print("take a minute of time for your order ")
else :
    print("your order food is not available, sorry ")
print( f"the total amount to pay = {total_order}")


