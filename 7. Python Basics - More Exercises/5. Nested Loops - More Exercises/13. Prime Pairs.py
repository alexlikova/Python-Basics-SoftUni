"""start_first_pair, start_second_pair, diff_first, diff_second = [int(input()) for _ in range(4)]

end_fist_pair = start_first_pair + diff_first
end_second_pair = start_second_pair + diff_second
primeNum = False

for a in range(start_first_pair, end_fist_pair + 1):
    for number in range(2, a):
        if a % number == 0:
            primeNum = False
            break
    else:
        primeNum = True

        for b in range(start_second_pair, end_second_pair + 1):
            for number in range(2, b):
                if b % number == 0:
                    primeNum = False
                    break
            else:
                primeNum = True

            if primeNum:
                print(f"{a}{b}")"""

"""def is_prime(n):
    return n > 1 and all(n % i for i in islice(count(2), int(sqrt(n) - 1)))"""

f_start = int(input())
s_start = int(input())
f_end = int(input()) + f_start
s_end = int(input()) + s_start
prime_numbers_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
                      101]

for i in range(f_start, f_end + 1):
    for j in range(s_start, s_end + 1):
        if i in prime_numbers_list and j in prime_numbers_list:
            print(str(i) + str(j))
