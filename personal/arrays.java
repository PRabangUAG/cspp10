
public class Arrays {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner list=new Scanner(System.in);
		System.out.println("How many items would you like on your list?");
		int v=list.nextInt();
		String[] item=new String[v];
		for(int k=0; k<v; k++){
 System.out.println("What would you like on your list?");
	item[k]=list.next();
    

	
	}
		for(int k=0; k<v; k++){
			System.out.println(item[k]);
			
		}
		}

}


//["gb"]["gh"]["pl"]["mk"]


//int[] t=new int[20];
//t[17]=4;
//System.out.print(t[17]);
//String[] eggs= new String[9];
//eggs[0]="ghjkg";
//System.out.print("");


