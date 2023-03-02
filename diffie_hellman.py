import string

def string_to_int (my_str):
    int_code = 0
    for i in range (len(my_str)):
        int_code += ord(my_str[i])
    return int_code

def alice (gen,key,prime):
        new_gen = (gen ** key) % prime
        return new_gen

def bob(gen,key,prime):
        new_gen = (gen ** key) % prime
        return new_gen

def main():
    alice_string = 'hello'
    bob_string = 'goodbye'
    A = B = gen = 5
    s_A = 1
    s_B = 2
    prime = 841000001
    # prime = 23

    alice_key = 5479
    bob_key = 69420

    while s_A != s_B:
        s_A = alice(B,alice_key,prime)
        s_B = bob(A,bob_key,prime)
        if s_A != s_B:
            A = s_A
            B = s_B
        else: 
            s = s_A

    print(s)

# If transposition_code_break.py is run (instead of imported as a module) call
# the main() function.
if __name__ == '__main__':
    main()
