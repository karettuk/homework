"""
프로그램 소개
 ##고 학생은 준비할 수행평가가 너무 많아 혼란스러워 한다. 이 학생을 위해 수행평가 준비 일정표 프로그램을 만들어보자.
프로그램이 시작되면 이번 주에 볼 수행평가 개수를 변수에 입력받는다. 그 후, 토요일부터 시작해 목요일까지 각 요일마다
수행평가 준비에 할애할 수 있는 시간(음이 아닌 정수 값 6개)을 입력한다. 그리고 나서 이름, 기한, 점수, 준비시간 등을 
포함한 수행평가 정보를 위에서 입력한 수행평가 개수 만큼 입력받는다. 단, 수행평가 과목명 뒤에 '!'가 붙어있으면 다른 과목보다 
더 중요한 과목이라고 판단해 실제 점수에 보정 점수 50점을 추가한다.수행 준비 시간을 채운 만큼 그에 비례해 점수를 얻을 수 
있다고 가정한다.(ex.시간을 모두 채우면 평가에 배당된 점수를 모두 얻을 수 있지만, 시간을 반만 채우면 배당된 점수의 반만
얻는다.) 위의 규칙을 따라 얻을 수 있는 수행평가 점수 합이 최대가 되도록 수행평가 준비 시간표를 각 요일별로 나눠 리스트 
6개를 출력한다. 단, 일부분 준비하지 못한 수행평가가 있다면 그것도 리스트로 함께 출력한다.
 
해결 방법
 탐욕 알고리즘을 사용해 기한을 지나지 않은 과목 중 준비 시간 대비 점수 이득이 가장 큰 과목부터 선택해 일정표에 배치한다. 
'금,목,수,화,월,일,토'순으로 거꾸로 흘러가면서 평가 기한을 맞출 수 있는 수행평가 목록을 전체 수행평가 리스트에서 뽑아내
배열 자료구조에 저장하고 '점수/준비시간'의 값이 큰 순서대로 내림차순 퀵정렬한다. 정렬한 배열의 0번 인덱스부터 하나씩 
수행평가 데이터를 뽑아내서 각 요일 준비 가능 시간을 넘지 않는 선에서 일정표에 배치한다. 만약 모든 준비 시간을 채웠다면,
더 이상 그 수행평가는 준비해야 할 대상이 아니므로 전체 수행평가 리스트에서 제거한다. 만약 시간이 넘는다면, 채울 수 
있는 시간만큼만 채우고 남은 준비 시간, 획득하지 못한 점수는 다음 요일에서 채택될 수 있도록 수행평가 정보를 바꾼 후 
전체 수행평가 리스트에 남겨둔다. 만약 토요일까지 일정표를 채웠는데도 불구하고, 전체 수행평가 리스트에 남아있는 수행평가가
있다면 그 수행평가는 일부분 준비하지 못한 수행평가이므로 마지막에 리스트로 출력한다.

입력 예시1
3
5 4 1 0 2 1
국어 목 20 2
수학! 화 20 3
역사 수 30 3

출력 예시1
토:[역사(수,1)]
일:[수학!(화,2),역사(수,2)]
월:[수학!(화,1)]
화:[]
수:[국어(목,2)]
목:[]

입력 예시2
4
1 1 1 1 1 1
국어 목 30 2
수학 수 20 2
정보과학 화 40 2
과학 월 20 2

출력 예시2
토:[수학(수,1)]    
일:[정보과학(화,1)]
월:[정보과학(화,1)]
화:[국어(목,1)]
수:[국어(목,1)]
목:[]
준비 못하는 거 : [수학(수,1), 과학(월,2)]
"""

class Test:
    def __init__(self, title, day, score, prepare):
        self.title = title
        self.day = day
        if self.day not in week: #요일 입력X ?
            print("지원하지 않는 입력 방식입니다.")
            exit()
        try:    
            if title[-1] == '!':    
                self.score = int(score) + 50  #'!'로 끝나면 50점 추가
            else : self.score = int(score)
            self.prepare = int(prepare)
        except: 
            print("지원하지 않는 입력 방식입니다.")
            exit()
    def __repr__(self):
        return("{}({},{})".format(self.title, self.day,self.prepare))

    #준비 시간 대비 높은 점수를 얻을 수 있는 순으로 정렬
    def __le__(self, other):
        return (self.score/self.prepare) <= (other.score/other.prepare)
    def __ge__(self, other):
        return (self.score/self.prepare) >= (other.score/other.prepare)
    
def quick_sort(array, start, end): #내림차순 퀵정렬
    if start >= end:
        return
    pivot = start
    left = start+1
    right = end
    while left <= right:    
        while left <= end and array[left] >= array[pivot]:  # 배열을 벗어나지 않는 선에서 기준보다 큰 값 찾기
            left+=1
        while right > start and array[right] <= array[pivot]: #배열을 벗어나지 않는 선에서 기준보다 작은 값 찾기
            right-=1    
        if left>right: # 엇갈렸다면 right 데이터와 기준을 교체
            array[right], array[pivot] = array[pivot], array[right]    
        else: # 엇갈리지 않았다면 작은 right 데이터와 큰 left 데이터를 교체 
            array[left], array[right] = array[right], array[left]

    # 두 묶음으로 분할해 다시 반복
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)

def schedule(H,l,n): #일정 짜기, 그리디 알고리즘_분할 가능 냅색문제 활용
    total = 0
    for i in range(0, len(l)):
        total += l[i].prepare
        if (total > H): #준비 가능 시간을 넘었다면
            over = testlist[testlist.index(l[i])]
            prepared = over.prepare-(total-H) #준비 완료 시간
            get_score = prepared*over.score / over.prepare #획득한 점수
            if prepared != 0:
                plan[n].append(Test(over.title,over.day,get_score,prepared))
            over.score -= get_score
            over.prepare = (total - H)
            break
        testlist.remove(l[i]) #준비 완료
        plan[n].append(l[i]) #일정표 배치

week = ["토","일","월","화","수","목","금"] #기한 확인용, index 값이 작을수록 더 빨리 보는 수행평가임
try: 
    n = int(input("이번 주에 준비해야 하는 수행평가 개수를 입력하세요 : "))
    if n<0:
        n=0
    time = list(map(int, input("토요일부터 목요일까지 각 요일의 수행준비 가능 시간을 입력하세요.").split()))
    for i in time:
        if i<0:
            i=0 
except: 
    print("지원하지 않는 입력 방식입니다.")
    exit()

plan = [[],[],[],[],[],[]]
testlist = []
print("수행평가의 정보를 작성해주세요 (이름,날짜기한,배당점수,준비필요 시간)")
for _ in range(n):
    a,b,c,d = map(str,input().split())
    testlist.append(Test(a, b, c, d)) #수행평가 정보 입력
for h in range(5,-1,-1): #금요일부터 토요일까지 거꾸로 흘러가며 기한 체크, 점수를 최대화시키는 일정표 작성
    daytest = []
    for d in testlist:
        if week.index(d.day) > h: #기한 체크
            daytest.append(d)
    quick_sort(daytest, 0, len(daytest)-1)
    schedule(time[h], daytest, h)

#결과 출력
for d in range(6):
    print("{}:{}".format(week[d],plan[d]))
if testlist:
    print("준비 못하는 거 :", testlist)

"""
코드를 작성하며 생각이 바뀐 것들
 가장 먼저 바꾼 점은 정렬 기준이었다. 7시간 준비해서 40점 받는 거 보다 1시간 준비해서 10점 얻는 수행평가 7개를 준비하는
것이 더 점수를 많이 얻을 수 있다는 것을 알게 되었고, 이로써 수행평가 점수가 더 높다고 해서 선택 우선 순위를 높게 두어서는
안 되겠다는 생각이 들었다. 이를 개선하기 위해 1시간동안 준비해서 얻을 수 있는 점수인 단위 점수를 기준으로 정렬하는 것으로
코드를 수정했다. 새롭게 바뀐 기준을 위 사례에 적용해보면 "40/7 < 10/1"로 후자가 더 시간 대비 점수 효율이 좋다고 판단한다.
 두 번째로 바꾼 점은 자료구조를 힙에서 배열로 바꾼 것이다. 힙 정렬은 중복을 허용하지 않는데 위 정렬 기준으로 계산해보면
2시간 걸려서 20점 얻는 수행평가와 4시간 걸려서 40점 얻는 수행평가의 효율성이 같은 것처럼 기준값이 같아져 중복되는 경우가
생길 수 있다는 생각이 들었다. 그러므로 중복을 허용하는 배열 자료구조에 Test자료형 데이터를 저장해두고 정렬하는 방식으로
코드를 수정했다. 정렬 방법은 수업 시간에 배운 정렬 방법 중 가장 시간 복잡도가 낮았던 퀵정렬을 사용했다.
 그 외에 "__str__: print"를 "__repr__: return"로 수정했고, 코드의 가독성을 위해 "time.reverse()"를 삭제하고 그와 
동일한 기능을 하는 "for h in range(5,-1,-1):~~"로 바꾸어 알고리즘을 구현했다.  
"""



"""
# 수정 전 코드(매우 불편...)
import heapq as hq
week = ["금","목","수","화","월","일","토"]
class Test:
    def __init__(self, title, day, score, prepare):
        self.title = title
        self.day = week.index(day) #index 값이 클수록 더 빨리 보는 수행평가임
        if title[-1] == '!':
            self.score = score + 50
        else : self.score = score
        self.prepare = prepare
    
    def __str__(self):
        print(self.title)
    
    def __le__(self, other):
        return self.score <= other.score

def schedule(map,testlist):
    pass

n = int(input("이번 주에 준비해야 하는 수행평가 개수를 입력하세요 : "))
time = list(map(int, input("토요일부터 목요일까지 각 요일의 수행준비 가능 시간을 입력하세요.").split()))
time.reverse() #금요일부터 시작해 거꾸로 기한을 체크해 가며 점수를 최대화시키는 일정표 작성 
plan = [[]*6] #수행평가 배정된 일정표
testlist = []
heap = [] #기한별 수행평가 힙
print("수행평가의 정보를 작성해주세요 (이름,날짜기한,배당점수,준비필요 시간)")
for _ in range(n):
    a,b,c,d = map(str, input().split())
    testlist.append(Test(a, b, int(c), int(d)))
for i in testlist:
    print(i)
for h in range(1,7):
    for d in testlist:
        if d.day < h: #기한 체크
            heap.append(d)
    hq.heapify(heap) 
"""