import sys


def format_price(price):
    try:
        preformatted_price = price.replace(' ', '').replace(',', '.')
        floated_price = float(str(preformatted_price))
    except ValueError:
        pass
    except TypeError:
        pass
    else:
        return '{:,.2f}'.format(floated_price).replace(',', ' ')


if __name__ == '__main__':
    try:
        user_price = sys.argv[1]
    except IndexError:
        exit('Please use script parameter (any formatted price)')
    else:
        print('Formatted price:')
        print(format_price(user_price))
