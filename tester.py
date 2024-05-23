import subprocess
import os


import subprocess
# Example of using ANSI escape codes to change text color in Python



def run_command(command):
    # Start the process
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    # Wait for the process to complete and get the output and error
    stdout, stderr = process.communicate()
    # Decode the byte strings to Python strings
    stdout = stdout.decode('utf-8')
    stderr = stderr.decode('utf-8')
    return stdout, stderr

# Example usage

def get_failed_test_cases():
    with open('failed_tests.txt', 'r') as file:
        return file.read().strip().split(',')


def read_arguments(file_path, index):
    """ Read CLI arguments from a file for a specific index. """
    with open(file_path, 'r') as file:
        for i, line in enumerate(file, 1):
            if i == index:
                return line.strip().split()

def read_input(file_path):
    """ Read additional input from a file to be passed to the script. """
    with open(file_path, 'r') as file:
        return file.read().strip()

def run_script(args, additional_input):
    """ Run a script with the given arguments and additional input, and return its output. """
    command = 'python compsci_project.py ' + args + ' < '+ additional_input

    print(command)
    result, error = run_command(command)
    return result

def compare_outputs(script_output, expected_output):
    """ Compare script output with the expected output. """
   
    # Compare script output with the expected output.
    script_output_lines = script_output.replace('\r', '').split('\n')[1:]
    expected_output_lines = expected_output.replace('\r', '').split('\n')[1:]
    
    # Remove empty array elements
    script_output_lines = '\n'.join([line for line in script_output_lines if line and "Hello from the pygame community" not in line])
    expected_output_lines = '\n'.join([line for line in expected_output_lines if line and "Hello from the pygame community" not in line])
        
    # Remove whitespace and newlines
    script_output_lines = ''.join(script_output_lines.split())
    expected_output_lines = ''.join(expected_output_lines.split())

    # Find the first 5 characters where the difference is observed
    diff_chars = []
    for i in range(min(len(script_output_lines), len(expected_output_lines))):
        script_char = script_output_lines[i]
        expected_char = expected_output_lines[i]
        if script_char != expected_char:
            diff_chars.append((script_char, expected_char))
            if len(diff_chars) == 5:
                break
    if len(diff_chars) == 0:
       pass
    else:
        print("First 5 characters where the difference is observed:")
    for diff_char in diff_chars:
        print(f"Script: [{diff_char[0]}], Expected: [{diff_char[1]}], Position: {script_output_lines.index(diff_char[0])}")

    return script_output_lines == expected_output_lines



def open_expected_output(file_path):
        #print(os.listdir('./'))
        print(file_path)
        
       
        #Read the expected output from the file
        with open(file_path, 'r') as file:
            expected_output = (file.read())
            print (expected_output)

def save_output_to_file( output, file_name):
    # Check if the directory "Christiaan_outputs" exists
    if not os.path.exists("Christiaan_outputs"):
        # Create the directory "Christiaan_outputs"
        os.makedirs("Christiaan_outputs")

    # Save the output to a file
    output_dir = "Christiaan_outputs"
    output_path = os.path.join(output_dir, file_name)
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(output)

def main():
    # Directories containing expected outputs and test cases
    expected_outputs_dir = 'Expected_Outputs'
    test_cases_dir = './TestCases'
    
   
    failed_test_cases = get_failed_test_cases()
    if len(failed_test_cases) > 0:
        print("Known Failed Test Cases")
        print(failed_test_cases)

    ignored_test_cases = [5, 44]
    
    # Filter file names to include only 001 to 148 and exclude those starting with 'MVP'
    # Create a list of filenames from '001.txt' to '148.txt'
    file_names = [f"{i:03}.txt" for i in range(1, 149)]

    counter = 1
    # Loop through each file in the sorted list
    for file_name in file_names:
       
        if counter not in ignored_test_cases:

            print(f"-----------------------Test Case {counter}: {file_name}-----------------------------------")
                
            expected_path = os.path.join(expected_outputs_dir, file_name)
            input_path = os.path.join(test_cases_dir, file_name)
            
            expected_path = expected_path.replace('\\', '/')    
            #print(os.listdir('./'))
            #print(expected_path)
            
        
            # Read the expected output from the file
            # with open(expected_path, 'r') as file:
            #     expected_output = str(file.read())
            
            # Read the corresponding input from the TestCases folder
            
            with open('TestCases/cli_arguments.txt', 'r') as argments_file:
                cli_arguments = argments_file.read().split('\n')

            
            for index in range(len(cli_arguments)):
                cli_arguments[index] = cli_arguments[index].split(" ")
            
    
    

            # Read the specific arguments from cli_arguments corresponding to the file index
            

            args = cli_arguments[0][1] +' '+ cli_arguments[0][2] + ' '+cli_arguments[0][3]
            
            # Run the script and get its output
            script_output = run_script(args, input_path)
            print("=========OUTPUT=========")
            print(script_output)

            
            print("=========EXPECTED=========")
            print(read_input(expected_path))
            

            print("=========RESULT=========")
            
            if str(counter) in failed_test_cases or compare_outputs(script_output, read_input(expected_path)) == False:
                print("Match: FAILURE")
                action = "Boo"
                while action !="":
                    action = input()
                    if action =="t":
                        testCase = read_input(input_path)
                        print("---------TEST CASE---------")
                        print(testCase)
                    if action == "o":
                        print("---------EXPECTED---------")
                        open_expected_output(expected_path)
                        action = input()

                    if action == 'r':
                        print("again!")
                        script_output = run_script(args, input_path)
                
                        print(script_output)
                    
            else:
                print("Match: SUCCESS")

                
        counter += 1
        print('--------------------------------------------------------------------------------------'        )

        # # Compare the outputs and print the result
        # if compare_outputs(script_output, expected_output):
        #     print(f"Match for {file_name}: SUCCESS")
        # else:
        #     print(f"Match for {file_name}: FAILURE")

if __name__ == "__main__":
    main()
    input()

