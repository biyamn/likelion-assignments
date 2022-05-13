import random

'''
덕성여대 멋쟁이사자처럼 10기 1차 python study 세션
실전 문제 도전!

작성일: 2022.04.28(목)
'''

'''
1. 회문
앞으로 읽으나 뒤로 읽으나 동일한 문장을 말한다.
예를 들어서 "mom", "civic", "dad" 등이 회문의 예이다.
사용자로부터 문자열을 입력받고 회문인지를 검사하는 프로그램을 작성하세요.

힌트) 파이썬에서 문자열을 조작하는 방법은?
'''



sentence = input("회문을 측정할 문장을 넣어주세요")
lst1 = []
lst2 = []
for i in sentence:
  lst1.append(i)
sentence_reverse = sentence[::-1]
for i in sentence_reverse:
  lst2.append(i)
  
if ''.join(lst1) == ''.join(lst2):
  print(sentence, '는 회문입니다')
else:
  print(sentence, '는 회문이 아닙니다')




'''
2. mbti의 검사결과는 아래와 같이 16가지 유형이 있다.
'ISTJ'
'ISFJ'
'INFJ'
'INTJ'
'ISTP'
'ISFP'
'INFP'
'INTP'
'ESTP'
'ESFP'
'ENFP'
'ENTP'
'ESTJ'
'ESFJ'
'ENTJ'

이때, 200명의 mbti 검사결과를 random 하게 만드는 함수를 작성해보세요

출력 조건) 200명의 검사 결과는 list로 담는다
힌트) 문자열을 랜덤하게 출력하는 코드는 아래와 같습니다.
import random

hint = "ABCDEFGH"
random.choice(hint)
'''



mbti_list = ['ISTJ','ISFJ','INFJ','INTJ','ISTP','ISFP','INFP','INTP','ESTP','ESFP','ENFP','ENTP','ESTJ','ESFJ','ENTJ']
sample_list = [random.choice(mbti_list) for i in range(200)]
print("200명의 랜덤한 mbti리스트는", sample_list)




'''
3. 200명의 검사 결과가 각 16가지의 유형별 몇 명이 있는지 구하기

출력 조건) 딕셔너리 형식( {'mbti유형': 총 명수})
출력 예시) {'ESFP':17, 'INFJ': 13...}
힌트) 각각의 mbti 유형을 세는 법(counting)을 생각해보자.
'''


mbti_dic = {}
number_list = []

for i in mbti_list:
  mbti_dic[i] = sample_list.count(i)


print('각각의 mbti 유형을 세어보면, ', mbti_dic)





'''
4. mbti 유형을 딕셔너리의 key로 입력했을 경우, value로 몇 명이 해당 mbti에 속해있는지 출력하는 함수를 작성
출력 조건) 알파벳 입력시 대,소문자는 결과에 영향을 미치지 않도록 코드를 작성할 것 
'''


input_key = input('mbti 유형을 딕셔너리의 key로 입력하여보자: ').upper()
print(mbti_dic[input_key], '명이 해당 mbti에 속해있다.')







'''
 5. 1992년 멋사는 300만원을 가지고 있었다.
 친구 A는 은행에 돈을 맡겨 매년 이자로 8.5%씩 받는 것을 추천하였고,
 친구 B는 매매가 300만원인 한정판 시계를 구매하라고 추천하였다.
 2022년 기준 한정판 시계의 가격은 3500만원이 되었고, 1992년 은행에 300만원을 넣었을 경우 2022년에는 얼마가 있을지 계산하여 친구 A와 친구 B 중 누구의 말을 듣는 것이 이득이었을지 판단해보자
 
추가 조건) 상수와 변수의 정의를 이용해 작성해볼 것 
출력 예시) "? 원 차이로 친구 ?가 맞았습니다."
'''

# 재귀함수
def interest(p, r, t):
  # 년수가 1년이면 재귀하지 않고 이자만 곱해서 끝낸다
  if t == 1:
    return p * (1 + r)
  # 년수가 2년 이상이면 재귀한다. (t번 재귀하면서 이자율을 곱함)
  elif t > 1:
    return interest(p, r, t - 1) * (1 + r)

HAVE_1992 = 3000000
WATCH_2022 = 35000000
INTEREST = 0.085
interest_2022 = interest(HAVE_1992, INTEREST, 30)

result = interest_2022 - WATCH_2022
if result > 0:
  print(result,"원 차이로 친구A가 맞았습니다.")
else:
  print(-result, "원 차이로 친구B가 맞았습니다.")