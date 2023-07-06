# 파이썬 객체를 파일에 저장하기, 가져오기

""" 파이썬은 객체를 파일에 저장하는 pickle 모듈을 제공한다.

다음과 같이 파이썬 객체를 저장하는 과정을 피클리(pickling)이라고 하고, 파일에서 객체를 읽어오는 과정을 언피클링(unpickling)이라고 한다."""



import pickle as p

name='james'
age=17
address='서울시 서초동 반포동'
scores={'korean':90,'english':95,'mathematics':85,'science':82}


with open('james.p','wb') as file:
    p.dump(name,file)
    p.dump(age,file)
    p.dump(address,file)
    p.dump(scores,file)




with open('james.p','rb')as file:
    name=p.load(file)
    age=p.load(file)
    address=p.load(file)
    scores=p.load(file)
    print(name)
    print(age)
    print(address)
    print(scores)




# 참고 모드

""" 파일을 열 때는 용도에 따라 다양한 파일 모드를 지정해야 한다."""



""" 'r' : 읽기 전용             : 파일을 읽기 전용으로 열기, 단, 파일이 반드시 있어야 하며 파일이 없음녀 에러 발생
    'w' : 쓰기 전용             : 쓰기 전용으로 새 파일을 생성. 만약 파일이 있다면 내용을 덮어씀
    'a' : 추가                  : 파일을 열어 파일 끝에 값을 이어씀. 만약 파일이 없으면 파일을 생성
    'x' : 배타적 생성(쓰기)     : 파일을 쓰기 모드로 생성. 파일이 이미 있으면 에러 발생
    'r+': 읽기/쓰기             : 파일을 읽기/쓰기용으로 열기. 단, 파일이 있어야 하며 파일이 없으면 에러 발생
    'w+': 읽기/쓰기             : 파일을 읽기/쓰기용으로 열기. 파일이 없으면 파일을 생성하고, 파일이 있으면 내용을 덮어씀
    'a+': 추가(읽기/쓰기)       : 파일을 열어 파일 끝에 값을 이어 씀. 만약 파일이 없으면 파일을 생성. 읽기는 파일의 모든 구간에서 가능하지만,
                                쓰기는 파일의 끝에서만 가능함
    'x+': 배타적 생성(읽기/쓰기) : 파일을 읽기/쓰기 모드로 생성. 파일이 이미 있으면 에러 발생
    't' : 텍스트 모드            : 파일을 읽거나 쓸 때 개행 문자 \n과 \r\n을 서로 변환 t를 생략하면 텍스트 모드
    'b' : 바이너리 모드          : 파일의 내용을 그대로 읽고, 값을 그대로 씀 
    """