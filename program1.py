def check_duplicates(arr, num):
    duplicates = []
    
    if num in arr:
        duplicates.append(num)
    
    for item in arr:
        if arr.count(item) > 1 and item not in duplicates:
            duplicates.append(item)
    
    if duplicates:
        return f"Here duplicate datas are: {duplicates}"
    else:
        return "From input1 and input2, there is no duplicate data."


arr = input("Enter the numeric array: ")
numeric_array = [int(x) for x in arr.split(',')]


num = int(input("Enter the integer number: "))

result = check_duplicates(numeric_array, num)
print(result)