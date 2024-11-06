# Print the table
def print_table(processes):
    print("Process | Arrival Time | Burst Time | Waiting Time | Turnaround Time")
    print("---------------------------------------------------------------------")
    
    for i, process in enumerate(processes):
        turnaround_time = process['waiting'] + process['burst']
        print(f"P{i+1:6} | {process['arrival']:12} | {process['burst']:10} | {process['waiting']:12} | {turnaround_time:10}")
    print("\n")


# 1. First-Come, First-Served (FCFS)
def fcfs(processes):
    processes.sort(key=lambda x: x['arrival'])
    total_waiting_time = 0
    current_time = 0

    for process in processes:
        if current_time < process['arrival']:
            current_time = process['arrival']
        process['waiting'] = current_time - process['arrival']
        total_waiting_time += process['waiting']
        current_time += process['burst']
    
    print("FCFS Scheduling:")
    print_table(processes)
    return total_waiting_time / len(processes)


# 2. Shortest Job First (SJF)
def sjf(processes):
    processes.sort(key=lambda x: (x['arrival'], x['burst']))
    total_waiting_time = 0
    current_time = 0

    for process in processes:
        if current_time < process['arrival']:
            current_time = process['arrival']
        process['waiting'] = current_time - process['arrival']
        total_waiting_time += process['waiting']
        current_time += process['burst']
    
    print("SJF Scheduling:")
    print_table(processes)
    return total_waiting_time / len(processes)


# 3. Round Robin (RR)
def round_robin(processes, quantum):
    print("\nRound Robin Process")
    # Initialize process data
    n = len(processes)
    remaining_burst = [process['burst'] for process in processes]  # To track remaining burst time
    waiting_times = [0] * n  # Waiting times for each process
    current_time = 0  # Track current time

    while True:
        done = True
        for i, process in enumerate(processes):
            # Check if process has remaining burst time
            if remaining_burst[i] > 0:
                done = False  # There is at least one process left to execute

                # Check if process burst time is greater than quantum
                if remaining_burst[i] > quantum:
                    current_time += quantum
                    remaining_burst[i] -= quantum
                else:
                    # Process finishes in this time slice
                    current_time += remaining_burst[i]
                    waiting_times[i] = current_time - process['burst'] - process['arrival']
                    remaining_burst[i] = 0  # Process is complete

        # Break the loop if all processes are done
        if done:
            break

    # Add waiting times to each process dictionary and calculate turnaround times
    for i in range(n):
        processes[i]['waiting'] = waiting_times[i]

    print_table(processes)

    # Calculate average waiting time
    avg_waiting_time = sum(waiting_times) / n
    return avg_waiting_time


# 4. Priority Scheduling
def priority_scheduling(processes):
    processes.sort(key=lambda x: (x['arrival'], x['priority']))
    total_waiting_time = 0
    current_time = 0

    for process in processes:
        if current_time < process['arrival']:
            current_time = process['arrival']
        process['waiting'] = current_time - process['arrival']
        total_waiting_time += process['waiting']
        current_time += process['burst']
    
    print("Priority Scheduling:")
    print_table(processes)
    return total_waiting_time / len(processes)


# processes
fcfs_processes = [{'arrival': 0, 'burst': 4}, {'arrival': 1, 'burst': 3}, {'arrival': 2, 'burst': 1}]
sjf_processes = [{'arrival': 0, 'burst': 4}, {'arrival': 1, 'burst': 3}, {'arrival': 2, 'burst': 1}]
rr_processes = [{'arrival': 0, 'burst': 4}, {'arrival': 1, 'burst': 3}, {'arrival': 2, 'burst': 1}]
priority_processes = [{'arrival': 0, 'burst': 4, 'priority': 2}, {'arrival': 1, 'burst': 3, 'priority': 1}, {'arrival': 2, 'burst': 1, 'priority': 3}]

# running each algorithm
print("FCFS Avg Waiting Time:", fcfs(fcfs_processes))
print("SJF Avg Waiting Time:", sjf(sjf_processes))
print("Round Robin Avg Waiting Time:", round_robin(rr_processes, quantum=2))
print("Priority Scheduling Avg Waiting Time:", priority_scheduling(priority_processes))
