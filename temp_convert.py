
def temp_convert():
    num = 1
    while(num == True):
        print('for example: if you want convert celcius to Farenhite, input: cf')
        wish = str(input('From which temp to which to you whant convert?'))
        if wish =='cf':
            cel = float(input('Enter Celcius temperature: '))
            f = (cel*1.8)+32
            print(f'Your temp. in Farenhite is {f}')