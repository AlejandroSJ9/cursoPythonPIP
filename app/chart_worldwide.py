import read_csv as reader
import charts
import pandas as pd
def clean():
  '''
  data = reader.read_csv('./data.csv')
  data = list(filter(lambda x:x['Continent'] == 'South America',data))
  percentage = [x['World Population Percentage'] for x in data]
  country = [x['Country/Territory'] for x in data]
  '''
  df = pd.read_csv('data.csv')
  df = df[df['Continent']=='South America']
  country = df['Country/Territory'].values
  percentage = df['World Population Percentage'].values
  return percentage, country

def run():
  values, labels = clean()
  charts.generate_pie_chart('South',labels,values)

if __name__ == '__main__':
 run() 