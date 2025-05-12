#주스 객체를 정의하는 파일, 
#주스의 이름, 가격, 갯수, 팔린 횟수, 구매 가능한가 등이 담겨있다. 
#juice의 객체 내에 포함되는 변수에는 ju를 붙였다. 

class juice:
    juName:str = ""
    juPrice:int = 0
    juCount:int = 0
    juSellCount:int = 0
    juCanBuy:bool = False


    def __init__(self, name, price, count = 0, sellCount = 0, canBuy = False) :
        self.juName = name
        self.juPrice = price
        self.juCount = count
        self.juSellCount = sellCount
        self.juCanBuy = canBuy 
    
