# x축, y축에 한글 라벨 설정

from matplotlib import font_manager, rc
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 2, 3, 4, 5]

# 한글 라벨 설정을 위한 추가

# 한글 라벨 설정을 위해 추가 -----------------------------------------------------
font_location = "c:/Windows/fonts/malgun.ttf"  # 맑은 고딕체
font_name = font_manager.FontProperties(fname=font_location).get_name()
plt.rc('font', family=font_name)
# ------------------------------------------------------------------------------------

plt.xlabel('x축')  # x축 라벨 (한글 라벨)
plt.ylabel('y축')  # y축 라벨
plt.plot(x, y)
plt.show()
