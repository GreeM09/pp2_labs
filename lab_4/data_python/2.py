from datetime import datetime as dt

time_now = dt.now()
print(f'yesterday: {time_now.day - 1}th {time_now.strftime("%B")}'
      f'\ntoday: {time_now.day}th {time_now.strftime("%B")}'
      f'\ntommorow: {time_now.day + 1}th {time_now.strftime("%B")}')
