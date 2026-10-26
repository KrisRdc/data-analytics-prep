def add_vat(net_amount, vat_rate):
    return round(net_amount * (1 + vat_rate / 100), 2)

neto = float(input('Enter net amount: '))
total = add_vat(neto, 9)
print('Total:', total)
 