#include<stdio.h>
#include<stdlib.h>
#include <bits/stdc++.h>
using namespace std;

struct rr
{
	int pno, priority, btime,sbtime,wtime,lst;
}p[10];

void Xuat(int n, int time) {
	printf("\n%d\t", time);
	for(int i=0;i<n;i++) {
		printf("%d\t", p[i].sbtime);
	}
	printf("\n");
}

int main()
{
	int pp=-1,ts,flag,count,ptm=0,i,n,twt=0,totttime=0;
	printf("enter no of processes:");
	scanf("%d",&n);
	printf("enter the time slice:");
	scanf("%d",&ts);
	printf("enter the burst time");
	for(i=0;i<n;i++)
	{
		printf("\nprocess%d\t",i+1);
		scanf("%d%d",&p[i].btime,&p[i].priority);
		p[i].wtime=p[i].lst=0;
		p[i].pno=i+1;
		p[i].sbtime=p[i].btime;
	}
	vector<bool> completed(n, false);
	printf("scheduling....\n");
	
	printf("\nTime\t");
	for (i=0;i<n;i++) {
		printf("P%d\t", i+1);
	}

	do
	{
		flag=0;
		int minB = INT_MAX;
		for (int i = 0; i < n; i++)
        {
            if (!completed[i])
            {
                if (p[i].priority < minB)
                {
                    minB = p[i].priority;
                }
            }
        }
		for(i=0;i<n;i++)
		{
			count=p[i].sbtime;
			if(minB == p[i].priority && count>0)
			{
				flag=-1;
				count=(count>=ts)?ts:count;
				//printf("\n process %d\t",p[i].pno);
				Xuat(n, ptm);
				//printf("from %d",ptm);
				ptm+=count;
				//printf("to %d",ptm);
				p[i].sbtime-=count;
				if (p[i].sbtime == 0)
					completed[i] = true;
				if(pp!=i)
				{
					pp=i;
					p[i].wtime+=ptm-p[i].lst-count;
					p[i].lst=ptm;
				}
			}	
		}	
	} while (flag);
	
	Xuat(n, ptm);
	for (i=0;i<n;i++) {
		twt += p[i].wtime;
		printf("%d ", p[i].wtime);
	}
	printf("\nAverage WaitTime: %f", double(twt/n));
}
	
