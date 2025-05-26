import tkinter

from inoutput import Juice #inoutput 패키지의 juice를 가져옴..
from tkinter import *
from tkinter import messagebox, simpledialog, PhotoImage, ttk

#전역 변수 선언
savedMoney:int = 0       #자판기 내에 '결제되어' 저장된 돈
inputMoney:int = 0       #사용자가 input한 돈
cardMode: bool = False   #카드 결제 가능 여부 플래그
masterMode: bool = False #마스터 모드 관련 플래그
listJuice : list = ["가나초코", "게토레이", "델몬트망고", "델몬트사과", "델몬트포도", "레몬워터", "레쓰비", "레쓰비라떼", "립톤",
                    "밀키스", "솔의눈", "아쿠아제로","오아시스", "옥수수수염차", "잔치집식혜", "칠성사이다", "코코리치포도", "트레비",
                    "펩시제로", "펩시콜라", "핫6제로", "핫식스", "황금보리"]


#음료 목록 초기화
def defaultJuInput (juArr:list) :
    juArr.append(Juice.juice("오아시스", 800, 10, 0))
    juArr.append(Juice.juice("오아시스", 800, 10, 0))
    juArr.append(Juice.juice("아쿠아제로", 2000, 10, 0))
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
    juArr.append(Juice.juice("델몬트망고", 1200, 10, 0))
    juArr.append(Juice.juice("델몬트망고", 1200, 10, 0))
    juArr.append(Juice.juice("립톤", 1200, 10, 0))
    juArr.append(Juice.juice("델몬트사과", 1100, 10, 0))
    juArr.append(Juice.juice("델몬트사과", 1100, 10, 0))
    juArr.append(Juice.juice("델몬트포도", 1100, 10, 0))
    juArr.append(Juice.juice("가나초코", 900, 10, 0))
    juArr.append(Juice.juice("레쓰비", 900, 10, 0))
    juArr.append(Juice.juice("펩시제로", 1100, 10, 0))
    juArr.append(Juice.juice("핫6제로", 1300, 10, 0))
    juArr.append(Juice.juice("솔의눈", 1200, 10, 0))
    juArr.append(Juice.juice("레쓰비라떼", 1200, 10, 0))
    juArr.append(Juice.juice("게토레이", 1000, 10, 0))
    juArr.append(Juice.juice("게토레이", 1000, 10, 0))
    juArr.append(Juice.juice("코코리치포도", 1000, 10, 0))
    juArr.append(Juice.juice("잔치집식혜", 1000, 10, 0))
    return juArr

available_juice_names = ["가나초코", "게토레이", "델몬트망고", "델몬트사과", "델몬트포도", "레몬워터", "레쓰비", "레쓰비라떼", "립톤",
                    "밀키스", "솔의눈", "아쿠아제로","오아시스", "옥수수수염차", "잔치집식혜", "칠성사이다", "코코리치포도", "트레비",
                    "펩시제로", "펩시콜라", "핫6제로", "핫식스", "황금보리"]
#------------------------------------------ 일반적인 자판기 func


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
    updateJuiceButtons()


#'1000원', '500원', '100원', '50원' 버튼을 눌렀을 때 실행되는 함수
def insertMoney(amount: int) :
    global inputMoney, cardMode
    inputMoney += amount
    cardMode = False
    print(f"현재 투입된 금액: {inputMoney}원")
    moneyLabel['text'] = f"{inputMoney}원"
    updateJuiceButtons()


#카드 결제 버튼 시 수행되는 함수
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
            juice.juCanBuy = inputMoney >= juice.juPrice and (juice.juCount!=0)


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


#자판기 내 음료 정보 확인 버튼 클릭 시 주스 리스트를 dialog로 출력하는 함수. 
def showJuiceInfoDialog() :
    messagebox.showinfo("주스 갯수와 항목", printJuice(juArr))





#마스터 모드 전환 버튼 클릭 시 master mode를 보이는 버튼 ---------- master mode
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


#관리자 모드 시 juice list를 출력한다.  
def printJuice (juArr:list) :
    juStr:str = ""
    for i in juArr:
        juStr += f"{i.juName} : {i.juCount} 개, 판매된 갯수: {i.juSellCount}\n"
    return juStr


#'음료수 재고 추가', '음료수 재고 관리' func를 통해 음료수의 정보가 수정되었을 때, 그를 GUI에 반영하기 위한 함수
def refreshJuiceText():
    juiceTextBox.config(state=NORMAL)
    juiceTextBox.delete(1.0, END)
    juiceTextBox.insert(END, printJuice(juArr))
    juiceTextBox.config(state=DISABLED)


#index를 직접 받아 수정한다. '음료수 재고 추가'에 쓰이는 함수.
def onEditJuice() :
    index = simpledialog.askinteger("음료 선택", "수정할 음료 번호(index)를 입력하세요:", minvalue=0, maxvalue=len(juArr)-1)
    if index is not None :
        editJuiceInfo(index)


#index를 입력받아 index에 따른 음료수의 갯수를 수정한다. '음료수 재고 관리'에 쓰이는 함수.
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

def get_new_juice_name_via_listbox(current_name, available_names):
    selected_value = None

    dialog_window = tkinter.Toplevel()
    dialog_window.title("음료 이름 선택 (리스트박스)")

    # 현재 이름 표시 레이블
    current_name_label = ttk.Label(dialog_window, text=f"현재 이름: {current_name}")
    current_name_label.pack(pady=10)

    # 리스트박스를 담을 프레임
    listbox_frame = tkinter.Frame(dialog_window)
    listbox_frame.pack(pady=5)

    # 리스트박스 생성
    listbox = tkinter.Listbox(listbox_frame, height=5, selectmode=tkinter.SINGLE)
    listbox.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True)

    # 리스트박스에 항목 추가
    for item in available_names:
        listbox.insert(tkinter.END, item)

    # 현재 주스 이름을 자동으로 선택
    try:
        current_index = available_names.index(current_name)
        listbox.selection_set(current_index)
        listbox.see(current_index) # 선택된 항목으로 스크롤
    except ValueError:
        pass # 현재 이름이 목록에 없으면 아무것도 안 함

    # 스크롤바 추가
    scrollbar = ttk.Scrollbar(listbox_frame, orient="vertical", command=listbox.yview)
    scrollbar.pack(side=tkinter.RIGHT, fill="y")
    listbox.config(yscrollcommand=scrollbar.set)

    # --- 선택 완료 버튼을 눌렀을 때 실행될 함수 ---
    def on_select():
        nonlocal selected_value
        selected_indices = listbox.curselection()
        if selected_indices:
            index = selected_indices[0]
            selected_value = listbox.get(index) # 선택된 값 저장
        dialog_window.destroy() # <-- 이 부분이 현재 팝업 창만 닫습니다!

    # "선택 완료" 버튼
    select_button = ttk.Button(dialog_window, text="선택 완료", command=on_select)
    select_button.pack(pady=10)

    # 창 X 버튼을 눌렀을 때도 selected_value가 None이 되도록 처리
    # dialog_window.protocol("WM_DELETE_WINDOW", dialog_window.destroy) # 이미 on_select에서 처리하므로 중복될 수 있음.

    # 이 창이 닫힐 때까지 대기 (모달 창처럼 동작)
    dialog_window.grab_set()    # 이 창에 포커스를 고정 (뒤의 메인 창 조작 불가)
    dialog_window.wait_window() # 이 창이 닫힐 때까지 대기

    return selected_value


#주스의 정보를 수정한다. 
def editJuiceInfo(index) :
    juice = juArr[index]

    #팝업으로 현재 값을 보여주고 새 값을 입력받는다.
    newName  = get_new_juice_name_via_listbox(juice.juName, available_juice_names)
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
    _ , btn, lbl = juiceWidgets[index]
    image_path = f"img/{newName}.png"
    #img['text'] = PhotoImage(file=image_path)
    btn['text'] = f"{juice.juPrice}"
    photo =PhotoImage(file=image_path)
    lbl.image = photo
    lbl.configure(image=photo)

    updateJuiceButtons()
    refreshJuiceText()


#--------------------main func --------------


if __name__ == "__main__":

    #루트 화면(root Wondow) 생성/설정
    tk = Tk()
    tk.title("자판기")
    tk.geometry("1000x800+500+300")
    tk.resizable(True,True)


    juArr = []             #주스의 정보를 담을 배열, 
    defaultJuInput(juArr)  #주스 list 초기화


    mainFrame = Frame(tk, relief="solid", bd=10, width="800", height="10", padx = 5, pady = 5)


    juiceFrame:Frame = []
    juiceWidgets = []  #[(juice_obj, button_obj 식으로 저장할 수 있도록 할 예정.)]


    for i in range(0,3):
        juFrame =  Frame(mainFrame, width = 1000, padx = 10, pady = 10)
        for j in range(0, 10):
            index = (i * 10) + j
            juice = juArr[index]

            juFrame2 = Frame(juFrame, relief = SOLID, bd = 2, height = 10, width = 5)
            juButton = Button(juFrame2, text = juice.juPrice, command = lambda idx = index: attemptPurchase(idx))
            # juImg = Label(juFrame2, text = juArr[(i*10)+(j+1)-1].juName, height = 8, width=5)
            image_path = f"img/{juArr[index].juName}.png"
            juImgpath = PhotoImage(file=image_path)
            juImg = Button(juFrame2, image=juImgpath, height=100, width=80)
            #객체 별로로 생성하게 하기 위한 코드
            juImg.image = juImgpath

            juiceWidgets.append((juice, juButton, juImg))

            juImg.pack(side=TOP, fill= BOTH, expand =TRUE)
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

    btn1000.grid(row = 0, column = 0, padx = 5)
    btn500.grid(row = 0, column = 1, padx = 5)
    btn100.grid(row = 0, column = 2, padx = 5)
    btn50.grid(row = 0, column = 3, padx = 5)
    cashBtn.grid(row = 0, column = 4, padx = 10) #side로 배치설정, padx로 좌우여백 설정, pady로 상하여백설정
    cardBtn.grid(row = 1, column = 4, padx = 10)  #text 수정 희망 시 button['text']에 접근하여 수정인가봄
    moneyLabel.grid(row = 1, column = 0, columnspan = 4, padx = 5)
    refundBtn.grid(row = 2, column = 4, padx = 10, pady = 5)
    explLabel.grid(row=5, column=0, columnspan=5, rowspan = 1, padx=5, pady=10, sticky='we')
    managerBtn.grid(row = 6, column = 4, padx = 5, pady = 20)
    payFrame.pack(fill = BOTH, pady = 30, padx = 10, side = RIGHT)
    updateJuiceButtons()


    #--------------------Master Mode
    masterFrame = Frame(tk, relief = SOLID, bd = 2, width = 800, height = 300)
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
    tk.mainloop()


