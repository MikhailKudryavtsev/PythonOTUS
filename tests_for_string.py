import pytest


def test_len():
    string_item = 'AaBbCcDd'
    assert len(string_item) == 8


def test_extraction():
    string_item = 'Hello World!'
    assert string_item[3: 7] == 'lo W'


@pytest.mark.parametrize('item', [100500, '100500'])
def test_comparison(item):
    string_item = '100500'
    assert string_item == item


def test_multiplication():
    string_item = 'Hello World!'
    assert string_item * 3 == 'Hello World!Hello World!Hello World!'


def test_сonvert_to_uppercase():
    string_item = 'Hello World!'
    assert string_item.upper() == 'HELLO WORLD!'
