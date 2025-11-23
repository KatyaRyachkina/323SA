def filter_scores(data_dict: dict[str, float | int], min_value: float | int) -> dict[str, float | int]:
    result = {}
    for key, value in data_dict.items():
        if value >= min_value:
            result[key] = value
    return result

scores = {"math": 95, "history": 78, "english": 88, "art": 92}
print(filter_scores(scores, 90))
