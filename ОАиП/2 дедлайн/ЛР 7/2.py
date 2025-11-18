def build_user_profile(user_id: int, **kwargs: str) -> dict[str, str | int]:
    """Создает профиль пользователя на основе ID и дополнительной информации.
    Args:
        user_id: Уникальный идентификатор пользователя.
        **kwargs: Произвольные именованные аргументы с дополнительной информацией.
    Returns:
    dict: Словарь с профилем пользователя."""
    profile = {"user_id": user_id}
    profile.update(kwargs)
    return profile
profile = build_user_profile(101, name="Анна", status="online", email="anna@example.com")
print(profile)
