TIME_DAY_STUDIED_MAPPING = [
    [1, [8, 9, 10, 11]],      # Morning: 8 am to 11 am
    [2, [12, 13, 14, 15]],     # Afternoon: 12 am to 3 pm
    [3, [16, 17, 18, 19,20]],     # Evening: 4 pm to 8 pm
    [4, [21, 22, 23, 24]]      # Midnight: 9 pm to 12 am 
]
        
def merge_timetables(best_individual, uni_timetable):
    
     # Define days and hours
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    hours = list(range(1, 25))
    
    # Initialize timetable with all cells empty
    timetable = [[' ' for _ in range(len(days))] for _ in range(len(hours))]

    # Extract values from the best individual
    hours_week = best_individual[1][1][0] 
    days_studied_week =  best_individual[1][1][1]
    hours_at_time = best_individual[1][1][2]
    time_day_studied_index = best_individual[0][3]

    # Map the time_day_studied using the mapping list
    time_day_studied = TIME_DAY_STUDIED_MAPPING[time_day_studied_index-1][1]
    
    # Select the specified number of days from the list of days
    days_studied = days[:days_studied_week]
    print(days_studied)
    
    total_hours_distributed = 0  # Initialize total hours distributed
    
    # Calculate average study hours per day
    average_hours_per_day = hours_week // days_studied_week
    
    # Distribute average study hours per day across all selected days
    total_hours_distributed = 0
    for day_index, day in enumerate(days_studied):
        hours_distributed_today = 0
        while hours_distributed_today < average_hours_per_day and total_hours_distributed < hours_week:
            for hour in time_day_studied:
                if total_hours_distributed >= hours_week or hours_distributed_today >= average_hours_per_day:
                    break
                if hour < time_day_studied[-1]:
                    for consecutive_hour in range(min(hours_at_time, time_day_studied[-1] - hour + 1)):
                        current_hour = hour + consecutive_hour
                        if total_hours_distributed >= hours_week or current_hour > time_day_studied[-1] or hours_distributed_today >= average_hours_per_day:
                            break
                        if timetable[current_hour - 1][day_index] != 'study':
                            timetable[current_hour - 1][day_index] = 'study'
                            total_hours_distributed += 1
                            hours_distributed_today += 1
                            print(f"Marked cell: ({current_hour}, {days_studied[day_index]})")
                            print("Total hours distributed:", total_hours_distributed)


    # Calculate remainder hours per day
    remainder_hours_per_day = hours_week % days_studied_week
    
    # Distribute remaining hours from the start of the selected days
    day_index = 0
    while total_hours_distributed < hours_week:
        for hour in time_day_studied:
            if total_hours_distributed >= hours_week:
                break
            if hour < time_day_studied[-1]:
                for consecutive_hour in range(min(hours_at_time, remainder_hours_per_day)):
                    current_hour = hour + consecutive_hour
                    if total_hours_distributed >= hours_week or current_hour > time_day_studied[-1]:
                        break
                    if timetable[current_hour - 1][day_index] != 'study':
                        timetable[current_hour - 1][day_index] = 'study'
                        total_hours_distributed += 1
                        print(f"Marked cell: ({current_hour}, {days_studied[day_index]})")
                        print("Total hours distributed:", total_hours_distributed)
        day_index = (day_index + 1) % len(days_studied)
        
    # Distribute subjects from the university timetable
    for entry in uni_timetable:
        slot, day, subject = entry
        # Adjust slot format
        slot = slot.replace(' ', '').replace('-', ' - ')
        # Construct the timetable entry as a string
        timetable_entry = f"{subject}"
        print(timetable_entry)

        # Parse slot to get start and end hours
        start_hour, end_hour = slot.split(' - ')
        start_hour = int(start_hour.split(':')[0])
        end_hour = int(end_hour.split(':')[0])

        # Find the corresponding indices for day and hours
        day_index = days.index(day)

        # Update the timetable with the subject for each hour slot
        for hour in range(start_hour, end_hour + 1):
            timetable[hour - 1][day_index] = timetable_entry
            
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


    return timetable