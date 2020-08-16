from matplotlib import pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
visits_per_month = [9695, 7909, 10831, 12942, 12495, 16794, 14161, 12762, 12777, 12439, 10309, 8724]

#라임의 종류별로 매달 판매된 갯수
key_limes_per_month = [92.0, 109.0, 124.0, 70.0, 101.0, 79.0, 106.0, 101.0, 103.0, 90.0, 102.0, 106.0]
persian_limes_per_month = [67.0, 51.0, 57.0, 54.0, 83.0, 90.0, 52.0, 63.0, 51.0, 44.0, 64.0, 78.0]
blood_limes_per_month = [75.0, 75.0, 76.0, 71.0, 74.0, 77.0, 69.0, 80.0, 63.0, 69.0, 73.0, 82.0]

#plot을 할 figure 크기 설정하기
plt.figure(figsize =(12,8))

#1행 2열의 subplot중 첫번째 subplot을 ax1으로 지정
ax1 = plt.subplot(1,2,1)

#x값은 총 달의 갯수의 범위로 12개 지정하기
x_values = range(len(months))

#x값은 0부터 11까지, y값은 각 달마다 방문한 방문자수를 주어 점으로 값을 나타내는 라인 그래프 plot하기
plt.plot(x_values, visits_per_month, marker = 'o')

#각 x축과 y축에 Months와 Visits의 이름 붙이기
plt.xlabel('Months')
plt.ylabel('Visits')

#해당 plot에 x값은 x_value를 주고 각 값의 Lable은 months 리스트의 값 주기
ax1.set_xticks(x_values)
ax1.set_xticklabels(months)
#해당 plot에 Visitors per months로 제목 붙이기 
plt.title('Visitors per months')

#1행 2열의 subplot 중 두번째 subplot을 ax2로 지정
ax2 = plt.subplot(1,2,2)

#x값은 달의 갯수만큼, y값은 key_lime의 판매갯수로 주고 빨간색 선으로 라인 그래프 plot하기
plt.plot(x_values, key_limes_per_month, color='red')
#x값은 달의 갯수만큼, y값은 persian_lime의 판매갯수로 주고 초록색 선으로 라인 그래프 plot하기
plt.plot(x_values, persian_limes_per_month, color='green')
#x값은 달의 갯수만큼, y값은 blood_lime의 판매갯수로 주고 파란색 선으로 라인 그래프 plot하기
plt.plot(x_values, blood_limes_per_month, color='blue')

#각 라인에 맞게 Key, Persian, Blood로 범례 지정하기
plt.legend(['Key','Persian','Blood'])

#해당 plot에 x값은 x_value를 주고 각 값의 Lable은 months 리스트의 값 주기
ax2.set_xticks(x_values)
ax2.set_xticklabels(months)

#해당 plot에 Sold per lime species로 제목 붙이기 
plt.title('Sold per lime species')

#Subplot간에 간격을 0.6으로 주기
plt.subplots_adjust(wspace=0.6)
plt.show()
plt.savefig('sold_limes.png')











