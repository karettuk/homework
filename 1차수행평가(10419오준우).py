def sorting(arr):
    if len(arr) <= 1:
        return arr
    elif len(arr) > 1:
        pivot = arr[0]
        short = []
        long = []
        for i in range(1, len(arr)):
            if len(arr[i]) < len(pivot) :
                short.append(arr[i])
            elif len(arr[i]) >= len(pivot) :
                long.append(arr[i])
        return sorting(short) + [pivot] + sorting(long)



size = int(input(''))
text = ['' for i in range(size)]
##print(text)
for i in range(size):
    text[i] = input('')
##print(text)

result = sorting(text)
##print(result)
for i in range(size):
    print(result[i])

    
