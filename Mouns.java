import java.util.Scanner;


public class Mouns {

	public static void main(String[] args) {
		int n,j=1;
		Scanner sc=new Scanner(System.in);
		System.out.println("Number of elements to be taken :");
		n=sc.nextInt();
		int arr[]=new int[n];
		for(int i=0;i<n;i++)
		{
			System.out.println("Enter the "+j+" element :");
			arr[i]=sc.nextInt();
			j++;
		}
		
		for(int i=0;i<n-1;i++)
		{
			for(int k=i+1;k<n;k++)
			{
				if(arr[i]==arr[k])
				{
					System.out.println("The repeating element is "+arr[i]);
					break;
				}
			}break;
		}
		sc.close();
	}
}
