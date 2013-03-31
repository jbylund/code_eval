#include <fstream>
#include <iostream>
#include <sstream>
#include <stdio.h>
#include <stdlib.h>
//#include <string>
#include <string.h>
#include <vector>

using namespace std;

long long get_value(string & istring)
{
    long long sum = 0;
    char lstring[istring.length() + 1];
    strcpy(lstring, istring.c_str());
    char * pch = strtok(lstring,"+");
    char * endptr;
    while (pch != NULL)
    {
        sum += strtoull(pch,&endptr,10); // will this fail if things get too big
        pch = strtok (NULL, "+");
    }
    return sum;
}

void init_uglies(vector <bool> & is_uglyv)
{
    vector <int> small_primes(0);
    small_primes.push_back(2);
    small_primes.push_back(3);
    small_primes.push_back(5);
    small_primes.push_back(7);
    for(unsigned int i = 0; i < is_uglyv.size(); ++i)
    {
        for(unsigned int j = 0; j < small_primes.size(); ++j)
        {
            if(0 == i % small_primes[j])
            {
                is_uglyv[i] = true;
                break;
            }
        }
    }
}

bool is_ugly(vector <bool> & is_uglyv, long long inum)
{
    return is_uglyv[abs(inum % 210)];
}

class operation_digit
{
private:
    int operation;
    int value;
public:
    operation_digit(int ivalue);
    bool next();
    string get_val();
};

inline std::ostream & operator<<(std::ostream & str, operation_digit * v)
{
    str << v->get_val();
    return str;
}

operation_digit :: operation_digit(int ivalue)
{
    value = ivalue;
    operation = 0;
}

string operation_digit :: get_val()
{
    string mystring = "";
    switch (operation)
    {
        case 0:
            // mystring += "";
            break;
        case 1:
            mystring += "+-";
            break;
        case 2:
            mystring += "+";
            break;
    }
    mystring += (char)(value + 48);
    return mystring;
}

bool operation_digit::next()
{
    operation = (operation + 1) % 3;
    return (0 == operation); // if true need to call next on the next up
}

class digit_operator_string
{
//    private:
//        vector <operation_digit> idigit_array;
    public:
        vector <operation_digit * > idigit_array;
        digit_operator_string(string & istring);
        bool next();
        ~digit_operator_string(); //destructor

};

digit_operator_string::~digit_operator_string()
{
    for(unsigned int i = 0; i < idigit_array.size(); ++i)
        delete idigit_array[i];
}

inline std::ostream & operator<<(std::ostream & str, digit_operator_string * s)
{
    for(unsigned int i = 0; i < s->idigit_array.size(); ++i)
        str << s->idigit_array[i];
    return str;
}

bool digit_operator_string::next()
{
    int i = idigit_array.size() - 1;
    if(i < 1)
        return false;

    // while need to "carry"
    while(true == idigit_array[i]->next())
    {
        i -= 1;
        // don't put signs in front of the 0th digit
        if(i < 1)
            return false;
    }
    return true;
}

digit_operator_string::digit_operator_string(string & istring)
{
    for(unsigned int i = 0; i < istring.length(); ++i)
    {
        idigit_array.push_back(new operation_digit( (int) istring[i] - 48 ));
    }
}

int count_ugly_expressions(vector <bool> & is_uglyv, string & istring)
{
    digit_operator_string * digit_rep = new digit_operator_string(istring);
    int num_uglies = 0;
    stringstream mystream;
    string string_rep;
    long long value;
    do
    {
        mystream.clear();//clear any bits set
        mystream.str(std::string());
        mystream << digit_rep;
        string_rep = mystream.str();
        value = get_value(string_rep);
        num_uglies += (int) is_ugly(is_uglyv,value);
        //cout << digit_rep << "\t=>\t" << string_rep << "\t=\t" << value << endl;
    } while (digit_rep->next());
    delete(digit_rep);
    return num_uglies;
}

int main(int argc, char* argv[])
{
    if(argc == 0)
    {
        cout << "Program requires input.\n";
        return 1;
    }
    vector <bool> is_uglyv(210,false);
    init_uglies(is_uglyv);

    string line;
    ifstream file;
    file.open(argv[1]);
    while(getline(file, line))
    {
        if (line.length() == 0)
            continue; //ignore all empty lines
        else
        {
            //cout << line << "\t" << count_ugly_expressions(is_uglyv, line) << endl;
            cout << count_ugly_expressions(is_uglyv, line) << endl;
        }
    }
}
