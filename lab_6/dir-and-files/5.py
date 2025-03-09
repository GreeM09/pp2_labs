with open('test.txt', 'w') as text:
    list = [input() for _ in range(10 ** 6)]
    
    for i in list:
        text.write(f'{i}\n')
        
