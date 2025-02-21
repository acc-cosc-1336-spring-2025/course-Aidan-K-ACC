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

def sum_odd_numbers(num):
    sum = 0
    i = 0
    while i <= num:
        if i%2 == 1:
            sum += i
        i += 1
    return sum
