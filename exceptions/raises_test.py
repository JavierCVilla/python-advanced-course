from raises import myraises_generator as myraises

def test_expected_exception():
    with myraises(ValueError):
        raise ValueError
    assert True

def test_unexpected_exception():
    try:
        with myraises(ValueError):
            raise IndexError
    except AssertionError:
        assert True
    except:
        assert False
    else:
        assert False

def test_no_exception():
    try:
        with myraises(IndexError):
            pass
    except AssertionError:
        assert True
    except:
        assert False
    else:
        assert False
