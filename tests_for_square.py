import pytest

from geometric_shapes import GeometricShapes


@pytest.mark.parametrize('item', [9.923, 1.0])
def test_square_area(item):
    area = GeometricShapes().calculate_the_area(name=GeometricShapes.Square.name, a=item, h=None, b=None, r=None)
    expected_area = int(item ** 2)
    assert expected_area == area


@pytest.mark.parametrize('item', [45.23, 15.0])
def test_square_perimeter(item):
    perimeter = GeometricShapes().calculate_perimeter(name=GeometricShapes.Square.name, a=item, b=None, c=None, r=None)
    expected_perimeter = int(4 * item)
    assert expected_perimeter == perimeter


@pytest.mark.parametrize('item', [(7.7, 10), (0.5, 2)])
def test_add_figure_area(item):
    sum_area = GeometricShapes().Square.add_square(a=item[0], h=None, b=None, r=None,
                                                   figure2=GeometricShapes().calculate_the_area(
                                                       name=GeometricShapes.Circle.name,
                                                       a=None, h=None, b=None, r=item[1]))
    assert sum_area, 'Передан неправильный класс'


def test_name():
    assert GeometricShapes.Square.name == 'Square'


def test_angles():
    assert GeometricShapes.Square.angles > GeometricShapes.Triangle.angles
