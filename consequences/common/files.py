import datetime
import json
import pathlib


def content_load(in_filename):
    """
    Loads content data from a given json file.
    Input: the Path to the specified file.
    Return: Content in dictionary format
    """
    with (in_filename.open()) as file:
        data = file.read()
    content = json.loads(data)
    # Verify that loaded file contains all required fields to generate content.
    valid = (
        ("title" in content.keys())
        and ("values" in content.keys())
        and ("text" in content.keys())
    )
    if not valid:
        return "Invalid input"
        # TODO: Throw an error
    else:
        return content


def output_save(generated_dictionary):
    """
    Saves user generated output into a re-loadable json output file.
    Filename generated from content title plus timestamp, contents of file
    include content title, timestamp, and the generated output.
    """
    output_directory = pathlib.Path.cwd() / "consequences" / "output"

    # Remove spaces and invalid file path characters, convert to lower case
    # for filename consistency
    invalid_chars = '<>:"\\/|?* '
    filename = "".join(
        c for c in generated_dictionary["title"] if c not in invalid_chars
    ).lower()

    # Add datetime
    filename += "-" + generated_dictionary["time"].strftime("%Y%m%d-%H%M")

    filename += ".json"

    generated_dictionary["time"] = generated_dictionary["time"].__str__()

    outputpath = output_directory / filename
    with open(outputpath, "w") as outfile:
        json.dump(generated_dictionary, outfile)


def output_load(in_filename):
    """
    Loads previously generated and saved user output for display.
    Input: File path to load
    Output: Dictionary matching original output of generate()
    """
    with (in_filename.open()) as file:
        data = file.read()
    json_data = json.loads(data)
    json_data['time'] = datetime.datetime.fromisoformat(json_data['time'])

    return json_data


def directory_load(in_directory):
    """
    Loads .json files in the specified directory.
    Input: the directory inside /consequences/ to search
    Return: a dictionary of {"json title field": "filename"}
    """
    # Set up function variables
    filenames = []
    results = dict()

    # Sets the input directory to the relevant subdirectory inside
    # the consequences/ folder.
    directory = pathlib.Path.cwd() / "consequences" / in_directory

    # Gets the filenames of any .json files in the specified directory
    # and any subdirectories.
    def get_filenames(directory):
        result = []
        if directory.exists():
            for item in directory.rglob("*.json"):
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
            with (item.open()) as file:
                data = file.read()
            json_data = json.loads(data)
            if (
                "title" not in str(json_data)
                or "text" not in str(json_data)
            ):
                pass
            elif str(json_data["title"]) not in results:
                results[str(json_data["title"])] = item
            else:
                results[str(json_data["title"]) + " " + str(i)] = item
                i += 1
    else:
        # TODO: implement error and appropriate handling in interface.
        results = {"Empty": "Error"}

    return results


if __name__ == "__main__":
    print("Test the functionality of the load functions:")

    print(directory_load('content').items())
    print(directory_load('output').items())

    contentpath = pathlib.Path() / "consequences" / "content" / "template.json"
    print(content_load(contentpath))

    badpath = pathlib.Path() / "consequences" / "content" / "bad.json"
    print(content_load(badpath))
