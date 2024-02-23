""" Working Hard, or hardly working? """
# Name 1: Sanjitha Venkata
# EID 1: sv28325

# Name 2: Swati Misra
# EID 2: SM83264

import time

# Purpose: Determines how many lines of code will be written
#          before the coder crashes to sleep.
# Input: lines_before_coffee - how many lines of code to write before coffee
#        prod_loss - factor for loss of productivity after coffee
# Output: returns the number of lines of code that will be written
#         before the coder falls asleep
def sum_series(lines_before_coffee, prod_loss):
    """sums series"""
    # print(lines_before_coffee)
    current_prod_loss= 1
    num = 1
    line_count = lines_before_coffee
    while num!=0:
        # print("start", num)
        num = lines_before_coffee // (prod_loss**current_prod_loss)
        # print(num)
        line_count += num
        # print(line_count)
        # print(prod_loss)
        # print()
        current_prod_loss+=1
        # prod_loss**=current_prod_loss
        # print(num)
        if num==0:
            return line_count
    return line_count
# sum_series(20,2)

# Purpose: Uses a linear search to find the initial lines of code to
#          write before the first cup of coffee, so that the coder
#          will complete the total lines of code before sleeping AND
#          get to have coffee as soon as possible.
# Input: total_lines - lines of code that need to be written
#        prod_loss - factor for loss of productivity after each coffee
# Output: returns the initial lines of code to write before coffee and
#         the number of calls to sum_series as a tuple
def linear_search(total_lines, prod_loss):
    """searches linearly"""
    counter=0
    num = 0
    for i in range(1, total_lines+1):
        num = sum_series(i, prod_loss)
        counter+=1
        if num >= total_lines:
            return (i,counter)
    return (i, counter)


# Purpose: Uses a binary search to find the initial lines of code to
#          write before the first cup of coffee, so that the coder
#          will complete the total lines of code before sleeping AND
#          get to have coffee as soon as possible.
# Input: total_lines - lines of code that need to be written
#        prod_loss - factor for loss of productivity after each coffee
# Output: returns the initial lines of code to write before coffee and
#         the number of calls to sum_series as a tuple
def binary_search(total_lines, prod_loss):
    """searches binarily"""
    counter=0
    num=0
    mid=0
    left, right = 0, total_lines
    while left <= right:
        # print(left, right, mid)
        mid = (left + right) // 2
        num = sum_series(mid, prod_loss)
        counter+=1

        if num==total_lines:
            return(mid, counter)

        if num>total_lines:
            right=mid-1
            num_minus_one=sum_series(mid-1,prod_loss)
            counter+=1
            if num_minus_one<total_lines:
                return(mid,counter)
        elif num<total_lines:
            left=mid+1
        else:
            return(mid,counter)
    return(mid,counter)


    #     if num > total_lines:
    #         right = mid-1
    #     elif num < total_lines:
    #         left = mid + 1
    #     else:
    #         return (mid, counter)
    # return (mid, counter)

def main():
    """main method"""

    num_cases = int(input())

    #Iterate for the number of test cases
    for i in range(num_cases):

        # read one line for one case
        #Replace this line with reading next line from stdin (input redirection or terminal)
        #line = "300 2"
        line = input()
        data = line.split()
        total_lines = int(data[0])  # total number of lines of code
        prod_loss = int(data[1])  # read productivity loss factor

        print("=====> Case #", i + 1)

        # Binary Search
        start = time.time()
        print("Binary Search:")
        lines, count = binary_search(total_lines, prod_loss)
        print("Ideal lines of code before coffee:", lines)
        print("sum_series called", count, "times")
        finish = time.time()
        binary_time = finish - start
        print(f"Elapsed Time: {binary_time:0.8f} seconds")
        print()

        # Linear Search
        start = time.time()
        print("Linear Search:")
        lines, count = linear_search(total_lines, prod_loss)
        print("Ideal lines of code before coffee:", lines)
        print("sum_series called", count, "times")
        finish = time.time()
        linear_time = finish - start
        print(f"Elapsed Time: {linear_time:0.8f} seconds")
        print()

        # Comparison
        comparison = linear_time / binary_time if binary_time else 1
        print(f"Binary Search was {comparison:0.1f}",
              "times faster.")
        print()
        print()


if __name__ == "__main__":
    main()
