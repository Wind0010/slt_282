class Bank:
    def __init__(self, name, balance):
        self.__name = name
        self.__balance = balance
    def moneyX(self):
        amount = float(input("Введите сумму для добавления на счет: "))
        self.__balance += amount
        print(f"Ваш новый баланс: {self.__balance}")

    def __kill(self):
        self.__balance = 0
        print("Баланс обнулен.")

    def __jackpot(self):
        self.__balance *= 10

    def __merge_balance(self, other):
        self.__balance += other.__balance
        print(f"Новый баланс: {self.__balance}")

    def merge(self, other):
        self.__merge_balance(other)

    def get_balance(self):
        return self.__balance

if __name__ == "__main__":
    client1 = Bank("Клиент 1", 100)
    client2 = Bank("Клиент 2", 100)

    client1.moneyX()
    print(f"Баланс клиента 1: {client1.get_balance()}")
    print(f"Баланс клиента 2: {client2.get_balance()}")

    client1.merge(client2)  # Объединяем балансы
    print(f"Баланс клиента 1 после объединения: {client1.get_balance()}")


    class Calculator:
        def __init__(self, value=0):
            self.value = value

        def __add__(self, other):
            return Calculator(self.value + other.value)

        def __sub__(self, other):
            return Calculator(self.value - other.value)

        def __mul__(self, other):
            return Calculator(self.value * other.value)

        def __truediv__(self, other):
            if other.value != 0:
                return Calculator(self.value / other.value)
            else:
                raise ValueError("Деление на ноль!")

        def __str__(self):
            return str(self.value)


    class Calculator:
        def __init__(self, value=0):
            self.value = value

        def __add__(self, other):
            return Calculator(self.value + other.value)

        def __sub__(self, other):
            return Calculator(self.value - other.value)

        def __mul__(self, other):
            return Calculator(self.value * other.value)

        def __truediv__(self, other):
            if other.value != 0:
                return Calculator(self.value / other.value)
            else:
                raise ValueError("Деление на ноль!")

        def __str__(self):
            return str(self.value)


    
    if __name__ == "__main__":
        calc1 = Calculator(10)
        calc2 = Calculator(5)

        sum_result = calc1 + calc2
        print(f"Сумма: {sum_result}")

        sub_result = calc1 - calc2
        print(f"Разность: {sub_result}")

        mul_result = calc1 * calc2
        print(f"Умножение: {mul_result}")

        div_result = calc1 / calc2
        print(f"Деление: {div_result}")

    if __name__ == "__main__":
        calc1 = Calculator(10)
        calc2 = Calculator(5)

        sum_result = calc1 + calc2
        print(f"Сумма: {sum_result}")

        sub_result = calc1 - calc2
        print(f"Разность: {sub_result}")

        mul_result = calc1 * calc2
        print(f"Умножение: {mul_result}")

        div_result = calc1 / calc2
        print(f"Деление: {div_result}")

