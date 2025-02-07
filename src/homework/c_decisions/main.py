from decisions import get_faculty_rating, get_options_ratio

option= float(input("Enter Option value.\n"))
total=  float(input("Enter Total value.\n"))

print(get_faculty_rating(get_options_ratio(option,total)))