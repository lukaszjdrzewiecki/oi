import subprocess
import glob
import time


def test(program_dir, program_file, given_dir, expected_dir):
    input_dir = program_dir + given_dir
    output_dir = program_dir + expected_dir
    print(f'---TEST START: {program_dir}{program_file}')

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
            start = time.time()
            result = subprocess.run(["python", program_dir + program_file], stdin=file_input, capture_output=True, text=True)
            prociessing_time = time.time() - start
            if result.stderr is not None and result.stderr != "":
                #print(f'ERROR file: {input_file}', result.stderr)
                continue
            program_output = result.stdout.strip()

            # Porównujemy uzyskane wyjście z oczekiwanym i drukujemy oba wyniki w odpowiednim formacie
            result = "NOT GOOD"
            if program_output == expected_output:
                result = "GOOD"
            #print(f'{result}, file: {input_file}, expected: {expected_output}, given: {program_output.}')
            print(f'{result}, file: {input_file}, processing_time: {prociessing_time}')
            #if result == "NOT GOOD":
            #    return
    print('---TEST END---')


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # test('wal/', 'wal.py', "in/", "out/")
    #test('spr/', 'spr.py', "in/", "out/")

    start = time.time()
    test('zam/', 'zam.py', "in/", "out/")
    print(time.time()-start)

