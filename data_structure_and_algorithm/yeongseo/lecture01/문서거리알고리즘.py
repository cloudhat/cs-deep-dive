# http://6.006.scripts.mit.edu/~6.006/spring08/wiki/index.php?title=Document_Distance_Problem_Definition

# 1
import math

def get_words(doc): 
    words = []

    word= ""
    for char in doc:
        if 48<=ord(char)<=57 or 65<=ord(char)<=90 or 97<=ord(char)<=122:
            word += str(char)
        else:
            words.append(word.lower())
            word = ""
    words.append(word.lower())
    
    return words

# 2
def count(words): 
    count = {}
    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1

    return count

"""
d' = D1 * D2 / |D1| * |D2| , 이때 |D1| = N(D) (Norm=크기)
N(D) = math.sqrt(D,D) = ΣDw^2
D1과 D2사이의 각도 = acrccos(d')
"""
    
# 3
def inner_product(count1, count2):   # 내적 계산 
    result = 0
    for key in count1:
        if key in count2:
            result += count1[key] * count2[key]

    return result

# 3-1
def vector_angle(count1, count2):
    # D1 * D2 : 두 벡터의 내적
    numerator = inner_product(count1, count2)
    
    # |D1| * |D2| : 벡터 D1의 크기 * 벡터 D2의 크기
    denominator = math.sqrt(inner_product(count1,count1) * inner_product(count2,count2))

    return math.acos(numerator/denominator)

def main(doc1, doc2):
    words1 = get_words(doc1)
    words2 = get_words(doc2)

    count1 = count(words1)
    count2 = count(words2)

    return vector_angle(count1,count2)

doc1 = "To be or not to be"

doc2 = "Doubt truth to be a liar"

print(main(doc1, doc2))


