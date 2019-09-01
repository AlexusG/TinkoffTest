import time
import os

# функция sosed возвращает количество элементов obj вокруг клетки a[i][j]
def sosed(obj,a,i,j):
    res = 0
    if i == 0:
        if j == 0:
            if a[i+1][j+1] == obj:
                res +=1
            if a[i][j+1] == obj:
                res +=1
            if a[i+1][j] == obj:
                res +=1
        if j == 9:
            if a[i+1][j] == obj:
                res +=1
            if a[i][j-1] == obj:
                res +=1
            if a[i+1][j-1] == obj:
                res +=1
        if j!=0 and j!=9:
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
    if i == 9:
        if j == 0:
            if a[i-1][j+1] == obj:
                res +=1
            if a[i][j+1] == obj:
                res +=1
            if a[i-1][j] == obj:
                res +=1
        if j == 9:
            if a[i-1][j] == obj:
                res +=1
            if a[i][j-1] == obj:
                res +=1
            if a[i-1][j-1] == obj:
                res +=1
        if j!=0 and j!=9:
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
    if i!=0 and i!=9:
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
        if j == 9:
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
        if j!=0 and j!=9:
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



def act(a):
    for i in range(10):
        for j in range(10):
            print(a[i][j],end=" ")
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
            
        print()
    print()



def main():
    # 8 - камень, он не меняет положения со временем
    # 9 - креветка, живет по своим правилам
    # 0 - пустая клетка - потенциально заполняема креветкой или рыбой
    # 7 - рыба, живет по своим правилам
    a=[ [7,0,0,0,0,7,7,0,0,8],
        [7,7,8,0,0,0,7,7,0,8],
        [7,7,8,7,8,7,7,7,0,8],
        [0,7,7,7,7,0,8,8,0,0],
        [0,0,7,7,0,0,9,9,0,0],
        [0,0,7,0,7,8,0,0,9,0],
        [0,0,0,8,7,9,9,9,0,0],
        [8,0,0,0,0,0,9,9,8,0],
        [0,8,0,8,0,0,0,9,9,0],
        [0,0,0,8,9,0,0,9,9,9] ]

    # a - вложенный список, размер 10*10, игровое поле
    # алгоритм одного пробега(1 пробег в цикл жизни):

    for _ in range(100):
        os.system("cls")
        act(a)
        time.sleep(1)
                 
main()
    
 
