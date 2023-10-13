import read_csv as file
import charts

def data_country(country):
  data = file.read_csv('./data.csv')
  return list(filter(lambda x: x['Country/Territory'].capitalize() == country.capitalize(), data))

def clean(country_dict):
  dict = country_dict[0]
  population_dict = {
    '2022': int(dict['2022 Population']),
    '2020': int(dict['2020 Population']),
    '2015': int(dict['2015 Population']),
    '2010': int(dict['2010 Population']),
    '2000': int(dict['2000 Population']),
    '1990': int(dict['1990 Population']),
    '1980': int(dict['1980 Population']),
    '1970': int(dict['1970 Population'])
  }
  labels = list(population_dict.keys())
  values = list(population_dict.values())
  return labels, values
def run():
  country = input('ingresa el pais => ')
  labels, values = clean(data_country(country))
  charts.generate_bar_chart(country,labels,values)
if __name__ == '__main__':
   run()
