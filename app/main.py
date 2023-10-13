import utils as miModulo
keys, values = miModulo.get_population()
print(keys, values)
data = [{
	'country': 'Colombia',
	'population': 500
},
{
	'country': 'Bolivia',
	'population': 300
}
]
def run():
  result = miModulo.population_by_country(data,'Colombia')
  print(result)
if __name__ == '__main__':
  run()