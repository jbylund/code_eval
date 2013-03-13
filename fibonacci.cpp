#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <math.h>

using namespace std;

int get_nth_fibonacci_number(int n)
{
    switch(n)
    {
        case 1:
            return 1;
            break;
        case 2:
            return 1;
            break;
        default:
            return get_nth_fibonacci_number(n-1) + get_nth_fibonacci_number(n-2);
    }
}

int fib_direct(int n)
{
    double sqrt_five = sqrt(5);
    double phi = (1 + sqrt_five)/2.0;
    double psi = (1 - sqrt_five)/2.0;
    return (int)((pow(phi,n) - pow(psi,n))/sqrt_five);
}

int main(int argc, char* argv[])
{
    ifstream input_file;
    input_file.open(argv[1]);
    string line;
    int index;
    while(input_file.good())
    {
        getline(input_file,line);
        if(0 == line.length())
            continue;
        index = atoi(line.c_str());
        //cout << get_nth_fibonacci_number(index) << endl;
        cout << fib_direct(index) << endl;
    }
    return 0;
}
