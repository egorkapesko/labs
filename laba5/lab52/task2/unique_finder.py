def find_unique(elements):

    if not elements:
        return []
    
    unique_elements = []
    
    for element in elements:
        if elements.count(element) == 1:
            unique_elements.append(element)
    
    return unique_elements