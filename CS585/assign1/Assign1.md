# IIT CS 585 Homework 1: Distributional Measures (80 points)

[ref](http://www.cs.iit.edu/~cs585/hw1/)

In this lab, you will wraite a python program, called dist_measures.py. This program should

* Read a list of words from text_a.txt, and calculate the frequency distribution of words in that text.

* Read a list of words from text_b.txt, and calculate the frequency distribution of words in that text.

* Calculate the following measures, and print them on eight consecutive lines, rounded to three digits:

    1. The entropy of the frequency distribution for list A -- H(P(A))
    
    2. The entropy of the frequency distribution for list B -- H(P(B))
       
    3. The cross-entropy -- H(P(A),P(B))
    
    4. The cross-entropy -- H(P(B),P(A))
    
    5. The KL divergence -- D_{KL}(P(A)||P(B))
    
    6. The KL divergence -- D_{KL}(P(B)||P(A))
    
    7. The JS divergence -- D_{JS}(P(A)||P(B))
    
    8. The JS divergence -- D_{JS}(P(B)||P(A))

For convenience (Python's math.log function is the natural log), calculate all values in nats rather than bits.

Download a template script for you to extend, as well as some sample inputs and outputs, here.

Do not import any python packages in your code other than those that are already included in the template script.

Submit your dist_measures.py file to Autolab using the "Submit file" link.