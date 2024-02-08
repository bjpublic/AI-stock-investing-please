coffee = 10
while True:
    coffee = coffee - 1
    print("커피를 한 잔 팔고, {}잔 남았습니다.".format(coffee))
    if coffee == 0:
        print("매진되었습니다.")
        break