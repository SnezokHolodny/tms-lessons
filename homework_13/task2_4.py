import re
def is_date(str: str) -> bool:
    return re.fullmatch(r'\d\d-\d\d-\d{4}', str) is not None

def is_float_number(str: str) -> bool:
    return re.fullmatch(r'\d+.\d+', str) is not None

class WordIterable:
    def __init__(self, text):
        self.text = text
        self.num = 0

    def __iter__(self):
        self.word = self.text.split()
        return self

    def __next__(self):
        self.num += 1
        if self.num > len(self.word):
            raise StopIteration()
        return self.word[self.num - 1]

def generate_words(text: str):
    words = text.split()
    for i in words:
        yield i





if __name__ == '__main__':
    assert is_date('19-06-1865')
    assert not is_date('233-05-1777')
    assert not is_date('23-025-777')
    assert is_float_number('20.15')
    assert is_float_number('1.053')
    assert not is_float_number('13')

    text = 'половина пять пятнадцать четвертого'
    for i in WordIterable(text):
        print(i)

    assert ['это', 'разборка', 'Питерская'] == [i for i in WordIterable('это разборка Питерская')]
