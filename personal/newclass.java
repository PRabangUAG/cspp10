import java.util.Scanner;

public class newclass {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Scanner test=new Scanner(System.in);

		System.out.println("Size of triangle at the base?");
		int s=test.nextInt();



		for(int v=0; v<s; v++){



        			for(int h=0; h<s-v; h++){
            				System.out.print(" ");
            			}
        			for(int p=1; p<=v+1; p++){
                        
        				System.out.print("*");
                        System.out.print(" ");
        			}
        			System.out.println("");
                     +
                     
                     
                     

            			

		}
	}
}
