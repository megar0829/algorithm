import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int N = scan.nextInt();
		int count = 0;
		int check = 0;
		
		for(int i=0; i<=N; i++) {
			check = i;
			while(check != 0) {
				if(check%10 == 3 || check%10 == 6 || check%10 == 9) 
					count ++;
				check /= 10;
			}
		}
		System.out.println(count);
		scan.close();
	}
}