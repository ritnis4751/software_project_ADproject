import random

# 카드들의 모양
marks = ['spades', 'diamonds', 'hearts', 'clubs']
# 카드들의 숫자, 영어
CARDNUMBER = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

# 파일 입출력
def load():
    try:
        f = open("money.dat", 'r')
        return int(f.readline())
    except FileNotFoundError:
        f = open("money.dat", 'w')
        f.write('100000')
        return 100000

# 보유 금액 변화 파일에 저장
def write(money):
    f = open("money.dat", 'w')
    f.write(money)
    f.close()

# 결과에 따라 보유 금액 저장
def setMoney(now, betting, result):
    # lose : 0
    if result == 0:
        write(str(now - betting))
        return now - betting
    # win : 1
    elif result == 1:
        write(str(now + betting))
        return now + betting
    # Black jack : 3
    elif result == 3:
        write(str(int(now + (1.5 * betting))))
        return int(now + (betting * 1.5))
    # draw
    else:
        return now


# 플레이어와 딜러에게 카드 두장씩 지급, 카드 뭉치에서 카드 제거
def twoCard(card):
    cardList = []
    for i in range(2):
        cardList.append(card.pop(0))
    return cardList


# 카드뭉치에서 새로운 카드 받기
def cardAppend(cardList, card):
    # cardlist에 카드 뭉치의 카드 추가
    cardList.append(card.pop(0))

# end 버튼 클릭 이벤트, Lose: 0 Win: 1 Draw 2
def fight(playerResult, dealerResult):
    if playerResult == dealerResult:
        return 2
    elif playerResult < dealerResult:
        return 0
    elif playerResult > dealerResult:
        return 1

# burst인지 확인
def burst(cards):
    result = count(cards)
    if result > 21:
        return True
    else:
        return False

# blackjack인지 확인
def blackjack(cards):
    result = count(cards)
    if result == 21:
        return True
    else:
        return False

# 카드 뭉치 생성
def setCard():
    # 카드를 아무리 많이 뽑아도 17장 이상은 뽑을 수 없음
    return random.sample(range(52), 17)

# 카드패의 합 계산
def count(cardsList):
        sum = 0
        cnt = 0
        for card in cardsList:
            if card % 13 >= 10:
                sum += 10
            else:
                sum += card % 13 + 1
                # 만약 카드가 A라면
                if card % 13 == 0:
                    cnt += 1

        for i in range(cnt):
            # A를 1로 사용할지 11로 사용할지 결정
            if sum + 10 <= 21:
                sum += 10
            else:
                break

        return sum

# 카드패를 문자열로 변환
def intToStringCard(card):
    cardList = []
    for data in card:
        cardSuit = marks[data//13]
        cardNumber = CARDNUMBER[data % 13]
        card = str(cardSuit) + str(cardNumber)
        cardList.append(card)

    return cardList
