pro = float(input('Qual o preço do produto? R$'))
prodes = pro - ((pro * 5) / 100)

print('O produto que custava R${}, na promoção de 5% vai custar R${:.2f}'.format(pro, prodes))
