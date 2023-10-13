import read_csv as reader
import charts

def clean():
  data = reader.read_csv('./data.csv')
  data = list(filter(lambda x:x['Continent'] == 'South America',data))
  percentage = [x['World Population Percentage'] for x in data]
  country = [x['Country/Territory'] for x in data]
  return percentage, country

def run():
  values, labels = clean()
  charts.generate_pie_chart('South',labels,values)

if __name__ == '__main__':
 run() 