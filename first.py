def first(source, target):
    for char in target:  
        if char not in source:  
            return -1
    
    res = 0
    targetIndex = 0
    
    while(targetIndex < len(target)):
        temp = targetIndex
        sourceIndex = 0
        while(sourceIndex < len(source) and targetIndex < len(target)):
            if source[sourceIndex] == target[targetIndex]:
                sourceIndex = sourceIndex + 1
                targetIndex = targetIndex + 1
            else :
                sourceIndex = sourceIndex + 1
        if sourceIndex == len(source) and targetIndex < len(target):
            res = res + 1
        if temp == targetIndex:
            return -1
    return res + 1


print(first("abc", "acababcbcd"))
