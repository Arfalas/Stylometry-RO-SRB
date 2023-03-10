
#Articles and texts are presented as dictionaries (Key:Author ; Value:.txt number)
articles = { 'Ljotic' : [1, 2, 3, 4, 5],
            'Unknown' : [6, 7],
             'Nedic' : [8, 9] }

# Opens .txt files, converts them to strings and groups them by author
def txt_files_to_strings(filenames):
    strings = []
    for filename in filenames:
        with open(f'C:/Users/No Name/OneDrive/Desktop/Stylometry Project/Lotic_{filename}.txt', 'r', encoding="utf_8") as f:
            strings.append(f.read())
    return '\n'.join(strings)

strings_by_creator = {}
for creator, files in articles.items():
    strings_by_creator[creator] = txt_files_to_strings(files)

# Testing if the strings are properly loaded
for creator in articles:
    print(strings_by_creator[creator][:100])

# Tokenization and POS for the Serbian cyrilic text
txt_file = open(f'C:/Users/No Name/OneDrive/Desktop/Stylometry Project/Lotic_1.txt', 'r', encoding="utf_8")
source_txt = txt_file.read()

import classla 
classla.download('sr')
nlp = classla.Pipeline('sr', processors = 'tokenize, pos')
doc = nlp(source_txt)

print(doc.to_conll())


