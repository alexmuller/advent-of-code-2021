import collections


def gamma(input_list):
    gamma_list = []
    num_bits = len(input_list[0])

    for i in range(num_bits):
        bits = [bit[i] for bit in input_list]

        counter = collections.Counter(bits)

        if counter['1'] > counter['0']:
            gamma_list.append('1')
        else:
            gamma_list.append('0')

    return ''.join(gamma_list)


def epsilon(input_list):
    epsilon_list = []
    num_bits = len(input_list[0])

    for i in range(num_bits):
        bits = [bit[i] for bit in input_list]

        counter = collections.Counter(bits)

        if counter['1'] < counter['0']:
            epsilon_list.append('1')
        else:
            epsilon_list.append('0')

    return ''.join(epsilon_list)


def binary_to_decimal(input_binary):
    return int(input_binary, 2)
