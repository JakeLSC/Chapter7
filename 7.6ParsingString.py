usrStr = ' '

while usrStr != 'q':
    usrStr = input('Enter input string:')
    if usrStr == 'q':
        break
    while ',' not in usrStr:
        print('\nError: No comma in string.\n')
        usrStr = input('Enter input string:')
    

    usrStr = usrStr.replace(' ','')
    newStrings = usrStr.split(',')

    print('\nFirst word: {}'.format(newStrings[0]))
    print('Second word: {}\n'.format(newStrings[1]))
