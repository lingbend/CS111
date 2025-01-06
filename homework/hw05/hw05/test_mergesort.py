from byu_pytest_utils import dialog, max_score, test_files, this_folder


@max_score(15)
@dialog(
    test_files / 'test1.dialog.txt',
    'mergesort.py', test_files / 'test1.input.txt', this_folder / 'test1.output.txt',
    output_file=this_folder / 'test1.output.txt'
)
def test_mergesort_already_sorted_data():
    ...


@max_score(15)
@dialog(
    test_files / 'test2.dialog.txt',
    'mergesort.py', test_files / 'test2.input.txt', this_folder / 'test2.output.txt',
    output_file=this_folder / 'test2.output.txt'
)
def test_mergesort_revered_data():
    ...


@max_score(20)
@dialog(
    test_files / 'test3.dialog.txt',
    'mergesort.py', test_files / 'test3.input.txt', this_folder / 'test3.output.txt',
    output_file=this_folder / 'test3.output.txt'
)
def test_mergesort_shuffled_data():
    ...
