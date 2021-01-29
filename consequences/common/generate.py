# from consequences.common.files_load import content_load, output_save


def generate(input_dictionary):
    '''
    Recombines the user generated input into the output text and sends to save
    function to be saved to the disk.
    '''
    output = dict()
    output['title'] = input_dictionary['title']
    output['text'] = input_dictionary['text'].format_map(input_dictionary["values"])
    # TODO: Get and save timestamp into dict
    # TODO: extract "Made By" field if not empty
    return output


if __name__ == "__main__":
    test = { "title": "Template",
            "values": {"name1": "a name", "verb1": "verb", "adjective1": "adjective", "noun1": "noun", "noun_plural1": "plural noun"},
            "text": "{name1} {verb1} to a/an {adjective1} {noun1} of {noun_plural1}."}
    generate(test)
