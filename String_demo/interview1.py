"""input = 'nava,neetha;krishnan' ; output should be output = 'avan,ahteen;nanhsirk'"""
input_str = "nava,neetha;krishnan!"

result = ""
word = ""

for char in input_str:
    if char.isalpha():
        word += char
    else:
        result += word[::-1]
        result += char
        word = ""

result += word[::-1]

print(result)