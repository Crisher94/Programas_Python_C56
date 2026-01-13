#Generar un código que determine si el número que se da de entrada es primo o no
import argparse

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Checar su un número es primo')
    parser.add_argument('number', type=int, help='numero a checar')
    args = parser.parse_args()
    if is_prime(args.number):
        print(f"{args.number} es primo")
    else:
        print(f"{args.number} no es primo") 