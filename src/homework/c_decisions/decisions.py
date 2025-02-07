ratio=0
def get_options_ratio(option,total):
        ratio= option/total
        return ratio

def get_faculty_rating(ratio):
    ratio= float(ratio)
    if ratio>=0.9 and ratio<1.0:
        return "Excellent"
    if ratio>0.8 and ratio<0.9:
        return "Very Good"
    if ratio>0.7 and ratio<=0.8:
        return "Good"
    if ratio>0.6 and ratio<=0.7:
        return "Needs Improvement"
    if ratio<=0.6:
        return "Unacceptable"

