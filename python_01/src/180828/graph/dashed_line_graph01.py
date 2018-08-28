import matplotlib.pyplot as plt

#  plot()함수에 linestyle='dashed' 추가

x = [0, 1, 2, 3, 4, 5, 6]
y = [1, 4, 5, 8, 9, 5, 3]

plt.figure(figsize=(10, 6))
plt.plot(x, y, color='green', linestyle='dashed')
plt.show()
