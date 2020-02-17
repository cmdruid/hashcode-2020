import os


def load_data_dir(directory, extension=".in", delimiter=" ", keymap=False):
    """
    Load all files in a given directory and compile into a data-set.

    :directory: - The relative path to where files are stored.
    :extension: - The file extension to look for.
    :delimiter: - The delimiter to use when splitting the file string.
    """
    data = []
    print(f"Loading files in directory: {directory}")

    for file in os.listdir(os.fsencode(directory)):
        filename = os.fsdecode(file)
        if filename.endswith(extension):
            try:
                filepath = os.path.join(directory, filename)
                data.append(load_file(filename, filepath, delimiter))
            except ValueError:
                print(f"Could not load {filename}")

    if data:
        print(f" {len(data)} files loaded successfully.")
        return data
    else:
        print("Something went wrong.")


def load_file(filename, filepath, delimiter):
    """
    Load file using given delimiter and return list object.
    """
    print(f"Loading file {filename}...")
    with open(filepath, 'r') as file:
        header = [filename.rsplit('.', 1)[0]]
        return header + [line.strip('\n').split(delimiter) for line in file.readlines()]


def export_results(directory, data_set):
    """
    Write our data sets into the proper file format.

    :directory: The directory to save our files to.
    :data_set:  The data to be exported.
    """
    file_count = 0
    print(f"Attempting to write {len(data_set)} data set(s) to directory {directory}...")

    for data in data_set:

        file_path = directory + "/" + str(data['set_name']) + '_results.txt'
        lines = str(data['set_size']), '\n', ' '.join([str(x) for x in data['values']])

        with open(file_path, 'w') as file:
            try:
                file.writelines(lines)
                file_count += 1
            except TypeError:
                print(f"Unable to write lines to file: {lines}")

    print(f" {file_count} files written successfully.")
