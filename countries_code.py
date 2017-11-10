# pip install pygal_maps_world
from pygal.maps.world import COUNTRIES

def get_country_code(country_name):
  "Возвращает для заланной страны ее код Pygal, состоящий из 2 букв"
  for code, name in COUNTRIES.items():
    if name == country_name:
      return code
  
  # Если страна не найдена, вернуть Ноне
  return None

# print(get_country_code('Kyrgyzstan'))
# print(get_country_code('Afghanistan'))