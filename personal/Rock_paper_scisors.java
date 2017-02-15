		//0=rock
		//1=paper
		//2=scissors


import java.util.Random;
import java.util.Scanner;

public class Rock_paper_scisors {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner test=new Scanner(System.in);
		Random rps=new Random();
		boolean tie=true;
		System.out.println("Rock, Paper, Scissors?");
		String p1rps=test.next();
		int ainum=rps.nextInt(3);
		
		if(ainum==0){
			System.out.println("Rock");
		}
		if(ainum==1){
			System.out.println("Paper");
		}
		if(ainum==2){
			System.out.println("Scissors");
		}
		
		if(ainum==0 && p1rps.equalsIgnoreCase("Paper")){
			System.out.println("I'll hold that L");
			}
		if(ainum==1 && p1rps.equalsIgnoreCase("Paper")){
			System.out.println("Tie");
			}
		if(ainum==2 && p1rps.equalsIgnoreCase("Paper")){
			System.out.println("Take this L");
			}
		if(ainum==0 && p1rps.equalsIgnoreCase("Rock")){
			System.out.println("Tie");
			}
		if(ainum==1 && p1rps.equalsIgnoreCase("Rock")){
			System.out.println("Take this L");
			}
		if(ainum==2 && p1rps.equalsIgnoreCase("Rock")){
			System.out.println("I'll hold that L");
			}
		if(ainum==0 && p1rps.equalsIgnoreCase("Scissors")){
			System.out.println("Take this L");
			}
		if(ainum==1 && p1rps.equalsIgnoreCase("Scissors")){
			System.out.println("Take this L");
			}
		if(ainum==2 && p1rps.equalsIgnoreCase("Scissors")){
			System.out.println("Tie");
			}
		
	

	}

}