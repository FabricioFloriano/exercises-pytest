from pathlib import Path


def hexadecimal_to_decimal(hex_digit: str) -> int:
    return int(hex_digit, 16)


def print_hexadecimal_to_decimal(hex_digit: str) -> None:
    print(hexadecimal_to_decimal(hex_digit))


def write_hexadecimal_to_decimal(hex_digit: str, output_file: Path) -> None:
    with open(output_file, "w") as file:
        file.write(str(hexadecimal_to_decimal(hex_digit)))


def main() -> int:
    input_number = input("Digite um número hexadecimal: ")
    return hexadecimal_to_decimal(input_number)
