

def check_list(ondergrens, texten):
    # sort on length biggest first
    texten.sort(key=len , reverse=True)

    # loop through all texten and check if there is a matching substring
    for text in texten:
        # loop through all possible substrings
        for i in range(len(text)):
            for j in range(len(text)):
            # check if the substring is in the text
                if text[i:j] in texten:
                    pass
    return ondergrens



def test(ondergrens, texten):
    texten.sort(key=len , reverse=True)
    possible_strings = []
    biggest_possible = texten[ondergrens-1]
    length_substring = len(biggest_possible)

    while (length_substring > 0):
        start_index = 0
        possible_strings = []
        while (start_index + length_substring <= len(biggest_possible)):
            matches = 0
            substring = biggest_possible[start_index:start_index+length_substring]
            for text in texten:
                if substring in text:
                    matches += 1
            if matches >= ondergrens:
                return substring
            else:
                start_index += 1
        if(len(possible_strings) != 0):
            return possible_strings
        length_substring -= 1
    return "ONMOGELIJK"















cases = int(input())


for j in range(cases):
    ondergrens = int(input())
    aantal_texten = int(input())

    texten = []
    for i in range(aantal_texten):
        texten.append(input())
    print(j, test(ondergrens, texten))
