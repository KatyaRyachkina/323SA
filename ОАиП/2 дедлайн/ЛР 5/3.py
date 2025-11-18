colors = {
    "красный": (255, 0, 0),
    "зеленый": (0, 255, 0),
    "синий": (0, 0, 255),
    "белый": (255, 255, 255),
    "черный": (0, 0, 0),
    "желтый": (255, 255, 0),
    "фиолетовый": (128, 0, 128)
}
def mix_colors(color1, color2):
"""Смешивает два цвета путем усреднения их компонентов"""
    r = (color1[0] + color2[0]) // 2
    g = (color1[1] + color2[1]) // 2
    b = (color1[2] + color2[2]) // 2
    return (r, g, b)
def invert_color(color):
    """Инвертирует цвет (255 - каждое значение)"""
    return (255 - color[0], 255 - color[1], 255 - color[2])
print("Исходные цвета:")
for name, rgb in colors.items():
    print(f"{name}: {rgb}")
mixed = mix_colors(colors["красный"], colors["синий"])
print(f"\nСмешанный цвет (красный + синий): {mixed}")
inverted_white = invert_color(colors["белый"])
print(f"Инвертированный белый цвет: {inverted_white}")
