from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('WorldCupMatches.csv')
#홈경기와 어웨이 경기의 골 수를 합한 값으로 Total Goals의 열을 생성하기
df['Total Goals'] = df['Home Team Goals'] + df['Away Team Goals']

#어두운색의 격자배경으로 설정하기
sns.set_style('darkgrid')

#poster의 폰트크기에 0.5로 세부 설정하기
sns.set_context('poster', font_scale =.5)

#figure크기를 설정하고 x축은 년도, y축은 총 골 수를 지정하여 df의 데이터를 기반으로 barplot 생성하기
f, ax = plt.subplots(figsize=(12,7))
ax = sns.barplot(x='Year', y='Total Goals', data =df)
ax.set_title('Total goals by year')
plt.show()

df_goals = pd.read_csv('goals.csv')
#노트북 폰트크기에 1.25로 세부설정하기
sns.set_context('notebook', font_scale=1.25)
f, ax2 = plt.subplots(figsize=(12,7))
#x축은 년도, y축은 골 수로 df_goals의 데이터를 기반으로하고 색상은 Spectral 팔레트를 사용해 boxplot 생성하기
ax2 = sns.boxplot(x='year', y='goals', data=df_goals, palette='Spectral')
ax2.set_title('home game')
plt.show()