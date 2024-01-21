import click
from alive_progress import alive_bar


# Get output string from array with indexes
def get_string_from_list_numbered(items: []):
    list_numbered = ['{}: {}'.format(index + 1, str(item)) for index, item in enumerate(items)]
    list_format = [(item[:-1] if item.endswith('/') else item) for item in list_numbered]
    return '\n'.join(list_format)


# Get output string from array
def get_string_from_list(items: []):
    list_format = [(item[:-1] if item.endswith('/') else item) for item in items]
    return '\n'.join(list_format)


# Prompt index by array
def prompt_index(items: []):
    index = -1
    while index < 0:
        index = click.prompt('Select index', type=int)
        if index > len(items) or index <= 0:
            click.echo(f"Error: '{index}' is not a valid index.", err=True)
            index = -1
    return index


# Bar for subprocess by symbol
def bar_subprocess_symbol(size, process):
    counter = 0
    with alive_bar(size) as bar:
        for _ in iter(lambda: process.stdout.read(1), b""):
            counter += 1
            if counter < size:
                bar()
        bar(size - counter)


# Bar for subprocess by lines
def bar_subprocess_lines(size, process):
    counter = 0
    with alive_bar(size) as bar:
        for out in iter(lambda: process.stdout.readline(), ""):
            if not out:
                break
            counter += 1
            if counter < size:
                bar()
        bar(size - counter)
