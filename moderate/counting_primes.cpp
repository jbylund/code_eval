#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <vector>
#include <math.h>

using namespace std;

unsigned int product(vector <unsigned int> & ivector)
{
    unsigned int ans = 1;
    for(unsigned int i = 0; i < ivector.size(); ++i)
    {
        ans *= ivector[i];
    }
    return ans;
}

int max(vector <unsigned int> ivector)
{
    unsigned int ans = ivector[0];
    for(unsigned int i = 1; i < ivector.size(); ++i)
    {
        if(ivector[i] > ans)
            ans = ivector[i];
    }
    return ans;
}

void primes_with_wheel(unsigned int limit, vector <unsigned int> & primes)
{
    primes.clear();

    // populate the list of primes with the first few primes
    // this is used to make the wheel
    primes.push_back(2);
    primes.push_back(3);
    primes.push_back(5);
    primes.push_back(7);
    primes.push_back(11);
    primes.push_back(13);
    primes.push_back(17);

    unsigned int step = product(primes);
    while(primes.size() > 2 && step*10 > limit)
    {
        primes.pop_back();
        step = product(primes);
    }

    vector <bool> rel_prime_remainders(step,true);

    // find valid remainders
    for(unsigned int i = 1; i < primes.size(); ++i) // loop over the primes, start with 3
    {
        for(unsigned int j = primes[i]; j < rel_prime_remainders.size(); j += 2*primes[i]) // kill the multiples of the prime
        {
            rel_prime_remainders[j] = false;
        }
    }

    // push the valid remainders onto a vector
    vector <int> v_remainders(0);
    for(unsigned int i = 1; i < rel_prime_remainders.size(); i = i + 2)
    {
        if(rel_prime_remainders[i])
        {
            v_remainders.push_back(i);
        }
    }

    // do a wheel
    // start with all false, as most things are
    vector<bool> is_prime(limit + 1, false); // start with false as the majority are
    unsigned int index = 0;
    for(unsigned int i = 0; i < is_prime.size(); i = i + step) // this is the step, or circle of the ring
    {
        // include things on this ring for all spokes
        for(unsigned int j = 0; j < v_remainders.size(); j++) // loop over remainders/spokes
        {
            index =  i + v_remainders[j];
            if(index >= is_prime.size())
                break;
            is_prime[index] = true;
        }
    }

    // include primes on inner ring, the rest of the ring is canceled out
    for(unsigned int i = 0; i < primes.size(); ++i)
    {
        is_prime[primes[i]] = true;
    }

    // start at 2+highest known prime
    // if prime
    //    remove all multiples
    //    and add to list of primes
    for(unsigned int i = max(primes) + 2; i*i < limit; i = i + 2)
    {
        if(false == is_prime[i])
        {
            continue;
        }
        else
        {
            primes.push_back(i);
            for(unsigned int j = i*i; j <= limit; j = j + 2 * i)
            {
                is_prime[j] = false;
            }
        }
    }

    // now start add in all the primes between sqrt(limit) and limit
    unsigned int sqrt_limit = (int) sqrt(limit);
    unsigned int max_prime = primes[primes.size()-1];
    for(unsigned int j = sqrt_limit/step; j * step < limit; ++j) // this is looping by step
    {
        for(unsigned int i = 0; i < v_remainders.size(); ++i) // loop over remainders
        {
            index =  j*step + v_remainders[i];
            if(index >= is_prime.size())
                break;
            if(index <= max_prime)
                continue;
            if(is_prime[index])
            {
                primes.push_back(index);
            }
        }
    }
}

int main(int argc, char* argv[])
{
    ifstream input_file;
    input_file.open(argv[1]);
    string line;
    vector <unsigned int> n(0);
    vector <unsigned int> m(0);
    while(input_file.good())
    {
        getline(input_file,line);
        if(0 == line.length())
            continue;
        n.push_back(atoi(line.c_str()));
        m.push_back(atoi(line.substr(line.find(",")+1).c_str()));
    }

    vector <unsigned int> primes(0);
    primes_with_wheel(max(m),primes);
    for(unsigned int i = 0; i < m.size(); ++i)
    {
        unsigned int count = 0;
        unsigned int j = 0;
        while(primes[j] < n[i])
            ++j;
        while(j+count < primes.size() && primes[j+count] <= m[i])
        {
            ++count;
        }
        cout << count << endl;
    }

    return 0;
}
