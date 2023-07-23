my_dict = {
    'outer_key1': {
        'inner_key1': 'value1',
        'inner_key2': 'value2',
        'inner_key3': 'value3'
    },
    'outer_key2': {
        'inner_key4': 'value4',
        'inner_key5': 'value5'
    },
    'outer_key3': {
        'inner_key6': 'value6'
    }
}

# Пример использования цикла for для перебора значений в словаре в словаре
for outer_key, inner_dict in my_dict.items():
    print(outer_key, inner_dict)
    print()
    for inner_key, value in inner_dict.items():
        print(f"Inner key: {inner_key}, Value: {value}")
    print()


