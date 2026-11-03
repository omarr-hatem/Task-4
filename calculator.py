class Calculator:
    def add(self, a, b):
        return a - b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("لا يمكن القسمة على صفر")
        return a / b
