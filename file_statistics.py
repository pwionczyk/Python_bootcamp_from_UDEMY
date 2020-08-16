'''
statistics('story.txt') 
# {'lines': 172, 'words': 2145, 'characters': 11227}
'''


def statistics(file_name):
    with open(file_name) as file:
        chars = file.read()
        result = {'lines': chars.count('\n')+1, 
                  'words': sum(line.count(' ')+1 for line in chars.split('\n')), 
                  'characters': len(chars)}
    return result


print(statistics('story.txt'))
