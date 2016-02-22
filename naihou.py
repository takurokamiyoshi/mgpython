# coding: shift_jis

#内包表記について書いてみました。速くて、1文で読みやすいとのこと。オライリーの「集合知プログラミング」によく出てきます。




#リストの定義です
list={'yasuhiro':{'nike':5,'adidas':2,'puma':4},'takuro':{'adidas':5,'nike':4,'asics':1}}

si={'yasuhiro':{'nike':5,'adidas':2,'puma':4},'takuro':{'adidas':5,'nike':4,'asics':1},'tomoko':{'nike':4,'puma':5}}

def test(dic,person):
    x=[item for item in dic if item!=person]
    print x

test(si,'yasuhiro')
