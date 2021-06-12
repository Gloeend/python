import io


# Раздел 5

# Общие функции

def fileReadToWriteAgain(filename: str, outfile: str):
    output = list()
    counter = 0
    with io.open(filename, encoding='utf-8') as file:
        for line in file:
            output.append(line.replace('.', '').split())
    end = open(outfile, 'w')
    for line in output:
        for j, word in enumerate(line):
            send = word + ' '
            if (len(send) + counter) >= 255:
                end.write('\n')
                end.write(send)
                counter = 0
                continue
            end.write(send)
            counter += len(send)
    return True


def fileReadToWriteVocabulary(filename: str, outfile: str, mod: dict = {}):
    output = list()
    with io.open(filename, encoding='utf-8') as file:
        for line in file:
            output.append(line.replace('.', '').split())
    end = open(outfile, 'w')

    for line in output:
        for j, word in enumerate(line):
            if len(mod) == 0:
                end.write(word)
                end.write('\n')
                continue
            if mod.get('min') != 0 and len(word) < mod.get('min'):
                continue
            if mod.get('max') and len(word) > mod.get('max'):
                continue
            end.write(word)
            end.write('\n')
    return True


# 1

# fileReadToWriteAgain('text.txt', 'textout.txt')

# 2

#
# fileReadToWriteVocabulary('text.txt', 'textout.txt', {'min': 5, 'max': 6})
