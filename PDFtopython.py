import pdfplumber

def extract_uni_timetable(pdf_path):
    timetable = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            table = page.extract_table()
            if table:
                for row in table[1:]:  # Skip the header row
                    time_slot = row[0]
                    for i, subject in enumerate(row[1:], start=1):
                        day = table[0][i]  # Assume the first row contains the days
                        if subject.strip() == "NLP (AMP)" or subject.strip() == "DL (SRO)":
                            timetable.append((time_slot, day, subject.strip()))
                            print(f"{{Slot: {time_slot}, Day: {day}, Subject: {subject.strip()}}}")
    return timetable

pdf_path = "Timetable - 8th Sem.pdf"
uni_timetable = extract_uni_timetable(pdf_path)



