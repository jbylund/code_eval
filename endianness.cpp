#include <iostream>

using namespace::std;

int main()
{

//This is the preprocessor solution, in general, I'd go this way, but I know
//nothing about the system here, so we'll make an exception
//    if(__BYTE_ORDER__ == __ORDER_LITTLE_ENDIAN__)
//    {
//        cout << "LittleEndian" << endl;
//    }
//    else if(__BYTE_ORDER__ == __ORDER_BIG_ENDIAN__)
//    {
//        cout << "BigEndian" << endl;
//    }

    unsigned char bytearray[2] = { 1, 0 };

    if( *(short *) bytearray == 1 ) // cast the swaptest as a short
    {
        cout << "LittleEndian";
    }
    else
    {
        cout << "BigEndian";
    }

    return 0;
}
