# This is my first python file and playing around with git and github
# Initialize daily goal and total water consumed
daily_goal = 64  # You can change this value as needed
total_water = 0

# Main loop for tracking water intake
while True:
    try:
        # Ask the user to input the amount of water consumed
        water_input = input("Enter water consumed in ounces (or type 'done' to stop): ")
        
        # Allow the user to exit the loop
        if water_input.lower() == 'done':
            break

        # Convert input to integer
        water = int(water_input)
        
        # Add the input amount to the total water consumed
        total_water += water
        
        # Display the updated total water consumed
        print(f"Total water consumed: {total_water} ounces")

        # Check if the daily goal has been met or exceeded
        if total_water >= daily_goal:
            print("Congratulations, you've met your daily hydration goal!")
    
    except ValueError:
        # Handle invalid input
        print("Please enter a valid number.")

# End of the day summary
print(f"Final total water consumed today: {total_water} ounces")
if total_water < daily_goal:
    print("You didn't reach your goal today. Try to drink more water tomorrow!")
else:
    print("Great job staying hydrated today!")
