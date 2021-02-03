import datetime


def generate(input_dictionary):
    """
    Recombines the user generated input into the output text and sends to save
    function to be saved to the disk.
    """
    # Get and format user input
    output = dict()
    output["title"] = input_dictionary["title"]
    output["text"] = input_dictionary["text"].format_map(input_dictionary["values"])

    # Check for and add Made by value if present
    if input_dictionary["values"]["Made by:"] != "Enter name(s)":
        output["Made by:"] = input_dictionary["values"]["Made by:"]

    # Include time and date for filename and display
    output["time"] = datetime.datetime.now()

    return output


if __name__ == "__main__":
    test = {
        "title": "Template",
        "values": {
            "name1": "a name",
            "verb1": "verb",
            "adjective1": "adjective",
            "noun1": "noun",
            "noun_plural1": "plural noun",
        },
        "text": "{name1} {verb1} to a/an {adjective1} {noun1} of {noun_plural1}.",
    }
    generate(test)
