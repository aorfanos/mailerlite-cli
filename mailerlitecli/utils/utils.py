
def args_parse(options_tuple):
    _data_dict = {}
    for _key_value_count in range(0, len(options_tuple)):
        _key_value_tuple = options_tuple[_key_value_count]
        _key_value_list = _key_value_tuple.split(":")
        _key = _key_value_list[0]
        _value = _key_value_list[1]
        _data_dict[_key] = str(_value)
    return(_data_dict)
