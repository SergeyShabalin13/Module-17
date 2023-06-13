per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit=[]
money = int(input('Введите сумму под процеты:'))
deposit.append (per_cent['ТКБ']*money/100)
deposit.append (per_cent['СКБ']*money/100)
deposit.append (per_cent['ВТБ']*money/100)
deposit.append (per_cent['СБЕР']*money/100)
print("Накопленные за год средства =",deposit)
print("Максимальная сумма, которую вы можете заработать:", max(deposit))