def get_fid(search_value):
    keys = [key for key, value in FID_CODES.items() if value == search_value]
    return keys[0]
