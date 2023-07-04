# 딕셔너리 안에서 딕셔너리 사용하기

""" 다음과 같이 딕셔너리는 값 부분에 다시 딕셔너리가 계속 들어갈 수 있다.


    * 딕셔너리 ={키1:{키A:값A}, 키2:{키B:값B}}
"""


terrestrial_planet={
    'Mercury':{
        'mean_radius':2439.7,
        'mass':3.3022E+23,
        'orbital_period':87.969
    }, 
    'Venus':{
        'mean_radius':6051.8,
        'mass':4.8676E+24,
        'orbital_period':224.70069
    }, 
    'Earth':{
        'mean_radius':6371,
        'mass':5.97219E+24,
        'orbital_period':365.25641
    }, 
    'Mercury':{
        'mean_radius':3389.5,
        'mass':6.4185E+23,
        'orbital_period':686.9600
    },
}

print(terrestrial_planet['Venus']['mean_radius']) # 6051.8



"""딕셔너리 terrestrial_planet에 키 'Mercury','Venus','Earth','Mars'가 들어있고, 이 키들은 다시 값 부분에 딕셔너리를 가지고 있다.
즉, 중첩 딕셔너리는 계층형 데이터를 저장할 때 유용하다.'"""


""" 딕셔너리 안에 들어있는 딕셔너리에 접근하려면 뒤에 [](대괄호)를 단계만큼 붙이고
    키를 지정해주면 된다.
    
    *딕셔너리[키][키]
    *딕셔너리[키][키]=값
    
    """