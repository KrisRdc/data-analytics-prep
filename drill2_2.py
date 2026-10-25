enter_net_amaunt = float(input('Enter net amaunt: '))
vat_rate = 9.0
vat = enter_net_amaunt * (vat_rate / 100)
total = enter_net_amaunt + vat

print('VAT: ', vat)
print('Total: ', total)