from byuimage import Image
from byu_pytest_utils import max_score, test_files, with_import
import sys

sys.path.append(str(test_files))
import image_solutions  # nopep8


def assert_equal(observed: Image, expected: Image):
    assert observed.width == expected.width
    assert observed.height == expected.height
    for y in range(observed.height):
        for x in range(observed.width):
            observed_pixel = observed.get_pixel(x, y)
            expected_pixel = expected.get_pixel(x, y)
            assert observed_pixel.red == expected_pixel.red, f"The pixels' red values at ({x}, {y}) don't match. Expected `{expected_pixel.red}`, but got `{observed_pixel.red}`."
            assert observed_pixel.green == expected_pixel.green, f"The pixels' green values at ({x}, {y}) don't match. Expected `{expected_pixel.green}`, but got `{observed_pixel.green}`."
            assert observed_pixel.blue == expected_pixel.blue, f"The pixels' blue values at ({x}, {y}) don't match. Expected `{expected_pixel.blue}`, but got `{observed_pixel.blue}`."



@max_score(3)
@with_import('lab05', 'iron_puzzle')
def test_iron_puzzle(iron_puzzle):
    observed = iron_puzzle(test_files / 'iron.png')
    assert_equal(observed, image_solutions.iron_solution)


@max_score(3)
@with_import('lab05', 'west_puzzle')
def test_west_puzzle(west_puzzle):
    observed = west_puzzle(test_files / 'west.png')
    assert_equal(observed, image_solutions.west_solution)


@max_score(3)
@with_import('lab05', 'darken')
def test_darken(darken):
    observed = darken(test_files / 'cougar.png', 0.8)
    assert_equal(observed, image_solutions.darken_solution)


@max_score(3)
@with_import('lab05', 'grayscale')
def test_grayscale(grayscale):
    observed = grayscale(test_files / 'cougar.png')
    assert_equal(observed, image_solutions.grayscale_solution)


@max_score(3)
@with_import('lab05', 'sepia')
def test_sepia(sepia):
    observed = sepia(test_files / 'cougar.png')
    assert_equal(observed, image_solutions.sepia_solution)


@max_score(5)
@with_import('lab05', 'create_left_border')
def test_create_left_border(create_left_border):
    observed = create_left_border(test_files / 'cougar.png', 25)
    assert_equal(observed, image_solutions.create_left_border_solution)
