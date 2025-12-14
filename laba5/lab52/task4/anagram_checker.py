def are_anagrams(str1, str2):

    str1_clean = str1.replace(" ", "").lower()
    str2_clean = str2.replace(" ", "").lower()

    if len(str1_clean) != len(str2_clean):
        return False

    return sorted(str1_clean) == sorted(str2_clean)