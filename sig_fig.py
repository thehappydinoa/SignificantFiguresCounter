#!/usr/bin/env python3
import readline


class SignificantFigure(object):
    def __init__(self, number):
        self.number = str(number).strip()
        self.float = float(self.number)
        self.count = self.count_figs(self.number)

    def __str__(self):
        return self.number

    def __float__(self):
        return self.float

    def __cmp__(self, other):
        self.other_instance(other)
        return cmp(self.float, other.float)

    def __gt__(self, other):
        self.other_instance(other)
        return self.float > other.float

    def __lt__(self, other):
        self.other_instance(other)
        return self.float < other.float

    def __add__(self, other):
        self.other_instance(other)
        sum_of_sig_figs = self.float + other.float
        return SignificantFigure(self.as_sig_fig(sum_of_sig_figs, self.lowest_count(other)))

    def __sub__(self, other):
        self.other_instance(other)
        sum_of_sig_figs = self.float - other.float
        return SignificantFigure(self.as_sig_fig(sum_of_sig_figs, self.lowest_count(other)))

    def __mul__(self, other):
        self.other_instance(other)
        product_of_sig_figs = self.float * other.float
        return SignificantFigure(self.as_sig_fig(product_of_sig_figs, self.lowest_count(other)))

    def __div__(self, other):
        self.other_instance(other)
        product_of_sig_figs = self.float / other.float
        return SignificantFigure(self.as_sig_fig(product_of_sig_figs, self.lowest_count(other)))

    def __rdiv__(self, other):
        self.other_instance(other)
        product_of_sig_figs = other.float / self.float
        return SignificantFigure(self.as_sig_fig(product_of_sig_figs, self.lowest_count(other)))

    def other_instance(self, other):
        if not isinstance(other, SignificantFigure):
            raise TypeError("%s is not a SignificantFigure" % other.__name__)

    def lowest_count(self, other):
        self.other_instance(other)
        if self > other:
            return other.count
        return self.count

    def count_figs(self, number):
        # if "." in number:
        #     decimal_split = number.split(".")
        #
        #     return len(number.replace(".", ""))
        # # Write code here
        # return len(number)
        number = number.lower()
        if ('e' in number):
            myStr = number.split('e')
            return len(myStr[0]) - 1
        n = ('%.*e' % (8, float(number))).split('e')
        if '.' in number:
            s = number.replace('.', '')
            l = len(s) - len(s.rstrip('0'))
            n[0] = n[0].rstrip('0') + ''.join(['0' for num in range(l)])
        else:
            n[0] = n[0].rstrip('0')
        return self.count_figs('e'.join(n))

    def as_sig_fig(self, number, places):
        x = float(number)
        n = int(places)

        if n < 1:
            raise ValueError("1+ significant digits required.")

        s, e = ''.join(('{:.', str(n - 1), 'e}')).format(x).split('e')
        e = int(e)

        if e == 0:
            return s

        s = s.replace('.', '')
        if e < 0:
            return ''.join(('0.', '0' * (abs(e) - 1), s))
        s += '0' * (e - n + 1)
        i = e + 1
        sep = ''
        if i < n:
            sep = '.'
        if s[0] is '-':
            i += 1
        return sep.join((s[:i], s[i:]))


def count_sig_figs():
    number = input("Enter a number: ")
    print("%d significant figures" % SignificantFigure(number).count)


def add_sig_figs():
    number1 = SignificantFigure(input("Enter a number 1: "))
    number2 = SignificantFigure(input("Enter a number 2: "))
    fig_sig_sum = number1 + number2
    print("%s + %s = %s" % (number1, number2, fig_sig_sum))


def subtract_sig_figs():
    number1 = SignificantFigure(input("Enter a number 1: "))
    number2 = SignificantFigure(input("Enter a number 2: "))
    fig_sig_sum = number1 - number2
    print("%s - %s = %s" % (number1, number2, fig_sig_sum))


def multiply_sig_figs():
    number1 = SignificantFigure(input("Enter a number 1: "))
    number2 = SignificantFigure(input("Enter a number 2: "))
    fig_sig_sum = number1 * number2
    print("%s * %s = %s" % (number1, number2, fig_sig_sum))


def divide_sig_figs():
    number1 = SignificantFigure(input("Enter a number 1: "))
    number2 = SignificantFigure(input("Enter a number 2: "))
    fig_sig_sum = number1 / number2
    print("%s / %s = %s" % (number1, number2, fig_sig_sum))


def exit_menu():
    print("Exiting...")
    exit(0)


def menu():
    readline.parse_and_bind("tab: complete")
    print("Significant Figures Counter\n")
    items = {
        1: ["Count Significant Figures", count_sig_figs],
        2: ["Adds Number", add_sig_figs],
        3: ["Subtract Number", subtract_sig_figs],
        4: ["Multiply Number", multiply_sig_figs],
        5: ["Divide Number", divide_sig_figs],
        0: ["Exit", exit_menu]
    }
    for item in items.keys():
        print("%d. %s" % (item, items.get(item)[0]))
    try:
        choice = int(input("\nWhat do you want to do: "))
        print()
        items.get(choice)[1]()
        menu()
    except (ValueError, TypeError) as error:
        print(repr(error))
        print("Invalid Choice")
        menu()


if __name__ == "__main__":
    try:
        menu()
    except KeyboardInterrupt:
        exit_menu()
