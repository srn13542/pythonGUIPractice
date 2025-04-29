from inoutput import Juice  #inoutput 패키지의 juice를 가져옴..
from tkinter import *

def defaultJuInput (juArr:list) :
    #list 초기화 function. 
    juArr.append(Juice.juice("오아시스", 800, 10, 0, True))
    juArr.append(Juice.juice("오아시스", 800, 10, 0, True))
    juArr.append(Juice.juice("아쿠아 제로", 2000, 10, 0, True))
    juArr.append(Juice.juice("레몬워터", 1800, 10, 0, True))
    juArr.append(Juice.juice("레몬워터", 1800, 10, 0, True))
    juArr.append(Juice.juice("옥수수 수염차", 1600, 10, 0, True))
    juArr.append(Juice.juice("옥수수 수염차", 1600, 10, 0, True))
    juArr.append(Juice.juice("황금보리", 1600, 10, 0, True))
    juArr.append(Juice.juice("트레비", 1300, 10, 0, True))
    juArr.append(Juice.juice("트레비", 1300, 10, 0, True))
    juArr.append(Juice.juice("밀키스", 1100, 10, 0, True))
    juArr.append(Juice.juice("펩시콜라", 1100, 10, 0, True))
    juArr.append(Juice.juice("핫식스", 1300, 10, 0, True))
    juArr.append(Juice.juice("칠성사이다", 1300, 10, 0, True))
    juArr.append(Juice.juice("델몬트 망고", 1200, 10, 0, True))
    juArr.append(Juice.juice("델몬트 망고", 1200, 10, 0, True))
    juArr.append(Juice.juice("립톤", 1200, 10, 0, True))
    juArr.append(Juice.juice("델몬트 사과에이드", 1100, 10, 0, True))
    juArr.append(Juice.juice("델몬트 사과에이드", 1100, 10, 0, True))
    juArr.append(Juice.juice("델몬트 포도에이드", 1100, 10, 0, True))
    juArr.append(Juice.juice("가나초코", 900, 10, 0, True))
    juArr.append(Juice.juice("레쓰비 마일드", 900, 10, 0, True))
    juArr.append(Juice.juice("펩시 제로 콜라", 1100, 10, 0, True))
    juArr.append(Juice.juice("핫6 제로", 1300, 10, 0, True))
    juArr.append(Juice.juice("솔의눈", 1200, 10, 0, True))
    juArr.append(Juice.juice("레쓰비 카페타임 라떼", 1200, 10, 0, True))
    juArr.append(Juice.juice("게토레이", 1000, 10, 0, True))
    juArr.append(Juice.juice("게토레이", 1000, 10, 0, True))
    juArr.append(Juice.juice("코코리치 포도", 1000, 10, 0, True))
    juArr.append(Juice.juice("잔치집 식혜", 1000, 10, 0, True))
    return juArr

def printJuice (juArr:list) :
    for i in juArr:
        print(i.juName)

def runningJapangi() :    #자판기의 mainFunc() 
    isRun:bool = True
    cmdJpg:str = ""    #cmd 자판기.. 나중에는 버튼으로 바꿔야 하나? gui 먼저 연구해봐도 좋을듯 
    while(isRun) :
        print("자판기 프로그램 사용 설명서입니다.")  #임시 gui
        print("--------------------------------------------------------------------------------------------------------")
        print("1. 지불 방법 선택")
        print("  - 현금 cash : 동전이나 지폐를 자판기에 투입해 물품을 구매합니다.")
        print("  - 카드 card : 현금 투입 없이, 판매중인 물품중 최고 금액을 투입합니다. 이후 현금 사용은 불가능합니다.\n")
        print("2. 지불")
        print("  - 현금 : 100원을 투입하려면 100을 입력하세요. (100원, 500원, 1000원만 투입 가능)")
        print("  - 카드 : 입력 없이 자동으로 잔고가 감소합니다.")
        print("3. 구매")
        print(" 원하는 상품의 버튼을 눌러주세요(임시:index)\n")
        print("명령어 목록    -추후 무슨 버튼에 ficus시 출력되도록 수정해야함")
        print("  - help 도움 : 프로그램 사용 설명서를 보여줍니다.")
        print("  - list 목록 : 물품의 모든 목록을 보여줍니다.")
        print("  - buyable 구매가능목록 : 현재 구매 가능한 물품의 목록을 보여줍니다.\n",
              "                          다음 단계가 정해지지 않은 경우, 명령어를 입력하지 않았을 때에도 본 목록이 보여집니다.")
        print("  - 100 500 1000 : 해당되는 금액을 자판기에 투입합니다.")
        print("  - refund 환불 : 투입한 금액을 환불받습니다.")
        print("  - exit 나가기 : 자판기 프로그램을 종료합니다.")
        print("--------------------------------------------------------------------------------------------------------")
        print("\n 계속하시려면 아무 키나 누르세요")
        print("TODO:: 사용자가 넣은 금액 1000/500/100 단위로 표시되어야 함")
        print("TODO:: 투입된 금액도 적어두어야 함")    
        #입력받아서 대충 값에 따라 switch-case문 돌리기..func 분리 
             # ++ python에는 switch 대신 발전된 match-case와 딕셔너리 사용 예시가 있다고. 
             # https://okeybox.tistory.com/395


def someBtnEvent() :
    button['text'] = "버튼 누름"

if __name__ == "__main__":
    #변수 선언
    savedMoney:int = 0     #자판기 내에 '결제되어' 저장된 돈, 있는 돈, 거스름돈으로 반환할 수 있는 돈
    inputMoney:int = 0     #사용자가 input한 돈
    input1000 :int = 0     #사용자가 1000원 몇 개 넣었는지
    input500  :int = 0     #사용자가 500원 몇 개 넣었는지
    input100  :int = 0     #사용자가 100원 몇 개 넣었는지지

    print ("자판기 프로그램 사용 설명서입니다.")

    juArr = []             #주스의 정보를 담을 배열, 
    defaultJuInput(juArr)  #주스 list 초기화
    printJuice(juArr)      #테스트용, 주스list 출력, 정상적 출력 확인(추후 삭제)

    #돈을 인풋받기 위한..

    #그 전에 tkinter gui 화면부터 먼저 만들기로 함
    #루트 화면(root Wondow) 생성/설정
    tk = Tk()
    tk.title("자판기")
    tk.geometry("600x800+500+300")
    tk.resizable(False,False)
    
    #frame1을 임시.. 버튼 넣는 곳으로 지정. 
    mainFrame = Frame(tk, relief="solid", bd=10, width="600", height="10")
    #텍스트 표시
    label = Label(mainFrame, text="자판기 프로그램 임시 gui \n")
    label.pack() #label 배치 실행
    # btnFrame1 = Frame(mainFrame, width="600")  

    #버튼들.. 임시로
    # button1 = Button(btnFrame1, text="Button-1\n", height=10)
    # button2 = Button(btnFrame1, text="Button-1\n", height=10)
    # button3 = Button(btnFrame1, text="Button-1\n", height=10)
    # button4 = Button(btnFrame1, text="Button-1\n", height=10)
    # button5 = Button(btnFrame1, text="Button-1\n", height=10)
    # button6 = Button(btnFrame1, text="Button-1\n", height=10)
    # button7 = Button(btnFrame1, text="Button-1\n", height=10)
    # button8 = Button(btnFrame1, text="Button-1\n", height=10)
    # button9 = Button(btnFrame1, text="Button-1\n", height=10)
    # button10 = Button(btnFrame1, text="Button-1\n", height=10)
    # button1.pack(side="left", fill="y", expand="true")
    # button2.pack(side="left", fill="y", expand="true")
    # button3.pack(side="left", fill="y", expand="true")
    # button4.pack(side="left", fill="y", expand="true")
    # button5.pack(side="left", fill="y", expand="true")
    # button6.pack(side="left", fill="y", expand="true")
    # button7.pack(side="left", fill="y", expand="true")
    # button8.pack(side="left", fill="y", expand="true")  
    # button9.pack(side="left", fill="y", expand="true")
    # button10.pack(side="left", fill="y", expand="true")  

    # btnFrame2 = Frame(mainFrame, width="600")  

    # button11 = Button(btnFrame2, text="Button-1\n", height=10)
    # button12 = Button(btnFrame2, text="Button-1\n", height=10)
    # button13 = Button(btnFrame2, text="Button-1\n", height=10)
    # button14 = Button(btnFrame2, text="Button-1\n", height=10)
    # button15 = Button(btnFrame2, text="Button-1\n", height=10)
    # button16 = Button(btnFrame2, text="Button-1\n", height=10)
    # button17 = Button(btnFrame2, text="Button-1\n", height=10)
    # button18 = Button(btnFrame2, text="Button-1\n", height=10)
    # button19 = Button(btnFrame2, text="Button-1\n", height=10)
    # button20 = Button(btnFrame2, text="Button-1\n", height=10)
    # button11.pack(side="left", fill="y", expand="true")
    # button12.pack(side="left", fill="y", expand="true")
    # button13.pack(side="left", fill="y", expand="true")
    # button14.pack(side="left", fill="y", expand="true")
    # button15.pack(side="left", fill="y", expand="true")
    # button16.pack(side="left", fill="y", expand="true")
    # button17.pack(side="left", fill="y", expand="true")
    # button18.pack(side="left", fill="y", expand="true")  
    # button19.pack(side="left", fill="y", expand="true")
    # button20.pack(side="left", fill="y", expand="true") 

    # btnFrame3 = Frame(mainFrame, width="600")  

    # button21 = Button(btnFrame3, text="Button-1\n", height=10)
    # button22 = Button(btnFrame3, text="Button-1\n", height=10)
    # button23 = Button(btnFrame3, text="Button-1\n", height=10)
    # button24 = Button(btnFrame3, text="Button-1\n", height=10)
    # button25 = Button(btnFrame3, text="Button-1\n", height=10)
    # button26 = Button(btnFrame3, text="Button-1\n", height=10)
    # button27 = Button(btnFrame3, text="Button-1\n", height=10)
    # button28 = Button(btnFrame3, text="Button-1\n", height=10)
    # button29 = Button(btnFrame3, text="Button-1\n", height=10)
    # button30 = Button(btnFrame3, text="Button-1\n", height=10)
    # button21.pack(side="left", fill="y", expand="true")
    # button22.pack(side="left", fill="y", expand="true")
    # button23.pack(side="left", fill="y", expand="true")
    # button24.pack(side="left", fill="y", expand="true")
    # button25.pack(side="left", fill="y", expand="true")
    # button26.pack(side="left", fill="y", expand="true")
    # button27.pack(side="left", fill="y", expand="true")
    # button28.pack(side="left", fill="y", expand="true")  
    # button29.pack(side="left", fill="y", expand="true")
    # button30.pack(side="left", fill="y", expand="true") 

    # btnFrame1.pack(fill="x", expand=True)
    # btnFrame2.pack(fill="x", expand=True)
    # btnFrame3.pack(fill="x", expand=True)

    juiceFrame:Frame = []
    for i in range(0,3):
        juFrame =  Frame(mainFrame, width="600")
        for j in range(0, 10):
            juButton = Button(juFrame, text=j, height=10)
            juButton.pack(side="left", fill="both", expand="true")
        juFrame.pack(fill="x", expand="true")
    mainFrame.pack(fill="both")


    frame3 = Frame(tk, width="600")
    frame4 = Frame(tk, width="600", height="10")


    button = Button(tk, text="버튼입니다. 누르면 함수가 실행됩니다.", command = someBtnEvent)
    button2 = Button(tk, text="버튼2입니다.")
    button.pack(side=LEFT, padx = 10, pady = 10) #side로 배치설정, padx로 좌우여백 설정, pady로 상하여백설정
    button2.pack(side=LEFT, padx = 10, pady = 10)  #text 수정 희망 시 button['text']에 접근하여 수정인가봄
    tk.mainloop()


