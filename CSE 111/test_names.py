from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    assert make_full_name ('joshua', 'herr-ing') == 'herr-ing; joshua'
    assert make_full_name ('michael', 'dunn') == 'dunn; michael'
    assert make_full_name ('trevor', 'alred') == 'alred; trevor'

def test_extract_family_name():
    assert extract_family_name ('herr-ing; joshua') == ('herr-ing')
    assert extract_family_name ('dunn; michael') == ('dunn')
    assert extract_family_name ('alred; trevor') == ('alred')

def test_extract_given_name():
    assert extract_given_name ('herr-ing; joshua') == 'joshua'
    assert extract_given_name ('dunn; michael') == 'michael'
    assert extract_given_name ('alred; trevor') == 'trevor'


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])