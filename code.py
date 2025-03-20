def my_info():
    student_id = 21244710077  
    first_name = "Bengisu"   
    last_name = "Acıerik"    
    return [student_id, first_name, last_name]

def get_number_list(n):
    num_list = []
    for i in range(n):
        num = int(input(f"Please enter positive number : "))
        num_list.append(num)
    return num_list

def process_number_list(num_list, k):
    
    if k <= 0:
        return None 
 
    unique_values = sorted(set(num_list))
   
    if k > len(unique_values):
        return None
    
    k_th_largest = unique_values[-k]
    k_th_smallest = unique_values[k-1]
    
    return [k_th_largest, k_th_smallest]
