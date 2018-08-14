def remove_dollar_sign(s):
    add_currency = '{}$'.format(s)
    # Thêm $ cho bài toán có ý nghĩa
    none_currency = add_currency.replace('$','')
    return none_currency
result = print(remove_dollar_sign(2000))
