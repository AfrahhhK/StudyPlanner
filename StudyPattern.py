import random

# Define mappings
HOURS_WEEK_MAPPING = [
    [1, 1, 2, 3, 4],
    [2, 5, 6, 7, 8, 9, 10],
    [3, 10, 11, 12, 13, 14, 15],
    [4, 15, 16, 17, 18, 19, 20],
    [5, 21, 22, 23, 24] 
]

DAYS_STUDIED_WEEK_MAPPING = [
    [1, 1],
    [2, 2, 3],
    [3, 4],
    [4, 5],
    [5, 6, 7] 
]

HOURS_AT_TIME_WEEK_MAPPING = [
    [1, 1],
    [2, 2],
    [3, 3],
    [4, 4] 
]

TIME_DAY_STUDIED_MAPPING = [
    [1, [8, 9, 10, 11]],      # Morning: 8 am to 11 am
    [2, [12, 13, 14, 15]],     # Afternoon: 12 am to 3 pm
    [3, [16, 17, 18, 19,20]],     # Evening: 4 pm to 8 pm
    [4, [21, 22, 23, 24]]      # Midnight: 9 pm to 12 am 
]
    
def fitness(study_pattern, total_hours_per_week_list, days_studied_per_week_list, hours_at_time_list):
    best_fitness = float('inf')
    best_params = None
    hours_at_time = hours_at_time_list
    
    for total_hours_per_week in total_hours_per_week_list:
        for days_studied_per_week in days_studied_per_week_list:
            
            # Initialize penalty for violating constraints
            penalty = 0
            
            # Constraint 1: Total hours per week
            total_hours = sum(study_pattern)
            if total_hours > total_hours_per_week:
                penalty += total_hours - total_hours_per_week
            
            # Constraint 2: Days per week
            for day_start in range(0, len(study_pattern), 24):
                daily_hours = sum(study_pattern[day_start:day_start + 24])
                if daily_hours > 0:
                    # Check if day is outside allowed days_per_week range
                    if day_start >= days_studied_per_week * 24:
                        penalty += daily_hours
            
            # Constraint 3: Hours per sitting
            for day_start in range(0, len(study_pattern), 24 * days_studied_per_week):
                for hour_start in range(0, 24, hours_at_time):
                    sitting_hours = sum(study_pattern[day_start + hour_start:day_start + hour_start + hours_at_time])
                    if sitting_hours > hours_at_time:
                        penalty += sitting_hours - hours_at_time
            
            # Calculate fitness score
            fitness_score = total_hours + penalty
            
            # Print fitness score for each combination
            print(f"Total Hours per Week: {total_hours_per_week}, Days Studied per Week: {days_studied_per_week}, Hours at a Time: {hours_at_time}, Fitness: {fitness_score}")
            
            # Store the best fitness and parameters
            if fitness_score < best_fitness:
                best_fitness = fitness_score
                best_params = (total_hours_per_week, days_studied_per_week, hours_at_time)
    
    return best_fitness, best_params


def initialize_population(population_size):
    population = []
    for _ in range(population_size):
        hours_week = random.choice(range(1, len(HOURS_WEEK_MAPPING) + 1))
        days_studied_week = random.choice(range(1, len(DAYS_STUDIED_WEEK_MAPPING) + 1))
        hours_at_time = random.choice(range(1, len(HOURS_AT_TIME_WEEK_MAPPING) + 1))
        time_day_studied = random.choice(range(1, len(TIME_DAY_STUDIED_MAPPING) + 1))
        population.append((hours_week, days_studied_week, hours_at_time, time_day_studied))
    return population


def crossover(parent1, parent2):
    # Convert parents to lists
    parent1_list = list(parent1)
    parent2_list = list(parent2)
    
    # Perform crossover (you can choose a suitable method)
    crossover_point = random.randint(1, 3)
    child1 = parent1_list[:crossover_point] + parent2_list[crossover_point:]
    child2 = parent2_list[:crossover_point] + parent1_list[crossover_point:]
    return child1, child2

def mutate(study_pattern):
    # Convert study_pattern tuple to a list for mutation
    study_pattern_list = list(study_pattern)
    
    # Perform mutation (you can choose a suitable method)
    gene_to_mutate = random.randint(0, 3)
    if gene_to_mutate == 0:
        study_pattern_list[0] = random.choice(range(1, len(HOURS_WEEK_MAPPING) + 1))
    elif gene_to_mutate == 1:
        study_pattern_list[1] = random.choice(range(1, len(DAYS_STUDIED_WEEK_MAPPING) + 1))
    elif gene_to_mutate == 2:
        study_pattern_list[2] = random.choice(range(1, len(HOURS_AT_TIME_WEEK_MAPPING) + 1))
    elif gene_to_mutate == 3:
        study_pattern_list[3] = random.choice(range(1, len(TIME_DAY_STUDIED_MAPPING) + 1))
    
    # Convert back to a tuple before returning
    return study_pattern_list

def selection(population, total_hours_per_week_list, days_studied_per_week_list, hours_at_time_list):
    # Evaluate fitness for each individual in the population
    fitness_scores = [fitness(individual, total_hours_per_week_list, days_studied_per_week_list, hours_at_time_list) for individual in population]
    
    # Select the individuals with the highest fitness scores
    selected_indices = sorted(range(len(population)), key=lambda x: fitness_scores[x], reverse=True)[:int(len(population) * 0.5)]
    selected_population = [population[i] for i in selected_indices]
    
    return selected_population

def genetic_algorithm(population_size, num_generations, mutation_rate, recommendation_dict):
    total_hours_per_week_list = recommendation_dict['hours_week']
    days_studied_per_week_list = recommendation_dict['days_studied_week']
    hours_at_time_list = recommendation_dict['hours_at_time']
    #time_day_studied_list = recommendation_dict['time_day_studied_list']
    #use all combinations and get the most best marked ones in the fitness
    
    population = initialize_population(population_size)
    for generation in range(num_generations):
        # Evaluate fitness for each individual in the population
        fitness_scores = [fitness(individual, total_hours_per_week_list, days_studied_per_week_list, hours_at_time_list) for individual in population]

        # Selection
        selected_population = selection(population, total_hours_per_week_list, days_studied_per_week_list, hours_at_time_list)

        # Crossover
        offspring_population = []
        for i in range(0, len(selected_population), 2):
            if i + 1 < len(selected_population):
                child1, child2 = crossover(selected_population[i], selected_population[i + 1])
                offspring_population.extend([child1, child2])

        # Mutation
        for i in range(len(offspring_population)):
            if random.random() < mutation_rate:
                offspring_population[i] = mutate(offspring_population[i])

        # New generation
        population = selected_population + offspring_population

    # Get the best individual based on the highest fitness score
    best_fitness = max(fitness_scores)
    best_individual_index = fitness_scores.index(best_fitness)
    best_individual_params = population[best_individual_index]
    
    return best_individual_params, best_fitness

def print_possibilities_fitness(population, recommendation_dict):
    total_hours_per_week = recommendation_dict['hours_week']
    days_per_week = recommendation_dict['days_studied_week']
    hours_per_sitting = recommendation_dict['hours_at_time']
    
    print("All possibilities with their fitness scores:")
    for study_pattern in population:
        fitness_score = fitness(study_pattern, total_hours_per_week, days_per_week, hours_per_sitting)
        print(f"Study Pattern: {study_pattern}, Fitness Score: {fitness_score}")

