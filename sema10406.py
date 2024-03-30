#세마고 10406 김윤성 정보과학 수행 구현(Q1. 문자열 길이 정렬)
try:
    a = int(input("기사 개수 : "))
    if a<=0:
        raise Exception
except :
    print("자연수를 적어주세요.")
    exit()
before = []
after = []
#입력
for _ in range(a):
    title = str(input())
    before.append(title)

#정렬
for _ in range(a):
    small = before[0]
    for i in range(1, len(before)):
        if len(small) > len(before[i]):
            small = before[i]
    after.append(small)
    before.remove(small)

#출력
for i in after:
    print(i)