mobile_data = {
    'status': True,
    'data': [
        {'name': 'Xiaomi Note 5', 'price': '300 USD', 'made': 'China'},
        {'name': 'Samsung Note 6', 'price': '200 USD', 'made': 'USA'},
        {'name': 'Iphone 5', 'price': '180.5 USD', 'made': 'Japan'},
        {'name': 'Pixel 5', 'price': '89.60 USD', 'made': 'Rusia'},
        {'name': 'Techno 5', 'price': '110 USD', 'made': 'Uk'},
        {'name': 'Huawei 5', 'price': '350 USD', 'made': 'Malaysia'},
    ],
    'exchnage_rate': 103.25
}


#  Your Code Starts from here

mobiles = mobile_data.get('data')
exchnage_rage = float(mobile_data.get('exchnage_rate'))
for mobile in mobiles : 
    Brand_name = mobile.get('name')
    price = mobile.get('price')
    broke = float(price.split(' ')[0])
    bd_price = round(broke * exchnage_rage, 2)
    made_in = mobile.get('made')
    sentence = f'{Brand_name} : {Brand_name} is made in {made_in}. The price of {Brand_name} is {price} which is almost equal to {bd_price} BDT'
    print(sentence)