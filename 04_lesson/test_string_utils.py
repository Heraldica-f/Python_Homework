import pytest
from string_utils import StringUtils

str_ut = StringUtils()

@pytest.mark.parametrize(
    'input_text, expected_result',
    [
        ('pumpkin','Pumpkin'),
        ('expecto patronum', 'Expecto patronum'),
        ('Inspector','Inspector')
    ]
)
def test_positive_capitalize(input_text, expected_result):
    str_ut = StringUtils()
    assert str_ut.capitalize(input_text) == expected_result

@pytest.mark.parametrize(
    'input_text, expected_result',
    [
        (' ',' '),
        ('12mm', '12mm'),
        ('','')
    ]
)
def test_negative_capitalize(input_text, expected_result):
    str_ut = StringUtils()
    assert str_ut.capitalize(input_text) == expected_result

@pytest.mark.parametrize(
    'input_text, expected_result',
    [
        (' Cabbage','Cabbage'),
        (' Golden Retriever', 'Golden Retriever'),
        ('carrot','carrot')
    ]
)
def test_positive_trim(input_text, expected_result):
    str_ut = StringUtils()
    assert str_ut.trim(input_text) == expected_result

@pytest.mark.parametrize(
    'input_text, expected_result',
    [
        (' ',''),
        ('64santimetres', '64santimetres'),
        ('','')
    ]
)
def test_negative_trim(input_text, expected_result):
    str_ut = StringUtils()
    assert str_ut.trim(input_text) == expected_result


@pytest.mark.parametrize(
    'input_text, symbol',
    [
        ('Summary','m'),
        ('160 meters', '1'),
        ('division','i')
    ]
)
def test_positive_contains(input_text, symbol):
    str_ut = StringUtils()
    assert str_ut.contains(input_text, symbol) == True

@pytest.mark.parametrize(
    'input_text, symbol',
    [
        ('Castle','K'),
        ('Mormoduke', ' '),
        ('03 december 2011','i')
    ]
)
def test_negative_contains(input_text, symbol):
    str_ut = StringUtils()
    assert str_ut.contains(input_text, symbol) == False

@pytest.mark.parametrize(
    'input_text, symbol, expected_result',
    [
        ('Cucumber', 'b', 'Cucumer'),
        ('Fallen Angel', 'e', 'Falln Angl'),
        ('tomato', 't', 'omao')
    ]
)
def test_positive_delete_symbol(input_text, symbol, expected_result):
    str_ut = StringUtils()
    assert str_ut.delete_symbol(input_text, symbol) == expected_result

@pytest.mark.parametrize(
    'input_text, symbol, expected_result',
    [
        ('07 march 2008', ' ', '07march2008'),
        ('Coca-Cola', '-', 'CocaCola'),
        (' ', '', ' ')
    ]
)
def test_negative_delete_symbol(input_text, symbol, expected_result):
    str_ut = StringUtils()
    assert str_ut.delete_symbol(input_text, symbol) == expected_result