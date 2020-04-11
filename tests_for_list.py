import pytest

def test_comparison():
    one_list = ['']
    two_list = ['1']
    assert one_list != two_list


@pytest.mark.parametrize("item", ['r', 't', 'y'])
def test_add(item):
    one_list = ['q', 'w', 'e']
    one_list.append(item)
    assert one_list[3] == item


def test_clear():
    one_list = ['q', 'w', 'e']
    one_list.clear()
    assert one_list == []


def test_insert():
    one_list = ['q', 'w', 'e']
    one_list.insert(0, 'QWE')
    assert one_list == ['QWE', 'q', 'w', 'e']


def test_extend():
    one_list = ['']
    two_list = ['1']
    one_list.extend(two_list)
    assert one_list == ['', '1']
