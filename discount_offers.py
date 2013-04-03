#!/usr/bin/python
# Makes use of the Munkres library from https://github.com/bmc/munkres
# for the implementation of the Hungarian Algorithm.

import sys,itertools,string

#========================================================================
# Begin Munkres Library:

#    This software is released under a BSD license, adapted from
#    <http://opensource.org/licenses/bsd-license.php>

#    Copyright (C) 2008 Brian M. Clapper
#    Modified 4/2013 for use in CodeEval "Discount Offers" Challenge
#    By Joseph Bylund
#    All rights reserved.

#    Redistribution and use in source and binary forms, with or without
#    modification, are permitted provided that the following conditions are met:

#    * Redistributions of source code must retain the above copyright notice,
#      this list of conditions and the following disclaimer.

#    * Redistributions in binary form must reproduce the above copyright notice,
#      this list of conditions and the following disclaimer in the documentation
#      and/or other materials provided with the distribution.

#    * Neither the name "clapper.org" nor the names of its contributors may be
#      used to endorse or promote products derived from this software without
#      specific prior written permission.

#    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
#    AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
#    IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
#    ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
#    LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
#    CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
#    SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
#    INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
#    CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
#    ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
#    POSSIBILITY OF SUCH DAMAGE.

class Munkres:
    # Calculate the Munkres solution to the classical assignment problem.
    # See the module documentation for usage.
    def __init__(self):
        self.C = None
        self.row_covered = []
        self.col_covered = []
        self.n = 0
        self.Z0_r = 0
        self.Z0_c = 0
        self.marked = None
        self.path = None

    def compute(self, cost_matrix):
    # Compute the indexes for the lowest-cost pairings between rows and
    # columns in the database. Returns a list of (row, column) tuples
    # that can be used to traverse the matrix.
    # :Parameters:
    # cost_matrix : list of lists
    # The cost matrix, must be square.
    # **WARNING**: This code handles only square matrices.
    # :rtype: list
    # :return: A list of ``(row, column)`` tuples that describe the lowest
    # cost path through the matrix
        self.C = cost_matrix
        self.n = len(self.C)
        self.original_length = len(cost_matrix)
        self.original_width = len(cost_matrix[0])
        self.row_covered = [False for i in range(self.n)]
        self.col_covered = [False for i in range(self.n)]
        self.Z0_r = 0
        self.Z0_c = 0
        self.path = self.__make_matrix(self.n * 2, 0)
        self.marked = self.__make_matrix(self.n, 0)
        done = False
        step = 1
        steps = { 1 : self.__step1,
                  2 : self.__step2,
                  3 : self.__step3,
                  4 : self.__step4,
                  5 : self.__step5,
                  6 : self.__step6 }
        while not done:
            try:
                func = steps[step]
                step = func()
            except KeyError:
                done = True
        # Look for the starred columns
        results = []
        for i in range(self.original_length):
            for j in range(self.original_width):
                if self.marked[i][j] == 1:
                    results += [(i, j)]
        return results

    def __copy_matrix(self, matrix):
        # Return an exact copy of the supplied matrix
        return copy.deepcopy(matrix)

    def __make_matrix(self, n, val):
        # Create an *n*x*n* matrix, populating it with the specific value.
        matrix = []
        for i in range(n):
            matrix += [[val for j in range(n)]]
        return matrix

    def __step1(self):
        # For each row of the matrix, find the smallest element and
        # subtract it from every element in its row. Go to Step 2.
        C = self.C
        n = self.n
        for i in range(n):
            minval = min(self.C[i])
            # Find the minimum value for this row and subtract that minimum
            # from every element in the row.
            for j in range(n):
                self.C[i][j] -= minval
        return 2

    def __step2(self):
        # Find a zero (Z) in the resulting matrix. If there is no starred
        # zero in its row or column, star Z. Repeat for each element in the
        # matrix. Go to Step 3.
        n = self.n
        for i in range(n):
            for j in range(n):
                if (self.C[i][j] == 0) and \
                   (not self.col_covered[j]) and \
                   (not self.row_covered[i]):
                    self.marked[i][j] = 1
                    self.col_covered[j] = True
                    self.row_covered[i] = True
        self.__clear_covers()
        return 3

    def __step3(self):
        # Cover each column containing a starred zero. If K columns are
        # covered, the starred zeros describe a complete set of unique
        # assignments. In this case, Go to DONE, otherwise, Go to Step 4.
        n = self.n
        count = 0
        for i in range(n):
            for j in range(n):
                if self.marked[i][j] == 1:
                    self.col_covered[j] = True
                    count += 1
        if count >= n:
            step = 7 # done
        else:
            step = 4
        return step

    def __step4(self):
        # Find a noncovered zero and prime it. If there is no starred zero
        # in the row containing this primed zero, Go to Step 5. Otherwise,
        # cover this row and uncover the column containing the starred
        # zero. Continue in this manner until there are no uncovered zeros
        # left. Save the smallest uncovered value and Go to Step 6.
        step = 0
        done = False
        row = -1
        col = -1
        star_col = -1
        while not done:
            (row, col) = self.__find_a_zero()
            if row < 0:
                done = True
                step = 6
            else:
                self.marked[row][col] = 2
                star_col = self.__find_star_in_row(row)
                if star_col >= 0:
                    col = star_col
                    self.row_covered[row] = True
                    self.col_covered[col] = False
                else:
                    done = True
                    self.Z0_r = row
                    self.Z0_c = col
                    step = 5
        return step

    def __step5(self):
    # Construct a series of alternating primed and starred zeros as
    # follows. Let Z0 represent the uncovered primed zero found in Step 4.
    # Let Z1 denote the starred zero in the column of Z0 (if any).
    # Let Z2 denote the primed zero in the row of Z1 (there will always
    # be one). Continue until the series terminates at a primed zero
    # that has no starred zero in its column. Unstar each starred zero
    # of the series, star each primed zero of the series, erase all
    # primes and uncover every line in the matrix. Return to Step 3
        count = 0
        path = self.path
        path[count][0] = self.Z0_r
        path[count][1] = self.Z0_c
        done = False
        while not done:
            row = self.__find_star_in_col(path[count][1])
            if row >= 0:
                count += 1
                path[count][0] = row
                path[count][1] = path[count-1][1]
            else:
                done = True
            if not done:
                col = self.__find_prime_in_row(path[count][0])
                count += 1
                path[count][0] = path[count-1][0]
                path[count][1] = col
        self.__convert_path(path, count)
        self.__clear_covers()
        self.__erase_primes()
        return 3

    def __step6(self):
    # Add the value found in Step 4 to every element of each covered
    # row, and subtract it from every element of each uncovered column.
    # Return to Step 4 without altering any stars, primes, or covered
    # lines.
        minval = self.__find_smallest()
        for i in range(self.n):
            for j in range(self.n):
                if self.row_covered[i]:
                    self.C[i][j] += minval
                if not self.col_covered[j]:
                    self.C[i][j] -= minval
        return 4

    def __find_smallest(self):
    # Find the smallest uncovered value in the matrix.
        minval = sys.maxint
        for i in range(self.n):
            for j in range(self.n):
                if (not self.row_covered[i]) and (not self.col_covered[j]):
                    if minval > self.C[i][j]:
                        minval = self.C[i][j]
        return minval

    def __find_a_zero(self):
    # Find the first uncovered element with value 0
        row = -1
        col = -1
        i = 0
        n = self.n
        done = False
        while not done:
            j = 0
            while True:
                if (self.C[i][j] == 0) and \
                   (not self.row_covered[i]) and \
                   (not self.col_covered[j]):
                    row = i
                    col = j
                    done = True
                j += 1
                if j >= n:
                    break
            i += 1
            if i >= n:
                done = True
        return (row, col)

    def __find_star_in_row(self, row):
    # Find the first starred element in the specified row. Returns
    # the column index, or -1 if no starred element was found.
        col = -1
        for j in range(self.n):
            if self.marked[row][j] == 1:
                col = j
                break
        return col

    def __find_star_in_col(self, col):
    # Find the first starred element in the specified row. Returns
    # the row index, or -1 if no starred element was found.
        row = -1
        for i in range(self.n):
            if self.marked[i][col] == 1:
                row = i
                break
        return row

    def __find_prime_in_row(self, row):
    # Find the first prime element in the specified row. Returns
    # the column index, or -1 if no starred element was found.
        col = -1
        for j in range(self.n):
            if self.marked[row][j] == 2:
                col = j
                break
        return col

    def __convert_path(self, path, count):
        for i in range(count+1):
            if self.marked[path[i][0]][path[i][1]] == 1:
                self.marked[path[i][0]][path[i][1]] = 0
            else:
                self.marked[path[i][0]][path[i][1]] = 1

    def __clear_covers(self):
        # Clear all covered matrix cells
        for i in range(self.n):
            self.row_covered[i] = False
            self.col_covered[i] = False

    def __erase_primes(self):
        # Erase all prime markings
        for i in range(self.n):
            for j in range(self.n):
                if self.marked[i][j] == 2:
                    self.marked[i][j] = 0

# End Munkres library
#========================================================================

def num_vowels(istring):
    return len([letter for letter in istring.lower() if letter in vowels])

def num_consonants(istring):
    return len([letter for letter in istring.lower() if letter in consonants])

def num_letters(istring):
    return len([letter for letter in istring.lower() if letter in letters])

def ss_score(customer, product):
    score = 0
    letters_product  = num_letters(product)
    letters_customer = num_letters(customer)
    if(0 == letters_product % 2):
        score = num_vowels(customer) * 1.5
    else:
        score = num_consonants(customer)
    b = min(letters_product,letters_customer)
    i = 2
    while(i**2 <= b):
        if(0 == letters_product % i):
            if(0 == letters_customer % i):
                return score*1.5
        i += 1
    a = max(letters_product,letters_customer)
    if(a % b == 0):
        return score*1.5
    return score

def best_possible_score(customers,products):
    score_dict = dict()
    for customer in customers:
        for product in products:
            key = tuple([customer,product])
            score_dict[key] = ss_score(customer, product)

    # no value could possibly be higher than this
    max_cost = max(map(len,customers)) * 1.5 * 1.5
    matrix_size = max(len(customers),len(products))
    cost_matrix = list()
    for customer_num in xrange(matrix_size):
        cost_matrix.append(list())
        for product_num in xrange(matrix_size):
            if(customer_num >= len(customers)):
                cost_matrix[-1].append(max_cost)
            elif(product_num >= len(products)):
                cost_matrix[-1].append(max_cost)
            else:
                key = tuple([customers[customer_num],products[product_num]])
                cost_matrix[-1].append(max_cost - score_dict[key])

    m = Munkres()
    indexes = m.compute(cost_matrix)

    score = 0
    for i in indexes:
        cust_index = i[0]
        if(cust_index >= len(customers)):
            continue
        prod_index = i[1]
        if(prod_index >= len(products)):
            continue
        customer = customers[cust_index]
        product  = products[prod_index]
        key = tuple([customer,product])
        score += score_dict[key]
    return score

letters = set(list(string.ascii_lowercase))
vowels = set(list("aeiouy"))
consonants = set(list(string.ascii_lowercase))
consonants -= vowels
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.rstrip()
    if(0 == len(test)):
        continue
    customers = test.split(";")[0].split(",")
    products  = test.split(";")[1].split(",")
    print '{0:.2f}'.format(best_possible_score(customers, products))
test_cases.close()
