def string_count(text_list):
    count_id = 1
    count_list = []
    valid_dict = []
    for index,data in enumerate(text_list):
        data_count = text_list.count(data)
        data_list = data, data_count
        valid_dict.append(data_list)
        max_count = 0
        if data_count > max_count:
            max_count = data_count
            most_frequent_word = data
    output_dict = {"Word Frequencies": valid_dict,
                   "Most Frequent" : most_frequent_word}
    print(output_dict)

text_string = "apple banana apple orange banana apple banana banana"
text_list = text_string.split(" ")
string_count(text_list)
