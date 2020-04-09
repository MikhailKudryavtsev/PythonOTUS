import pytest


@pytest.mark.parametrize("item", [34, 29, 12, 59])
def test_append(item):
    dict_item = {'hour': 12, 'minutes': 59}
    dict_item['second'] = item
    assert dict_item == {'hour': 12, 'minutes': 59, 'second': item}


def test_del():
    dict_item = {'fruit': 'apple', 'vegetable': 'potato', 'berry': 'watermelon'}
    del dict_item['vegetable']
    assert dict_item == {'fruit': 'apple', 'berry': 'watermelon'}


def test_presence():
    dict_item = {'fruit': 'apple', 'vegetable': 'potato', 'berry': 'watermelon'}
    assert 'berry' in dict_item


def test_comparison():
    dict_item = {'fruit': 'apple', 'vegetable': 'potato', 'berry': 'watermelon'}
    key_list = list(dict_item.keys())
    sorted_keys = sorted(dict_item.keys())
    assert key_list != sorted_keys


def test_combination():
    one_dict_item = {'fruit': 'apple', 'vegetable': 'potato', 'berry': 'watermelon'}
    two_dict_item = {'color': 'red', 'size': 'large', 'freshness': 'fresh'}
    dict_item = {**one_dict_item, **two_dict_item}
    assert dict_item == {'fruit': 'apple',
                         'vegetable': 'potato',
                         'berry': 'watermelon',
                         'color': 'red',
                         'size': 'large',
                         'freshness': 'fresh'}
