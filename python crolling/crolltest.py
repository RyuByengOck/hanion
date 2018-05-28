"""
파이썬으로 크롤링 하기 준비 
환경 : visual studio code
교제 : 파이썬으로 배우는 웹 크롤러, 파이써으로 웹크롤러 만들기
"""
################ 오픈url테스트 #############################################################################################################
"""
from urllib.request import urlopen # urllib라이브러리에서 파이썬 모듈 requst를 읽어 open함수 하나만 임포트
html=urlopen("https://search.naver.com/search.naver?where=nexearch&query=%EC%B9%B4%EB%A6%AC%EC%9A%B0%EC%8A%A4&sm=top_lve&ie=utf8")
#오픈하려는 주소 (나중에 api 주소 입력과 변수설정 추가해서 사용할듯)
print(html.read()) #데이터 읽어드림 (파싱하기 전에 출력 확인)
"""
################## 오픈url 테스 끝#############################################################################################################
"""
beautifulsoup 가 bs4 임 (라이브러리)
크롤링 파싱할떄 쓰는거임 (파싱모듈)

설치법 (윈도우에서) : http://wwww.crummy.com/software/BeautifulSoup/bs4/doc/ 
                   에 들어가서 최신 bs4다운받고 cmd에서 cd로 디렉터리 이동후  >python setup.py install 하면 끝 
                
                 bs가 내장이라고 설치안해도 된다하는데 ModuleNotFoundError: No module named 'bs4' 이라뜸 설치해야함

                 easy_install 이랑 pip는 파이썬 3부터 깔려잇어서 안깔아도됨

    **윈도우에서 설치시 ->(참고 :https://blog.naver.com/panda220/221178698558)

    cmd 에서 내 파이선 깔려잇는 디렉토리로 이동 C:/Users/LG gram/AppData/Local/Programs/Python/Python36 (신상윤 컴터)
    -> 환경변수 path 에 C:/Users/LG gram/AppData/Local/Programs/Python/Python36/Scripts 와 위에꺼 둘다 등록 먼저해야함  <- \ 로 입력하면 에러떠서 /로 해둠...
     pip 설치안되잇으면 설치할것. (사진첨부)
     virtualenv로 충돌 방지


"""
########### bs 간단 테스트 #################################################################################################
'''
from urllib.request import urlopen # urllib라이브러리에서 파이썬 모듈 requst를 읽어 open함수 하나만 임포트
from bs4 import BeautifulSoup
html = urlopen("https://search.naver.com/search.naver?where=nexearch&query=%EC%B9%B4%EB%A6%AC%EC%9A%B0%EC%8A%A4&sm=top_lve&ie=utf8")
#오픈하려는 주소 (나중에 api 주소 입력과 변수설정 추가해서 사용할듯)
bsObj = BeautifulSoup(html.read(),"html.parser")
print(bsObj.h1) #h1만 걸러서 프린트해주는듯 위에 bs4에서 html로 이쁘게 정리해서
'''
########bs 간단 테스트 완료 #############################################################

########### api 간단 테스트 #################################################################################################
"""
from urllib.request import urlopen # urllib라이브러리에서 파이썬 모듈 requst를 읽어 open함수 하나만 임포트
from bs4 import BeautifulSoup
html = urlopen("http://data.suwon.go.kr/suwon/openapi/service/getDataList.api?serviceId=weatherAreainfo&apiType=json&serviceKey=8e7c858a1cdd4423838f607d3111266e180528224912")
#api 수원시청 내 인증키 넣은거 
bsObj = BeautifulSoup(html.read(),"html.parser")
print(bsObj) #test ㅜㅜ
"""
########  api 간단 테스트 완료 #############################################################

########### api 간단 테스트 lxml #################################################################################################

from urllib.request import urlopen # urllib라이브러리에서 파이썬 모듈 requst를 읽어 open함수 하나만 임포트
from bs4 import BeautifulSoup
html = urlopen("http://data.suwon.go.kr/suwon/openapi/service/getDataList.api?serviceId=weatherAreainfo&apiType=json&serviceKey=8e7c858a1cdd4423838f607d3111266e180528224912")
#api 수원시청 내 인증키 넣은거 
bsObj = BeautifulSoup(html.read(),"lxml")
print(bsObj) #test ㅜㅜ

########  api 간단 테스트 완료 #############################################################
