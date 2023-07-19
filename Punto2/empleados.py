# Con la ayuda del IDE (recomiendo PyCharm), abre un repositorio nuevo (recomiendo
# Github) y genera el siguiente ejercicio:
# Una clase Employee que tenga los atributos name y salary. La clase también debe
# tener un método get_salary() que devuelva el salario del empleado y un método
# change_salary() que cambie el salario del empleado.
# Genera la base del script, con (if __name__) , donde instancies la clase y uses los
# métodos declarados.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_name(self):
        print("¡El nombre del empleado es: %s" % self.name)

    def get_salary(self):
        print("El salario del empleado es: %s" % self.salary)

    def change_salary(self, new_salary):
        self.salary = new_salary


if __name__ == '__main__':

    empleado = Employee('Juan', 20)
    empleado.get_name()
    empleado.get_salary()
    empleado.change_salary(30)
    empleado.get_salary()
