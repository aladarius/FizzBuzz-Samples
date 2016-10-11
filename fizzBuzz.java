public class fizzBuzz{
  public static void main(String[] args){

    String ans = " ";

    for(int x = 0; x++ < 100;){
      System.out.print("> ");
      if(x % 3 == 0 && x % 5 == 0){
        System.out.println("Fizz Buzz");
      } else if(x % 3 == 0){
        System.out.println("Fizz");
      } else if(x % 5 == 0){
        System.out.println("Buzz");
      } else{
        System.out.println(x);
      }
    }
  }
}
