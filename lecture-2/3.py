names = input('Вашите имена: ')
holder = names.split()
len_holder = len(holder)
titles = ['von', 'van', 'proffessor', 'proff.', 'doctor', 'doc.', 'професор', 'проф.', 'доктор', 'д-р', 'др.']
for i in range(0, len_holder):
    str_holder = holder[i]
    if str_holder not in titles:
        print(str_holder[:1] + '.', end = '')
