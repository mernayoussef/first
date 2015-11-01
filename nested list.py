def nested(dept):
    for each_item in dept:
        if isinstance(each_item, list):
            for nested_item in each_item:
                if isinstance(nested_item, list):
                    for deeper_item in nested_item:
                        print(deeper_item)
                else:
                   print(nested_item)
        else:
            print(each_item)
