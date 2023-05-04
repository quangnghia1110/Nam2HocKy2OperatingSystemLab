#include<stdio.h>
#include<stdlib.h>

// Khai bao struct de luu tru thon tin cua mot qua trinh
struct priority_preeptive
{
	int process_id;         // ID cua qua trinh
	int burst_time;         // Thoi gian thuc hien qua trinh
	int waiting_time;       // Thoi gian cho doi qua trinh
	int turnaround_time;    // Thoi gian hoan thanh qua trinh
	int arrive_time;		// Thoi gian den cua qua trinh
	int priority;			// Do uu tien
	int check;
} p[10];                   // Mang chua cac qua trinh

int main()
{
	int i, j, n, total_waiting_time = 0, total_turnaround_time = 0;
	printf("Priority Preeptive Scheduling...\n");
	printf("Enter the number of processes: ");// Nhap so luong qua trinh
	scanf("%d", &n);
	struct priority_preeptive temp;
    // Nhap thong tin cua tung qua trinh
	for(i = 0; i < n; i++)
	{
		p[i].process_id = i+1;
		printf("Arrival time of process %d: ", i+1);
        scanf("%d", &p[i].arrive_time); 
		printf("Burst time of process %d: ", i+1);
		scanf("%d", &p[i].burst_time);
		printf("Priority of process %d: ", i+1);
		scanf("%d", &p[i].priority);
	}
	if (p[0].arrive_time==0, p[1].arrive_time==0,p[2].arrive_time==0) 
	{
    	for(i = 0; i < n; i++)
		{
			for(j = i+1; j < n; j++)
			{
				if(p[i].priority > p[j].priority)
				{
					temp = p[i];
					p[i] = p[j];
					p[j] = temp;
				}
			}
		}
		p[0].waiting_time = 0;
    	p[0].turnaround_time = p[0].burst_time;
    	for(i=1;i<n;i++)
    	{	
        	p[i].waiting_time = p[i-1].waiting_time + p[i-1].burst_time + p[i-1].arrive_time - p[i].arrive_time;
        	p[i].turnaround_time = p[i].waiting_time + p[i].burst_time;
        	total_turnaround_time += p[i].turnaround_time;
        	total_waiting_time += p[i].waiting_time;
    	}
	    total_turnaround_time += p[0].turnaround_time;
	} 
	
	// Hien thi thong tin vua nhap va ket qua tinh duoc
	printf("\nProcess ID\tArrive Time\tBurst Time\tPriority\tTurnaround Time\tWaiting Time\n");
	for(i = 0; i < n; i++)
	{
		printf("%d\t\t%d\t\t%d\t\t%d\t\t%d\t\t%d\n", p[i].process_id, p[i].arrive_time,p[i].burst_time,p[i].priority, p[i].turnaround_time, p[i].waiting_time);
	}
	printf("\nTotal waiting time: %d", total_waiting_time);
	printf("\nAverage waiting time: %f", (float) total_waiting_time / n);
	printf("\nTotal turnaround time: %d", total_turnaround_time);
	printf("\nAverage turnaround time: %f", (float) total_turnaround_time / n);
	return 0;
}

