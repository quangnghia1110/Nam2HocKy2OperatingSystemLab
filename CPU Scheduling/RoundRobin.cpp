#include<stdio.h>
#include<stdlib.h>

struct process {
    int process_id;
    int burst_time;
    int arrive_time;
    int remaining_time;
    int waiting_time;
    int turnaround_time;
} p[10];

int main() {
    int i, j, n, time_quantum, time = 0, completed = 0, total_waiting_time = 0, total_turnaround_time = 0;
    printf("Enter the number of processes: ");
    scanf("%d", &n);
    for(i = 0; i < n; i++)
	{
		p[i].process_id = i+1;
		printf("Arrive time of process %d: ", i+1);
		scanf("%d", &p[i].arrive_time);
		printf("Burst time of process %d: ", i+1);
		scanf("%d", &p[i].burst_time);
		p[i].remaining_time = p[i].burst_time;
	}
    printf("Enter the time quantum: ");
    scanf("%d", &time_quantum);
    // time luu tru thoi gian da thuc hien
    while (completed != n) {
        for (i = 0; i < n; i++) { //Tao vong lap de xet tat ca cac tien trinh
            if (p[i].remaining_time > 0) {// Kiem tra thoi gian con lai cua tung tien trinh
                if (p[i].remaining_time <= time_quantum) {//Thuc hien khi thoi gian con lai nho hon time_quantum
                    time += p[i].remaining_time;// time la bien luu tru cho tong thoi gian con lai cua no
                    p[i].remaining_time = 0;// Gan cho no bang 0 
                } else {
                    time += time_quantum;// time la bien luu tru cho tien trinh lon hon time_quantum
                    p[i].remaining_time -= time_quantum;
                }
                if (p[i].remaining_time == 0 ) {
                    completed++;
                    p[i].turnaround_time = time - p[i].arrive_time;
                    p[i].waiting_time = p[i].turnaround_time - p[i].burst_time;
                    total_waiting_time += p[i].waiting_time;
                    total_turnaround_time += p[i].turnaround_time;
                }
            }
        }
    }
    printf("\nProcess\tBurst Time\tArrival Time\tWaiting Time\tTurnaround Time\n");
    for (i = 0; i < n; i++) {
        printf("%d\t%d\t\t%d\t\t%d\t\t%d\n", p[i].process_id, p[i].burst_time, p[i].arrive_time, p[i].waiting_time, p[i].turnaround_time);
    }
    printf("\nAverage waiting time: %.2f\n", (float) total_waiting_time / n);
    printf("Average turnaround time: %.2f\n", (float) total_turnaround_time / n);
    return 0;
}
