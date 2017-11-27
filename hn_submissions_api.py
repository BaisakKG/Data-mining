import requests

from operator import itemgetter

# Создание вызова API и сохранение ответа
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print('Satus code: ', r.status_code)

# Обработка информации о каждой статье
sm_ids = r.json()
sm_dicts = []
for sm_id in sm_ids[:30]:
  # Создание отдельного вызова АПИ для каждой статьи
  url = ('https://hacker-news.firebaseio.com/v0/item/' +str(sm_id) + '.json')
  sm_r = requests.get(url)
  print(sm_r.status_code)
  response_dict = sm_r.json()
  sm_dict = {
    'title': response_dict['title'],
    'link': 'http://news.ycombinator.com/item?id=' + str(sm_id),
    'comments': response_dict.get('descendants', 0)
  }
  sm_dicts.append(sm_dict)

sm_dicts = sorted(sm_dicts, key=itemgetter('comments'), reverse=True)

for submission_dict in sm_dicts:
  print("\nTitle:", submission_dict['title'])
  print("Discussion link:", submission_dict['link'])
  print("Comments:", submission_dict['comments'])