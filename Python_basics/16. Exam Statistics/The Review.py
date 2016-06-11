"""Review: printing all grades, finding total, average, variance, standard deviation"""
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades):
    for grade in grades:
        print grade

def grades_sum(grades):
    total = 0
    print_grades(grades)
    for grade in grades: 
        total += grade
    print "Sum of grades: ", total
    return total
    
def grades_average(grades):
    sum_of_grades = grades_sum(grades)
    average = sum_of_grades / float(len(grades))
    print "Average= ", average
    return average

def grades_variance(scores):
    average = grades_average(scores)
    variance = 0.0
    for score in scores:
        variance += float((average - score) ** 2)
    variance = float(variance/len(scores))
    print "Variance = ", variance
    return variance

def grades_std_deviation(variance):
    std_dev = float(variance ** 0.5)
    return std_dev
    
variance = grades_variance(grades)
print grades_std_deviation(variance)
