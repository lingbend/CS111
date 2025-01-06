import random
import filecmp
import pytest
from byu_pytest_utils import max_score, with_import, run_python_script, this_folder, test_files, run_python_script


@max_score(2)
@with_import("admissions", "check_row_types")
def test_check_row_types(check_row_types):
    assert not check_row_types([])
    assert not check_row_types([1, 2, 3, 4, 5, 6, 7])
    assert check_row_types([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0])
    assert not check_row_types([1, 2, 3, 4, 5, 6, 7, 8, 9])
    assert not check_row_types([1, 2, 3, 4, 5, 6, 7, 8])
    assert not check_row_types(["1", "2", "3", "4", "5", "6", "7", "8"])
    assert not check_row_types([""])


@max_score(2)
@with_import("admissions", "convert_row_type")
def test_convert_row_type(convert_row_type):
    for _ in range(10):
        ranlist = [random.randint(0, 20) for i in range(random.randint(3, 9))]
        for i in convert_row_type(ranlist):
            assert isinstance(i, float)


@max_score(2)
@with_import("admissions", "calculate_score")
def test_calculate_score(calculate_score):
    assert calculate_score([1330, 3.48, 1, 2]) == pytest.approx(5.77775)
    assert calculate_score([1400.0, 3.67, 0.0, 9.0]) == pytest.approx(7.361)
    assert calculate_score([1190.0, 3.63, 3.0, 3.0]) == pytest.approx(6.03525)
    assert calculate_score([1000.0, 2.62, 1.0, 0.0]) == pytest.approx(4.071)
    assert calculate_score([1380.0, 3.33, 10.0, 10.0]) == pytest.approx(8.2515)


@max_score(2)
@with_import("admissions", "is_outlier")
def test_is_outlier(is_outlier):
    true_cases = [
            [1180.0, 3.38, 0.0, 6.0],
            [1160.0, 2.81, 0.0, 1.0],
            [1270.0, 3.17, 0.0, 1.0],
            [950.0, 4.1, 0.0, 2.0]]
    false_cases = [
            [1200.0, 2.87, 1.0, 3.0],
            [1320.0, 3.54, 10.0, 4.0],
            [1250.0, 3.07, 9.0, 7.0],
            [950.0, 2.79, 1.0, 4.0]]
    for i in true_cases:
        assert is_outlier(i)
    for i in false_cases:
        assert not is_outlier(i)


@max_score(2)
@with_import("admissions", "grade_outlier")
def test_grade_outlier(grade_outlier):
    true_cases = [
            [85.0, 84.0, 98.0, 61.0],
            [96.0, 82.0, 84.0, 58.0],
            [97.0, 86.0, 82.0, 56.0],
            [89.0, 87.0, 83.0, 55.0]]
    false_cases = [
            [91.0, 85.0, 97.0, 88.0],
            [92.0, 92.0, 84.0, 92.0],
            [93.0, 91.0, 89.0, 81.0],
            [91.0, 91.0, 81.0, 83.0]]
    for i in true_cases:
        assert grade_outlier(i)
    for i in false_cases:
        assert not grade_outlier(i)


@max_score(2)
@with_import("admissions", "calculate_score_improved")
def test_calculate_score_improved(calculate_score_improved):
    true_cases = [
            [1180.0, 3.38, 0.0, 6.0],
            [1370.0, 3.63, 9.0, 4.0],
            [980.0, 2.86, 0.0, 3.0],
            [1380.0, 3.33, 10.0, 10.0]]
    false_cases = [
            [1200.0, 2.87, 1.0, 3.0],
            [950.0, 2.79, 1.0, 4.0],
            [930.0, 2.52, 7.0, 0.0],
            [1170.0, 2.93, 8.0, 0.0]]
    for i in true_cases:
        assert calculate_score_improved(i)
    for i in false_cases:
        assert not calculate_score_improved(i)


@max_score(2)
@with_import("admissions", "grade_improvement")
def test_grade_improvement(grade_improvement):
    true_cases = [
            [87.0, 87.0, 91.0, 93.0],
            [85.0, 87.0, 92.0, 98.0],
            [87.0, 87.0, 88.0, 96.0],
            [91.0, 92.0, 96.0, 96.0]]
    false_cases = [
            [91.0, 85.0, 97.0, 88.0],
            [86.0, 83.0, 96.0, 93.0],
            [96.0, 82.0, 89.0, 95.0],
            [90.0, 89.0, 89.0, 97.0]]
    for i in true_cases:
        assert grade_improvement(i)
    for i in false_cases:
        assert not grade_improvement(i)


# Run the student file
@pytest.fixture(scope="module",autouse=True)
def run_program():
    script = this_folder / "admissions.py"
    run_python_script(script)

def convert_file(filename):
    from platform import system
    if system() == "Windows":
        import re
        with open(filename, "rb") as fin:
            buffer = re.sub(b"\r\n", b"\n", fin.read())
        with open(filename, "wb") as fout:
            fout.write(buffer)
    return filename


# Diff
@max_score(6)
def test_student_scores():
    assert filecmp.cmp(test_files / "key_student_scores.csv", convert_file(this_folder / "student_scores.csv"))

@max_score(6)
def test_chosen_students():
    assert filecmp.cmp(test_files / "key_chosen_students.csv", convert_file(this_folder / "chosen_students.csv"))

@max_score(6)
def test_outliers():
    assert filecmp.cmp(test_files / "key_outliers.csv", convert_file(this_folder / "outliers.csv"))

@max_score(6)
def test_chosen_improved():
    assert filecmp.cmp(test_files / "key_chosen_improved.csv", convert_file(this_folder / "chosen_improved.csv"))

@max_score(6)
def test_better_improved():
    assert filecmp.cmp(test_files / "key_better_improved.csv", convert_file(this_folder / "better_improved.csv"))

@max_score(6)
def test_composite_chosen():
    assert filecmp.cmp(test_files / "key_composite_chosen.csv", convert_file(this_folder / "composite_chosen.csv"))
