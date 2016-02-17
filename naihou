# coding: shift_jis

#リストの定義です
list={'yasuhiro':{'nike':5,'adidas':2,'puma':4},'takuro':{'adidas':5,'nike':4,'asics':1}}

#リスト内包です。1文で書けるので楽です。辞書型で共通するキーを引っ張ってきます
y=[x for x in list['yasuhiro'] if x in list['takuro']]
  print y

#共通しているキーの平均点をリスト型で出します
z=[(x,(list['yasuhiro'][x]+list['takuro'][x])/2.0) for x in list['yasuhiro'] if x in list['takuro']]
print z

#共通しているキーの平均点を辞書型で出します
si={}
z=dict([(x,(list['yasuhiro'][x]+list['takuro'][x])/2.0) for x in list['yasuhiro'] if x in list['takuro']])
print z
