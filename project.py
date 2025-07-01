items = ['coffee','Cheese Burger','Spring Rolls','Dosa','Waffle','Hot & crispy fries','Smoky Red Chicken Strips','Choclate Sandwich']

### Design
print("#*"*30+"\n    Welcome To CHOICE FOOD Cafeteria\n"+"#"*30+ "\nPlease Choose your Order:")
# Declare Variables
menue = {"Coffee":80,"Cheese Burger":250,"Spring Rolls":150,"Dosa":100,
"Waffle":120,"Hot & crispy fries":350,"Smoky Red Chiken Strips":550,
"Choclate Sandwich":180}
# Show Menue Card
for item,price in menue.items():
      print(item.title()+" - Price: "+str(price)+"Rs")
print('#*'*20)
# Add items
x = True
total_price = 0 # total price
orders = [] # store selected items 
while x:
     items = input("Enter Food Name :")
     print("Order More or Type: done")
     x = items
     if x == 'done':
           x = False
      
     else:
           total_price += (menue[items])
           orders.append(items)
print('#*'*20)

print("You order the follwing Items: ")
for i in range(len(orders)):
  print(str(i+1)+" - "+orders[i].title() +" - "+str(menue[orders[i]]))
print("Your Total Price: "+str(total_price))

address = input("Enter your address: ")
print(address)
print("Your Order is accepted!!!\nWe will diliver your order within 30 minutues!")

print('#*#'*20+"\nThanks! Order Again.\n")

