# Einer Funktion erlauben, eine variable Anzahl an Parametern entgegenzunehmen.
#Dafür wird die *-Schreibweise verwendet und die Parameter landen dann in einem Tupel. Dadurch akzeptiert diese Funktion dann eine variable Anzahl an Parametern:

def calculate_max(*params):
    print(params)
    current_max = params[0]
    for item in params:
        if item > current_max:
            current_max = item
    return current_max

calculate_max(1, 2, 3


# Über die **-Schreibweise können mehrere, benannte Parameter entgegen genommen werden.
# Diese Parameter landen dann in einem Dictionary, und man kann dann über die Funktion darauf zugreifen:


def f(**args):
    print(args)

f(key="value", key2="Value 2")
