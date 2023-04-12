import requests
import json


def getVacancie(page=0):
    '''Получаем вакансии с API'''
    params = {
        'text': 'NAME:Python',
        'area': 66,
        'page': page,
        'per_page': 1
    }
    request = requests.get('https://api.hh.ru/vacancies', params)
    print(request)
    data = request.content.decode()
    request.close()
    return data


def parse():
    '''Записываем вакансии в файл'''
    data = getVacancie()
    fileName = 'data/vacancies.json'
    with open(fileName, mode='w', encoding='utf8') as f:
        f.write(data)
        f.close()


def checkVacancie():
    pass


def printVacancie():
    '''Читаем файл и возвращаем нужные данные'''
    with open('data/vacancies.json') as f:
        data = json.load(f)
        name = data['items'][0]['name']
        city = data['items'][0]['area']['name']
        salary_from = data['items'][0]['salary']['from']
        salary_to = data['items'][0]['salary']['to']
        salary = f' от {salary_from} до {salary_to}'
        url = data['items'][0]['alternate_url']
        exData = (name, city, salary, url)
        return exData


parse()
