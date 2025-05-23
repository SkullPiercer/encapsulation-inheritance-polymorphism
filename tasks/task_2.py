# Реализуй класс GradeBook (электронный дневник), который хранит оценки студентов по пятибалльной шкале.
# Требования:

# Добавление оценок:
# Метод add_grade(student_name: str, grade: int) добавляет оценку студенту.
# Оценка должна быть целым числом от 1 до 5.
# Если указана неправильная оценка (например, 0, 6, -1), метод должен выбросить ValueError.

# Просмотр средней оценки одного студента:
# Метод get_average(student_name: str) -> float возвращает среднюю оценку для указанного студента.
# Если у студента пока нет оценок, возвращается 0.0.

# Просмотр всех средних оценок:
# Метод get_all_averages() -> dict[str, float] возвращает словарь, где ключ — имя студента, а значение — его средняя оценка.
# Внутреннее хранилище оценок (словарь) должно быть приватным (self.__grades), чтобы не допустить прямого изменения извне.

class GradeBook:
    pass
