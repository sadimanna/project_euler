#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main()
{
	int lenstr,nnum,i,j,n = 15,k=0;
	char data[50],num[2];
	long int grsum=0,temp = 0;
	FILE *file;
	file = fopen("pe18.txt","r");
	int **matrix = (int **)malloc(n*sizeof(int *));
	int **pathsum = (int **)malloc(n*sizeof(int *));
	if(file != NULL)
	{
		//parsing the data
		while(fgets(data,50,file)!=NULL)
		{
			lenstr = strlen(data);
			nnum = lenstr/3;
			matrix[k] = (int *)malloc(nnum*sizeof(int));
			pathsum[k] = (int *)malloc(nnum*sizeof(int));
			for(i=0;i<lenstr;i++)
			{
				if(data[i]==' '  || data[i]=='\n')
					matrix[k][(i-2)/3] = (data[i-2]-48)*10+(data[i-1]-48);
			}
			/*for(i=0;i<nnum;i++)
				printf("%d ",matrix[k][i]);
			printf("\n");*/
			k+=1;
		}
	}
	//printf("\n\n");
	//path finding
	pathsum[0][0]=matrix[0][0];
	for(i=0;i<n-1;i++)
	{
		temp = 0;
		for(k=0;k<=i;k++)
		{
			temp = 0;
			for(j=0;j<=1;j++)
			{
				temp = pathsum[i][k]+matrix[i+1][k+j];
				if(temp>pathsum[i+1][k+j])
					pathsum[i+1][k+j]=temp;
			}
		}
	}
	/*nnum=1;
	for(k=0;k<n;k++)
	{
		for(i=0;i<nnum;i++)
				printf("%d ",pathsum[k][i]);
		printf("\n");
		nnum+=1;
	}*/
	for(i=0;i<n;i++)
	{
		if(pathsum[n-1][i]>grsum)
			grsum = pathsum[n-1][i];
	}
	printf("Greatest Sum :: %ld\n",grsum);
	fclose(file);
}
