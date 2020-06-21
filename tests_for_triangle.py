import pytest

from geometric_shapes import GeometricShapes


@pytest.mark.parametrize('item', [(4, 4), (6, 8)])
def test_triangle_area(item):
    area = GeometricShapes().calculate_the_area(name=GeometricShapes.Triangle.name,
                                                a=item[0], h=item[1], b=None, r=None)
    expected_area = int(1 / 2 * item[0] * item[1])
    assert expected_area == area


@pytest.mark.parametrize('item', [(4, 4, 4), (6, 8, 8)])
def test_triangle_perimeter(item):
    perimeter = GeometricShapes().calculate_perimeter(name=GeometricShapes.Triangle.name,
                                                      a=item[0], b=item[1], c=item[2], r=None)
    expected_perimeter = int(item[0] + item[1] + item[2])
    assert expected_perimeter == perimeter


@pytest.mark.parametrize('item', [(3.5, 4, 10), (6, 8, 25)])
def test_add_figure_area(item):
    sum_area = GeometricShapes().Triangle.add_square(a=item[0], h=item[1], b=None, r=None,
                                                     figure2=GeometricShapes().calculate_the_area(
                                                         name=GeometricShapes.Square.name,
                                                         a=item[2], h=None, b=None, r=None))
    assert sum_area, 'Передан неправильный класс'


def test_name():
    assert GeometricShapes.Triangle.name == 'Triangle'


def test_angles():
    assert 3 == GeometricShapes.Triangle.angles
