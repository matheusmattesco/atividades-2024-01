# Exercicio 01
def max_consecutive_sum(nums):
    max_atual = max_global = nums[0]

    for num in nums[1:]:
        max_atual = max(num, max_atual + num)
        max_global = max(max_global, max_atual)

    return max_global

# Testes 01
def test_max_consecutive_sum():
    print('1',max_consecutive_sum([1, -3, 2, 1, -1]) == 3)
    print('2',max_consecutive_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6)
    print('3',max_consecutive_sum([5, -1, -2, 3, -1, 2, -4]) == 7)
    print('4',max_consecutive_sum([1]) == 1)
    print('5',max_consecutive_sum([-1, -2, -3, -4, -5]) == -1)


# Exercício 02
def is_palindrome(word):
    return word == word[::-1]

# Testes 02
def text_is_palindrome():
    print('6',is_palindrome("radar") == True)
    print('7',is_palindrome("racecar") == True)
    print('8',is_palindrome("level") == True)
    # Testes negativos
    print('9',is_palindrome("python") == False)
    print('10',is_palindrome("hello") == False)
    print('11',is_palindrome("12321") == False)
    print('12',is_palindrome("abccbaa") == False)


# Exercício 03
def count_increasing_subsets(nums):
    if not nums:
        return 0

    subconjuntos = 1 

    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            subconjuntos += 1

    return subconjuntos

# Testes 03
def test_count_increasing_subsets():
    # Teste com lista vazia
    print('13',count_increasing_subsets([]) == 0)
    # Teste com uma lista de um elemento
    print('14',count_increasing_subsets([1]) == 1)
    # Teste com uma lista de números aleatórios
    print('15',count_increasing_subsets([1, 3, 2, 4]) == 8)
    # Teste com uma lista de números ordenados
    print('16',count_increasing_subsets([1, 2, 3, 4, 5]) == 31)
    # Teste com uma lista de números em ordem decrescente
    print('17',count_increasing_subsets([5, 4, 3, 2, 1]) == 0)
    # Teste com uma lista contendo números repetidos
    print('18',count_increasing_subsets([1, 2, 2, 3, 3, 3, 4]) == 16)


# Run the tests
if __name__ == "__main__":
    test_max_consecutive_sum()
    text_is_palindrome()
    test_count_increasing_subsets()

