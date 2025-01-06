from byu_pytest_utils import max_score, with_import


def get_request_guard(RequestGuard):
    guard = RequestGuard("https://cs111.byu.edu")
    # Mocking a different robots.txt
    guard.forbidden = ['/data', '/images', '/lectures']
    return guard

@max_score(8)
@with_import('RequestGuard', 'RequestGuard')
def test_request_guard_1(RequestGuard):
    guard = get_request_guard(RequestGuard)
    assert not guard.can_follow_link('https://byu.edu')


@max_score(8)
@with_import('RequestGuard', 'RequestGuard')
def test_request_guard_2(RequestGuard):
    guard = get_request_guard(RequestGuard)
    assert guard.can_follow_link('https://cs111.byu.edu/HW/HW01')


@max_score(8)
@with_import('RequestGuard', 'RequestGuard')
def test_request_guard_3(RequestGuard):
    guard = get_request_guard(RequestGuard)
    assert not guard.can_follow_link(
        'https://cs111.byu.edu/images/logo.png')


@max_score(8)
@with_import('RequestGuard', 'RequestGuard')
def test_request_guard_4(RequestGuard):
    guard = get_request_guard(RequestGuard)
    assert not guard.can_follow_link(
        'https://cs111.byu.edu/data/spectra1.txt')


@max_score(8)
@with_import('RequestGuard', 'RequestGuard')
def test_request_guard_5(RequestGuard):
    guard = get_request_guard(RequestGuard)
    assert guard.can_follow_link(
        'https://cs111.byu.edu/Projects/Project4/images/cat.jpg')


@max_score(10)
@with_import('RequestGuard', 'RequestGuard')
def test_parse_robots(RequestGuard):
    guard = get_request_guard(RequestGuard)
    assert RequestGuard('https://cs111.byu.edu').forbidden == ['/proj/proj4/assets/page5.html']
