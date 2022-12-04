import InnerFunction as IF

def plus100(gameWindow):
    gameWindow.bettingCost += 100
    gameWindow.bDisplay.setText('bet: ' + str(gameWindow.bettingCost))

def minus100(gameWindow):
    gameWindow.bettingCost -= 100
    gameWindow.bDisplay.setText('bet: ' + str(gameWindow.bettingCost))

def deal(gameWindow):# 베팅 값이 음수일 때 (비정상)
    if gameWindow.bettingCost < 0:
        # 경고메세지 출력
        gameWindow.display.setText("Bet on the positive value.")
        # 베팅 값을 1000으로 초기화
        gameWindow.bettingCost = 1000
        # 현재 베팅된 금액 표시
        gameWindow.bDisplay.setText('bet: ' + str(gameWindow.bettingCost))
        return
    # 베팅 값이 음수일 때
    elif gameWindow.bettingCost > 0:
        # 베팅 값이 1000 이하일 때 (비정상)
        if gameWindow.bettingCost < 1000:
            # 경고 메세지 출력
            gameWindow.display.setText("betting min is 1000")
            # 베팅 값 1000으로 초기화
            gameWindow.bettingCost = 1000
            # 현재 베팅된 금액 표시
            gameWindow.bDisplay.setText('bet: ' + str(gameWindow.bettingCost))
            return
        # 현재 갖고있는 돈 보다 베팅액이 많을 때 (비정상)
        elif gameWindow.bettingCost > gameWindow.money:
            # 경고 메세지 출력
            gameWindow.display.setText("You don't have much money")
            # 베팅 값 1000으로 초기화
            gameWindow.bettingCost = 1000
            # 현재 베팅된 금액 표시
            gameWindow.bDisplay.setText('bet: ' + str(gameWindow.bettingCost))
            return
        # 위의 조건을 전부 충족하지 않을 때 (정상)
        else:
            # 시작 메세지 출력
            gameWindow.display.setText("let's start!")
            # 각 버튼들의 사용 가능 여부를 설정
            gameWindow.stayBtn.setDisabled(False)
            gameWindow.appendBtn.setDisabled(False)
            gameWindow.plusBetBtn.setDisabled(True)
            gameWindow.minusBetBtn.setDisabled(True)
            gameWindow.dealBtn.setDisabled(True)
            # 카드 뭉치 생성
            gameWindow.card = IF.setCard()
            # Player에게 카드 두 장 주기 (int 형 list)
            gameWindow.intPlayercards = IF.twoCard(gameWindow.card)
            # print(gameWindow.intPlayercards)
            # [34, 5]F
            # Dealer에게 카드 두 장 주기 (int 형 list)
            gameWindow.intDealercards = IF.twoCard(gameWindow.card)
            # Player와 Dealer의 카드들을 int에서 string으로 변환
            gameWindow.dealerCards = IF.intToStringCard(gameWindow.intDealercards)
            gameWindow.playerCards = IF.intToStringCard(gameWindow.intPlayercards)
            # print(gameWindow.intToStringCard)
            # ['hearts9', 'spades6']
            # 플레이어의 카드 두 장 표시
            gameWindow.displayPlayerCard(gameWindow.pCardList[0], gameWindow.playerCards[0], gameWindow.xPoint[0])
            gameWindow.displayPlayerCard(gameWindow.pCardList[1], gameWindow.playerCards[1], gameWindow.xPoint[1])
            # 딜러의 카드 한 장 표시
            gameWindow.displayDealerCard(gameWindow.dCardList[0], gameWindow.dealerCards[0], gameWindow.xPoint[0])
            # gameWindow.displayDealerCard(gameWindow.dCardList[1], gameWindow.dealercards[1], gameWindow.xPoint[1])
            # 플레이어의 카드의 총합이 21일 때 (블랙잭)
            if IF.count(gameWindow.intPlayercards) == 21:
                # 메세지 출력
                gameWindow.QMessageBoxExec("Congratulations! \nBlack Jack!")
                # money Update
                gameWindow.money = IF.setMoney(gameWindow.money, gameWindow.bettingCost, 3)
                gameWindow.mDisplay.setText('money: ' + str(gameWindow.money))
            return
    # 베팅값이 0일 때
    else:
        # 경고 메세지 출력
        gameWindow.display.setText("Please click betting number")
        return

def newCard(gameWindow):# 플레이어의 카드 더미에 카드 추가하기
    IF.cardAppend(gameWindow.intPlayercards, gameWindow.card)
    # print(gameWindow.intPlayercards)
    # [34, 5, 7]
    # 플레이어의 카드를 string으로 변경
    gameWindow.playerCards = IF.intToStringCard(gameWindow.intPlayercards)
    for pLabel in gameWindow.pCardList:
        # pl의 인덱스 값을 저장할 idx 변수
        idx = gameWindow.pCardList.index(pLabel)
        # pl이 intPlatercards 안의 변수일 때
        if idx < len(gameWindow.intPlayercards):
            # pl을 화면에 배치
            gameWindow.displayPlayerCard(pLabel, gameWindow.playerCards[idx], gameWindow.xPoint[idx])
    # burst인지 확인
    if IF.burst(gameWindow.intPlayercards):
        # burst 메세지 출력
        gameWindow.QMessageBoxExec("Burst!")
        # money 차감
        gameWindow.money = IF.setMoney(gameWindow.money, gameWindow.bettingCost, 0)
        # money 반영
        gameWindow.mDisplay.setText('money: ' + str(gameWindow.money))
    # Black Jack 완성
    elif IF.count(gameWindow.intPlayercards) == 21:
        # Black Jack 메세지 출력
        gameWindow.QMessageBoxExec("Congratulations! \nBlack Jack!")
        # money 증가
        gameWindow.money = IF.setMoney(gameWindow.money, gameWindow.bettingCost, 3)
        # money 반영
        gameWindow.mDisplay.setText('money: ' + str(gameWindow.money))
    # 아무런 일도 일어나지 않음
    else:
        return

def stay(gameWindow):# Dealer 카드
    gameWindow.displayDealerCard(gameWindow.dCardList[1], gameWindow.dealerCards[1], gameWindow.xPoint[1])
    # Dealer Burst
    if IF.count(gameWindow.intDealercards) > 21:
        # 메세지 출력
        gameWindow.QMessageBoxExec("you win!")
        # money 증가
        gameWindow.money = IF.setMoney(gameWindow.money, gameWindow.bettingCost, 1)
        # money 반영
        gameWindow.mDisplay.setText('money: ' + str(gameWindow.money))
        return
    else:
        # Dealer 카드 합이 17이상이면 더이상 추가 카드를 받을 수 없음
        while IF.count(gameWindow.intDealercards) < 17:
            # Dealer 카드 추가
            IF.cardAppend(gameWindow.intDealercards, gameWindow.card)
            # Dealer의 카드를 string으로 변환
            gameWindow.dealerCards = IF.intToStringCard(gameWindow.intDealercards)
            # Dealer의 카드 배치
            for dLabel in gameWindow.dCardList:
                # 현재 카드의 인덱스를 저장할 변수 idx
                idx = gameWindow.dCardList.index(dLabel)
                # 카드가 리스트 안에 있는지 확인
                if idx < len(gameWindow.intDealercards):
                    # Dealer의 카드 배치
                    gameWindow.displayDealerCard(dLabel, gameWindow.dealerCards[idx], gameWindow.xPoint[idx])
        # Dealer가 burst되었을 때
        if IF.burst(gameWindow.intDealercards):
            # 메세지 출력
            gameWindow.QMessageBoxExec("you win!")
            # money 증가
            gameWindow.money = IF.setMoney(gameWindow.money, gameWindow.bettingCost, 3)
            # money 반영
            gameWindow.mDisplay.setText('money: ' + str(gameWindow.money))
            return
        # Dealer가 Black Jack일 때
        elif IF.count(gameWindow.intDealercards) == 21:
            # 메세지 출력
            gameWindow.QMessageBoxExec("You lose!")
            # money 유지
            gameWindow.money = IF.setMoney(gameWindow.money, gameWindow.bettingCost, 0)
            # money 반영
            gameWindow.mDisplay.setText('money: ' + str(gameWindow.money))
            return
        else:
            # 그렇지 않았을 때
            # 결과 확인
            res = IF.fight(IF.count(gameWindow.intPlayercards), IF.count(gameWindow.intDealercards))
            # 비겼을 때
            if res == 2:
                # 메세지 출력
                gameWindow.QMessageBoxExec("Draw!")
                # money 증가
                gameWindow.money = IF.setMoney(gameWindow.money, gameWindow.bettingCost, 2)
                # money 반영
                gameWindow.mDisplay.setText('money: ' + str(gameWindow.money))
                return
            # Player가 이겼을 때
            elif res == 1:
                # 메세지 출력
                gameWindow.QMessageBoxExec("You win!")
                # money 증가
                gameWindow.money = IF.setMoney(gameWindow.money, gameWindow.bettingCost, 3)
                # money 반영
                gameWindow.mDisplay.setText('money: ' + str(gameWindow.money))
                return
            # Player가 졌을 때
            else:
                # 메세지 출력
                gameWindow.QMessageBoxExec("You lose!")
                # money 감소
                gameWindow.money = IF.setMoney(gameWindow.money, gameWindow.bettingCost, 0)
                # money 반영
                gameWindow.mDisplay.setText('money: ' + str(gameWindow.money))
                return

def reset(gameWindow):
    # 조건 초기화
    gameWindow.stayBtn.setDisabled(True)
    gameWindow.appendBtn.setDisabled(True)
    gameWindow.dealBtn.setDisabled(False)
    gameWindow.plusBetBtn.setDisabled(False)
    gameWindow.minusBetBtn.setDisabled(False)
    gameWindow.clear()
    gameWindow.display.setText('Play more? Click deal button')
    return