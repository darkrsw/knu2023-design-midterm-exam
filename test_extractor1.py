from extractor import collect_function_structure

test_input_path = "./newinput.py"

def test_app_analyzer():
    expected = {"MyClassA":
                 {
                   "func1": {"num_total_if": 5, "max_nested_if": 5, "num_total_for": 0, "max_nested_for": 0},
                   "func2": {"num_total_if": 1, "max_nested_if": 1, "num_total_for": 2, "max_nested_for": 2}
                 },
                "MyClassB":
                 {
                   "func1": {"num_total_if": 2, "max_nested_if": 1, "num_total_for": 2, "max_nested_for": 2}
                 }
               }

    assert expected == collect_function_structure(test_input_path)


def another_function():
    pass
