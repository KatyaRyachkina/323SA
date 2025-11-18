def is_anagram(str1: str, str2: str) -> bool:
 """Проверяет, являются ли две строки анаграммами (игнорируя регистр и пробелы).
    Args:
        str1: Первая строка для сравнения
        str2: Вторая строка для сравнения
    Returns:
        bool: True если строки являются анаграммами, иначе False"""

    clean_str1 = ''.join(str1.lower().split())
    clean_str2 = ''.join(str2.lower().split())
    
    return sorted(clean_str1) == sorted(clean_str2)
print(is_anagram("Каприз силача", "Приказ числа А")) 
print(is_anagram("Listen", "Silent"))    
print(is_anagram("Hello", "World"))       
