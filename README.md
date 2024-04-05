dependency-injector 패키지를 사용해서 의존성 주입
service에서 repository를 의존성 주입함

# poetry로 가상환경 만들고 패키지 설치
```
brew install python@3.9
brew info python@3.9
poetry env use /opt/homebrew/bin/python3.9

#set interpreter
/Users/xxx/Library/Caches/pypoetry/virtualenvs/flask-dependency-injection-example-D5rM-1hU-py3.9

poetry install
```

# 명령어 실행
flask station update  
# 환경변수 적용
sample.env 참고해서 .env 생성  
환경변수 수정해도 반영 안될 때 새 터미널에서 실행하기  
