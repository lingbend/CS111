from byu_pytest_utils import max_score, run_python_script, test_files, this_folder, with_import
from byuimage import Image
from matplotlib import pyplot as plt


def do_invalid_args_test(capsys, *args):
    try:
        run_python_script(str(this_folder / 'webcrawler.py'), *args)
    except SystemExit:
        pass  # ignore any exceptions
    captured = capsys.readouterr()
    assert 'invalid arguments' in captured.out.lower()


@max_score(10)
def test_invalid_arguments(capsys):
    do_invalid_args_test(capsys)
    do_invalid_args_test(capsys, 'asdf')
    do_invalid_args_test(capsys, '-a')
    do_invalid_args_test(capsys, '-c')
    do_invalid_args_test(capsys, '-c', 'https://cs111.byu.edu/')
    do_invalid_args_test(capsys, '-p')
    do_invalid_args_test(capsys, '-p', 'https://cs111.byu.edu/')
    do_invalid_args_test(capsys, '-i')
    do_invalid_args_test(capsys, '-i', 'https://cs111.byu.edu/')
    do_invalid_args_test(capsys, '-i', 'https://cs111.byu.edu/', 'asdf_', '-a')


request_guard_works = False


@max_score(15)
@with_import('RequestGuard', 'RequestGuard')
def test_request_guard(RequestGuard):
    guard = RequestGuard('https://cs111.byu.edu')
    # Mocking a different robots.txt
    guard.forbidden = ["/data", "/images/jpg", "/Projects/Project4/Project4.md"]

    assert not guard.can_follow_link('https://byu.edu/')
    assert guard.can_follow_link('https://cs111.byu.edu/')
    assert guard.can_follow_link('https://cs111.byu.edu/asdf.html')
    assert not guard.can_follow_link('https://cs111.byu.edu/data/')
    assert not guard.can_follow_link('https://cs111.byu.edu/data/asdf.csv')
    assert guard.can_follow_link('https://cs111.byu.edu/images/asdf.jpg')
    assert guard.can_follow_link(
        'https://cs111.byu.edu/images/png/asdf.png')
    assert not guard.can_follow_link('https://cs111.byu.edu/images/jpg/')
    assert not guard.can_follow_link(
        'https://cs111.byu.edu/images/jpg/asdf.jpg')
    assert guard.can_follow_link(
        'https://cs111.byu.edu/Projects/Project4/')
    assert guard.can_follow_link(
        'https://cs111.byu.edu/Projects/Project4/Project3.md')
    assert not guard.can_follow_link(
        'https://cs111.byu.edu/Projects/Project4/Project4.md')

    global request_guard_works
    request_guard_works = True


def assert_equal(observed: Image, expected: Image):
    assert observed.width == expected.width
    assert observed.height == expected.height
    for y in range(observed.height):
        for x in range(observed.width):
            observed_pixel = observed.get_pixel(x, y)
            expected_pixel = expected.get_pixel(x, y)
            assert observed_pixel.red == expected_pixel.red, f"the pixels at ({x}, {y}) don't match"
            assert observed_pixel.green == expected_pixel.green, f"the pixels at ({x}, {y}) don't match"
            assert observed_pixel.blue == expected_pixel.blue, f"the pixels at ({x}, {y}) don't match"


@max_score(25)
def test_count_links():
    assert request_guard_works, 'RequestGuard must work before the rest of the assignment can be tested'

    plt.clf()
    run_python_script(
        this_folder / 'webcrawler.py', '-c',
        'https://cs111.byu.edu/proj/proj4/assets/page1.html',
        this_folder / 'count_links.output.png',
        this_folder / 'count_links.output.csv'
    )

    observed = Image(this_folder / 'count_links.output.png')
    expected = Image(test_files / 'count_links.key.png')
    assert_equal(observed, expected)

    with open(this_folder / 'count_links.output.csv') as fin:
        observed = fin.read()
    with open(test_files / 'count_links.key.csv') as fin:
        expected = fin.read()
    assert observed == expected


@max_score(25)
def test_plot_data():
    assert request_guard_works, 'RequestGuard must work before the rest of the assignment can be tested'

    plt.clf()
    run_python_script(
        this_folder / 'webcrawler.py', '-p',
        'https://cs111.byu.edu/proj/proj4/assets/data.html',
        this_folder / 'plot_data.output.png',
        this_folder / 'plot_data.output.csv'
    )

    observed = Image(this_folder / 'plot_data.output.png')
    expected = Image(test_files / 'plot_data.key.png')
    assert_equal(observed, expected)

    with open(this_folder / 'plot_data.output.csv') as fin:
        observed = fin.read()
    with open(test_files / 'plot_data.key.csv') as fin:
        expected = fin.read()
    assert observed == expected


def modify_images_test(images, prefix, filter):
    run_python_script(
        this_folder / 'webcrawler.py', '-i',
        'https://cs111.byu.edu/proj/proj4/assets/images.html',
        prefix, filter
    )

    for image in images:
        observed = Image(f'{prefix}{image}')
        expected = Image(test_files / f'{prefix}{image}')
        assert_equal(observed, expected)


@max_score(6.25)
def test_modify_images_sepia():
    assert request_guard_works, 'RequestGuard must work before the rest of the assignment can be tested'
    modify_images_test(['flamingo-float.png', 'landscape.png'], 's_', '-s')


@max_score(6.25)
def test_modify_images_grayscale():
    assert request_guard_works, 'RequestGuard must work before the rest of the assignment can be tested'
    modify_images_test(['flamingo-float.png', 'landscape.png'], 'g_', '-g')


@max_score(6.25)
def test_modify_images_vertical_flip():
    assert request_guard_works, 'RequestGuard must work before the rest of the assignment can be tested'
    modify_images_test(['flamingo-float.png', 'landscape.png'], 'f_', '-f')


@max_score(6.25)
def test_modify_images_horizontal_flip():
    assert request_guard_works, 'RequestGuard must work before the rest of the assignment can be tested'
    modify_images_test(['flamingo-float.png', 'landscape.png'], 'm_', '-m')