import java.util.Scanner;

public class tic_tac_toe {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Scanner test=new Scanner(System.in);
		char [][] f=new char [3][3];
		boolean end=false;

		for(int k=0; k<3; k++){
			for(int c=0; c<3; c++){
				f[k][c]='_';

			}



		}


		for(int i=0; i<5; i++){



			System.out.println("0 would be first row, 1 would be middle row, 2 would be last row");
			System.out.println("Player one go");
			System.out.println("row? (0-2)");
			int l=test.nextInt();
			System.out.println("column? (0-2) ");
			int p=test.nextInt();
			if(f[l][p]=='x' ||f[l][p]=='o'){
				System.out.println("Dont Cheat");
				System.out.println("");


			}
			else{
				f[l][p]='x';	
				if(f[0][0]=='x' && f[0][1]=='x'  && f[0][2]=='x'){ 
					end=true;
					System.out.println("Player 1 wins");}
				if (f[1][0]=='x' && f[1][1]=='x' && f[1][2]=='x'){
					end=true;
					System.out.println("Player 1 wins");}
				if (f[2][0]=='x' && f[2][1]=='x' && f[2][2]=='x'){
					end=true;
					System.out.println("Player 1 wins");}
				if (f[0][0]=='x' && f[1][0]=='x' && f[2][0]=='x'){
					end=true;
					System.out.println("Player 1 wins");}
				if (f[0][1]=='x' && f[1][1]=='x' && f[2][1]=='x'){
					end=true;
					System.out.println("Player 1 wins");}
				if (f[0][2]=='x' && f[1][2]=='x' && f[2][2]=='x'){
					end=true;
					System.out.println("Player 1 wins");}
				if (f[0][0]=='x' && f[1][1]=='x' && f[2][2]=='x'){
					end=true;
					System.out.println("Player 1 wins");}
				if (f[0][2]=='x' && f[1][1]=='x' && f[2][0]=='x'){
					end=true;`
					System.out.println("Player 1 wins");}
				//if (f[1][0]!='_' && f[1][1]!='_' && f[1][2]!='_'){
				if(f[0][0]!='_' && f[0][1]!='_'  && f[0][2]!='_' &&
						f[1][0]!='_' && f[1][1]!='_' && f[1][2]!='_' &&
						f[2][0]!='_' && f[2][1]!='_' && f[2][2]!='_' &&
						f[0][0]!='_' && f[1][0]!='_' && f[2][0]!='_' &&
						f[1][0]!='_' && f[1][1]!='_' && f[1][2]!='_'){
					end=true;
					System.out.println("tie!");}

			}

			for(int x=0; x<3; x++){

				for(int j=0; j<3; j++){
					System.out.print(f[x][j]);
					System.out.print(f[x][j]);
					System.out.print(f[x][j]);
					System.out.print(" ");

				} 
				System.out.println("");
			}
			if(end==false){




				System.out.println(" ");
				System.out.println("Player two go (0-2) ");
				System.out.println("row?");
				int numoneforp2=test.nextInt();
				System.out.println("column?");
				int numtwoforp2=test.nextInt();
				if(f[numoneforp2][numtwoforp2]=='x'||f[numoneforp2][numtwoforp2]=='o'){
					System.out.print("Dont Cheat");
					System.out.println("");
				} 
				else{
					f[numoneforp2][numtwoforp2]='o';
					if(f[0][0]=='o' && f[0][1]=='o' && f[0][2]=='o'){
						end=true;
						System.out.println("Player 2 wins");}
					if (f[1][0]=='o' && f[1][1]=='o' && f[1][2]=='o'){
						end=true;
						System.out.println("Player 2 wins");}
					if (f[2][0]=='o' && f[2][1]=='o' && f[2][2]=='o'){
						end=true;
						System.out.println("Player 2 wins");}
					if (f[0][0]=='o' && f[1][0]=='o' && f[2][0]=='o'){
						end=true;
						System.out.println("Player 2 wins");}
					if (f[0][1]=='o' && f[1][1]=='o' && f[2][1]=='o'){
						end=true;
						System.out.println("Player 2 wins");}
					if (f[0][2]=='o' && f[1][2]=='o' && f[2][2]=='o'){
						end=true;
						System.out.println("Player 2 wins");}
					if (f[0][0]=='o' && f[1][1]=='o' && f[2][2]=='o'){
						end=true;
						System.out.println("Player 2 wins");}
					if (f[0][2]=='o' && f[1][1]=='o' && f[2][0]=='o'){
						end=true;
						System.out.println("Player 2 wins");}
					if(f[0][0]!='_' && f[0][1]!='_'  && f[0][2]!='_' &&
							f[1][0]!='_' && f[1][1]!='_' && f[1][2]!='_' &&
							f[2][0]!='_' && f[2][1]!='_' && f[2][2]!='_' &&
							f[0][0]!='_' && f[1][0]!='_' && f[2][0]!='_' &&
							f[1][0]!='_' && f[1][1]!='_' && f[1][2]!='_'){
						end=true;
						System.out.println("tie!");}
				}

				for(int x=0; x<3; x++){

					for(int j=0; j<3; j++){
						System.out.print(f[x][j]);
						System.out.print(f[x][j]);
						System.out.print(f[x][j]);
						System.out.print(" ");

					}
					System.out.println(" ");
				}
			}
			if(end==true){
				i=5;
			}

		}






	}
}
