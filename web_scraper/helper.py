def convert_list_to_dict(datas: list):
    '''Convert list to hierarchical dictionary'''

    def recursive(data):
        d = {}
        if len(data) == 2:
            key = data[0]
            value = data[1]
            d[key] = value

        else:
            key = data[0]
            value = recursive(data[1:])

            d[key] = value

        return d

    return recursive(datas)
