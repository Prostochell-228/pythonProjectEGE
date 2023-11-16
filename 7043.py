import re

f = open('9377.txt')
s = f.readline()


def find_min_substring_length(s):
    pattern = '0?1?2?3?4?5?6?7?8?9?a?b?c?d?e?f?A?B?C?D?E?F?'

    match = re.findall(pattern, s)
    return len(match)


print(find_min_substring_length(s))
