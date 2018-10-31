#Part 1 - Title
title = input('Enter a title for the data:\n')
print('You entered: {}\n'.format(title))


#Part 2 - Column Headers
column1 = input('Enter the column 1 header:\n')
print('You entered: {}\n'.format(column1))

column2 = input('Enter the column 2 header:\n')
print('You entered: {}\n'.format(column2))


#Part 3 - Input Data & Part 4 - Error Checking
dataString = [ ]
dataInt = [ ]
dataPoint = 0
count = 0
while dataPoint != -1:
    dataPoint = input('Enter a data point (-1 to stop input):\n')
    if dataPoint == '-1':
        print()
        break
    if ',' not in dataPoint:
        print('Error: No comma in string.\n')
        continue
    commas = dataPoint.count(',')
    if commas > 1:
        print('Error: Too many commas in input.\n')
        continue
    dataPt = dataPoint.split(',')
    dataPt[1] = dataPt[1].replace(' ','')
    isNum = dataPt[1].isdigit()
    if isNum == False:
        print('Error: Comma not followed by an integer.\n')
        continue
    dataString.append(str(dataPt[0]))
    dataInt.append(int(dataPt[1]))
    print('Data string: {}'.format(dataString[count]))
    print('Data integer: {}\n'.format(dataInt[count]))
    count += 1

#Part 5 Formatted Table
print('{0:>33}'.format(title))
print('{0:<20}'.format(column1) + '|' + '{0:>23}'.format(column2))
print('-' * 44)
for i in range(len(dataInt)):
    print('{0:<20}'.format(dataString[i]) + '|' + '{0:>23}'.format(dataInt[i]))

print()
#Part 6 Formatted Histogram
for i in range(len(dataInt)):
	print('{0:>20}'.format(dataString[i]), ('*' * dataInt[i]))
