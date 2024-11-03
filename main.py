import subprocess
import glob


def test(dir, program_file):
    input_dir = dir + "in/"
    output_dir = dir + "out/"
    print(f'---TEST START: {dir}{program_file}')

    # Przechodzimy przez każdy plik .in w katalogu in
    for input_file in glob.glob(input_dir + "*.in"):
        # Nazwa pliku wynikowego, odpowiadająca nazwie pliku wejściowego
        expected_output_file = output_dir + input_file.split("/")[-1].replace(".in", ".out")

        # Sprawdzamy, czy odpowiadający plik z wynikiem istnieje
        try:
            with open(expected_output_file, "r") as expected_file:
                expected_output = expected_file.read().strip()
        except FileNotFoundError:
            print(f'Expected output file {expected_output_file} not found. Skipping.')
            continue

        # print(f'Running wal.py with input file: {input_file}')
        with open(input_file, "r") as file_input:
            # Uruchamiamy wal.py i przechwytujemy wyjście
            result = subprocess.run(["python", dir + program_file], stdin=file_input, capture_output=True, text=True)
            program_output = result.stdout.strip()

            # Porównujemy uzyskane wyjście z oczekiwanym i drukujemy oba wyniki w odpowiednim formacie
            result = "NOT GOOD"
            if program_output == expected_output:
                result = "GOOD"
            print(f'{result}, file: {input_file}, expected: {expected_output}, given: {program_output}')
    print('---TEST END---')


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test('wal/', 'wal.py')
