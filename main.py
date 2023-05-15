import requests

def get_data(num):

    headers = {
        'authority': 'rasp.dmami.ru',
        'accept': '*/*',
        'accept-language': 'ru,en;q=0.9',
        'referer': 'https://rasp.dmami.ru/',
        'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "YaBrowser";v="23"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 YaBrowser/23.3.3.719 Yowser/2.5 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    params = {
        'group': num,
        'session': '0',
    }

    response = requests.get('https://rasp.dmami.ru/site/group', params=params, headers=headers).json()

    sbj = response.get('grid')



    for i in range(1,7):
        day =str(i)
        if i == 1:print("Понедельник")
        elif i == 2:print("Вторник")
        elif i == 3:print("Среда")
        elif i == 4:print("Четверг")
        elif i == 5:print("Пятница")
        elif i == 6:print("Суббота")
        for i in range(1,8):
            num = str(i)
            try:
                print(num + ": " + sbj.get(day).get(num)[0].get('sbj')+" ("+sbj.get(day).get(num)[0].get('type')+'),', "Препод: "+sbj.get(day).get(num)[0].get('teacher'))
            except:
                print(num + ": " + "Пусто")
        print()

def main():
    get_data('221-375')

if __name__ == '__main__':
    main()





