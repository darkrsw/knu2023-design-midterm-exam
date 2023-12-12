from extractor import collect_function_structure

test_input_path = "./newinput.py"
def get_nested_depth(collect_function_structure, current_depth=0):
    if not isinstance(collect_function_structure, dict):
        return current_depth
    if not collect_function_structure:
        return current_depth + 1

    return max(get_nested_depth(value, current_depth + 1) for value in collect_function_structure.values())


def get_nested_size(collect_function_structure):
    size = len(collect_function_structure)
    for value in collect_function_structure.values():
        if isinstance(value, dict):
            size += get_nested_size(value)
    return size


def check_nested_structure(collect_function_structure):
    if not isinstance(collect_function_structure, dict):
        return False

    keys = list(collect_function_structure.keys())
    for key in keys:
        if not isinstance(collect_function_structure[key], dict):
            continue  # Non-dictionary value encountered, moving to the next key
        if not check_nested_structure(collect_function_structure[key]):
            return False  # Nested structure is invalid
    return True


def validate_nested_dict_integrity(collect_function_structure):
    if not isinstance(collect_function_structure, dict):
        return False

    for key, value in collect_function_structure.items():
        if isinstance(value, dict):
            if not validate_nested_dict_integrity(value):
                return False
        elif not isinstance(value, (int, float, str)):
            return False

    return True

def check_key_presence(collect_function_structure, key_path):
    keys = key_path.split('.')
    current = collect_function_structure
    for key in keys:
        if key not in current:
            return False
        current = current[key]
    return True