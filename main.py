import pandas
nato_file = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dic = {row.letter: row.code for (index, row) in nato_file.iterrows()}
print(phonetic_dic)

def gen_phonetic():
    user_word = input("Enter a word: ").upper()
    try:
        phonetic_list = [phonetic_dic[letter] for letter in user_word]
    except KeyError:
        print('Sorry, words only in alphabet please.')
        gen_phonetic()
    else:
        print(phonetic_list)

gen_phonetic()

