#include <iostream>
#include <fstream>
#include <stdlib.h>

using namespace std;

int smallest_multiple_n_gt_x(int x,int n)
{
    int ans = n;
    while(ans < x)
    {
        ans += n;
    }
    return ans;
}

int main(int argc, char* argv[])
{
    ifstream input_file;
    input_file.open(argv[1]);
    string line;
    int x, n, comma_pos;
    while(input_file.good())
    {
        getline(input_file,line);
        if(0 == line.length())
            continue;
        comma_pos = line.find(",");
        x = atoi(line.substr(0,comma_pos).c_str());
        n = atoi(line.substr(comma_pos+1,line.length()).c_str());
        //index = atoi(line.c_str());
        cout << smallest_multiple_n_gt_x(x,n) << endl;
    }
    return 0;
}
