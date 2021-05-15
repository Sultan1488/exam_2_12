def func(name, **kwargs):
    print(name)
    for keys in kwargs:
        print(f'{keys} - {kwargs[keys]}')

func(name='USA', population = '330 million', is_democratic = True)
func(name='Kyrgyzstan', area='200 km2', 
	have_borders_with=['Kazakhstan', 'Uzbekistan', 'Tajikistan', 'China'])
