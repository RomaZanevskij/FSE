import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
from collections import defaultdict

def load_users_data():
    try:
        users_tree = ET.parse('lab6/users.xml')
        users = []
        for user_elem in users_tree.getroot().findall('user'):
            user = {
            'user_id': int(user_elem.find('user_id').text),
            'name': user_elem.find('name').text,
            'age': int(user_elem.find('age').text),
            'weight': int(user_elem.find('weight').text),
            'fitness_level': user_elem.find('fitness_level').text,
            'workouts': []
            }
            users.append(user)
        return users
    except FileNotFoundError:
        print("Файл не найден")
    return []

def load_workouts_data():
    try:
        workouts_tree = ET.parse('lab6/workouts.xml')
        workouts = []
        for workout_elem in workouts_tree.getroot().findall('workout'):
            workout = {
                'workout_id': int(workout_elem.find('workout_id').text),
                'user_id': int(workout_elem.find('user_id').text),
                'date': workout_elem.find('date').text,
                'type': workout_elem.find('type').text,
                'duration': int(workout_elem.find('duration').text),
                'distance': float(workout_elem.find('distance').text),
                'calories': int(workout_elem.find('calories').text),
                'avg_heart_rate': int(workout_elem.find('avg_heart_rate').text),
                'intensity': workout_elem.find('intensity').text
            }
            workouts.append(workout)
        return workouts
    except FileNotFoundError:
        print("Файл не найден")
    return []

def get_stats(users, workouts):
    total_workouts = len(workouts)
    total_users = len(users)
    total_calories = sum(workout['calories'] for workout in workouts)
    total_time = sum(workout['duration'] for workout in workouts) / 60
    total_distance = sum(workout['distance'] for workout in workouts)

    print("ОБЩАЯ СТАТИСТИКА")
    print("="*40)
    print(f"Всего тренировок: {total_workouts}")
    print(f"Всего пользователей: {total_users}")
    print(f"Сожжено калорий: {total_calories}")
    print(f"Общее время: {round(total_time, 1)} часов")
    print(f"Пройдено дистанции: {total_distance} км")

def analyze_user_activity(users, workouts):
    user_stats = []
    for user in users:
        user_workouts = [w for w in workouts if w['user_id'] == user['user_id']]
        total_sessions = len(user_workouts)
        total_calories = sum(w['calories'] for w in user_workouts)
        total_time = sum(w['duration'] for w in user_workouts) / 60 

        user_stats.append({
            'name': user['name'],
            'fitness_level': user['fitness_level'],
            'sessions': total_sessions,
            'calories': total_calories,
            'time': round(total_time, 1)
        })

    top_users = sorted(user_stats, key=lambda u: (-u['sessions'], -u['calories']))[:3]

    print("\nТОП-3 АКТИВНЫХ ПОЛЬЗОВАТЕЛЕЙ:")
    for i, user in enumerate(top_users, 1):
        print(f"{i}. {user['name']} ({user['fitness_level']}):")
        print(f"   Тренировок: {user['sessions']}")
        print(f"   Калорий: {user['calories']}")
        print(f"   Время: {user['time']} часов")

def analyze_workout_types(workouts):
    type_stats = defaultdict(list)

    for workout in workouts:
        type_stats[workout['type']].append(workout)

    total_workouts = len(workouts)

    print("\nРАСПРЕДЕЛЕНИЕ ПО ТИПАМ ТРЕНИРОВОК:")
    for workout_type, group in sorted(type_stats.items(), key=lambda x: len(x[1]), reverse=True):
        count = len(group)
        percent = round(count / total_workouts * 100, 1)
        avg_duration = round(sum(w['duration'] for w in group) / count)
        avg_calories = round(sum(w['calories'] for w in group) / count)

        print(f"{workout_type}: {count} тренировок ({percent}%)")
        print(f"Средняя длительность: {avg_duration} мин")
        print(f"Средние калории: {avg_calories} ккал\n")

def find_user_workouts(users, workouts, user_name):
    user_ids = [user['user_id'] for user in users if user['name'].lower() == user_name.lower()]
    if not user_ids:
        print(f"Пользователь с именем '{user_name}' не найден.")
        return []

    user_id = user_ids[0]
    user_workouts = [w for w in workouts if w['user_id'] == user_id]

    return user_workouts

def analyze_user(user, workouts):
    user_workouts = [w for w in workouts if w['user_id'] == user['user_id']]
    total_sessions = len(user_workouts)
    total_calories = sum(w['calories'] for w in user_workouts)
    total_time = round(sum(w['duration'] for w in user_workouts) / 60, 1) 
    total_distance = round(sum(w['distance'] for w in user_workouts), 1)
    avg_calories = round(total_calories / total_sessions) if total_sessions else 0

    type_count = {}
    for w in user_workouts:
        type_count[w['type']] = type_count.get(w['type'], 0) + 1
    favorite_type = max(type_count, key=type_count.get) if type_count else "—"

    print(f"\nДЕТАЛЬНЫЙ АНАЛИЗ ДЛЯ ПОЛЬЗОВАТЕЛЯ: {user['name']}")
    print("=" * 40)
    print(f"Возраст: {user['age']} лет, Вес: {user['weight']} кг")
    print(f"Уровень: {user['fitness_level']}")
    print(f"Тренировок: {total_sessions}")
    print(f"Сожжено калорий: {total_calories}")
    print(f"Общее время: {total_time} часов")
    print(f"Пройдено дистанции: {total_distance} км")
    print(f"Средние калории за тренировку: {avg_calories}")
    print(f"Любимый тип тренировки: {favorite_type}")
