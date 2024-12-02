
print("별찍기")
print("1.☆")
print("2.★")
print("3.#")
symbol = int(input("특수문자 선택 (1. ☆ 2. ★ 3. ＃): "))
size = int(input("크기 입력: "))

if symbol == 1:
    char = '☆'
elif symbol == 2:
    char = '★'
elif symbol == 3:
    char = '＃'

for i in range(1, size + 
1):
    print(char * i)
print("별찍기")
print("1.☆")
print("2.★")
print("3.＃")
symbol = int(input("특수문자 선택 (1. ☆ 2. ★ 3. ＃): "))
size = int(input("크기 입력하세요: "))

if symbol == 1:
    char = '☆'
elif symbol == 2:
    char = '★'
elif symbol == 3:
    char = '＃'

for i in range(size):
    if i==0:
        print(" "*(size*2+2),"☆",sep='')
    else:
        print(" "*(size*2+2-i), "☆"," "*(i*2-1),"☆",sep='')

print("☆"*size," "*(size*2-1),"☆"*size,sep='')
for i in range(5):
    for j in range(4-i):
        print(" ", end="")
    for i in range(2*i+1):
        if i == 0 or i == 5-1 or i == 2*i:
            print(" ", end="")
        else:
            print(" ", end="")
    print()