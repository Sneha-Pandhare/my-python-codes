file = open('data.txt', 'a')
for i in range(1, 101):
    file.write(str(i) + ' : ' + str(i*i) + '\n')
file.close()