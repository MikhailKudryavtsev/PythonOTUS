import pytest

from geometric_shapes import GeometricShapes


@pytest.mark.parametrize('item', [(7.7, 8.4), (6, 0.5)])
def test_rectangle_area(item):
    area = GeometricShapes().calculate_the_area(name=GeometricShapes.Rectangle.name,
                                                a=item[0], h=None, b=item[1], r=None)
    expected_area = int(item[0] * item[1])
    assert expected_area == area


@pytest.mark.parametrize('item', [(7.7, 10), (80, 19.2)])
def test_rectangle_perimeter(item):
    perimeter = GeometricShapes().calculate_perimeter(name=GeometricShapes.Rectangle.name,
                                                      a=item[0], b=item[1], c=None, r=None)
    expected_perimeter = int(2 * (item[0] + item[1]))
    assert expected_perimeter == perimeter


@pytest.mark.parametrize('item', [(7.7, 10, 8.4, 16), (6, 3, 0.5, 2)])
def test_add_figure_area(item):
    sum_area = GeometricShapes().Rectangle.add_square(a=item[0], h=None, b=item[1], r=None,
                                                      figure2=GeometricShapes().calculate_the_area(
                                                          name=GeometricShapes.Triangle.name,
                                                          a=item[2], h=item[3], b=None, r=None))
    assert sum_area, 'Передан неправильный класс'


def test_name():
    assert GeometricShapes.Rectangle.name == 'Rectangle'


def test_angles():
    assert GeometricShapes.Square.angles == GeometricShapes.Rectangle.angles
