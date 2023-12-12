from extractor import collect_function_structure
from  methods import get_nested_size,get_nested_depth,check_key_presence,check_nested_structure,validate_nested_dict_integrity

input_hard = "./hard_input.py"
input_medium="./medium_input.py"
input_simple= "./simple_input.py"

def test_simple():
    expected = {
        'Pokemon': {'__init__': {'num_total_if': 0, 'max_nested_if': 0, 'num_total_for': 0, 'max_nested_for': 0},
                    'fight': {'num_total_if': 6, 'max_nested_if': 2, 'num_total_for': 5, 'max_nested_for': 1}}}
    studentAnswer = collect_function_structure(input_simple)
    print(studentAnswer)

    assert expected == studentAnswer
    assert len(expected) == len(studentAnswer)
    assert expected.items() == studentAnswer.items()
    assert  expected.keys() == studentAnswer.keys()
    assert list(expected["Pokemon"]["__init__"].values()) == list(studentAnswer["Pokemon"]["__init__"].values())
def test_medium():
    expected = {
        'Board': {'__init__': {'num_total_if': 0, 'max_nested_if': 0, 'num_total_for': 0, 'max_nested_for': 0},
                  'draw_board': {'num_total_if': 3, 'max_nested_if': 1, 'num_total_for': 2, 'max_nested_for': 2},
                  'deselect': {'num_total_if': 1, 'max_nested_if': 1, 'num_total_for': 2, 'max_nested_for': 2},
                  'redraw': {'num_total_if': 5, 'max_nested_if': 3, 'num_total_for': 3, 'max_nested_for': 2},
                  'visualSolve': {'num_total_if': 4, 'max_nested_if': 2, 'num_total_for': 2, 'max_nested_for': 1},
                  'hint': {'num_total_if': 3, 'max_nested_if': 2, 'num_total_for': 0, 'max_nested_for': 0}},
        'Tile': {'__init__': {'num_total_if': 0, 'max_nested_if': 0, 'num_total_for': 0, 'max_nested_for': 0},
                 'draw': {'num_total_if': 0, 'max_nested_if': 0, 'num_total_for': 0, 'max_nested_for': 0},
                 'display': {'num_total_if': 0, 'max_nested_if': 0, 'num_total_for': 0, 'max_nested_for': 0},
                 'clicked': {'num_total_if': 1, 'max_nested_if': 1, 'num_total_for': 0, 'max_nested_for': 0}}}
    studentAnswer = collect_function_structure(input_medium)
    # print(studentAnswer)

    ##item
    assert expected.items() == studentAnswer.items()
    assert expected["Board"].items() == studentAnswer["Board"].items()
    assert expected["Tile"]["__init__"].items() == studentAnswer["Tile"]["__init__"].items()

    # keys
    assert expected.keys() == studentAnswer.keys()
    assert expected["Board"].keys() == studentAnswer["Board"].keys()

    # sort
    assert sorted(expected) == sorted(studentAnswer)
    assert sorted(expected["Board"]) == sorted(studentAnswer["Board"])
    assert sorted(expected["Tile"]["__init__"]) == sorted(studentAnswer["Tile"]["__init__"])

    assert sorted(expected.keys()) == sorted(studentAnswer.keys())

    # length
    assert len(expected) == len(studentAnswer)
    assert len(expected["Tile"]) == len(studentAnswer["Tile"])
    assert len(expected["Board"]["__init__"]) == len(studentAnswer["Board"]["__init__"])

def test_hard():
    expected = {
        'Server': {'__init__': {'num_total_if': 0, 'max_nested_if': 0, 'num_total_for': 0, 'max_nested_for': 0},
                   'handle_client': {'num_total_if': 0, 'max_nested_if': 0, 'num_total_for': 0, 'max_nested_for': 0},
                   'broadcast': {'num_total_if': 0, 'max_nested_if': 0, 'num_total_for': 1, 'max_nested_for': 1},
                   'runServer': {'num_total_if': 2, 'max_nested_if': 1, 'num_total_for': 0, 'max_nested_for': 0},
                   'closeConnection': {'num_total_if': 0, 'max_nested_if': 0, 'num_total_for': 0, 'max_nested_for': 0}},
        'Client': {'__init__': {'num_total_if': 0, 'max_nested_if': 0, 'num_total_for': 0, 'max_nested_for': 0},
                   'connect_to_server': {'num_total_if': 1, 'max_nested_if': 1, 'num_total_for': 0, 'max_nested_for': 0},
                   'sendMsg': {'num_total_if': 1, 'max_nested_if': 1, 'num_total_for': 0, 'max_nested_for': 0},
                   'recieveMsg': {'num_total_if': 2, 'max_nested_if': 2, 'num_total_for': 0, 'max_nested_for': 0},
                   'add_lines': {'num_total_if': 1, 'max_nested_if': 1, 'num_total_for': 0, 'max_nested_for': 0},
                   'send_msg_button': {'num_total_if': 0, 'max_nested_if': 0, 'num_total_for': 0, 'max_nested_for': 0},
                   'run_gui': {'num_total_if': 0, 'max_nested_if': 0, 'num_total_for': 0, 'max_nested_for': 0},
                   'runClient': {'num_total_if': 0, 'max_nested_if': 0, 'num_total_for': 0, 'max_nested_for': 0},
                   'closeConnection': {'num_total_if': 0, 'max_nested_if': 0, 'num_total_for': 0, 'max_nested_for': 0}},
        'Start': {'main_start': {'num_total_if': 5, 'max_nested_if': 3, 'num_total_for': 1, 'max_nested_for': 1}}}
    studentAnswer = collect_function_structure(input_hard)
    # print(studentAnswer)

    # fromkey
    assert dict.fromkeys(expected["Server"]["__init__"]) == dict.fromkeys(studentAnswer["Server"]["__init__"])

    # get
    assert expected.get("Start") == studentAnswer.get("Start")

    ## To Check if any of the items in a list are True
    assert any(expected) == any(studentAnswer)

    # count
    assert (list(expected["Client"]["connect_to_server"].values())).count(2) == (list(studentAnswer["Client"]["connect_to_server"].values())).count(2)

    ##depth
    assert get_nested_depth(expected) == get_nested_depth(studentAnswer)
    assert get_nested_depth(expected["Server"]) == get_nested_depth(studentAnswer["Server"])
    assert get_nested_depth(expected["Start"]["is_simple"]) == get_nested_depth(studentAnswer["Start"]["is_simple"])

    # #size
    assert get_nested_size(expected) == get_nested_size(studentAnswer)
    assert get_nested_size(expected["Server"]["broadcast"]) == get_nested_size(studentAnswer["Server"]["broadcast"])

    ## nestedStructure
    assert check_nested_structure(expected) == check_nested_structure(studentAnswer)
    assert check_nested_structure(expected["Client"]) == check_nested_structure(studentAnswer["Client"])

    ##Data integrity
    assert validate_nested_dict_integrity(expected) == validate_nested_dict_integrity(studentAnswer)
    assert validate_nested_dict_integrity(expected["Server"]) == validate_nested_dict_integrity(studentAnswer["Server"])

    ## key Presense
    assert check_key_presence(expected, "Client") == check_key_presence(studentAnswer, "Client")
    assert check_key_presence(expected, "Start.main_start") == check_key_presence(studentAnswer, "Start.main_start")
    assert check_key_presence(expected, "Server.__init__.num_total_if") == check_key_presence(studentAnswer, "Server.__init__.num_total_if")






