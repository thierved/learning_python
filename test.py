file = open('./data', 'a')
res = ''

while res != '0' :
    res = input('what is your name: ')
    if res != '0': file.write(res + '\n')
file.close()