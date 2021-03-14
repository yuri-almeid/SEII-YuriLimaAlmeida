print('Imported my_module...')

test = 'Teste'

def find_index(to_search, target):
    '''Encontra o índice de um item'''
    for i, value in enumerate(to_search):
        if value == target:
            return i
        
        return -1
    