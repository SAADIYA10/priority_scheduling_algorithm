# Priority Scheduling Algorithm in Python

 About the Project
This project implements the Priority CPU Scheduling Algorithm using Python. In this algorithm, processes are executed based on their priority values. The process with the highest priority is executed first.

Objectives
- Understand the Priority Scheduling Algorithm.
- Arrange processes based on priority.
- Calculate waiting time and turnaround time.
- Calculate average waiting time and average turnaround time.

 Technologies Used
- Python
- Operating Systems Concepts

 Algorithm
1. Initialize the processes, burst times, and priority values.
2. Arrange the processes according to their priority.
3. Calculate the waiting time for each process.
4. Calculate the turnaround time for each process.
5. Display the results.
6. Calculate the average waiting time and average turnaround time.

## 📖 Formulas

**Waiting Time (WT)**

WT = Completion time of previous processes − Previous processes' accumulated execution time, expressed as the sum of all preceding burst times when all arrival times are zero.

**Turnaround Time (TAT)**

TAT = Waiting Time + Burst Time.

How to Run
1. Install Python on your computer.
2. Save the program as `priority_scheduling.py`.
3. Open the terminal in the project folder.
4. Run the command:

```bash
python priority_scheduling.py
```

 Concepts Covered
- CPU Scheduling
- Priority Scheduling
- Waiting Time
- Turnaround Time
- Python Lists, Functions, and Sorting

 Conclusion
This project demonstrates how the Priority Scheduling Algorithm schedules processes based on their priority and calculates the waiting time, turnaround time, and their averages.

 Tags
`Python` `Priority Scheduling` `CPU Scheduling` `Operating Systems` `OS Practical`
