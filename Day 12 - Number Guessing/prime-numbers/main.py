def is_prime(num):
    count = 0
    for check in range(1, num+1):
        if num % check == 0:
            count += 1
    if count == 2:
        print("True")
    else:
        print("False")


is_prime(7)
