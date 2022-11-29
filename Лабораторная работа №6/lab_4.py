import json

INPUT_FILE = "input.csv"

def line_separator(line_s, delimeter=',') -> list:
    line_s = line_s.rstrip()
    line_s = line_s.split(delimeter)
    return line_s


def csv_to_list_dict() -> list[dict]:
     # TODO реализовать конвертер из csv в json
    with open(INPUT_FILE, 'r') as f:
        json_list = []
        keys = line_separator(f.readline())

        for lines in f:
            # if line_separator(lines) != keys:
            lines_new = line_separator(lines)
            json_list.append(dict(zip(keys, lines_new)))

    return json_list


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))

print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
