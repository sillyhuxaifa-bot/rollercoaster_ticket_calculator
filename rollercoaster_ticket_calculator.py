# Rollercoaster Ticket Calculator

# This program checks whether a person can ride the rollercoaster

# and calculates the total ticket price based on age and photo choice.

print("Welcome to the RollerCoastahhh!")

bill = 0

# Ask the user for their height

height = int(input("Enter your height (cm): "))

# Check if the user meets the minimum height requirement

if height >= 120:
  print("Great! You can ride the rollercoaster.")         
  
  # Ask the user's age
  age = int(input("Enter your age: "))
  # Calculate ticket price based on age
  if age <= 12:          
    bill += 5          
    print("Child Ticket: $5")          
  elif age <= 18:
    bill += 7          
    print("Youth Ticket: $7")          
  elif age >= 45 and age <= 55:       
    print("Good news! Your ride is on us!")          
  else:          
    bill += 12          
    print("Adult Ticket: $12")          

  while True:
    # Ask if the user wants a ride photo
    wants_photos = input("Would you like a ride photo? (y/n): ").lower()  
    if wants_photos == "y":          
      bill += 3          
      print("Photo added: $3")    
      break    
    elif wants_photos == "n":        
      print("No photos selected")     
      break    
    else:          
      print('please type "y" for Yes or "n" for No')         
  print(f"Your total bill is: ${bill}")

else:
  print("Sorry, you must be at least 120 cm tall to ride.")