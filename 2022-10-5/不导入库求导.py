# 为了不import，我甚至连product都是自己写的=_=
def product(items):
    res = 1
    for i in items:
        res = res * i
    return res

# 继承关系：
# Node <- Constant, Variable, Operator
#                             Operator <- Add, Multiply, Divide, Pow, ...

# 所有的Operator都有子节点，所有的Constant和Variable都没有子结点
class Node:
    def __init__(self, name, value=0):
        self.name = name
        self.value = value

    def __eq__(self, other):
        return self.name == other.name

    def __str__(self):
        return str(self.name)

    def __repr__(self):
        return self.__str__()


class Constant(Node):
    def __init__(self, value):
        super().__init__(value, value)

    def compute_value(self):
        return self.value

    def compute_derivative(self, to_variable):
        return 0


class Variable(Node):
    def compute_value(self):
        return self.value

    def compute_derivative(self, to_variable):
        if to_variable.name == self.name:
            return 1
        else:
            return 0


class Operator(Node):
    def __init__(self, inputs, name):
        self.inputs = inputs
        self.name = f"Opt {name} of {inputs}"

    def __str__(self):
        opt2str = {"Add": "+", "Power": "^", "Multiply": "*", "Divide": "/"}
        return "(" + opt2str[self.name.split(" ")[1]].join(map(str, self.inputs)) + ")"


class Add(Operator):
    def __init__(self, inputs):
        super().__init__(inputs, name="Add")

    def compute_value(self):
        return sum(inp.compute_value() for inp in self.inputs)

    def compute_derivative(self, to_variable):
        return sum(inp.compute_derivative(to_variable) for inp in self.inputs)


class Multiply(Operator):
    def __init__(self, inputs):
        super().__init__(inputs, name="Multiply")

    def compute_value(self):
        return product(inp.compute_value() for inp in self.inputs)

    def compute_derivative(self, to_variable):
        return sum(
            inp.compute_derivative(to_variable)
            * product(
                other_inp.compute_value()
                for other_inp in self.inputs
                if other_inp != inp
            )
            for inp in self.inputs
        )


class Divide(Operator):
    def __init__(self, inputs):
        super().__init__(inputs, name="Divide")

    def compute_value(self):
        a, b = [inp.compute_value() for inp in self.inputs]
        return a / b

    def compute_derivative(self, to_variable):
        a, b = [inp.compute_value() for inp in self.inputs]
        da, db = [inp.compute_derivative(to_variable) for inp in self.inputs]
        return (da * b - db * a) / (b ** 2)


class Power(Operator):
    # Constant Power
    def __init__(self, inputs):
        super().__init__(inputs, name="Power")

    def compute_value(self):
        x, n = self.inputs
        n = n.value
        return x.compute_value() ** n

    def compute_derivative(self, to_variable):
        x, n = self.inputs
        n = n.value
        return n * (x.compute_value() ** (n - 1)) * x.compute_derivative(to_variable)


if __name__ == "__main__":
    print(Add([Varaible("x"),Constant(5)]).compute_derivative())