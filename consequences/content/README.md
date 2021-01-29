# Content Files

The content files for Consequences are stored in a JSON format and have three
important parts that must be named correctly for the program to read them.

The template file as an example:

```json
{
    "title": "Template",
    "text": "{name1} {verb1} to a/an {adjective1} {noun1} of {noun_plural1}.",
    "values": {"name1": "a name", "verb1": "verb", "adjective1": "adjective", "noun1": "noun", "noun_plural1": "plural noun"}
}
```

## Title

The title is displayed in the load menu, in the gameplay screen, and in the
output screen, and is used (with the timestamp) to make filenames for any saved
output. Duplicate titles will be modified on-screen to avoid conflicts. Single
words or short phrases are best.

## Text

The text is the unchanging body of your Consequences / Mad Libs style story. For
each position you want the player to insert a word, pick a variable name to
describe the choice. You can use numbers and capital letters (but no spaces or
other characters, and it can't start with a number!). Make sure each one is
different: use 1, 2, etc if you have, for example, more than one noun (noun1,
noun2...). In the position in the story where you want the word to appear, place
the variable name in curly brackets {noun1}, making sure to add spaces or
punctuation around the brackets as if it were a complete word. Then, add the
variable name to...

## Values

Values is a little more complicated than the first two items. Inside values, we
have another set of curly braces to contain the variable names you picked in the
text, plus a hint for the user (if desired) about what to put in. For each word
you picked to replace (that is, for each variable name), you will need to put
the variable name in quotes `"noun1"`, followed by a colon and a space `: `,
then the hint in quotes `"a noun"`. (If you choose not to put in a hint, you
still need the quotes, or it won't work: for example: `"verb1": ""`) Then a
comma and a space `, ` and then proceed with the next word. Don't add a comma
after the last value.
