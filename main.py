from Recommendation import get_recommendation
from StudyPattern import genetic_algorithm
from PDFtopython import extract_uni_timetable
from WeeklyTimetable import generate_weekly_timetable

def main():
    recommendation_dict = get_recommendation()

    # Run genetic algorithm
    best_individual = genetic_algorithm(100, 50, 0.1, recommendation_dict)
    print("Recommended study pattern:")
    print(best_individual)
    
    #Extract the university timetable from PDF
    pdf_path = "Timetable - 8th Sem.pdf"
    uni_timetable = extract_uni_timetable(pdf_path)
    
    #Web Scraping the relevant 
    
    #Generate the timetable
    generate_weekly_timetable(best_individual, uni_timetable)
    
if __name__ == "__main__":
    main()

