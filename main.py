def read_file(input_file: str) -> list[str]:
    """
    Read the content of an input file.

    Args:
        input_file (str): The path to the input file.

    Returns:
        list[str]: A list that contains each line of the file as a string.
    """
    with open(input_file, 'r') as f:
        lines = f.readlines()
        return lines


def find_lines_with_keyword(lines: list[str], keyword: str) -> list[str]:
    """
    Find lines containing a specific keyword within a list of strings.

    Args:
        lines (list[str]): A list of strings representing lines of text.
        keyword (str): The keyword to search for within the lines.

    Returns:
        list[str]: A list of lines from the input list containing the specified keyword.
    """
    res = []
    for line in lines:
        if keyword in line:
            res.append(line)
    return res


if __name__ == '__main__':
    try:
        file_data = read_file('data.txt')
        result = find_lines_with_keyword(file_data, 'Lorem')
    except:
        print('An error occurred')
