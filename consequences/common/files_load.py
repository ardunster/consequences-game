import json
import pathlib


def content_load(filepath):
    '''
    Loads content data from a given json file.
    Input: the Path to the specified file.
    '''
    with(filepath.open()) as file:
        data = file.read()
    content = json.loads(data)
    # Verify that loaded file contains all required fields to generate content.
    valid = (('title' in content.keys()) and
             ('values' in content.keys()) and
             ('text' in content.keys()))
    if not valid:
        return "Invalid input"
        # TODO: Throw an error
    else:
        return content


def output_save(generated_dictionary):
    '''
    Saves user generated output into a re-loadable json output file.
    Filename generated from content title plus timestamp, contents of file
    include content title, timestamp, and the generated output.
    '''
    # if doesn't exist, create directory output
    pass


def output_load():
    pass


def directory_load(in_directory):
    '''
    Loads .json files in the specified directory.
    Input: the directory inside /consequences/ to search
    Return: a dictionary of {"json title field": "filename"}
    '''
    # Set up function variables
    filenames = []
    results = dict()

    # Sets the input directory to the relevant subdirectory inside
    # the consequences/ folder.
    directory = (pathlib.Path.cwd() / 'consequences' / in_directory)

    # Gets the filenames of any .json files in the specified directory
    # and any subdirectories.
    def get_filenames(directory):
        result = []
        if directory.exists():
            for item in directory.rglob('*.json'):
                result.append(item)
        return result

    filenames = get_filenames(directory)

    # For each .json file found, we read the title and use the title as a key
    # to the filename value in the results. For duplicate titles, a number is
    # appended to the title name, because you cannot have duplicate keys
    # in the dictionary.
    if filenames:
        i = 2
        for item in filenames:
            with(item.open()) as file:
                data = file.read()
            json_data = json.loads(data)
            # TODO: Verify 'title' exists, decide on handling if no 'title'
            #       in the .json file. Skip? Error handling? use "untitled"?
            if str(json_data['title']) not in results:
                results[str(json_data['title'])] = item
            else:
                results[str(json_data['title']) + " " + str(i)] = item
                i += 1
    else:
        # TODO: implement error and appropriate handling in interface.
        results = {"Empty": "Error"}

    return results


if __name__ == "__main__":
    print("Test the functionality of the load functions:")

    # print(directory_load('content').items())
    # print(directory_load('output').items())

    contentpath = pathlib.Path() / 'consequences' / 'content' / 'template.json'
    print(content_load(contentpath))

    badpath = pathlib.Path() / 'consequences' / 'content' / 'bad.json'
    print(content_load(badpath))
    # print(output_load())
