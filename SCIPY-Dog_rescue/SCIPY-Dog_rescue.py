import numpy as np
import pandas as pd
from scipy.stats import binom_test, f_oneway, chi2_contingency

dogs = pd.read_csv("dog_data.csv")

def get_attribute(breed, attribute):
  if breed in dogs.breed.unique():
    if attribute in dogs.columns:
      return dogs[dogs["breed"] == breed][attribute]
    else:
      raise NameError('Attribute {} does not exist.'.format(attribute))
  else:
    raise NameError('Breed {} does not exist.'.format(breed))
  
def get_weight(breed):
  return get_attribute(breed, 'weight')
  
def get_tail_length(breed):
  return get_attribute(breed, 'tail_length')

def get_color(breed):
  return get_attribute(breed, 'color')

def get_age(breed):
  return get_attribute(breed, 'age')

def get_is_rescue(breed):
  return get_attribute(breed, 'is_rescue')

def get_likes_children(breed):
  return get_attribute(breed, 'likes_children')

def get_is_hypoallergenic(breed):
  return get_attribute(breed, "is_hypoallergenic")

def get_name(breed):
  return get_attribute(breed, "name")

#롯트웨일러 종의 꼬리길이 구하기
rottweiler_tl = get_tail_length('rottweiler')

#위펫의 분양여부 구하기
whippet_rescue = get_is_rescue('whippet')

#위펫의 분양횟수 구하기
num_whippet_rescues = np.count_nonzero(whippet_rescue)
num_whippets = np.size(whippet_rescue)

#위펫의 분양횟수가 8%가 되는지 유의확률 구하기 
pval = binom_test(num_whippet_rescues, n=num_whippets, p=0.08)
print(pval)

#위펫, 테리어, 핏불의 평균 몸무게에 유의미한 차이가 있는지 확인하기
tstat, pval1 = f_oneway(get_weight('whippet'),get_weight('terrier'), get_weight('pitbull'))
print( pval1)

#[푸들, 시츄]순으로 Black, Brown, Gold, Grey, White색을 가지는 종류 수 리스트 만들기
poodle_colors = get_color('poodle')
shihtzu_colors = get_color('shihtzu')
color_table = [[17,10],[13, 36],[8, 6],[52,41],[10,7]]

#각 색깔별로 유의미한 차이가 있는지 확인하기 
pval = chi2_contingency(color_table)
print(pval)
