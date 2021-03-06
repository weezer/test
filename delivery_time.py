def delivery_time(input_string):
    len_input = len(input_string)
    if len_input == 0:
        return 0
    matrics = [0,0],[0,0]
    split_string = []
    for i in range(len_input):
        split_string.append(map(int, input_string[i].split("-")))
    if len_input == 1:
        if split_string[0][1] <= 50:
            return split_string[0][1]
        else:
            return False

    # print split_string
    matrics[0][0] = split_string[0][1]
    line_num = 0
    current = 1
    prev = 0
    steps = split_string[0][1]
    print steps
    while current < len_input:
        if split_string[current][0] != split_string[prev][0]:
            line_num ^= 1
            if steps - matrics[line_num][1] > split_string[current][1] - matrics[line_num][0]:
                steps += 1
            else:
                steps = matrics[line_num][1] + split_string[current][1] - matrics[line_num][0] + 1
        else:
            steps += split_string[current][1] - split_string[prev][1] + 1
        if split_string[current][1] <= matrics[line_num][0] or split_string[current][1] > 50:
            # print matrics
            # print split_string[current][1]
            return False
        matrics[line_num][0] = split_string[current][1]
        matrics[line_num][1] = steps
        prev += 1
        current += 1
        # print steps
    return steps


print delivery_time(['1-15', '1-5'])