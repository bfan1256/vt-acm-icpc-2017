def read_input(input_string, cases_from_first_line=True, length_per_case=None):
    '''process input'''
    lines = input_string.split('\n')
    cases = 1
    if cases_from_first_line:
        cases = lines[0]
        assert length_per_case is not None
    end_index = 1
    case_data = []
    for case in range(1, cases + 1):
        start_index = end_index
        end_index = length_per_case * case + 1
        case_data.append(lines[start_index:end_index)
    return case_data
