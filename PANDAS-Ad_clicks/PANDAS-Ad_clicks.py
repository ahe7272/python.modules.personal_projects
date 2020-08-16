import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')
# path 값끼리 묶어서 id 갯수 세기
#print(ad_clicks.groupby('path').id.count().reset_index())

#클릭한 시간이 있는지 여부를 나타내는 부울린 값으로 click열 새로 생성
ad_clicks['click'] = ~ad_clicks.ad_click_time.isnull()

#path값에 click의 True, False값에 해당하는 id 갯수 세기
#해당 광고를 클릭하여 들어왔는지 다른 경로로 들어왔는지 확인할 수 있으며 각각의 비중을 알 수 있다.
clicks_by_source = ad_clicks.groupby(['path', 'click']).id.count().reset_index()

#위의 결과 값을 pivot을 바꾸어 보기 편한 테이블로 만들기
clicks_pivot = clicks_by_source.pivot(index='path', columns='click', values='id').reset_index()

#총 클릭 수 중에서 경로를 통해 들어온 비중을 나타내는 열 추가하기
clicks_pivot['percent_clicked'] = \
   clicks_pivot[True] / \
   (clicks_pivot[True] + 
    clicks_pivot[False])

#각 실험집단의 표본개수 확인하기
#print(ad_clicks.groupby('group').id.count().reset_index())
#각 실험집단에서 광고클릭 여부에 따라 테이블 만들기
#print(ad_clicks.groupby(['group', 'click']).id.count().reset_index().pivot(index='group', columns='click', values='id').reset_index())

#기존 테이블을 A그룹과 B그룹으로 나누기
a_clicks = ad_clicks[ad_clicks.group == 'A']
b_clicks = ad_clicks[ad_clicks.group == 'B']

#A그룹의 테이블에서 요일별로 클릭 유무에따라 개수를 세고 보기 편하도록 행을 요일 열을 클릭 여부로 만들기 
a_clicks_pivot = a_clicks.groupby(['click','day']).id.count().reset_index().pivot(index='day', columns='click', values='id').reset_index()

#위 표에서 총 클릭수 당 클릭한 비율을 열로 추가하기
a_clicks_pivot['percent_clicked'] = a_clicks_pivot[True] / (a_clicks_pivot[True] + a_clicks_pivot[False])

#A그룹과 똑같이 만들어주기
b_clicks_pivot = b_clicks.groupby(['click','day']).id.count().reset_index().pivot(index='day', columns='click', values='id').reset_index()
b_clicks_pivot['percent_clicked'] = b_clicks_pivot[True] / (b_clicks_pivot[True] + b_clicks_pivot[False])

#A그룹과 B그룹의 테이블 확인하기
print(a_clicks_pivot)
print(b_clicks_pivot)

























