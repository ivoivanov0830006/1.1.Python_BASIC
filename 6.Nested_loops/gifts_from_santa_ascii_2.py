n_input = int(input())
m_input = int(input())
s_input = int(input())
adress = 0

for num_adress in range(m_input, n_input - 1, - 1):
    if num_adress % 2 == 0 and num_adress % 3 == 0:
        adress = num_adress
        if num_adress == s_input:
            break
        print(adress, end=" ")
