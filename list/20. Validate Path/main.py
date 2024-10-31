def validate_path(expected_path, character_path):
    missing_paths = []

    for exp in expected_path:
        if exp not in character_path[1::]:
            missing_paths.append(exp)

    matches = 100 - (len(missing_paths) / len(expected_path)) * 100

    return character_path[0], matches
