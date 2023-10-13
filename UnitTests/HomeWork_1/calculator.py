def calculate(first_operand: int, second_operand: int, operator: str) -> int | float:
    match operator:
        case '+':
            result = first_operand + second_operand
        case '-':
            result = first_operand - second_operand
        case '*':
            result = first_operand * second_operand
        case '/':
            if second_operand != 0:
                result = first_operand / second_operand
            else:
                raise ArithmeticError("Division by zero is not possible")
        case _:
            raise ValueError("Unexpected value operator: " + operator)
    return result


def calculate_discount(purchase_amount: float, discount_amount: int) -> float:
    if discount_amount < 0:
        raise ArithmeticError("Discount can't be less then zero")
    elif discount_amount > 100:
        raise ArithmeticError("Discount can't be more then 100")

    return purchase_amount - discount_amount / 100 * purchase_amount