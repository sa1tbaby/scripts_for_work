import time
from requests import Session

try:
    result_query = []

    with Session() as session:
        session.auth = (input('дай дай логин: '), input('пароль дай: '))

        print('relative or absolute ')
        choice = input('введи r или a: ')

        print('\n*Примечание точные параметры для ввода лучше брать '
              'из инструментов разработчика в браузере после тестов\n')
        match choice:


            case 'r':
                req = session.get(
                    url='http://grlog-prod.esphere.local/api/search/universal/relative',
                    params={'query': '"document missing" AND facility:courier.search.indexer',
                            'interval': 'hour',
                            'range': input('range: ')}
                )

            case 'a':
                req = session.get(
                    url='http://grlog-prod.esphere.local/api/search/universal/relative',
                    params={'query': '"document missing" AND facility:courier.search.indexer',
                            'from': input('from: '),
                            'to': input('to: '),
                            'limit': '150',
                            'sort': 'timestamp:desc'}
                )

        for index, value in enumerate(req.json()['messages']):
            print(value)
            tmp = value['message']
            tmp = tmp['message']
            tmp = tmp[tmp.find('][') + 2:tmp.rfind(']:')]
            if tmp.find('_Out') != -1:
                tmp = tmp.replace('_Out', '')
            if tmp.find('_In') != -1:
                tmp = tmp.replace('_In', '')
            if int(tmp[0]) > 3 and tmp not in result_query:
                result_query.append(tmp)

        print('\n', result_query)

    with Session() as session:
        ans = session.post(
            url='https://courier.esphere.ru/auth/UI/Login?realm=lkk_sfera&goto=https%3A%2F%2Fcourier.esphere.ru%3A443%2F',
            data={'IDToken1': input('\nтеперь еще раз логин, но для курьера: '),
                  'IDToken2': input('пароль дай: ')}
        )
