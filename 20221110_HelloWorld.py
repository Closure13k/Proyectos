# Single line comment.

"""
Multiline comment.
"""

# variables: do not require explicit naming.


def main():
    my_name = "Aaron"
    print(type(my_name), my_name)
    my_name = float(3)
    print(type(my_name), my_name)

    v1, v2, v3 = 1, 1.2213, "Hola"
    print(type(v1), v1, type(v2), v2, type(v3), v3)
    """
        Built-in functions.
    """
    # Data input
    """
    money = input("Dame dinero: ")
    print(money)
    """
    # Exponentiation
    number1, number2 = 2, 3
    print(number1, '^', number2, '=', number1**number2)

    # String utils
    # String.length
    print(len("123456"))

    # Operator overload
    a = "first"
    b = "added"
    print(a+b)
    # May multiply a string by an integer in order to repeat it.
    print(a*2, b*3, (a+b)*2)

    # Logical operators
    #   	https://www.pythontutorial.net/python-basics/python-logical-operators/
    print(1 > 3 and not 3 > 4)

    # Format -> just like java
    # String %dataType -> args for each.
    print("String: %s, number: %d" % ("str", 23))
    print("{} - {:.2f} - -> {}".format(23, 54, "Hola"))
    print(f"Example test like {a} and {b} with {v2:.2f}")

    # Strings splitting based on var number
    a, b, c, d = "ABCD"
    print(a, b, c, d)

    lang = "Hello world"
    lang_slice = lang[2:7]

    print(lang_slice, "Hello world"[::+3])

    """
        Error handling and exceptions
    """
    print("Hola".isnumeric())

    """
        Collections
    """

    # Lists
    my_list = list()
    other_list = [1, 2, 3, 4]
    print(my_list)
    print(other_list)

    a, b, c, d = other_list

    my_list = [1, 123.3, "Hi"]

    print([type(item) for item in my_list])

    new_list = my_list + other_list
    new_list.append(8)
    new_list.insert(3, "asd")
    new_list.insert(-1, "ASDAA")
    print(new_list)

    print(new_list)


"""
    Main call.
"""
main()
