##if
weather="비"
if weather == "비":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else :
    print("준비물 필요없어요")


# weather = input("오늘 날씨는 어때요? ")
# if weather == "비" or weather == "눈":
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else :
#     print("준비물 필요없어요")


# temp=int(input("기온은 어때요? "))
# if temp >= 30:
#     print("너무 더워요. 나가지 마세요")
# elif temp >= 10 and temp < 30 :
#     print("괜찮은 날씨에요")
# elif 0 <= temp < 10:
#     print("외투를 챙기세요")
# else:
#     print("너무 추워요. 나가지 마세요")

# ################################ for(반복문)
# print("대기번호 : 1")
# print("대기번호 : 2")
# print("대기번호 : 3")
# print("대기번호 : 4")

# for waiting_no in [0,1,2,3,4]:
#     print("대기번호 : {0}".format(waiting_no))

    
# for waiting_no in range(1,6):
#     print("대기번호 : {0}".format(waiting_no))

starbucks=["아이언맨","토르","아이엠 그루트"]
for costomer in starbucks:
    print("{0},커피가 준비 되었습니다.".format(costomer))


##########while
# customer="토르"
# index=5
# while index>=1:
#     print("{0},커피가 준비 되었습니다. {1} 번 남았어요.".format(customer,index))
#     index-=1
#     if index == 0:
#         print("커피는 폐기처분되었습니다.")

#무한 루프
# customer="아이언맨" 
# while True:
#     print("{0},커피가 준비 되었습니다.".format(costomer)) 


customer="토르"
person="Unknown"
while person != customer:
    print("{0},커피가 준비 되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요? ")