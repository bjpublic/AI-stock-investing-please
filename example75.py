def intro(name, age, sex=5):
    print("나의 이름은 {}이며, 나이는 {}살입니다.".format(name, age))
    if sex == 5:
        print("저는 남자입니다.")
    else:
        print("저는 여자입니다.")

intro("홍길동", 30)
intro("아이유", 20, 3)