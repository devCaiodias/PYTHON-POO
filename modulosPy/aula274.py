# Criando datas com módulo datetime
# datetime(ano, mês, dia)
# datetime(ano, mês, dia, horas, minutos, segundos)
# datetime.strptime('DATA', 'FORMATO')
# datetime.now()
# https://pt.wikipedia.org/wiki/Era_Unix
# datetime.fromtimestamp(Unix Timestamp)
# https://docs.python.org/3/library/datetime.html
# Para timezones
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# Instalando o pytz
# pip install pytz types-pytz

from datetime import datetime
# from pytz import timezone

# data = datetime(2024,4,7, 20, 17, 23)

# print('Data Python')
# data_str_data = '2024/04/07 20:17:23'
# data_str_fmt = '%Y/%m/%d %H:%M:%S'
# data_s = datetime.strptime(data_str_data, data_str_fmt)
# print(data_s)


# print()
# print('Data BR')
# data_str_data_br = '20/04/2022'
# data_str_fmt_br = '%d/%m/%Y'
# data_s_br = datetime.strptime(data_str_data_br, data_str_fmt_br)
# print(data_s_br)

# data = datetime.now(timezone('Asia/Tokyo'))
# data = datetime(2024,4,7, 20, 17, 23, tzinfo=timezone('Asia/Tokyo'))


data = datetime.now()
print(data.timestamp()) # Isso  está na base de dados
print(datetime.fromtimestamp(1712534815))