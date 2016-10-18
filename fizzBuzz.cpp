#include <iostream.h>
#include <string.h>

using namespace std;

int main(){

	int n;
	cout << "What number would you like to play FizzBuzz to?";
	cin >> n;
	string result;
	
	for(int x = 1; x <= n; x++){
		result = "";
		if(x % 3 == 0){
			result += "Fizz";
		}
		if(x % 5 == 0){
			result += "Buzz";
		}
		if(result == "" ){
			result = (to_string(x));
		}
		cout << (result + "\n");
	}
	return 0;
}