def remove_dollar_sign(s):
    add_currency = '{}$'.format(s)
    # Thêm $ cho bài toán có ý nghĩa
    none_currency = add_currency.replace('$','')
    return none_currency

string_with_no_dollars = remove_dollar_sign("$80% percent of $life is to show $up")
if string_with_no_dollars == "80% percent of life is to show up":
    print("Your function is correct")
else:
    print("Oops, there's a bug")