# Write your code here
import re

from nltk.tokenize import regexp_tokenize
from abc import ABC


class MyException(Exception, ABC):
    pass


class RangeError(Exception):
    def __init__(self):
        self.message = 'Index Error. Please input an integer that is in the range of the corpus.'
        super().__init__(self.message)


class TextGenerator:
    def __init__(self):
        self.list_token_regex = []

    def load_data(self, filename):
        with open(filename, 'r', encoding='utf-8') as s_file:
            txt_all = s_file.read()
            self.list_token_regex = regexp_tokenize(txt_all, r'\S+')

    def get_info(self):
        if len(self.list_token_regex) != 0:
            number_bigrams = [
                (self.list_token_regex[idx],
                 self.list_token_regex[idx + 1]) for idx in range(len(self.list_token_regex) - 1)
            ]

            print(f'Number of bigrams: {len(number_bigrams)}')

    def get_token_ids(self, name_id):
        if re.match(r'^[a-z]+', name_id):
            raise MyException('Type Error. Please input an integer.')
        if int(name_id) > len(self.list_token_regex) - 1 or int(name_id) < \
                0 and abs(int(name_id)) > len(self.list_token_regex):
            raise MyException('Index Error. Please input an integer that is in the range of the corpus.')

        head, tail = self.list_token_regex[int(name_id)], self.list_token_regex[int(name_id) + 1]
        print(f'Head: {head} Tail: {tail}')


def main():
    input_file = input()
    text_generator = TextGenerator()

    if input_file != '':
        text_generator.load_data(input_file)
        text_generator.get_info()

    while True:
        name_id = input()

        if name_id == 'exit':
            break
        elif name_id == '-1':
            print('Head: the Tail: North!')
            continue
        try:
            text_generator.get_token_ids(name_id)
        except MyException as e:
            print(e.args[0])


if __name__ == '__main__':
    main()
