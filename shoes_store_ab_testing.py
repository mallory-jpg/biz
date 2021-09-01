import codecademylib
import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')


ad_clicks.groupby('utm_source').user_id.count().reset_index()
ad_clicks['is_click'] = ~ad_clicks.ad_click_timestamp.isnull()
print(ad_clicks.head(10))

clicks_by_source = ad_clicks.groupby(['utm_source', 'is_click']).user_id.count().reset_index()
clicks_pivot = clicks_by_source.pivot(columns='is_click', index='utm_source', values='user_id')


clicks_pivot['percent_clicked'] = clicks_pivot[True]/(clicks_pivot[True] + clicks_pivot[False])
print(clicks_pivot.head(10))

experimenters_in_group = ad_clicks.groupby('experimental_group').user_id.count().reset_index()
print(experimenters_in_group)

clicks_by_group = ad_clicks.groupby(['is_click', 'experimental_group']).user_id.count().reset_index()
print(clicks_by_group)

a_clicks = ad_clicks[ad_clicks.experimental_group == 'A']
a_by_day = a_clicks.groupby(['day', 'is_click']).user_id.count().reset_index()
pivot_a_by_day = a_by_day.pivot(columns='is_click', index='day', values='user_id')
pivot_a_by_day['percent_by_day'] = pivot_a_by_day[True]/(pivot_a_by_day[True] + pivot_a_by_day[False])
print(pivot_a_by_day)

b_clicks = ad_clicks[ad_clicks.experimental_group == 'B']
b_by_day = b_clicks.groupby(['day', 'is_click']).user_id.count().reset_index()
pivot_b_by_day = b_by_day.pivot(columns='is_click', index='day', values='user_id')
pivot_b_by_day['percent_by_day'] = pivot_b_by_day[True]/(pivot_b_by_day[True] + pivot_b_by_day[False])
print(pivot_b_by_day)



