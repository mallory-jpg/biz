import codecademylib
import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])

#print(visits.head(10))
#print(cart.head(10))
#print(checkout.head(10))
#print(purchase.head(10))

visits_cart = pd.merge(visits, cart, how='left')
#print(len(visits_cart))

null_cart_time = visits_cart[visits_cart.cart_time.isnull()]

percent_null_cart_time = null_cart_time.count() / float(len(visits_cart))

print(percent_null_cart_time)

cart_checkout = pd.merge(cart, checkout, how='left')
cart_checkout_rows = len(cart_checkout)
null_checkout = len(cart_checkout[cart_checkout.checkout_time.isnull()])

print(float(null_checkout) / cart_checkout_rows)

all_data = visits.merge(cart, how='left').merge(checkout, how='left').merge(purchase, how='left')
#print(all_data.head(10))

checkout_purchase = pd.merge(checkout, purchase, how='left')
checkout_purchase_rows = len(checkout_purchase)

null_purchase = len(checkout_purchase[checkout_purchase.purchase_time.isnull()])

checkout_null_purchase = null_purchase / checkout_purchase_rows
print(float(checkout_null_purchase))

all_data['time_to_purchase'] = \
    all_data.purchase_time - \
    all_data.visit_time
print(all_data.time_to_purchase)
print(all_data.time_to_purchase.mean())
