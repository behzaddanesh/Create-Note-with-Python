from main import giyu
from main import date
from main import hours

def main():
    test_giyu()
    test_date()
    test_hours()

def test_giyu():
    assert giyu("1234") == True
    assert giyu("B2") == None

def test_date():
    assert date("210/09/2024") == True
    assert date("12/31/2022") == True
    assert date("12/05/1432") == True
    assert date("12/05/2023") == None


def test_hours():
    assert hours("giyu") == True
    assert hours("3n") == True
    assert hours("2") == None

if __name__ == '__main__':
    main()