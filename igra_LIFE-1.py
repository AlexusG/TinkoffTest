import time
import os
from random import randint


sprites = [0, 8, 7, 9]
ghost = {0 : '_', 8 : str(chr(30)), 7 : '&', 9 : '^'}


# функция sosed возвращает количество элементов obj вокруг клетки a[i][j]
def sosed(obj,a,i,j):
    res = 0
    n = len(a) - 1
    m = len(a[0]) - 1

    if i == 0:
        if j == 0:
            if a[i+1][j+1] == obj:
                res +=1
            if a[i][j+1] == obj:
                res +=1
            if a[i+1][j] == obj:
                res +=1
        if j == m:
            if a[i+1][j] == obj:
                res +=1
            if a[i][j-1] == obj:
                res +=1
            if a[i+1][j-1] == obj:
                res +=1
        if j!=0 and j!=m:
            if a[i][j-1] == obj:
                res +=1
            if a[i][j+1] == obj:
                res +=1
            if a[i+1][j-1] == obj:
                res +=1
            if a[i+1][j] == obj:
                res +=1
            if a[i+1][j+1] == obj:
                res +=1
    if i == n:
        if j == 0:
            if a[i-1][j+1] == obj:
                res +=1
            if a[i][j+1] == obj:
                res +=1
            if a[i-1][j] == obj:
                res +=1
        if j == m:
            if a[i-1][j] == obj:
                res +=1
            if a[i][j-1] == obj:
                res +=1
            if a[i-1][j-1] == obj:
                res +=1
        if j!=0 and j!=m:
            if a[i][j-1] == obj:
                res +=1
            if a[i][j+1] == obj:
                res +=1
            if a[i-1][j-1] == obj:
                res +=1
            if a[i-1][j] == obj:
                res +=1
            if a[i-1][j+1] == obj:
                res +=1
    if i!=0 and i!=n:
        if j == 0:
            if a[i-1][j] == obj:
                res +=1
            if a[i-1][j+1] == obj:
                res +=1
            if a[i][j+1] == obj:
                res +=1
            if a[i+1][j+1] == obj:
                res +=1
            if a[i+1][j] == obj:
                res +=1
        if j == m:
            if a[i-1][j] == obj:
                res +=1
            if a[i-1][j-1] == obj:
                res +=1
            if a[i][j-1] == obj:
                res +=1
            if a[i+1][j-1] == obj:
                res +=1
            if a[i+1][j] == obj:
                res +=1
        if j!=0 and j!=m:
            if a[i-1][j] == obj:
                res+=1
            if a[i-1][j] == obj:
                res+=1
            if a[i-1][j+1] == obj:
                res+=1
            if a[i][j-1] == obj:
                res+=1
            if a[i][j+1] == obj:
                res+=1
            if a[i+1][j-1] == obj:
                res+=1
            if a[i+1][j] == obj:
                res+=1
            if a[i+1][j+1] == obj:
                res+=1
            
    return res


def output_(a, it):
    print('iteration {} :\n'.format(it))

    for i in range(len(a)):
        for j in range(len(a[i])):
            print('{} '.format(a[i][j]), end='')
        print()
        #print(a[i])


def output(a, it):
    print('iteration {} :\n'.format(it))

    for i in range(len(a)):
        for j in range(len(a[i])):
            print('{} '.format(ghost[a[i][j]]), end='')
        print()
        #print(a[i])


def act(a):
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] == 7:
                if (sosed(7,a,i,j)>=4 or sosed(7,a,i,j)<2):
                    a[i][j]=0
            if a[i][j] == 9:
                if (sosed(9,a,i,j)>=4 or sosed(9,a,i,j)<2):
                    a[i][j]=0
            if a[i][j] == 0:
                if sosed(7,a,i,j) == 3 :
                    a[i][j]=7
                else:
                    if sosed(9,a,i,j) == 3 :
                        a[i][j]=9


def rand_gen(n, m):
    a = []
    for i in range(n):
        a.append([])
        for j in range(m):
            a[i].append(sprites[randint(0, len(sprites) - 1)])

    return a






def main():
    # 8 - камень, он не меняет положения со временем
    # 9 - креветка, живет по своим правилам
    # 0 - пустая клетка - потенциально заполняема креветкой или рыбой
    # 7 - рыба, живет по своим правилам

    a = rand_gen(23, 7)
    output(a, 0)

    for it in range(100):
        os.system("cls")
        act(a)
        output(a, it+1)
        time.sleep(1)
                 
main()
    
 
