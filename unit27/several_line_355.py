""" 앞에서 문자열 한 줄을 파일에 썼는데 문자열 여러 줄을 쓰면 어떻게 되는가?
    간단하게 반복문을 쓰면 된다."""


with open('hello.txt','w') as file: # hello.txt 파일을 쓰기 모드(w)로 열기
    for i in range(3):
        file.write('Hello, world! {0} \n'.format(i))


# Hello, world! 0 
# Hello, world! 1 
# Hello, world! 2 


""" 파일에 문자열 여러 줄을 저장할 때 주의할 부분은 개행 문자 부분이다. 'Hello, world!{0}\n'와 같이
    문자열 끝에 개행 문자 \n를 지정해주어야 줄바꿈이 된다. 만약 \n를 붙이지 않으면 문자열이 모두 한 줄로
    붙어서 저장되므로 주의해야 한다. """





# 리스트에 있는 문자열을 파일에 쓰기

""" 이번에는 리스트에 있는 문자열을 파일에 써 보겠다. 
        
        * 파일객체.writelines(문자열리스트)
        """


lines=['안녕하세요.\n','파이썬\n','코딩 도장입니다.\n']

with open('hello.txt','w') as file: # hello.txt 파일을 쓰기 모드(w)로 열기
    file.writelines(lines)


""" writelines는 리스트에 들어있는 문자열을 파일에 쓴다. 특히 writelines를 사용할 때는 반드시 리스트의
    각 문자열 끝에 개행 문자 \n을 붙여주어야 한다. 그렇지 않으면 붙어서 저장되므로 주의해야 한다."""



with open('hello.txt','r') as file:
    lines=file.readlines()
    print(lines)

# ['안녕하세요.\n', '파이썬\n', '코딩 도장입니다.\n']

""" 파일의 형태를 한 줄씩 리스트 형태로 가지고 왔다."""\






# 파일의 내용을 한 줄씩 읽기


""" 파일의 내용을 한 줄씩 순차적으로 읽으려면 readline을 사용한다. 

    * 변수=파일객체.readline()
"""

with open('hello.txt','r') as file:  # hello.txt 파일을 읽기 모두(r)로 열기
    line=None       # 변수 line을 None으로 초기화
    while line !='':
        line=file.readline()
        print(line.strip('\n'))     # 파일에서 읽어온 문자열에서 \n 삭제하여 출력




""" readline으로 파일을 읽을 때는 while 반복문을 사용해야 한다. 왜냐함녀 파일에 문자열이 몇 줄이나 있는지
    모르기 때문이다. while은 특정 조건이 만족할 때 계속 반복하므로 파일의 크기에 상관없이 문자열을 읽어올 수 있기 때문이다.
    
    readline은 더 이상 읽을 줄이 없을 때는 빈 문자열을 반환하는데, while에는 이런 특성을 이용하여 조건식을 만들어 준다. 즉, line!=''
    와 같이 빈 문자열이 아닐 때 계속 반복하도록 만든다. 그리고 반복문 안에서는 line=file.readline()과 같이 문자열 한 줄을 읽어서 변수 line에
    저장해 주면 된다.
    
    특히 변수 line는 while로 반복하기 전에 None으로 초기화해 준다. 만약 변수 line을 만들지 않고 while을 실행하면 없는 변수와 빈 문자열 ''을 비교하게
    되므로 에러가 발생한다. 또는, line을 만들지 않고 while을 실행하면 없는 변수와 빈 문자열 ''을 비교하게 되므로 에러가 발생한다. 또는, line을 None이 아닌
    ''으로 초기화하면 처음부터 line!=''은 거짓이 되므로 반복을 하지 않고 코드가 그냥 끝나버린다. while 문을 사용할 때에는 이 부분을 주의해야 한다.
    
    문자열을 출력할 때는 print(line.strip('\n'))와 같이 strip 메서드로 \n를 삭제했다. 왜냐하면 파일에서 읽어온 문자열은 '안녕하세요.\n'와 같이 \n이 이미 들어
    있기 때문이다. 만약 strip('\n')을 생략하면 문자열 한 줄을 출력할 때마다 빈 줄이 계속 출력이 된다. 즉, 문자열 안에 든 \n과 print가 출력하는 \n 때문에 줄바꿈이
    두 번 일어난다.
    
    """



# for 반목문으로 파일의 내용을 줄 단위로 읽기

""" while 반복문에서 readline을 사용하니 동작방식이 조금 헷갈리는데, 파이썬에서는 for 반복문으로 좀 더 간단하게 파일의 내용을 읽을 수 있다. 다음은 for 반복문에 파일
    객체를 지정하여 줄 단위로 파일의 내용을 읽는다."""


with open('hello.txt','r') as file: # hello.txt 파일을 읽기 모드(r)로 열기
    for line in file:               # for에 파일 객체를 지정하면
                                    # 파일의 내용을 한 줄씩 읽어서 변수에 저장함
        print(line.strip('\n'))     # 파일에서 읽어온 문자열에서 \n를 삭제하여 출력







# 참고: 파일 객체는 이터레이터

""" 파일의 객체는 이터레이터이다. 따라서 변수 여러 개에 저장하는 언패킹(unpacking)도 가능하다. (이터레이터는 앞에 나온다.)"""

file=open('hello.txt','r')
a,b,c=file
print(a,b,c)



""" 물론 a,b,c=file과 같이 사용하려면 hello.txt에는 문자열 3줄이 있어야 한다. 즉, 할당할 변수의 개수와 파일에 저장된 문자열의 줄 수가 일치해야 한다."""