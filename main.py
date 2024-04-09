from Recommendation import get_recommendation
from StudyPattern import genetic_algorithm, generate_weekly_timetable

# User inputs
def main():
    recommendation_dict = get_recommendation()

    # Run genetic algorithm
    best_individual = genetic_algorithm(100, 50, 0.1, recommendation_dict)
    print("Recommended study pattern:")
    print(best_individual)
    generate_weekly_timetable(best_individual)
    
if __name__ == "__main__":
    main()

