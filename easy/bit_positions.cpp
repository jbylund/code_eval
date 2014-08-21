#include <fstream>
#include <iostream>
#include <sstream>
#include <stdlib.h>
#include <string>
#include <vector>

using namespace std;

bool bits_equal_num_pos1_pos2(int num, int pos1, int pos2)
{
    int pos1_mask = 1 << (pos1-1);
    int pos2_mask = 1 << (pos2-1);
    if((bool)(num & pos1_mask) == (bool)(num & pos2_mask))
    {
        cout << "true\n";
        return true;
    }
    else
    {
        cout << "false\n";
        return false;
    }
}

int main(int argc, char* argv[])
{
    ifstream input_file;
    input_file.open(argv[1]);
    string line,tmp;
    int n, p1, p2;
    while(input_file.good())
    {
        getline(input_file,line);
        if(0 == line.length())
            continue;
        istringstream liness(line);
        getline(liness,tmp,',');
        n = atoi(tmp.c_str());
        getline(liness,tmp,',');
        p1 = atoi(tmp.c_str());
        getline(liness,tmp,',');
        p2 = atoi(tmp.c_str());
        bits_equal_num_pos1_pos2(n,p1,p2);
    }
    return 0;
}
