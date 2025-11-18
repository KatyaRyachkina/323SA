students = [
    ("Анна", 21, 4.5),
    ("Петр", 22, 4.2),
    ("Екатерина", 19, 4.8),
    ("Дарья", 20, 4.1),
    ("Азалия", 23, 4.6)
]
print("Студенты старше 20 лет:")
for name, age, avg_score in students:
    if age > 20:
        print(f"- {name} ({age}), средний балл: {avg_score}")
best_student = max(students, key=lambda x: x[2])
print(f"\nЛучший студент: {best_student[0]}, средний балл: {best_student[2]}")
sorted_students = sorted(students, key=lambda x: x[0])
print("\nОтсортированный список студентов:")
for name, age, avg_score in sorted_students:
    print(f"- {name} ({age}), средний балл: {avg_score}")
