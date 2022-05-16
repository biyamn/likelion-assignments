print("\t멋사 커피 자판기")

# 1. 메뉴 선택
# 메뉴의 이름이나 가격은 변경가능!
print("\t  - 메  뉴 -")
print("\t1 : 아메리카노 1,800원")
print("\t2 : 카페라떼 2,700원")
print("\t3 : 핫초코 2,300원")
print("\n========================================")

coffee_won_dict = {1:1800, 2:2700, 3:2300}
coffee_kind_dict = {1: '아메리카노', 2:'카페라떼', 3:'핫초코'}
coffee_kind = int(input("커피 종류를 선택하세요. 번호 입력 >>> ")) # 1 2 3
whipping_YesorNo = input("휘핑크림 추가해드릴까요? (Y/N) >>> ") # Yy Nn
hotOrIce = input("hot / ice를 선택하세요. (hot/ice) >>> ") # hot ice
many_coffee = int(input("몇 잔 드릴까요? >>> ")) # 0 1 2 3 ...
money = many_coffee * coffee_won_dict[coffee_kind]



putMoney1 = int(input(f'총 금액은 {money}원입니다. 돈을 투입해주세요 >>> '))

cnt = 0
while (1):
  # 투입한 금액이 부족한 경우 최대 3번 요청 기능 구현
  if putMoney1 < money:
    if cnt == 3:
        print('금액이 부족합니다. 주문이 취소되었습니다')
        break
    putMoney2 = int(input(f'{money-putMoney1}원이 부족합니다. 돈을 추가로 투입해주세요 >>> '))
    money -= putMoney2
    cnt += 1
  # 한번에 성공시 거스름돈 구현
  else:
    if cnt == 0:
      print(f'{putMoney1}원을 받았습니다. 거스름돈은 {putMoney1 - money}입니다.')
      break
    else:
      print(f'{putMoney2}원을 받았습니다. 거스름돈은 {putMoney1 - money}입니다.')
      break
  
print(f'주문하신 {coffee_kind_dict[coffee_kind]} 나왔습니다.')


# 메뉴 아스키 아트 제공
# 아스키아트가 깨진다면 수정하거나 이모티콘을 사용하셔도 좋습니다!
# 모락모락 뜨거운 김 아스키아트
hot = '''
         S    S 
      S    S    S
'''
#휘핑크림 아스키아트
whipp = '''
           @@@
        @@@   @@
     @@@@      @@ 
    @            @  
'''
# 아메리카노 아스키아트
cup_1 = '''
    **************  
    **         ** ****
      **Coffee**  *** 
        ****** 
'''
# 카페라떼 아스키아트
cup_2 = '''
    **************  
    ***        *** 
    ****Coffee****  
      ****  ****
        ******  
'''
#핫초코 아스키아트
cup_3 = '''
    **************
  ***     *  *   *
  * *      **    * 
  * **   Choco  ** 
  ** **        ** 
      **********
'''

if whipping_YesorNo == 'Y' or whipping_YesorNo == 'y':
  print(whipp)
if hotOrIce == 'hot':
  print(hot)
if coffee_kind == 1:
  print(cup_1)
elif coffee_kind == 2:
  print(cup_2)
else:print(cup_3)