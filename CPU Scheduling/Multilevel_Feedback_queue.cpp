#include <iostream>
#include <vector>
#include <queue>

using namespace std;

struct Process {
    int pid;
    int burstTime;
    int waitingTime;
    int turnaroundTime;
    int lst;
};

void calculateWaitingTime(vector<Process>& processes, vector<int>& quantumTimes, vector<int>& priorities) {
    int currentTime = 0;
    int n = processes.size();
    vector<int> remainingTime(n);
    for (int i = 0; i < n; i++) {
        remainingTime[i] = processes[i].burstTime;
    }

    // Create queues for each level
    vector<queue<int>> q(priorities.size());

    // Create a vector to track which processes are completed
    vector<bool> completed(n, false);

    // Start with the highest priority queue
    int currentLevel = 0;

    for (int i = 0; i < n; i++) {
        q[currentLevel].push(i);
    }

    while (true) {
        bool allCompleted = true;
        for (int i = 0; i < n; i++) {
            if (!completed[i]) {
                allCompleted = false;
            }
        }
        if (allCompleted) {
            break;
        }
        while (!q[currentLevel].empty()) {

            int currentProcess = q[currentLevel].front();
            q[currentLevel].pop();

            if (remainingTime[currentProcess] <= quantumTimes[currentLevel]) {
                currentTime += remainingTime[currentProcess];
                processes[currentProcess].waitingTime += currentTime - remainingTime[currentProcess] - processes[currentProcess].lst;
                remainingTime[currentProcess] = 0;
                completed[currentProcess] = true;
                processes[currentProcess].turnaroundTime = currentTime;
                processes[currentProcess].lst = currentTime;
            }
            else {
                currentTime += quantumTimes[currentLevel];
                remainingTime[currentProcess] -= quantumTimes[currentLevel];
                processes[currentProcess].waitingTime += currentTime - quantumTimes[currentLevel] - processes[currentProcess].lst;
                processes[currentProcess].lst = currentTime;
                q[currentLevel + 1].push(currentProcess);
            }
        }
        currentLevel++;
    }
}

int main() {
    int n;
    cout << "Enter the number of processes: ";
    cin >> n;
    vector<Process> processes(n);
    for (int i = 0; i < n; i++) {
        cout << "Enter the burst time and priority of process " << i + 1 << ": ";
        cin >> processes[i].burstTime;
        processes[i].pid = i + 1;
        processes[i].waitingTime = 0;
        processes[i].lst = 0;
    }

    vector<int> quantumTimes = { 17, 25, INT_MAX }; // Quantum times for each level
    vector<int> priorities = { 0, 1, 2 }; // Priorities for each level

    calculateWaitingTime(processes, quantumTimes, priorities);

    cout << "Process\tBurst Time\tWaiting Time\tTurnaround Time\n";
    for (int i = 0; i < n; i++) {
        cout << "P" << processes[i].pid << "\t" << processes[i].burstTime << "\t\t" << processes[i].waitingTime << "\t\t" << processes[i].turnaroundTime<< "\n";
    }
    int total_waiting_time = 0;
    int total_turnaround_time = 0;

    for (int i = 0; i < n; i++) {
        total_waiting_time += processes[i].waitingTime;
        total_turnaround_time += processes[i].turnaroundTime;
    }
    cout << "Total waiting time: " << total_waiting_time << "\n";
    cout << "Average waiting time: " << total_waiting_time / n << "\n";
    cout << "Total turnaround time: " << total_turnaround_time << "\n";
}

