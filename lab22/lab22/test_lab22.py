from byu_pytest_utils import max_score, test_files, with_import
from byuimage import Image


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


@max_score(6)
@with_import('lab22', 'plot_histogram')
def test_plot_histogram(plot_histogram):
    sat_key = Image(test_files / 'sat_score.key.png')
    gpa_key = Image(test_files / 'gpa.key.png')

    plot_histogram()

    sat_observed = Image('sat_score.png')
    gpa_observed = Image('gpa.png')

    assert_equal(sat_observed, sat_key)
    assert_equal(gpa_observed, gpa_key)


@max_score(6)
@with_import('lab22', 'plot_scatter')
def test_plot_scatter(plot_scatter):
    correlation_key = Image(test_files / 'correlation.key.png')
    plot_scatter()
    correlation_observed = Image('correlation.png')
    assert_equal(correlation_observed, correlation_key)


@max_score(8)
@with_import('lab22', 'plot_spectra')
def test_plot_spectra(plot_spectra):
    spectra_key = Image(test_files / 'spectra.key.png')
    plot_spectra()
    spectra_observed = Image('spectra.png')
    assert_equal(spectra_observed, spectra_key)
