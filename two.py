book1=int(input("Enter no.of Introduction to Python Programming Book: "))
book2=int(input("Enter no.of Python Libraries Cookbook Book: "))
book3=int(input("Enter no.of Data Science in Pyhton Book: "))
cost=book1*499.0+book2*855.0+book3*645.0
delivery_charges=250.0
total_cost=cost+cost*(12/100)+250.0
print(total_cost)
