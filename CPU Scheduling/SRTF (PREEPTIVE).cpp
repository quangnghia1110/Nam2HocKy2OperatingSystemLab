#include<stdio.h>
#include<stdlib.h>

// Khai bao struct de luu tru thon tin cua mot qua trinh
struct srtf
{
	int process_id; // ID cua qua trinh
	int burst_time; // Thoi gian thuc hien qua trinh
	int waiting_time; // Thoi gian cho doi qua trinh
	int turnaround_time; // Thoi gian hoan thanh qua trinh
	int remaining_time; // Thoi gian con lai cua qua trinh
	int arrive_time;
} p[10]; // Mang chua cac qua trinh

int main()
{
	int i, j, n, end, time,total_waiting_time = 0, total_turnaround_time = 0,completed=0, shortest;
	printf("SJF Scheduling...\n");
	printf("Enter the number of processes: ");// Nhap so luong qua trinh
	scanf("%d", &n);
	struct srtf temp;
	// Nhap arrive time va burst time cua tung qua trinh
	for(i = 0; i < n; i++)
	{
		p[i].process_id = i+1;
		printf("Arrive time of process %d: ", i+1);
		scanf("%d", &p[i].arrive_time);
		printf("Burst time of process %d: ", i+1);
		scanf("%d", &p[i].burst_time);
		
		p[i].remaining_time = p[i].burst_time;
	}
	for(time=0;completed!=n;time++)
    {
        shortest = -1;
        // Tim qua trinh co remaining time nho nhat
        for(i = 0; i < n; i++) 
        {
            if (p[i].remaining_time > 0 && p[i].arrive_time <=time &&(shortest == -1 || p[i].remaining_time < p[shortest].remaining_time)) 
            {
                shortest = i;
            }
        }
        // Cap nhat thong tin cho qua trinh tam thoi
        p[shortest].remaining_time--;
        // Neu qua trinh do hoan thanh thi tinh thoi gian va tang bien completed
        if (p[shortest].remaining_time == 0) 
        {
            completed++; // Cap nhat danh sach tien trinh da hoan thanh
            end=time+1; // Thoi gian da thuc hien truoc khi ket thuc +1
            p[shortest].turnaround_time = end - p[shortest].arrive_time; 
            p[shortest].waiting_time = end - p[shortest].burst_time - p[shortest].arrive_time;
            total_waiting_time += p[shortest].waiting_time;
            total_turnaround_time += p[shortest].turnaround_time;
        }
        // Toi day se quay lai vong lap tim tien trinh co remaining time nho nhat
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
	for(int i=0;i<n;i++)
    {
    	printf ("----------");
	}
	printf("\n");
	for(shortest=0;shortest<n;shortest++)
    {  
        printf("|  P%d(%d) ",p[shortest].process_id,p[shortest].burst_time);
        
    }
    printf("|\n");
    for(int i=0;i<n;i++)
    {
    	printf ("----------");
	}
    printf("\n");    
    printf("%d        ",p[shortest].turnaround_time);
    for(shortest=0;shortest<n;shortest++)
    {
    	printf("%d        ",p[shortest].turnaround_time+p[shortest].arrive_time);
	}
	return 0;
}
