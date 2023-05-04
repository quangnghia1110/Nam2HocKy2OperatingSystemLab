#include<stdio.h>
#include<stdlib.h>

// Khai bao struct de luu tru thon tin cua mot qua trinh
struct sjf
{
	int process_id; // ID cua qua trinh
	int burst_time; // Thoi gian thuc hien qua trinh
	int arrive_time; //Thoi gian den qua trinh
	int waiting_time; // Thoi gian cho doi qua trinh
	int turnaround_time; // Thoi gian hoan thanh qua trinh
} p[10]; // Mang chua cac qua trinh

int main()
{
	int i, j, n, total_waiting_time = 0, total_turnaround_time = 0;
	struct sjf temp;
	printf("SJF Scheduling...\n");
	printf("Enter the number of processes: ");// Nhap so luong qua trinh
	scanf("%d", &n);
	// Nhap burst time cua tung qua trinh
	for(i = 0; i < n; i++)
	{
		p[i].process_id = i+1;
		printf("Arrival time of process %d: ", i+1);
        scanf("%d", &p[i].arrive_time); 
		printf("Burst time of process %d: ", i+1);
		scanf("%d", &p[i].burst_time);
	}
	for(int i=0;i<n;i++)
	{
		if(p[0].arrive_time==0&&p[1].arrive_time==0&&p[0].arrive_time==0)
		{
			// Sap xep cac qua trinh theo thu tu tang dan cua burst time
			for(i = 0; i < n; i++)
			{
				for(j = i+1; j < n; j++)
				{
					if(p[i].burst_time > p[j].burst_time)
					{
						temp = p[i];
						p[i] = p[j];
						p[j] = temp;
					}
				}
			}
			p[0].waiting_time = 0;
			p[0].turnaround_time = p[0].waiting_time + p[0].burst_time;
			// Tinh thoi gian cho doi va thoi gian hoan thanh cua tung qua trinh tinh tu qua trinh 1
			for(i = 1; i < n; i++)
			{
				p[i].waiting_time = p[i-1].waiting_time + p[i-1].burst_time;
				p[i].turnaround_time = p[i].waiting_time + p[i].burst_time;
				total_turnaround_time += p[i].turnaround_time;
				total_waiting_time += p[i].waiting_time;
			}
			total_turnaround_time += p[0].turnaround_time;
		}
		else
		{
			p[0].waiting_time=0;
			p[0].turnaround_time = p[0].waiting_time + p[0].burst_time; 
			// Tinh thoi gian cho doi va thoi gian hoan thanh cua tung qua trinh tinh tu qua trinh 1
			for(i = 1; i < n; i++)
			{
				p[i].waiting_time = p[i-1].waiting_time + p[i-1].burst_time - p[i].arrive_time +p[i-1].arrive_time ;
				p[i].turnaround_time = p[i].waiting_time + p[i].burst_time;
				total_waiting_time += p[i].waiting_time;
				total_turnaround_time += p[i].turnaround_time;
			}
			// Phai cong them tien trinh dau
			total_turnaround_time += p[0].turnaround_time;
			
		}
	}
	// Hien thi thong tin vua nhap va ket qua tinh duoc
	printf("\nProcess ID\tBurst Time\tTurnaround Time\tWaiting Time\n");
	for(i = 0; i < n; i++)
	{
		printf("%d\t\t%d\t\t%d\t\t%d\n", p[i].process_id, p[i].burst_time, p[i].turnaround_time, p[i].waiting_time);
	}
	printf("\nTotal waiting time: %d", total_waiting_time);
	printf("\nAverage waiting time: %f", (float) total_waiting_time / n);	
	printf("\nTotal turnaround time: %d", total_turnaround_time);
	printf("\nAverage turnaround time: %f", (float) total_turnaround_time / n);
	
	printf("\n\n\nGANTT CHART\n\n");
	for(int i=0;i<n;i++)
    {
    	printf ("----------");
	}
	printf("\n");
	for(i=0;i<n;i++)
    {  
        printf("|  P%d(%d) ",p[i].process_id,p[i].burst_time);
        
    }
    printf("|\n");
    for(int i=0;i<n;i++)
    {
    	printf ("----------");
	}
    printf("\n");
    printf("%d        ",p[0].waiting_time);
    
    printf("%d        ",p[0].turnaround_time);
    for(i=1;i<n;i++)
    {
    	printf("%d        ",p[i].turnaround_time+p[i].arrive_time);
	}
	return 0;
}
