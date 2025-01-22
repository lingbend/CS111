# Provided code
# This function checks to ensure that a list is of length
# 8 and that each element is type float
# Parameters:
# row - a list to check
# Returns True if the length of row is 8 and all elements are floats
def check_row_types(row):
    if len(row) != 8:
        print("Length incorrect! (should be 8): " + str(row))
        return False
    ind = 0
    while ind < len(row):
        if type(row[ind]) != float:
            print("Type of element incorrect: " + str(row[ind]) + " which is " + str(type(row[ind])))
            return False
        ind += 1
    return True

# define your functions here


def convert_row_type(student_data):
    return [float(i) for i in student_data]


def calculate_score(metrics):
    sat = metrics[0] / 160
    gpa = metrics[1] * 2
    interest = metrics[2]
    hs_quality = metrics[3]
    return (sat * .3) + (gpa * .4) + (interest * .1) + (hs_quality * .2)
    # return ((metrics[0] / 160)* .3) + ((metrics[1] * 2) * .4) + (metrics[2] * .1) + (metrics[3] * .2)


def is_outlier(metric):
    sat = metric[0] / 160
    gpa = metric[1] * 2
    interest = metric[2]
    return (not interest or (gpa > sat + 2))


def calculate_score_improved(student_data):
    student_score = calculate_score(student_data)
    if student_score >= 6 or is_outlier(student_data):
        return True


def grade_outlier(grades):
    lowest = grades[0]
    second_lowest = None
    for grade in grades:
        if grade < lowest:
            second_lowest = lowest
            lowest = grade
        elif second_lowest is None:
            second_lowest = grade
    difference = second_lowest - lowest
    if difference > 20:
        return True


def grade_improvement(grades):
    for i in range(len(grades)):
        if i == 0:
            continue
        elif grades[i] < grades[(i-1)]:
            return False
    return True


def outlier_condition(semester_grades, student_metric):
    return is_outlier(student_metric) or grade_outlier(semester_grades) or grade_improvement(semester_grades)


def main():
    filename = "admission_algorithms_dataset.csv"
    input_file = open(filename, "r")
    out_score_file = open("student_scores.csv", "w")
    out_chosen_file = open("chosen_students.csv", "w")
    out_outliers_file = open("outliers.csv", "w")
    out_better_file = open("better_improved.csv", "w")
    out_composite_file = open("composite_chosen.csv", "w")
    out_improved_file = open("chosen_improved.csv", "w")

    file_data = input_file.readlines()
    processed_data = []

    print("Processing " + filename + "...")
    # grab the line with the headers
    headers = file_data.pop(0)

    # make each line into a list of strings and add that list to the list of data
    for i in range(len(file_data)):
        data_list = file_data[i].strip().split(',')
        name = data_list[0]
        # remove the names from the data and put them in their own list
        data_list.remove(name)
        # change strings to floats and add to list
        data_list = convert_row_type(data_list)
        if not check_row_types(data_list):
            print('Error: too much data / data is not numbers.')
        processed_data.append(data_list)
        # get students score
        score = calculate_score(data_list)
        out_score_file.write(f'{name},{score:.2f}\n')
        # check for normal qualifications and write to file
        if score >= 6:
            out_chosen_file.write(f'{name}\n')

        # separate semester grades from other variables
        student_metric = data_list[:4]
        semester_grades = data_list[4:]

        # check if student is outlier and write to file
        if is_outlier(student_metric):
            out_outliers_file.write(f'{name}\n')

        # use outliers and score to create improved list
        if score >= 6 or (is_outlier(student_metric) and score >= 5):
            out_improved_file.write(f'{name}\n')

        # check more accurately for qualifying students and write to file
        if calculate_score_improved(student_metric):
            better_data = [name]
            better_data += [str(i) for i in student_metric]
            better_data = ','.join(better_data) + '\n'
            out_better_file.write(better_data)
        grade_outlier(semester_grades)

        # use composite methods to determine eligibility and write to file
        if score >= 6:
            out_composite_file.write(f'{name}\n')
        elif score >= 5 and outlier_condition(semester_grades, student_metric):
            out_composite_file.write(f'{name}\n')

    # bookkeeping
    out_improved_file.close()
    out_composite_file.close()
    out_better_file.close()
    out_outliers_file.close()
    out_chosen_file.close()
    out_score_file.close()
    input_file.close()

    print("done!")


# this bit allows us to both run the file as a program or load it as a
# module to just access the functions
if __name__ == "__main__":
    main()
