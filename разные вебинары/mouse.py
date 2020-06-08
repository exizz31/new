#короновориус - данные: точность теста и процент заболеваемости в регионе
accuracy = 98   # % - точность теста
incidence = 2   # % - заболеваемость в регионе
#формула Байеса:
#P(B|A) = P(A|B) * P(B) / P(A)
#P(A|B) - вероятность события, probability = 0.99 (accuracy перевели в дробь)
#P(B) - заболеваемость в регионе = 0,01 (incidence превратили в дробь)
#P(A) = ИП + ЛП (ип - истинно положительные случаи, лп - ложно-положительные)
#
# ИП = 0.99 * 0.01 = 0.0099 ,positive
# ЛП = всего небольных = 100% - 1% = 99% тест врет 100-99 = 1% \\ 0,99 * 0,01 = 0,0099
#P(A) = 0.0099 + 0,0099 = 0.0198
# P(B|A) = 0.99 * 0,01 / 0.0198

probability = accuracy / 100  #P(A|B)
print("Вероятность события: ", probability)
incidence2 = incidence / 100  #P(B)
print("Заболеваемость в регионе: ", incidence2)
IP = accuracy * incidence2 / 100
print("IP", IP)
LP = ((100 - accuracy) / 100) * ((100 - incidence) / 100)
print('LP', LP)
positive = IP + LP #P(A)
print('PA', positive)
test = probability * incidence2 / positive
print("Болен ли Вася? - ", test)