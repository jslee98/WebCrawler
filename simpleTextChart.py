"""This is a simple program demonstrating the use of Matplotlib.
   Adapted from the CSCI 203 final project in the fall 2016 semester,
   as well as other CSCI 203 final projects.
   Xiannong Meng
   2016-12-14
"""
import numpy as np
import matplotlib.pyplot as plt

DISPLAY_WORD_LIMIT = 20    # by default we display the top frequent words only

def createSortedList():
    """ createSortedList returns a list of tuples containing a common word
        and its count for testing displayChart().  The list is sorted on the
        counts from highest to lowest.  Returns a similar data structure as
        expected from text cloud analyzer. """

    # some artifially created word list and frequency
    """
    sortedList = [('spam', 10), ('page', 4), ('love', 3), ('text', 2),
                  ('number', 1), ('example', 1), ('cloud', 1)]
    """
    # 31 most common words on CSCI 203 home web page, frequencies are random
    sortedList = [('lab', 19), ('homework', 16), ('due', 13), ('monday', 12),
                  ('dana', 9), ('prof', 7), ('academic', 6), ('course', 5),
                  ('exam', 5), ('instructor', 5), ('oct', 4), ('nov', 4),
                  ('university', 4), ('sept', 4), ('submit', 4), ('work', 4),
                  ('guide', 4), ('student', 4), ('mwf', 3), ('policy', 3),
                  ('resource', 3), ('lecture', 3), ('understand', 3),
                  ('problem', 3), ('read', 3), ('principle', 3), ('python', 2),
                  ('practice', 2),  ('dishonest', 2),
                  ('specific', 2), ('computer', 2)]

    return sortedList

def displayChart(list):
    """ Displays bar chart using the Matplotlib library
        Input: sortedList - a list of tuples with first item a common word
               and second item the count for that word.  Sorted from high
               to low on counts. """

    # extract the y labels and x values
    # while it is easier to maintain a list of tuples in word
    # collection, Matplotlib requires separated data items
    ylabels = []
    xvals = []
    if len(list) > DISPLAY_WORD_LIMIT:
        display_len = DISPLAY_WORD_LIMIT
    else:
        display_len = len(list)

    for i in range(display_len):
        ylabels.append(list[i][0])   # extrat the word
        xvals.append(list[i][1])     # extrac the frequency 

    plt.rcdefaults()

    y_pos = np.arange(len(ylabels))
    plt.barh(y_pos, xvals)
    plt.yticks(y_pos, ylabels)
    plt.xlabel('Word Frequency')
    plt.title('Most Frequently Used Words')
    plt.show()

def main():
    list = createSortedList()
    displayChart(list)

main()
