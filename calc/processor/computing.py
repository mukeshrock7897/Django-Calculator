
def brackets_balance(expression):
    
	balance = 0

	for symbol in balance:
		if symbol == '(':
			balance += 1
		elif symbol == ')':
			balance -= 1

	if balance == 0:
		is_ok = True
		answer = 'Баланс скобок соблюдён'
	else:
		is_ok = False
		answer = 'Нет баланса скобок'

	return is_ok, answer


def compute(expression):

    is_ok = True
    answer = None

    try:
        answer = eval(expression)
    except SyntaxError:
        is_ok = False
        answer = 'Ошибка синтаксиса'
    except ZeroDivisionError:
    	is_ok = False
    	answer = 'Деление на ноль недопустимо'
    except TypeError as e:
    	is_ok = False
    	answer = str(e)


    return is_ok, answer
