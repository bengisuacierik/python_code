from hw1 import get_number_list, process_number_list
from unittest.mock import patch

# Function to test get_number_list with multiple test cases
def test_get_number_list(test_cases):
    for i, (mock_inputs, expected_list) in enumerate(test_cases, 1):
        with patch('builtins.input', side_effect=mock_inputs):
            result = get_number_list(len(mock_inputs))
            if result == expected_list:
                print(f"Test {i} passed for get_number_list with input {mock_inputs}")
            else:
                print(f"Test {i} failed: expected {expected_list}, got {result}")

# Function to test process_number_list with multiple test cases
def test_process_number_list(test_cases):
    for i, (number_list, rank, expected) in enumerate(test_cases, 1):
        result = process_number_list(number_list, rank)
        if result == expected:
            print(f"Test {i} passed for process_number_list with rank {rank} and list {number_list}")
        else:
            print(f"Test {i} failed: expected {expected}, got {result}")

def main():
    # Test cases for get_number_list (mock inputs and expected list)
    get_number_list_cases = [
        (['10', '20', '30', '40', '50'], [10, 20, 30, 40, 50]),   # Simple input case
        (['5', '15', '25'], [5, 15, 25]),                         # Smaller input case
        (['100', '200', '300', '400'], [100, 200, 300, 400]),     # Another simple input case
    ]

    # Test cases for process_number_list (number list, rank, expected result)
    process_number_list_cases = [
        ([10, 20, 30, 40, 50], 2, [40, 20]),  # 2nd largest and smallest
        ([5, 10, 15, 20, 25], 1, [25, 5]),   # Largest and smallest
        ([8, 3, 6, 2, 10], 3, [6, 6]),       # 3rd largest and smallest
        ([1, 1, 1, 2, 2, 2, 2, 3, 3, 3], 2, [2, 2]),    # Duplicates
        ([10, 20], 3, None),                 # Out of bounds rank
    ]
    
    # Run the test cases in a loop for both functions
    print("Testing get_number_list:")
    test_get_number_list(get_number_list_cases)

    print("\nTesting process_number_list:")
    test_process_number_list(process_number_list_cases)

if __name__ == "__main__":
    main()
