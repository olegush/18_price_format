import sys


def format_price(price):
    price_formatted = price.replace(' ', '')
    if not price_formatted.isdigit():
        price_formatted = formaf_price_with_separator(price)
    if int(price_formatted) > 999:
        price_formatted = '{} {}'.format(
            str(price_formatted)[:-3],
            str(price_formatted)[-3:]
        )
    return price_formatted


def formaf_price_with_separator(price):
    price_kop = ''
    flag = False
    index_kop = len(price)
    for char in price[::-1]:
        if char.isdigit() and not flag:
            price_kop += char
        elif price_kop:
            flag = True
            index_kop -= 1
    price_rub = ''
    for char in price[:-index_kop]:
        if char.isdigit():
            price_rub += char
    return round(float(price_rub + '.' + price_kop[::-1]))


if __name__ == '__main__':
    try:
        user_price = sys.argv[1]
    except IndexError:
        exit('Please use script parameter (any formatted price)')
    else:
        print('Formatted price:')
        print(format_price(user_price))
