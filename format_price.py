import sys


def format_price(price):
    try:
        floated_price = float(str(price).replace(' ', ''))
    except (ValueError, TypeError):
        pass
    else:
        preformatted_price = '{:,.2f}'.format(floated_price)
        return preformatted_price.replace(',', ' ').replace('.00', '')


if __name__ == '__main__':
    try:
        user_price = sys.argv[1]
    except IndexError:
        exit('Please use script parameter (price)')
    else:
        print('Formatted price:')
        print(format_price(user_price))
