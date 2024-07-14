def main(input_str: str):
    try:
        parts = input_str.split()
        if len(parts) != 3:
            return ('throws Exception //т.к. строка не является математической операцией или формат математической '
                    'операции не удовлетворяет заданию - два операнда и один оператор (+, -, /, *)')

        num1, operator, num2 = parts

        try:
            num1 = int(num1)
            num2 = int(num2)
        except ValueError:
            return 'throws Exception //Числа должны быть целыми числами'

        if not (1 <= num1 <= 10) or not (1 <= num2 <= 10):
            return 'throws Exception //Числа должны быть от 1 до 10 включительно'

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                return 'throws Exception //Деление на ноль невозможно'
            result = num1 // num2
        else:
            return 'throws Exception //Неподдерживаемый оператор'

        return str(result)

    except Exception as e:
        return f'throws Exception // {e}'


def run_calculator():
    while True:
        try:
            expression = input('Введите выражение (например, 1 + 2): ')
            result = main(expression)
            if isinstance(result, str) and 'throws Exception' in result:
                print(result)
                break
            print(result)
        except Exception as e:
            print(f"throws Exception // {e}")
            break


if __name__ == "__main__":
    run_calculator()
