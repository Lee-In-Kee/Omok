import re
# 오목판 설계
row = {}
column = {}

for i in range(0,15):
    row[i] = '+'*15
    column[i] = '+'*15

cnt = 0
while cnt < 15*15+1:
    cnt += 1

    # 0~14사이 정수 입력
    x = input("x: ")
    y = input("y: ")

    while x == '' or y == '':
        x = input("재입력 x: ")
        y = input("재입력 y: ")
    while int(x) > 14 or int(y) > 14:
        x = input("범위 초과 x: ")
        y = input("범위 초과 y: ")
    while row[int(y)][int(x)] != '+':
        x = input("재입력 x: ")
        y = input("재입력 y: ")

    x = int(x)
    y = int(y)

    # 33은 안됨
    cntO = 0
    cntX = 0
    # row 방향
    if cnt % 2 == 1:
        keepO = 'O'
        indx = x + 1
        if indx < 15:
            while row[y][indx] == 'O' or row[y][indx] == '+':
                if row[y][indx] == '+':
                    keepO += '+'
                    break
                keepO += 'O'
                indx += 1
        indx = x - 1
        if indx >= 0:
            while row[y][indx] == 'O' or row[y][indx] == '+':
                if row[y][indx] == '+':
                    keepO += '+'
                    break
                keepO += 'O'
                indx -= 1

        numO = re.findall('[O]', keepO)
        num = re.findall('[+]', keepO)     
        if len(numO) + len(num) == 5:
            cntO += 1

    if cnt % 2 == 0:
        keepX = 'X'
        indx = x + 1
        if indx < 15:
            while row[y][indx] == 'X' or row[y][indx] == '+':
                if row[y][indx] == '+':
                    keepX += '+'
                    break
                keepX += 'X'
                indx += 1
        indx = x - 1
        if indx >= 0:
            while row[y][indx] == 'X' or row[y][indx] == '+':
                if row[y][indx] == '+':
                    keepX += '+'
                    break
                keepX += 'X'
                indx -= 1

        numX = re.findall('[X]', keepX)
        num = re.findall('[+]', keepX)
        if len(numX) + len(num) == 5:
            cntX += 1
    
    # column 방향
    if cnt % 2 == 1:
        keepO = 'O'
        indy = y + 1
        if indy < 15:
            while column[x][indy] == 'O' or column[x][indy] == '+':
                if column[x][indy] == '+':
                    keepO += '+'
                    break
                keepO += 'O'
                indy += 1
        indy = y - 1
        if indy >= 0:
            while column[x][indy] == 'O' or column[x][indy] == '+':
                if column[x][indy] == '+':
                    keepO += '+'
                    break
                keepO += 'O'
                indy -= 1

        numO = re.findall('[O]', keepO)
        num = re.findall('[+]', keepO)     
        if len(numO) + len(num) == 5:
            cntO += 1

    if cnt % 2 == 0:
        keepX = 'X'
        indy = y + 1
        if indy < 15:
            while column[x][indy] == 'X' or column[x][indy] == '+':
                if column[x][indy] == '+':
                    keepX += '+'
                    break
                keepX += 'X'
                indy += 1
        indy = y - 1
        if indy >= 0:
            while column[x][indy] == 'X' or column[x][indy] == '+':
                if column[x][indy] == '+':
                    keepX += '+'
                    break
                keepX += 'X'
                indy -= 1

        numX = re.findall('[X]', keepX)
        num = re.findall('[+]', keepX)     
        if len(numX) + len(num) == 5:
            cntX += 1
    
    # +1, +1 방향
    if cnt % 2 == 1:
        keepO = 'O'
        indx, indy = x + 1, y + 1
        if indx < 15 and indy < 15:
            while row[indy][indx] == 'O' or row[indy][indx] == '+':
                if row[indy][indx] == '+':
                    keepO += '+'
                    break
                keepO += 'O'
                indx += 1
                indy += 1
        indx, indy = x - 1, y - 1
        if indx >= 0 and indy >= 0:
            while row[indy][indx] == 'O' or row[indy][indx] == '+':
                if row[indy][indx] == '+':
                    keepO += '+'
                    break
                keepO += 'O'
                indx -= 1
                indy -= 1
        numO = re.findall('[O]', keepO)
        num = re.findall('[+]', keepO)     
        if len(numO) + len(num) == 5:
            cntO += 1
    
    if cnt % 2 == 0:
        keepX = 'X'
        indx, indy = x + 1, y + 1
        if indx < 15 and indy < 15:
            while row[indy][indx] == 'X' or row[indy][indx] == '+':
                if row[indy][indx] == '+':
                    keepX += '+'
                    break
                keepX += 'X'
                indx += 1
                indy += 1
        indx, indy = x - 1, y - 1
        if indx >= 0 and indy >= 0:
            while row[indy][indx] == 'X' or row[indy][indx] == '+':
                if row[indy][indx] == '+':
                    keepX += '+'
                    break
                keepX += 'X'
                indx -= 1
                indy -= 1
        numX = re.findall('[X]', keepX)
        num = re.findall('[+]', keepX)     
        if len(numX) + len(num) == 5:
            cntX += 1
    
    # -1, +1 방향
    if cnt % 2 == 1:
        keepO = 'O'
        indx, indy = x - 1, y + 1
        if indx >= 0 and indy < 15:
            while row[indy][indx] == 'O' or row[indy][indx] == '+':
                if row[indy][indx] == '+':
                    keepO += '+'
                    break
                keepO += 'O'
                indx -= 1
                indy += 1
        indx, indy = x + 1, y - 1
        if indx < 15 and indy >= 0:
            while row[indy][indx] == 'O' or row[indy][indx] == '+':
                if row[indy][indx] == '+':
                    keepO += '+'
                    break
                keepO += 'O'
                indx += 1
                indy -= 1
        numO = re.findall('[O]', keepO)
        num = re.findall('[+]', keepO)     
        if len(numO) + len(num) == 5:
            cntO += 1
    
    if cnt % 2 == 0:
        keepX = 'X'
        indx, indy = x - 1, y + 1
        if indx >= 0 and indy < 15:
            while row[indy][indx] == 'X' or row[indy][indx] == '+':
                if row[indy][indx] == '+':
                    keepX += '+'
                    break
                keepX += 'X'
                indx -= 1
                indy += 1
        indx, indy = x + 1, y - 1
        if indx < 15 and indy >= 0:
            while row[indy][indx] == 'X' or row[indy][indx] == '+':
                if row[indy][indx] == '+':
                    keepX += '+'
                    break
                keepX += 'X'
                indx += 1
                indy -= 1
        numX = re.findall('[X]', keepX)
        num = re.findall('[+]', keepX)     
        if len(numX) + len(num) == 5:
            cntO += 1
    

    if cntO >= 2 or cntX >= 2:
        x = int(input("33불가 x: "))
        y = int(input("33불가 y: "))
    
        

    # row와 column 데이터 수집
    if cnt % 2 == 1:
        columnlist = list(column[x])
        columnlist[y] = "O"
        column[x] = "".join(columnlist)

        rowlist = list(row[y])
        rowlist[x] = "O"
        row[y] = "".join(rowlist)
    
    else :
        columnlist = list(column[x])
        columnlist[y] = "X"
        column[x] = "".join(columnlist)

        rowlist = list(row[y])
        rowlist[x] = "X"
        row[y] = "".join(rowlist)


    # 최종 출력
    for i in range(14,-1,-1):
        my_list = list(row[i])
        final = ' '.join(my_list)
        final += ' '
        final += str(i)

        print(final)
    print('0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 !')


    # 승리 조건
    # row 5개 연달아
    rowO = re.findall('[O]',row[y])
    rowX = re.findall('[X]',row[y])
    if len(rowO) >= 5:
        keepO = ''
        indx = x
        while indx < 15 and row[y][indx] == 'O':
            keepO += 'O'
            indx += 1
        indx = x - 1
        while indx >= 0 and row[y][indx] == 'O':
            keepO += 'O'
            indx -= 1
        if keepO == 'O'*5:
            print('Win!-player O')
            break
    
    if len(rowX) >= 5:
        keepX = ''
        indx = x
        while indx < 15 and row[y][indx] == 'X':
            keepX += 'X'
            indx += 1
        indx = x - 1
        while indx >= 0 and row[y][indx] == 'X':
            keepX += 'X'
            indx -= 1
        if keepX == 'X'*5:
            print('Win!-player X')
            break

    # column 5개 연달아
    colO = re.findall('[O]',column[x])
    colX = re.findall('[X]',column[x])
    if len(colO) >= 5:
        keepO = ''
        indy = y
        while indy < 15 and column[x][indy] == 'O':
            keepO += 'O'
            indy += 1
        indy = y - 1
        while indy >= 0 and column[x][indy] == 'O':
            keepO += 'O'
            indy -= 1
        if keepO == 'O'*5:
            print('Win!-player O')
            break

    if len(colX) >= 5:
        keepX = ''
        indy = y
        while indy < 15 and column[x][indy] == 'X':
            keepX += 'X'
            indy += 1
        indy = y - 1
        while indy >= 0 and column[x][indy] == 'X':
            keepX += 'X'
            indy -= 1
        if keepX == 'X'*5:
            print('Win!-player X')
            break
        
    # +1,+1 방향으로 5개 연달아
    if cnt % 2 == 1:
        keepO = 'O'
        indx, indy = x + 1, y + 1
        while indx < 15 and indy < 15 and row[indy][indx] == 'O':
            keepO += 'O'
            indx += 1
            indy += 1
        indx, indy = x - 1, y - 1
        while indx >= 0 and indy >= 0 and row[indy][indx] == 'O':
            keepO += 'O'
            indx -= 1
            indy -= 1
        if keepO == 'O'*5:
            print('Win!-player O')
            break

    if cnt % 2 == 0:
        keepX = 'X'
        indx, indy = x + 1, y + 1
        while indx < 15 and indy < 15 and row[indy][indx] == 'X':
            keepX += 'X'
            indx += 1
            indy += 1
        indx, indy = x - 1, y - 1
        while indx >= 0 and indy >= 0 and row[indy][indx] == 'X':
            keepX += 'X'
            indx -= 1
            indy -= 1
        if keepX == 'X'*5:
            print('Win!-player X')
            break

    # -1, +1 방향으로 5개 연달아
    if cnt % 2 == 1:
        keepO = 'O'
        indx, indy = x - 1, y + 1
        while indx >= 0 and indy < 15 and row[indy][indx] == 'O':
            keepO += 'O'
            indx -= 1
            indy += 1
        indx, indy = x + 1, y - 1
        while indx < 15 and indy >= 0 and row[indy][indx] == 'O':
            keepO += 'O'
            indx += 1
            indy -= 1
        if keepO == 'O'*5:
            print('Win!-player O')
            break

    if cnt % 2 == 0:
        keepX = 'X'
        indx, indy = x - 1, y + 1
        while indx >= 0 and indy < 15 and row[indy][indx] == 'X':
            keepX += 'X'
            indx -= 1
            indy += 1
        indx, indy = x + 1, y - 1
        while indx < 15 and indy >= 0 and row[indy][indx] == 'X':
            keepX += 'X'
            indx += 1
            indy -= 1
        if keepX == 'X'*5:
            print('Win!-player X')
            break
