def longestCommonPrefix(strs):

    # edge case
    if not strs:
        return ""

    prefix = ""

    # loop through characters of first word
    for i in range(len(strs[0])):
        char = strs[0][i]

        # compare with all words
        for word in strs:
            if i >= len(word) or word[i] != char:
                return prefix

        prefix += char

    return prefix


# -------- MAIN PROGRAM --------
strs = ["flower", "flow", "flight"]

result = longestCommonPrefix(strs)

print("Longest Common Prefix:", result)