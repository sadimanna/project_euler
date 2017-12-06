#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int isprime(long int pnum)
{
	int i,p=1;
	long int sqrtpnum;
	if (pnum >0)
	{
		sqrtpnum = sqrt(pnum);
		if (sqrtpnum < 2)
			return 1;
		else if (pnum%2 == 0)
			return 0;
		else
		{
			for(i=3;i<=sqrtpnum;i=i+2)	
			{
				if(pnum%i==0)
				{
					p=0;
					break;
				}
			}
		if(p==1)
			return 1;
		else
			return 0;
		}
	}
	else
		 return 0;	
}

int numPrime(long int a,long int b)
{
	int n=0;
	long int val,count = 0;
	while(1)
	{
		val = n*n + a*n + b;
		//printf("%ld ",val);	
		n++;
		if (isprime(val)==1)
			count++;
		else
			break;
	}
	return count;
}
int main()
{
	long int tempc,maxcount=0;
	long int a,b,ab,maxa,maxb;
	for(a=999;a>-1000;a--)
	{
		for(b=-1000;b<=1000;b++)
		{
			tempc = numPrime(a,b);
			if (tempc>maxcount)
			{
				maxcount = tempc;
				maxa = a;
				maxb = b;
			}
		}
	}
	printf("\nmaxcount :: %ld\n",maxcount);
	ab = maxa*maxb;
	printf("ab :: %ld\n",ab);
	/*tempc = numPrime(-79,1601);
	printf("numPrime :: %d\n",tempc);*/
}
