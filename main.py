import json

# Open the input file for reading
with open('accents.txt', 'r', encoding='utf-8') as infile:

  # Create an empty dictionary to hold the output
  output = {}

  # Iterate over each line in the input file
  for line in infile:

    # Split the line into its three components
    parts = line.strip().split('\t')
    kanji = parts[0]
    hiragana = parts[1]
    accents = parts[2]

    # Remove any text inside brackets
    accents = accents.replace('(', '').replace(')', '')

    # Split the accents into a list
    accents = accents.split(',')

    # Convert the accents to integers if they exist
    accents = [int(accent) for accent in accents if accent.isdigit()]

    # Add the word to the output dictionary
    output[kanji] = {'hiragana': hiragana, 'accents': accents}

# Write the output dictionary to a JSON file
with open('output.json', 'w', encoding='utf-8') as outfile:
  json.dump(output, outfile, ensure_ascii=False, indent=4)
