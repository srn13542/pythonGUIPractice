#주스 객체를 정의하는 파일, 
#주스의 이름, 가격, 갯수, 팔린 횟수, 구매 가능한가 등이 담겨있다. 
#juice의 객체 내에 포함되는 변수에는 ju를 붙였다. 

class juice:
    juName = ""
    juPrice = 0
    juCount = 0
    juSellCount = 0
    juCanBuy = False


    def __init__(name, price, count = 0, sellCount = 0, canBuy = False) :
        juName = name
        juPrice = price
        juCount = count
        juSellCount = sellCount
        juCanBuy = canBuy
    
    
