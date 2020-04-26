import math

import pytest

from geometric_shapes import GeometricShapes


@pytest.mark.parametrize('item', [3, 0.6, 1.5])
def test_circle_area(item):
    area = GeometricShapes().calculate_the_area(name=GeometricShapes.Circle.name, a=None, h=None, b=None, r=item)
    expected_area = int(math.pi * (item ** 2))
    assert expected_area == area


@pytest.mark.parametrize('item', [5, 3, 1.5])
def test_circle_perimeter(item):
    perimeter = GeometricShapes().calculate_perimeter(name=GeometricShapes.Circle.name, a=None, b=None, c=None, r=item)
    expected_perimeter = int(2 * math.pi * item)
    assert expected_perimeter == perimeter


@pytest.mark.parametrize('item', [(7.7, 10, 8.4), (6, 3, 0.5)])
def test_add_figure_area(item):
    sum_area = GeometricShapes().Circle.add_square(a=None, h=None, b=None, r=item[0],
                                                   figure2=GeometricShapes().calculate_the_area(
                                                       name=GeometricShapes.Rectangle.name,
                                                       a=item[1], h=None, b=item[2], r=None))
    assert sum_area, 'Передан неправильный класс'


def test_name():
    assert GeometricShapes.Circle.name == 'Circle'


def test_angles():
    assert 0 == GeometricShapes.Circle.angles
