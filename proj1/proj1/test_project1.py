from byuimage import Image
from byu_pytest_utils import max_score, run_python_script, test_files
import functools
import pytest


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




@max_score(20)
def test_display_image(monkeypatch):
    observed = None

    @functools.wraps(Image.show)
    def patched_Image_show(self):
        nonlocal observed
        observed = self
    monkeypatch.setattr(Image, 'show', patched_Image_show)

    run_python_script('image_processing.py', '-d',
                      test_files / 'explosion.input.jpg')

    if observed is None:
        pytest.fail('No Image was shown')

    assert_equal(observed, Image(test_files / 'explosion.input.jpg'))


def make_filter_tester(observed_file, key_file, *script_args):
    def decorator(func):
        @functools.wraps(func)
        def inner_func():
            run_python_script('image_processing.py', *script_args)
            assert_equal(Image(observed_file), Image(key_file))
        return inner_func
    return decorator


@max_score(5)
@make_filter_tester(
    'darkened-explosion.output.png', test_files / 'darkened-explosion.key.png',
    '-k', test_files / 'explosion.input.jpg', 'darkened-explosion.output.png', 0.3
)
def test_darken_filter():
    ...


@max_score(5)
@make_filter_tester(
    'sepia-explosion.output.png', test_files / 'sepia-explosion.key.png',
    '-s', test_files / 'explosion.input.jpg', 'sepia-explosion.output.png'
)
def test_sepia_filter():
    ...


@max_score(5)
@make_filter_tester(
    'grayscale-explosion.output.png', test_files / 'grayscale-explosion.key.png',
    '-g', test_files / 'explosion.input.jpg', 'grayscale-explosion.output.png'
)
def test_grayscale_filter():
    ...


@max_score(5)
@make_filter_tester(
    'bordered-explosion.output.png', test_files / 'bordered-explosion.key.png',
    '-b', test_files / 'explosion.input.jpg', 'bordered-explosion.output.png', 10, 120, 20, 14
)
def test_border_filter():
    ...


@max_score(5)
@make_filter_tester(
    'flipped-explosion.output.png', test_files / 'flipped-explosion.key.png',
    '-f', test_files / 'explosion.input.jpg', 'flipped-explosion.output.png'
)
def test_flip_filter():
    ...


@max_score(15)
@make_filter_tester(
    'mirrored-explosion.output.png', test_files / 'mirrored-explosion.key.png',
    '-m', test_files / 'explosion.input.jpg', 'mirrored-explosion.output.png'
)
def test_mirror_filter():
    ...


@max_score(20)
@make_filter_tester(
    'collage.output.png', test_files / 'collage.key.png',
    '-c', test_files / 'beach1.input.jpg', test_files / 'beach2.input.jpg',
    test_files / 'beach3.input.jpg', test_files / 'beach4.input.jpg',
    'collage.output.png', 10
)
def test_collage_filter():
    ...


@max_score(20)
@make_filter_tester(
    'greenscreen.output.png', test_files / 'greenscreen.key.png',
    '-y', test_files / 'man.input.jpg', test_files / 'explosion.input.jpg',
    'greenscreen.output.png', 90, 1.3
)
def test_greenscreen_filter():
    ...
