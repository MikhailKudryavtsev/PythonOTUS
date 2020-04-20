import pytest


@pytest.mark.parametrize("item", ['one', 'moon', 'house', 'car'])
def test_presence(item):
    set_items = {'one', 'moon', 'house', 'car'}
    assert item in set_items


def test_set_creation():
    set_items = set('qwerty')
    assert set_items == {'q', 'w', 'e', 'r', 't', 'y'}


def test_comparison():
    one_set_items = set('qwerty')
    two_set_items = set('ytrewq')
    set_items = one_set_items - two_set_items
    assert set_items == set()


def test_remove():
    one_list = {'q', 'w', 'e'}
    one_list.remove('w')
    assert one_list == {'q', 'e'}


def test_add():
    one_list = {'q', 'w', 'e'}
    one_list.add('QWE')
    assert one_list == {'QWE', 'q', 'w', 'e'}
