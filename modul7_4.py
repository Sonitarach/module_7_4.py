# Using %
print('В команде Мастера кода участников: %(team1_num)s!' % {'team1_num':5})
print('Итого сегодня в командах участников:%(team1_num)s и %(team2_num)s!' % {'team1_num':5, 'team2_num':6})

# Using format()
print('Команда Волшебники данных решила задач: {score2}!'.format(score2 = 42))
print('Волшебники данных решили задачи за {team1_time} c'.format(team1_time = 18015.2))

# Using f-strings
score1 = 40
score2 = 42
task_total = 82
time_avg = 350.4
print(f'Команды решили {score1} и {score2} задач')
print(f'Результат битвы: победа команды Мастера кода!')
print(f'Сегодня было решено {task_total} задач, в среднем по {time_avg} секунды на задачу!')


