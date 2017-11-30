#include <stdio.h>
#include<math.h>
#include<stdlib.h>
int isprime(long int pnum)
{
	int i,p=1;
	long int sqrtpnum;
	sqrtpnum = sqrt(pnum);
	if (sqrtpnum < 2)
		return 1;
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
	}
	if(p==1)
		return 1;
	else
		return 0;
}


int main()
{
	long int i,nop=0,prevnop=0;
	long int num = 2000000,sumOfPrimes = 2; //since 2 is the lowest prime number
	//since even and odd occur at alternate positions and all even expect 2 are composite
	//iterating over only the odd values
 	//printf("\n Factors of the Given Number are:\n");
 	for (i = 3; i <= num; i=i+2)
 	{
 		if (isprime(i))
		{
			//printf("%ld\n",i);
			sumOfPrimes = sumOfPrimes + i;
		}
   	}
	printf("Sum of all primes less than %ld is :: \n",num);
	printf("%ld\n",sumOfPrimes);
}
