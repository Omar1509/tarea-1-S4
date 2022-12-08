def fibonacci(div):
    fila = [0,1]
    if div==1:
        print('0')
    elif div==2:
        print('[0,','1]')
    else:
        while(len(fila)<div):
            fila.append(0)
        if(div==0 or div==1):
            return 1
        else:
            fila[0]=0
            fila[1]=1
            for i in range(2,div):
                fila[i]=fila[i-1]+fila[i-2]
            print(fila)

fibonacci(1000)