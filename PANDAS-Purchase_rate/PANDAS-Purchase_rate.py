import pandas as pd

visits = pd.read_csv('visits.csv', parse_dates=[1])
cart = pd.read_csv('cart.csv', parse_dates=[1])
checkout = pd.read_csv('checkout.csv', parse_dates=[1])
purchase = pd.read_csv('purchase.csv', parse_dates=[1])

#방문한 user를 기준으로 장바구니에 물건을 담은 시간을 왼쪽 정렬을 해 테이블 만들기
visit_to_cart = visits.merge(cart, how='left')

#방문했지만 장바구니에 물건을 담지 않은 user 확인하기
no_purchase_v_c= visit_to_cart[visit_to_cart.cart_time.isnull()]

#방문했지만 장바구니에 물건을 담지 않은 user 비율 확인하기
rate_no_purchase_v_c = float(len(no_purchase_v_c))/len(visit_to_cart)

#방문해 장바구니에 담고 결제를 클릭한 시간을 기준으로 왼쪽 정렬 해 테이블 만들기
cart_to_checkout = cart.merge(checkout, how='left')

#장바구니에 담았지만 결제를 클릭하지 않은 user 확인하기
no_purchase_c_ch= cart_to_checkout[cart_to_checkout.checkout_time.isnull()]
#장바구니에 담았지만 결제를 클릭하지 않은 user 비율 확인하기
purchase_c_ch = float(len(no_purchase_c_ch))/len(cart_to_checkout)

#결제단계에서 구매를 한 시간으로 왼쪽 정렬해 테이블 만들기
checkout_to_purchase = checkout.merge(purchase, how='left')
#결제단계에서 결제를 하지 않은 user 확인하기
no_purchase_ch_p= checkout_to_purchase[checkout_to_purchase.purchase_time.isnull()]
#결제단계에서 결제를 하지 않은 user 비율 확인하기
purchase_ch_p = float(len(no_purchase_ch_p))/len(checkout_to_purchase)

#위의 단계들을 한꺼번에 만들기
all_data = visits.merge(cart, how='left').merge(checkout, how='left').merge(purchase, how='left')

#방문하고부터 구매를 완료하기까지 걸린 시간을 새 열로 추가하기
all_data['time_to_purchase'] = all_data.purchase_time - all_data.visit_time

#평균 구매시간 확인하기
print(all_data['time_to_purchase'].mean())
