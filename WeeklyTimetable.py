TIME_DAY_STUDIED_MAPPING = [
    [1, [8, 9, 10, 11]],      # Morning: 8 am to 11 am
    [2, [12, 13, 14, 15]],     # Afternoon: 12 am to 3 pm
    [3, [16, 17, 18, 19,20]],     # Evening: 4 pm to 8 pm
    [4, [21, 22, 23, 24]]      # Midnight: 9 pm to 12 am 
]

def print_weekly_timetable(timetable, days, hours):
    # Print the timetable header with day names
    print("{:<15}".format(""), end="")
    for day in days:
        print("|{:^12}".format(day), end="")
    print()

    # Print each hour row with corresponding subjects for each day
    for hour in range(len(hours)):
        print("{:<15}".format(f"{hours[hour]:02d}:00"), end="")
        for day in range(len(days)):
            print("|{:^12}".format(timetable[hour][day]), end="")
        print()
        
def update_timetable_manually(timetable):
    # Define days and hours
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    hours = list(range(1, 25))

    # Display the generated timetable
    print("Generated Timetable:")
    print_weekly_timetable(timetable, days, hours)

    # Continuously prompt user for manual input
    while True:
        try:
            # Get user input for hour and day
            hour = int(input("Enter hour (1-24, 0 to exit): "))
            if hour == 0:
                break
            day = input("Enter day (Monday-Sunday): ")

            # Validate input
            if hour < 1 or hour > 24 or day.capitalize() not in days:
                print("Invalid input. Please try again.")
                continue

            # Get subject input from the user
            subject = input("Enter Task: ")

            # Update the timetable with the user input
            day_index = days.index(day.capitalize())
            timetable[hour - 1][day_index] = subject

            # Display the updated timetable
            print("\nUpdated Timetable:")
            print_weekly_timetable(timetable, days, hours)

        except ValueError:
            print("Invalid input. Please enter a valid hour (1-24) or day (Monday-Sunday).")

    return timetable
