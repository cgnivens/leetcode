# https://leetcode.com/problems/minimize-deviation-in-array/
from typing import List


"""
How to solve

[4, 1, 5, 20, 3]

How do we know we want to start with 20?
It's farthest away from the other values. First, let's brute force.

We know if a value is even we can divide it and if it's odd we can multiply it.

Start with the first item and divide:
[2, 1, 5, 20, 3]
Then the second
[2, 2, 5, 20, 3]

This starts to look like a tree problem

       val_1
  op         no-op


However, we need to catch a circular case here. Define the depth of a tree for each
element. That is, the maximum number of divisions that can occur until a value
is odd. An odd value can only be multiplied once until it is even.

val_1
no-op
op_1
...
op_n (sign flip)

A table of cases catches the sign flip. Now, the brute force way is to generate all
combinations of the values of the table and sum up the number of operations, as well
as get the deviation of the list


We generate a table like:

    # Moves     Value
    =======     =====
    0           4
    1           2
    2           1


For each value in nums. So to get the total number of moves, we simply sum
the values in position 0 on the tuples, and find the min/max in position 1, and minimize
the deviation from there.

def indefinite_iterator(it, *iterators):
    if iterators:
        yield from ((val, *chunk) for chunk in indefinite_iterator(*iterators) for val in it)
    else:
        yield from ((val,) for val in it)


Our recursive iterator hits a recursion error. No worries, we can fix it. Let's generate
a cartesian product using itertools' product rather than rolling our own
"""
from itertools import product
import sys
from operator import itemgetter


def get_even_values(val, min_=1):
    i = 0
    result = []

    while (not val % 2) and val > min_:
        result.append((i, val))
        val /= 2
        i += 1

    result.append((i, val))

    return result


def get_odd_values(val, max_=sys.maxsize):
    return [(i, val * (i + 1)) for i in range(2) if val * (i + 1) < max_]


class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        # This tabulates out all of the results
        max_val, min_val = max(nums), min(nums)
        min_dev = max_val - min_val

        value_table = [get_even_values(val, min_val) if not val % 2 else get_odd_values(val) for val in nums]

        # A naive way of generating all possible options here
        for move in product(*value_table):
            (_, min_val), (_, max_val) = min(move, key=itemgetter(1)), max(move, key=itemgetter(1))
            min_dev = min((max_val - min_val), min_dev)

        return min_dev


def run_tests():
    s = Solution()
    n = len(tests)

    for i, (case, result) in enumerate(tests, start=1):
        solution = s.minimumDeviation(case)
        try:
            assert solution == result
        except:
            raise RuntimeError(
                f"Bad result for the test case {i}:"
                "\n"
                f" case: {case}"
                "\n"
                f"Expected {result} but got {solution}"
            )
        else:
            print(f"Passed case {i} of {n}")

    print('All test cases passed')


tests = [
    ([1,2,3,4], 1),
    ([4,1,5,20,3], 3),
    ([2,10,8], 3),
    ([135834,836419,680692,782524,212751,344904,151812,854509,785665,711553,118450,225619,984089,927522,305363,221331,285523,359469,301309,352860,811160,121335,641379,610328,183633,637056,587508,513675,917257,376603,519307,560079,251287,281137,864540,818533,952649,821606,706074,876301,991947,827960,537837,244156,962031,202991,736005,789378,915307,170879,338873,464822,510193,576150,141686,170041,370531,246984,794898,603031,266890,369233,939309,639763,875624,160573,499240,262482,606556,339549,360057,942245,136356,118044,461767,345309,494942,567487,975821,344774,718333,942136,600779,998962,246095,370384,411034,494093,351765,914237,333122,962424,170428,784896,401346,974354,947835,869224,252495,905915,982928,109701,247308,847013,866577,273712,501449,153278,562836,664600,635005,686627,544873,259726,973403,474178,466904,771336,579599,530909,606286,583501,576873,416937,127372,976497,701599,606552,962481,195908,411251,804448,857390,182998,844085,175265,350947,122776,538026,258960,145100,709073,497166,139583,153253,759108,729462,462661,152063,594710,950094,453404,154555,130903,338490,982255,955181,936282,252912,921070,438173,925986,929970,334475,337409,983529,328188,117987,878252,788072,212328,535997,269357,517213,721062,227391,101266,627052,619136,908011,889483,275927,788124,988961,884221,880588,329607,319804,139993,454746,829225,123123,154944,433619,557438,546116,401699,863421,543349,126922,627007,470126,588376,486935,225634,483215,313258,108722,289667,679671,399926,497517,338331,501312,916667,522865,513887,654970,515745,327362,910088,124788,497728,415837,874326,962534,914517,679838,763867,617703,206020,783550,133018,493480,735601,376639,899263,497104,677995,137827,322159,246162,473984,237133,811471,143429,808764,675338,780159,207233,637064,629454,264526,116339,167983,621029,407748,920428,679244,932157,954625,936052,173418,282060,514009,900869,929253,727791,248500,883706,804943,806245,446152,794597,706132,617765,918897,891775,945278,248070,676359,700642,512573,879090,577253,435511,156318,190258,612323,405276,572466,481703,904515,901973,552105,118236,364573,900127,562128,531137,710881,129285,638289,898869,600938,378479,732708,924457,191293,618826,680650,289436,397799,439211,789907,298663,163073,438399,295869,806211,127959,287482,530997,348158,911773,949576,137778,733327,905729,422394,877362,194156,440333,336669,462485,855773,970880,158566,776539,860463,506148,814890,242237,165592,220969,220789,738983,730903,874618,740863,195583,709552,812699,405589,937667,770804,570062,139164,489824,494430,826883,737350,728875,215338,614815,518578,958160,416369,422173,453071,292793,482450,255833,688618,761946,296482,100060,234764,308164,950691,557939,963192,840582,944783,835038,699441,440631,484286,195850,916964,484508,113859,819947,466555,220356,738065,532830,244267,114041,123001,424183,487952,757475,886588,998746,706957,198712,448957,264074,662844,607071,302062,532759,786206,370587,284058,572443,114713,829229,331612,148055,890469,139251,171324,410015,546662,522916,765772,727170,104622,108519,663671,513993,639925,970552,331041,416971,989737,490147,883797,464859,746080,774731,655465,661698,762669,824830,762955,876027,460269,167023,624503,366088,332119,222393,109466,508526,415145,933186,183819,964796,416603,275600,977622,865800,928142,858765,436246,697066,958917,245251,565688,485446,312795,862625,849766,906197,105176,209920,209697,764113,134857,387478,886160,574838,783723,958913,871572,198576,497139,194978,679547,779890,220034,416661,388637,105291,564546,571791], 10)
]

if __name__ == "__main__":
    run_tests()
