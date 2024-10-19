# 아래 함수를 수정하시오.
def count_character(character, sep):
    new_chr = character.split(sep='o')
    count = len(new_chr)-1
    return count
    


result = count_character("Hello, World!", "o")
print(result)  # 2
