def calculator(num_1: float, operation: str, num_2: float):
    return num_1 + num_2 if operation == '+' else num_1 - num_2 if operation == '-' else num_1 * num_2 if operation == '*' else num_1 / num_2 if operation == '/' else 'Invalid operation'