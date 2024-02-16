# print("\t\t|Mon\t|Tues\t|Wed\t|Thurs\t|Fri\t|Sat\t|Sun\t|")
# print("8:00 - 9:00\t|   \t|    \t|   \t|     \t|   \t|   \t|   \t|")
# print("9:00 - 10:00\t|   \t|    \t|   \t|     \t|   \t|   \t|   \t|")
# print("10:00 - 11:00\t|   \t|    \t|   \t|     \t|   \t|   \t|   \t|")
# print("11:00 - 12:00\t|   \t|    \t|   \t|     \t|   \t|   \t|   \t|")
# print("12:00 - 1:00\t|   \t|    \t|   \t|     \t|   \t|   \t|   \t|")
# print("1:00 - 2:00\t|   \t|    \t|   \t|     \t|   \t|   \t|   \t|")
# print("2:00 - 3:00\t|   \t|    \t|   \t|     \t|   \t|   \t|   \t|")
# print("3:00 - 4:00\t|   \t|    \t|   \t|     \t|   \t|   \t|   \t|")
# print("4:00 - 5:00\t|   \t|    \t|   \t|     \t|   \t|   \t|   \t|")
# print("5:00 - 6:00\t|   \t|    \t|   \t|     \t|   \t|   \t|   \t|")
# print("6:00 - 7:00\t|   \t|    \t|   \t|     \t|   \t|   \t|   \t|")
# print("7:00 - 8:00\t|   \t|    \t|   \t|     \t|   \t|   \t|   \t|")
# print("8:00 - 9:00\t|   \t|    \t|   \t|     \t|   \t|   \t|   \t|")
# print("9:00 - 10:00\t|   \t|    \t|   \t|     \t|   \t|   \t|   \t|")
# print("10:00 - 11:00\t|   \t|    \t|   \t|     \t|   \t|   \t|   \t|")
# print("11:00 - 12:00\t|   \t|    \t|   \t|     \t|   \t|   \t|   \t|")

# --------------------------------most accurate
# import random

# DAYS = 7
# HOURS = 12
# PREFERRED_TIME = 4  # 1-Morning, 2-Noon, 3-Evening, 4-Night

# def generate_timetable(total_hours_per_week, days_per_week, hours_per_sitting, preferred_time):
#     timetable = [[" "]*DAYS for _ in range(HOURS)]

#     # If days_per_week is greater than 7, set it to 7
#     days_per_week = min(days_per_week, DAYS)

#     # If days_per_week is less than 7, distribute study days randomly
#     study_days = random.sample(range(DAYS), days_per_week)

#     # Distribute available hours over the preferred time and study days
#     for day in study_days:
#         remaining_hours = total_hours_per_week
#         study_start = preferred_time
#         while remaining_hours > 0 and study_start < HOURS:
#             for hour in range(study_start, min(study_start + hours_per_sitting, HOURS)):
#                 if timetable[hour][day] == " ":
#                     timetable[hour][day] = "X"
#                     remaining_hours -= 1
#             study_start += hours_per_sitting + random.randint(1, 3)  # Add a gap between study sessions

#     return timetable

# def print_timetable(timetable):
#     print("{:<15}".format(""), end="")
#     for day in range(DAYS):
#         print("|{:^7}".format(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"][day]), end="")
#     print()

#     for hour in range(HOURS):
#         print("{:<15}".format(f"{hour+8:02d}:00 - {hour+9:02d}:00"), end="")
#         for day in range(DAYS):
#             print("|{:^7}".format(timetable[hour][day]), end="")
#         print()

# # User inputs
# total_hours_per_week = 20
# days_per_week = 5  # You can change this to any value between 1 and 7
# hours_per_sitting = 2
# preferred_time = PREFERRED_TIME

# # Generate and print the timetable
# timetable = generate_timetable(total_hours_per_week, days_per_week, hours_per_sitting, preferred_time)
# print_timetable(timetable)


# import random

# DAYS = 7
# HOURS = 12
# PREFERRED_TIME = 4  # 1-Morning, 2-Noon, 3-Evening, 4-Night

# def generate_timetable(total_hours_per_week, days_per_week, hours_per_sitting, preferred_time):
#     timetable = [[" "]*DAYS for _ in range(HOURS)]

#     # If days_per_week is greater than 7, set it to 7
#     days_per_week = min(days_per_week, DAYS)

#     # If days_per_week is less than 7, distribute study days randomly
#     study_days = random.sample(range(DAYS), days_per_week)

#     # Distribute available hours over the preferred time and study days
#     for day in study_days:
#         remaining_hours = total_hours_per_week
#         study_start = preferred_time
#         while remaining_hours > 0 and study_start < HOURS:
#             for hour in range(study_start, min(study_start + hours_per_sitting, HOURS)):
#                 if timetable[hour][day] == " ":
#                     timetable[hour][day] = "X"
#                     remaining_hours -= 1
#             study_start += hours_per_sitting + random.randint(1, 3)  # Add a gap between study sessions

#     return timetable

# def print_timetable(timetable):
#     print("{:<15}".format(""), end="")
#     for day in range(DAYS):
#         print("|{:^7}".format(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"][day]), end="")
#     print()

#     for hour in range(HOURS):
#         print("{:<15}".format(f"{hour+8:02d}:00 - {hour+9:02d}:00"), end="")
#         for day in range(DAYS):
#             print("|{:^7}".format(timetable[hour][day]), end="")
#         print()

# # User inputs
# total_hours_per_week = 20
# days_per_week = 5  # You can change this to any value between 1 and 7
# hours_per_sitting = 2
# preferred_time = PREFERRED_TIME

# # Generate and print the timetable
# timetable = generate_timetable(total_hours_per_week, days_per_week, hours_per_sitting, preferred_time)
# print_timetable(timetable)

# ---------------------using genetic algo: -------------------------------
import random

DAYS = 7
HOURS = 12
PREFERRED_TIME = 4  # 1-Morning, 2-Noon, 3-Evening, 4-Night

def initialize_population(population_size):
    return [[random.randint(0, 1) for _ in range(DAYS * HOURS)] for _ in range(population_size)]

def calculate_fitness(individual, total_hours_per_week, hours_per_sitting):
    study_hours = sum(individual)
    return abs(study_hours - total_hours_per_week) + individual.count(1) * (hours_per_sitting - 1)

def crossover(parent1, parent2):
    crossover_point = random.randint(0, len(parent1) - 1)
    child = parent1[:crossover_point] + parent2[crossover_point:]
    return child

def mutate(individual, mutation_rate):
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            individual[i] = 1 - individual[i]
    return individual

def get_study_time(preferred_time):
    if preferred_time == 4:  
        return random.randint(8, 11)
    else:
        return random.randint(0, 7)

def generate_timetable(total_hours_per_week, days_per_week, hours_per_sitting, preferred_time, population_size, generations, mutation_rate):
    population = initialize_population(population_size)

    for generation in range(generations):
        fitness_scores = [calculate_fitness(individual, total_hours_per_week, hours_per_sitting) for individual in population]
        sorted_indices = sorted(range(len(fitness_scores)), key=lambda k: fitness_scores[k])

        # Select the top 50% of individuals as parents
        parents = [population[i] for i in sorted_indices[:population_size // 2]]

        # Generate offspring through crossover and mutation
        offspring = []
        while len(offspring) < population_size - len(parents):
            parent1 = random.choice(parents)
            parent2 = random.choice(parents)
            child = mutate(crossover(parent1, parent2), mutation_rate)
            offspring.append(child)

        # Replace the old population with the new generation
        population = parents + offspring

    best_individual = min(population, key=lambda x: calculate_fitness(x, total_hours_per_week, hours_per_sitting))
    return best_individual

def print_timetable(individual):
    print("{:<15}".format(""), end="")
    for day in range(DAYS):
        print("|{:^7}".format(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"][day]), end="")
    print()

    for hour in range(HOURS):
        print("{:<15}".format(f"{hour+8:02d}:00 - {hour+9:02d}:00"), end="")
        for day in range(DAYS):
            print("|{:^7}".format("X" if individual[hour * DAYS + day] == 1 else ""), end="")
        print()

# User inputs - only frm web page
total_hours_per_week = 10
days_per_week = 5  
hours_per_sitting = 2
preferred_time = PREFERRED_TIME
population_size = 100
generations = 100
mutation_rate = 0.1

# Run the genetic algorithm to generate timetable
best_solution = generate_timetable(total_hours_per_week, days_per_week, hours_per_sitting, preferred_time, population_size, generations, mutation_rate)

# Print the best timetable
print_timetable(best_solution)
