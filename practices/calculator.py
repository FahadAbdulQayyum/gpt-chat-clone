from cal import calculator

def test_calculator():
    # assert calculator(2, '+', 3) == 5, "Test case 1 failed"
    resutl = calculator(2, '+', 3)
    print(resutl)
    resutl = calculator(2, '*', 3)
    print(resutl)
    resutl = calculator(50, '/', 2)
    print(resutl)

test_calculator()