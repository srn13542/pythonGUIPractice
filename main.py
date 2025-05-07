from inoutput import Juice  #inoutput 패키지의 juice를 가져옴..
from tkinter import *
from tkinter import messagebox, simpledialog

#변수 선언
savedMoney:int = 0       #자판기 내에 '결제되어' 저장된 돈, 있는 돈, 거스름돈으로 반환할 수 있는 돈
inputMoney:int = 0       #사용자가 input한 돈
cardMode: bool = False   #카드 결제 가능 여부 플래그
masterMode: bool = False #마스터 모드 관련 플래그

#음료 목록 초기화
def defaultJuInput (juArr:list) :
    juArr.append(Juice.juice("오아시스", 800, 10, 0))
    juArr.append(Juice.juice("오아시스", 800, 10, 0))
    juArr.append(Juice.juice("아쿠아 제로", 2000, 10, 0))
    juArr.append(Juice.juice("레몬워터", 1800, 10, 0))
    juArr.append(Juice.juice("레몬워터", 1800, 10, 0))
    juArr.append(Juice.juice("옥수수수염차", 1600, 10, 0))
    juArr.append(Juice.juice("옥수수수염차", 1600, 10, 0))
    juArr.append(Juice.juice("황금보리", 1600, 10, 0))
    juArr.append(Juice.juice("트레비", 1300, 10, 0))
    juArr.append(Juice.juice("트레비", 1300, 10, 0))
    juArr.append(Juice.juice("밀키스", 1100, 10, 0))
    juArr.append(Juice.juice("펩시콜라", 1100, 10, 0))
    juArr.append(Juice.juice("핫식스", 1300, 10, 0))
    juArr.append(Juice.juice("칠성사이다", 1300, 10, 0))
    juArr.append(Juice.juice("델몬트 망고", 1200, 10, 0))
    juArr.append(Juice.juice("델몬트 망고", 1200, 10, 0))
    juArr.append(Juice.juice("립톤", 1200, 10, 0))
    juArr.append(Juice.juice("델몬트 사과", 1100, 10, 0))
    juArr.append(Juice.juice("델몬트 사과", 1100, 10, 0))
    juArr.append(Juice.juice("델몬트 포도", 1100, 10, 0))
    juArr.append(Juice.juice("가나초코", 900, 10, 0))
    juArr.append(Juice.juice("레쓰비", 900, 10, 0))
    juArr.append(Juice.juice("펩시 제로", 1100, 10, 0))
    juArr.append(Juice.juice("핫6 제로", 1300, 10, 0))
    juArr.append(Juice.juice("솔의눈", 1200, 10, 0))
    juArr.append(Juice.juice("레쓰비 라떼", 1200, 10, 0))
    juArr.append(Juice.juice("게토레이", 1000, 10, 0))
    juArr.append(Juice.juice("게토레이", 1000, 10, 0))
    juArr.append(Juice.juice("코코리치 포도", 1000, 10, 0))
    juArr.append(Juice.juice("잔치집 식혜", 1000, 10, 0))
    return juArr

#관리자 모드에 str 반환하기 위한 코드.. 
def printJuice (juArr:list) :
    juStr:str = ""
    for i in juArr:
        juStr += f"{i.juName} : {i.juCount} 개, 판매된 갯수: {i.juSellCount}\n"
    return juStr

def runningJapangi() :    #자판기의 mainFunc() 
    isRun:bool = True
    cmdJpg:str = ""    #cmd 자판기.. 나중에는 버튼으로 바꿔야 하나? gui 먼저 연구해봐도 좋을듯 
    print("자판기 프로그램 사용 설명서입니다.")  #임시 cmd
    print("--------------------------------------------------------------------------------------------------------")
    print("--------------------------------------------------------------------------------------------------------")
    print("\n 계속하시려면 아무 키나 누르세요")


#거스름돈 반환 함수
def changeMoney() :
    global inputMoney
    mon1000 = inputMoney//1000
    inputMoney -= mon1000*1000
    mon500 = inputMoney//500
    inputMoney -= mon500*500
    mon100 = inputMoney//100
    inputMoney -= mon100*100
    mon50 = inputMoney//50
    inputMoney -= mon50*50

    explLabel['text'] = f"거스름돈 1000원 {mon1000}장, 500원 {mon500}개, 100원 {mon100}개, 50원 {mon50}개 반환되었습니다."
    moneyLabel['text'] = f"{inputMoney}원"
    canBuyJuice()

def insertMoney(amount: int) :
    global inputMoney, cardMode
    inputMoney += amount
    cardMode = False
    print(f"현재 투입된 금액: {inputMoney}원")
    moneyLabel['text'] = f"{inputMoney}원"
    updateJuiceButtons()

def selectCard() :
    global cardMode
    cardMode = True
    explLabel['text'] = "카드 결제 모드: 모든 음료 구매 가능"
    updateJuiceButtons()

#구매 가능 여부 판단
def canBuyJuice() :
    global inputMoney, cardMode
    for juice in juArr: 
        if cardMode :
            juice.juCanBuy = True
        else :
            juice.juCanBuy = inputMoney >= juice.juPrice

#버튼 색상 업데이트
def updateJuiceButtons():
    canBuyJuice()
    for juice, button, juImg in juiceWidgets :
        if juice.juCanBuy :
            button['bg'] = 'green'
        else :
            button['bg'] = 'red'

#음료 구매 시도 
def attemptPurchase(index):
    global inputMoney, savedMoney, cardMode
    juice = juArr[index]
    if juice.juCanBuy and juice.juCount > 0:
        juice.juCount -= 1
        juice.juSellCount += 1
        if not cardMode:
            inputMoney -= juice.juPrice
            savedMoney += juice.juPrice
        elif cardMode:
            savedMoney += juice.juPrice
            cardMode = False
        explLabel['text'] = f"{juice.juName} 구매 완료!"
        moneyLabel['text'] = f"{inputMoney}원"
        updateJuiceButtons()
    else:
        explLabel['text'] = "잔액 부족 또는 품절입니다."
    showSavedMoney['text'] = f"자판기로 번 돈: {savedMoney}원"
    checkThing()

def checkThing() :
    global inputMoney, savedMoney, cardMode
    print(f"inputMoney = {inputMoney}, savedMoney = {savedMoney}, cardMode = {cardMode}")

def showJuiceInfoDialog() :  #참고: https://blog.naver.com/kquddlr/223773510071
    messagebox.showinfo("주스 갯수와 항목", printJuice(juArr))

def masterShow() :
    global masterMode
    if masterMode == True: 
        masterFrame.pack_forget()
        masterMode = False
        explLabel['text'] = "관리자 모드 종료"
    else : 
        masterFrame.pack(fill = "both", side = TOP, padx = 5, pady = 5)
        masterMode = True
        explLabel['text'] = "관리자 모드 진입"

def refreshJuiceText():
    juiceTextBox.config(state=NORMAL)
    juiceTextBox.delete(1.0, END)
    juiceTextBox.insert(END, printJuice(juArr))
    juiceTextBox.config(state=DISABLED)

# 예: index를 직접 입력받아 수정하는 방식
def onEditJuice() :
    index = simpledialog.askinteger("음료 선택", "수정할 음료 번호(index)를 입력하세요:", minvalue=0, maxvalue=len(juArr)-1)
    if index is not None :
        editJuiceInfo(index)

def onPlusJuice() :
    index = simpledialog.askinteger("음료 선택", "수정할 음료 번호(index)를 입력하세요:", minvalue=0, maxvalue=len(juArr)-1)
    if index is not None :
        juice = juArr[index]
        newCount = simpledialog.askinteger("몇 개 추가할 것인지 말씀해주십시오.", f"현재 수량: {juice.juCount}", initialvalue = 0)
        if newCount is not None and newCount - juice.juCount > -1 :
            juice.juCount += newCount
        elif newCount is not None and newCount - juice.juCount <= -1 :
            explLabel['text'] = "음료수의 갯수는 음수가 될 수 없습니다. 0으로 처리합니다."
            juice.juCount = 0

def editJuiceInfo(index) :
    juice = juArr[index]

    #팝업으로 현재 값을 보여주고 새 값을 입력받는다.
    newName  = simpledialog.askstring("이름 수정", f"현재 이름: {juice.juName}", initialvalue = juice.juName)
    newPrice = simpledialog.askinteger("가격 수정", f"현재 가격: {juice.juPrice}", initialvalue = juice.juPrice)
    newCount = simpledialog.askinteger("수량 수정", f"현재 수량: {juice.juCount}", initialvalue = juice.juCount)

    if newName is not None :
        juice.juName = newName
        juice.juSellCount = 0  #메뉴가 바뀌며 판매량도 초기화
    if newPrice is not None :
        juice.juPrice = newPrice
    if newCount is not None :
        juice.juCount = newCount

    explLabel['text'] = f"{index}번 음료가 수정되었습니다."

        # GUI 반영
    _, btn, lbl = juiceWidgets[index]
    btn['text'] = f"{juice.juPrice}"
    lbl['text'] = juice.juName

    updateJuiceButtons()
    refreshJuiceText()

if __name__ == "__main__":

    #루트 화면(root Wondow) 생성/설정
    tk = Tk()
    tk.title("자판기")
    tk.geometry("800x1000+500+300")
    tk.resizable(False,False)

    runningJapangi()
    juArr = []             #주스의 정보를 담을 배열, 
    defaultJuInput(juArr)  #주스 list 초기화

    mainFrame = Frame(tk, relief="solid", bd=10, width="800", height="10", padx = 5, pady = 5)

    juiceFrame:Frame = []
    juButtonList = []
    juiceWidgets = []  #[(juice_obj, button_obj 식으로 저장할 수 있도록 할 예정.)]

    for i in range(0,3):
        juFrame =  Frame(mainFrame, width = 800, padx = 10, pady = 10)
        for j in range(0, 10):
            index = (i * 10) + j
            juice = juArr[index]

            juFrame2 = Frame(juFrame, relief = SOLID, bd = 2, height = 10, width = 5)
            juButton = Button(juFrame2, text = juice.juPrice, command = lambda idx = index: attemptPurchase(idx))
            juImg = Label(juFrame2, text = juArr[(i*10)+(j+1)-1].juName, height = 8, width = 5)
            
            juiceWidgets.append((juice, juButton, juImg))

            juImg.pack(side = TOP, fill = BOTH, expand = TRUE)
            juButton.pack(side = TOP, fill = BOTH, expand = TRUE)
            juFrame2.pack(side = LEFT, fill = BOTH, expand = TRUE)
        juFrame.pack(fill = "x", expand = "true")
    mainFrame.pack(fill = "both")

    payFrame = Frame(tk)
    btn1000 = Button(payFrame, text = "1000원", width = 10, command = lambda: insertMoney(1000))
    btn500  = Button(payFrame, text = "500원", width = 10,  command = lambda: insertMoney(500))
    btn100  = Button(payFrame, text = "100원", width = 10,  command = lambda: insertMoney(100))
    btn50   = Button(payFrame, text = "50원" , width = 10,  command = lambda: insertMoney(50))  #인자가 필요하기에 lambda를 쓴다. 
    cashBtn = Button(payFrame, text="현금", width = 20)
    cardBtn = Button(payFrame, text="카드", width = 20, command = selectCard)
    refundBtn = Button(payFrame, text = "거스름돈 반출", width = 20, command = changeMoney)  #혹은 command = changeMoney의 식으로, 함수 참조만 전달할 수 있다고 한다. 
    moneyLabel = Label(payFrame, text = "0원", width = 20, bg = 'white', bd = 1, relief = SOLID)
    explLabel = Label(payFrame, text = "설명이 출력되는 창입니다.", bg = 'white', bd = 1, relief = SOLID, width = 10, height = 5)
    managerBtn = Button(payFrame, text = "관리자 모드 전환 버튼", width = 20, command = masterShow)

    btn1000.grid(row = 0, column = 0, padx = 5, pady = 5)
    btn500.grid(row = 0, column = 1, padx = 5, pady = 5)
    btn100.grid(row = 0, column = 2, padx = 5, pady = 5)
    btn50.grid(row = 0, column = 3, padx = 5, pady = 5)
    cashBtn.grid(row = 0, column = 4, padx = 10) #side로 배치설정, padx로 좌우여백 설정, pady로 상하여백설정
    cardBtn.grid(row = 1, column = 4, padx = 10)  #text 수정 희망 시 button['text']에 접근하여 수정인가봄
    moneyLabel.grid(row = 1, column = 0, columnspan = 4, padx = 5, pady = 5)
    refundBtn.grid(row = 2, column = 4, padx = 10, pady = 5)
    explLabel.grid(row=5, column=0, columnspan=5, rowspan = 3, padx=5, pady=10, sticky='we')
    managerBtn.grid(row = 8, column = 4, padx = 5, pady = 90, sticky = 'se')
    payFrame.pack(fill = BOTH, pady = 30, padx = 10, side = RIGHT)

    updateJuiceButtons()

    #--------------------Master Mode
    masterFrame = Frame(tk, relief = SOLID, bd = 2, width = 800, height = 500)
    #자판기 관리자 모드에서, 이미 있는 배열을 넘어서도록 음료수를 추가할 수는 없게 할 예정
    #단, 이미 있는 음료수들의 '종류'와 '갯수'를 수정하고, 
    #음료수가 판매된 갯수, 등을... 알 수 있도록 한다...
    # showJuiceCountxt = printJuice(juArr)
    showSavedMoney = Label(masterFrame, text = f"자판기로 번 돈: {savedMoney}원")
    inputJuice  = Button(masterFrame, text = "음료수 재고 추가", command = onPlusJuice)
    editJuice   = Button(masterFrame, text = "음료수 재고 관리", command = onEditJuice)
    showJpgInfo = Button(masterFrame, text = "자판기 내 음료 정보 확인", command = lambda : showJuiceInfoDialog())
    juiceTextBox = Text(masterFrame, height = 10, width = 60, state = DISABLED)
    showSavedMoney.pack(side = TOP, fill = X, padx = 5, pady = 5)
    inputJuice.pack(side = TOP, fill = X, padx = 5, pady = 5)
    editJuice.pack(side = TOP, fill = X, padx = 5, pady = 5)
    showJpgInfo.pack(side = TOP, fill = X, padx = 5, pady = 5)
    juiceTextBox.pack(side = TOP, fill = X, padx = 5, pady = 5)
    # masterFrame.pack(fill = "both", side = TOP)
    tk.mainloop()


