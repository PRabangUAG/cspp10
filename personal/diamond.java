import java.util.Scanner;

public class diamond {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Scanner test=new Scanner(System.in);

		System.out.println("Size of triangle?");
		int s=test.nextInt();



		for(int v=0; v<s; v++){
			for(int h=0; h<s-v; h++){
				System.out.print("");
				System.out.print(" ");
			}
			for(int i=1; i<=v+1; i++){

				System.out.print("*");
				System.out.print(" ");
			}
			System.out.println("");




		}
		for(int k=1; k<=s; k++){	
			for(int i=1; i<=k+1; i++){


				System.out.print("");
				System.out.print(" ");
                

			}
			for(int r=0; r<=s-k-1; r++){
				System.out.print("*");
				System.out.print(" ");
			}
			System.out.println("");


			}


		}
	}
