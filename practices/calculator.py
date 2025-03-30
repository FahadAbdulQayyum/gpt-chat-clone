from cal import calculator, input_displayer

def test_calculator():
    # assert calculator(2, '+', 3) == 5, "Test case 1 failed"
    resutl = calculator(2, '+', 3)
    print(resutl)
    resutl = calculator(2, '*', 3)
    print(resutl)
    resutl = calculator(50, '/', 2)
    print(resutl)

    print(input_displayer("Successfully Working..."))

test_calculator()