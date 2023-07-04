# 구분자 문자열과 문자열 리스트 연결하기


""" join(리스트)는 구분자 문자열과 문자열 리스트의 요소를 연결하여 문자열로 만든다. 다음은 공백 ' '에 join을 사용하여 각 문자열 사이에 공백이
들어가도록 한다."""


print(' '.join(['apple','pear','grape','pineapple','orange']))

# apple pear grape pineapple orange

"""마이너스 '-'에 join을 사용하면 각 문자열 사이에 마이너스가 들어간다."""

print('-'.join(['apple','pear','pineapple','orange']))

# apple-pear-pineapple-orange