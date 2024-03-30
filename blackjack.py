# Ace가 1, 11 둘 중 하나로 사용할 수 있다는 거 구현할 방법??
# 무승부 추가 배팅?
# 딜러의 카드 오픈 룰
# 합 21, 블랙잭 처리

import random

#플레이어 상태(손 패, 숫자, 보유 금액)
class State:
    def __init__(self):
        self.deck = []
        self.num = 0
        self.money = 1000
    def __str__(self):
        for i in range(len(self.deck)):
            print(self.deck[i], end=' / ')
        print("총합 : {}".format(self.num), end=' / ')
        print("현재 소지 금액 : {}".format(self.money), end=' ')
        return ''
    
#초기화
num = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
shape = ['♠', '❤', '♦', '♣']
deck = []
myState = State()
dealerState = State()

#덱 구성
def reset():
    for h in range(0,4):
        for i in range(0,13):
            card = str(num[i])+shape[h]
            dic = {}
            if i <= 9:
                dic[card] = i+1
            else : dic[card] = 10
            deck.append(dic) 
    random.shuffle(deck)
    print("\n덱이 리셋되었습니다.\n")
#카드 뽑기
def pick(state):
    if len(deck) == 0:
        reset()
    Card = eval(str(deck[len(deck)-1]))
    deck.remove(deck[len(deck)-1])
    pos = list(Card.keys())[0]
    state.deck.append(pos)
    state.num += Card[pos]

#라운드 시작 뽑기
def start():
    for i in range(1,5):
        if len(deck) == 0:
            reset()
        if i%2 == 1 :
            pick(myState)
        elif i%2 == 0 :
            pick(dealerState)

#게임 전체 진행
if __name__ == "__main__":    
    reset()
    i = 1
    win = 0
    lose = 0
    draw = 0
    while myState.money > 0 and dealerState.money > 0 : 
        print("Round {}".format(i))
        myState.deck = []
        dealerState.deck = []
        myState.num = 0
        dealerState.num = 0
        start()
        print("{} (플레이어 상황)".format(myState))
        print("{} (딜러 상황)".format(dealerState))
        bet = input("얼마를 베팅하시겠습니까? (50~300원 안에서 베팅해주세요)")
        try: 
            bet = int(bet)
            while bet<50 or bet > 300:
                print("주어진 범위 안에서 베팅해주세요.")
                bet = int(input("얼마를 베팅하시겠습니까? (50~300)"))
        except:
            print("다음번엔 제대로 베팅해주세요. 최소 금액인 50원으로 베팅합니다.")
            bet = 50 
        while myState.num <= 21 and dealerState.num <= 21:
            decision = str(input("카드를 더 받으시겠습니까? (y/n)"))
            print("")  #줄 나누기 용 blank code
            if decision == 'y':
                pick(myState)
                if myState.num<=21 and dealerState.num <=16:
                    pick(dealerState)
                print("{} (플레이어 상황)".format(myState))
                print("{} (딜러 상황)".format(dealerState))
            elif decision == 'n':
                while dealerState.num <= 16:
                    pick(dealerState)
                print("{} (플레이어 상황)".format(myState))
                print("{} (딜러 상황)".format(dealerState))
                break
            else : print("제대로 된 결정을 내려주세요")
        if dealerState.num <= 21 and (dealerState.num > myState.num or myState.num>21):
            print("당신이 졌습니다. {}원 만큼을 잃습니다.\n".format(bet))
            myState.money -= bet
            dealerState.money += bet
            lose += 1
        elif myState.num <= 21 and (dealerState.num < myState.num or dealerState.num > 21):
            print("당신이 이겼습니다. {}원 얻으셨습니다.\n".format(bet))
            myState.money += bet
            dealerState.money -= bet
            win += 1
        elif dealerState.num == myState.num :
            print("비겼습니다. 베팅한 돈을 돌려드리겠습니다.\n")
            draw += 1
        i = i + 1
    if dealerState.money <= 0:
        print("제가 졌습니다. 실력이 좋으시네요.")
    elif myState.money <= 0:
        print("제가 이겼습니다. 탕진하셨네요.")
    print("전적 : 승({}) / 패({}) / 무({})".format(win, lose, draw))