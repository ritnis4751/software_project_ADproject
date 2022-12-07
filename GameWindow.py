from PyQt5.QtWidgets import QWidget, QMessageBox, QVBoxLayout, QHBoxLayout, QLabel, QDesktopWidget
from PyQt5.QtGui import QPixmap
from button import Button
from InnerFunction import *
import ButtonFunction as BF
# 게임화면
class GameWindow(QWidget):

    def __init__(self):
        super().__init__()
        
        # window 제목 설정
        self.setWindowTitle("Kookmin Land")
        
        # window 크기 조정
        self.setGeometry(0, 0, 1000, 700)
        
        # window 위치 조정
        self.move(400, 200)
        
        # 메세지 박스 생성
        self.qMsgBox = QMessageBox()
        self.qMsgBox.setWindowTitle("Result")
        
        # money.dat에 있는 정보
        self.money = load()
        # bettingCost 생성
        self.bettingCost = 1000

        self.display = QLabel()
        self.bDisplay = QLabel('bet: ' + str(self.bettingCost))
        self.mDisplay = QLabel('money: ' + str(self.money))
        # 버튼 생성 및 함수와 연결 -----------------따로 임포트
        self.dealBtn = Button("deal", self.deal)
        self.stayBtn = Button("stay", self.stay)
        self.appendBtn = Button("new card", self.newCard)
        self.resetBtn = Button("reset", self.reset)
        self.plusBetBtn = Button("+100", self.plus100)
        self.minusBetBtn = Button("-100", self.minus100)

        # 세로 상자 생성 (+ Button과 - Button을 한 줄에 넣기 위해)
        bettingVbox = QVBoxLayout()
        # +100 버튼과 -100 버튼 세로 박스에 삽입
        bettingVbox.addWidget(self.plusBetBtn)
        bettingVbox.addWidget(self.minusBetBtn)
        
        # +, - 버튼을 담은 세로 박스와 나머지 버튼들을 넣을 가로상자 생성
        displayVbox = QVBoxLayout()
        displayVbox.addStretch(1)
        displayVbox.addWidget(self.display)
        displayVbox.addWidget(self.bDisplay)
        displayVbox.addWidget(self.mDisplay)
        
        # +, - 버튼을 담은 세로 박스와 나머지 버튼들 삽입
        hbox = QHBoxLayout()
        hbox.addLayout(bettingVbox)
        hbox.addWidget(self.dealBtn)
        hbox.addWidget(self.stayBtn)
        hbox.addWidget(self.appendBtn)
        hbox.addWidget(self.resetBtn)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(displayVbox)
        vbox.addLayout(hbox)
        self.setLayout(vbox)
        
        # 사진들을 띄울 x좌표의 리스트
        self.xPoint = [0, 150, 300, 450, 600, 750]

        # Dealer의 카드들을 저장할 리스트
        self.dCardList = []
        # Player의 카드들을 저장할 리스트
        self.pCardList = []
        # 카드들을 레이아웃 할 때 쓸 라벨 생성, 추가
        for i in range(len(self.xPoint)):
            dLabel = QLabel(self)
            pLabel = QLabel(self)
            self.dCardList.append(dLabel)
            self.pCardList.append(pLabel)

        # 카드 배치, 베팅 초기화
        self.clear()
        # show all the widgets
        self.show()

    # 플레이어의 카드 배치
    def displayPlayerCard(self, label, cardShape, xPoint):
        # pixmap: 이미지 삽입 메서드
        self.pixmap = QPixmap(f"./PNG-cards-1.3/{cardShape}").scaledToWidth(100)
        # setPixmap: label 이미지 객체 삽입 메서드
        label.setPixmap(self.pixmap)
        label.move(xPoint, 200)
        label.resize(self.pixmap.width(), self.pixmap.height())
        # label.setText(cardShape)
        # label.move(xPoint, 100)
    
    # 딜러의 카드 배치
    def displayDealerCard(self, label, cardShape, xPoint):
        # pixmap: 이미지를 저장할 객체
        self.pixmap = QPixmap(f"./PNG-cards-1.3/{cardShape}").scaledToWidth(100)
        # setPixmap: label 이미지 객체 삽입 메서드
        label.setPixmap(self.pixmap)
        label.move(xPoint, 0)
        label.resize(self.pixmap.width(), self.pixmap.height())
        # label.setText(cardshape)
        # label.move(xPoint, 0)

    # 게임 보드를 초기화
    def clear(self):
        # Player의 카드가 2장이 될 때까지 카드 뽑기
        for pLabel in self.pCardList:
            # cardsCnt: 현재 카드가 몇 번째 카드인지 세기 위한 int 변수
            cardsCnt = self.pCardList.index(pLabel)
            # 현재 카드의 순서가 2보다 적을 때
            if cardsCnt < 2:
                # 카드 뽑기
                self.displayPlayerCard(pLabel, 'Unknown', self.xPoint[cardsCnt])
            else:
                # 카드를 더이상 뽑지 않음
                self.displayPlayerCard(pLabel, 'None', self.xPoint[cardsCnt])
                
        # Dealer의 카드가 2장이 될 때 까지 카드 뽑기
        for dLabel in self.dCardList:
            # cardsCnt: 현재 카드가 몇 번째 카드인지 세기 위한 int 변수
            cardsCnt = self.dCardList.index(dLabel)
            # 현재 카드의 순서가 2보다 적을 때
            if cardsCnt < 2:
                # 카드 뽑기
                self.displayDealerCard(dLabel, 'Unknown', self.xPoint[cardsCnt])
            else:
                # 카드를 더이상 뽑지 않음
                self.displayDealerCard(dLabel, 'None', self.xPoint[cardsCnt])
        # 베팅 금액 1000으로 초기화
        self.bettingCost = 1000
        self.display.setText('')
        self.bDisplay.setText('bet: ' + str(self.bettingCost))
        self.stayBtn.setDisabled(True)
        self.appendBtn.setDisabled(True)


    def QMessageBoxExec(self, msg):
        msgBox = self.qMsgBox
        msgBox.setText(msg)
        msgBox.exec()
        self.appendBtn.setDisabled(True)
        self.stayBtn.setDisabled(True)
        self.display.setText('If you wanna restart, click reset button')

    def plus100(self):
        BF.plus100(self)

    def minus100(self):
        BF.minus100(self)

    def deal(self):
        BF.deal(self)

    def newCard(self):
        BF.newCard(self)

    def stay(self):
        BF.stay(self)

    def reset(self):
        BF.reset(self)