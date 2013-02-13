#include <iostream>
#include <fstream>
#include <stdlib.h>

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
        cout << get_nth_fibonacci_number(index) << endl;
    }
    return 0;
}
