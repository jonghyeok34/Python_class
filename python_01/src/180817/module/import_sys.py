# 파이썬 모듈 파일을 찾는 순서
# 1. 파이썬 인터프리터 내장 모듈
# 2. sys.path에 정의 되어 있는 디렉토리 안에 있는 모듈

import sys

# 1. 파이썬 인터프리터 내장 모듈
print(sys.builtin_module_names)

# 2. sys.path에 정의 되어 있는 디렉토리 안에 있는 모듈
for path in sys.path:
    print(path)

