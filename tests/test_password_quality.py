# -*- coding: utf-8 -*-

from swissutil.password_quality import is_acceptable
from swissutil.password_quality import evaluate_string_for_stuff
from swissutil.caesar_cipher import rot15


from swissutil.password_quality import ERROR_MESSAGE, SUCCESS_MESSAGE


def test_is_acceptable():
    # no uppercase
    assert not is_acceptable("testing123")
    # uppercase only first
    assert not is_acceptable("Testing123")
    assert is_acceptable("123Testing")
    assert not is_acceptable("aBCdefgHIJK")


# py.test all about convenience. When a function matches the test signature
# and has specifically named parameters, like capsys in this test and mocker
#  in the below test the user
def test_evaluate_string_for_stuff(capsys):
    #capsys captures sys.stdout and sys.stderr
    assert evaluate_string_for_stuff("123Testing") == 0
    assert evaluate_string_for_stuff("123testinG") != 0

def test_evaluate_string_for_stuff_with_mocking(mocker):
    # mocker can be used to *patch* objects so that instead of
    # a real object a MagicMock object is called.
    # The MagicMock can be e.g. configured to return a value when called
    # to isolate a function from another one.
    mocked_function = mocker.patch("swissutil.password_quality.is_acceptable")
    mocked_function.return_value = True
    assert evaluate_string_for_stuff("not_used") == 0
    assert mocked_function.called_once_with("not_used")

    mocked_function.reset_mock()
    mocked_function.return_value = False
    assert evaluate_string_for_stuff("not_used") != 0
    assert mocked_function.called_once_with("not_used")


