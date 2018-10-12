Idiomatic Programming with Iterators
====================================

---

 __Anand B Pillai__ <br/>
 _anandpillai@letterboxes.org_ <br/>
 _@pythonhacker_ <br/>

<div class="footer">
Coyright &copy; Anand B Pillai 2013.
</div>
---
Iterators are everywhere in Python

          
    !python
    # iterating a list
    for i in range(10):
        print i

    # iterating a dictionary by key
    fruits = {'apple': 'red', 'grapes': 'green'}
    for fruit in fruits:
        print fruit

    # iterating a set
    import string
    for alphabet in set(string.letters):
        print alphabet
---
__Idiomatic__

   * adj.
     * Peculiar to or characteristic of a given language.
     * Characterized by proficient use of idiomatic expressions: a foreigner who speaks idiomatic English.

---
Iterating a list

    !python
    fruits = ['apple','mango','grapes','jackfruit','lemon']
    for i in range(len(fruits)):
        print fruits[i]
        
    # Idiomatic - Use list as an iterator with no index
    for fruit in fruits:
        print fruit
---
Reversing a list

    !python
    # Eh, ugly!
    fruits = ['apple','mango','grapes','jackfruit','lemon']
    for i in range(len(fruits)-1,-1,-1):
        print fruits[i]
        
    # Better
    for fruit in fruits[-1::-1]:
        print fruit

    # Idiomatic
    for fruit in reversed(fruits):
        print fruit
---
Enumerating a list

    !python
    # C-style
    fruits = ['apple','mango','grapes','jackfruit','lemon']
    for i in range(len(fruits)):
        print i,'-->',fruits[i]

    # Idiomatic
    for i,fruit in enumerate(fruits):
        print i,'-->',fruit
     
    0 --> apple
    1 --> mango
    2 --> grapes
    3 --> jackfruit
    4 --> lemon 
---
Why enumerate ?

    !python
    # Create indexed dictionaries from lists
    fruit_dict = {}
    for i,fruit in enumerate(fruits):
        fruit_dict[i] = fruit

    # Idiomatic
    fruit_dict = dict(enumerate(fruits))
    {0: 'apple', 1: 'mango', 2: 'grapes', 3: 'jackfruit', 4: 'lemon'}            

---
Sorting a list
        
    !python
    languages = ['D', 'Ada','Python','Smalltalk','C','Ruby','Perl']
    # Alpha numeric sort
    languages.sort()
    ['Ada', 'C', 'D', 'Java', 'Perl', 'Python', 'Ruby', 'Smalltalk']
    
    # Sort by length - In place
    languages.sort(key=len)
    
    # Sort by length - produces new list
    # Idiomatic
    sorted(languages, key=len)
    ['C', 'Ada', 'Java', 'Perl', 'Ruby', 'Python', 'Smalltalk']

---
Sorting to a field with the ___operator___ module

    !python
    # Sort a website according to its alexa rank
    topsites = {'google': 1,
                'wikipedia': 6,
                'linkedin': 8,
                'yahoo': 4,
                'baidu': 5,
                'youtube': 3,
                'facebook': 2,
                'qq': 7}

    import operator
    [x[0] for x in sorted(topsites.items(), key=operator.itemgetter(1))]
    ['google', 'facebook', 'youtube', 'yahoo', 'baidu', 'wikipedia', 
     'qq', 'linkedin']

    
---
Merge two lists

    !python
    languages = ['Ada','C','Java', 'Perl','Python','Smalltalk']
    whatithink = ['Old','Fundamental','Widely Used','Hacky','Cool']

    # C-like, error-prone
    n = min(len(languages), len(whatithink))
    for i in range(n):
       print 'I think',languages[i],'is',whatithink[i]

    # Idiomatic - uses zip
    for language, ithink in zip(languages, whatithink):
        print 'I think',language,'is',ithink

    I think Ada is Old
    I think C is Fundamental
    I think Java is Widely Used
    I think Perl is Hacky
    I think Python is Cool

---
Find if any member in a list satisfies a condition.

    !python   
    
    numbers = [1, 8, 10, 12, 15, 17]
    # Find if any number is odd        
    flag = False     
    for num in numbers:
        if num % 2:
           flag = True
           break

    # More Pythonic 
    print len([num for num in numbers if num %2])

    # Idiomatic
    print any((num for num in numbers if num % 2))

---

Similary, find if all members in a list satisfies a condition

    !python
    print all((num for num in nums if num % 2))

---
List comprehensions
===================

---
Make your own lists

A list comprehension contains at least one for statement
and zero or more if statements.

    !python
    # Produce squares of numbers
    [x*x for x in range(10)]
    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

    # Produce squres of odd numbers
    [x*x for x in range(10) if x % 2]
    [1, 9, 25, 49, 81]

---
Using two indices

    !python
    # Multiply two lists by using two indexes
    # Example - Produce multiplication tables 
    # for numbers 1..10
    dict([(y,[x*y for x in range(1,11)]) for y in range(1,11)])
    {1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 
     2: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20], 
     3: [3, 6, 9, 12, 15, 18, 21, 24, 27, 30], 
     4: [4, 8, 12, 16, 20, 24, 28, 32, 36, 40], 
     5: [5, 10, 15, 20, 25, 30, 35, 40, 45, 50], 
     6: [6, 12, 18, 24, 30, 36, 42, 48, 54, 60], 
     7: [7, 14, 21, 28, 35, 42, 49, 56, 63, 70], 
     8: [8, 16, 24, 32, 40, 48, 56, 64, 72, 80], 
     9: [9, 18, 27, 36, 45, 54, 63, 72, 81, 90], 
     10: [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]}
---
Pros

   * Concise, single line syntax.
   * Efficient and optimized.
   * Perform operations on existing list(s), producing new ones.

Cons

   * No "else" syntax, hence can't take complex conditions.
   * Produces lists in memory.

---
Generators
==========

---
Produce iterators that are memory-efficient

    !python
    # Example - Fibonacci function
    def fibonacci(n):
        """ Fibonacci number using recursion """
        
        if n in (0, 1):        
            return 1
        else:
            return fibonacci(n-1) + fibonacci(n-2)

Problems
 
   * Stack heavy and memory inefficient
   * Needs to compute all (n-1)th fibonacci numbers to
     compute the nth fibonacci number.

---
Fibonacci

    !python
    def fibonacci(n):
        """ Fibonacci generator function """

        x, y = 1, 2
        for in range(n):
            yield x            
            z = x + y
            x, y = y, z

---
Generator Syntax

   * Produces an iterator 
   * Use __yield__ instead of __return__ to produce an output
   * Stack is frozen at yield and re-entered in next iteration
   
Pros

   * Memory efficient iterators
   * Lazy computation - Produces values at request
   * State keeping is taken care of automatically
   
Cons

   * Slightly cryptic code
   * Needs rewriting of functions sometimes

---
Dictionaries
============
---
Iterating dictionary keys

    !python
    country_capitals = {'India':'New Delhi','Germany':'Berlin',
                        'England':'London', 'Canada':'Ottawa',
                        'China':'Beijing','Norway':'Oslo'}

    for country in country_capitals.keys():
        print country,'-->',capital_dict[country]

    # Idiomatic
    for country in country_capitals:
        print country,'-->',capital_dict[country]

    for country,capital in country_capitals.iteritems():
        print country,'-->',capital

---
Creating a dictionary from two lists

    !python
    countries = ['India','Germany','England','Canada','China','Norway']
    capitals = ['New Delhi','Berlin','London','Ottawa','Beijin','Oslo']

    n = min(len(countries),len(capitals))
    
    country_capitals = {}
    for i in range(n):
        country_capitals[countries[i]] = capitals[i]

    # Idiomatic
    for country,capital in zip(countries,capitals):
        country_capitals[country] = capital

    # Even better 
    # This form is called a "dict" comprehension
    country_capitals = {country:capital for country,capital in 
                        zip(countries,capitals)}

    # Most concise
    country_capitals = dict(zip(countries,capitals))

---
Grouping with dictionaries

    !python
    fruits = ['apple','grapes','apple','mango','mango','apple',
             'banana','orange','guava','sapota','apple','orange',
             'litchi','strawberry','lemon','apple','grapes']

    # Group according to counts
    fruit_bag = {}
    for fruit in fruits:
        if fruit not in fruit_bag:
            fruit_bag[fruit] = 0
        fruit_bag[fruit] += 1

    # Idiomatic
    for fruit in fruits:
        fruit_bag[fruit] = fruit_bag.get(fruit,0) + 1

    print fruit_bag
    {'sapota': 1, 'apple': 5, 
     'litchi': 1, 'strawberry': 1, 
     'mango': 2, 'grapes': 2, 
     'orange': 2, 'lemon': 1, 
     'guava': 1, 'banana': 1})

---
___collections___ module

Provides the defaultdict type which is useful to
create dictionaries that automatically set a key
according to a type

    !python
    # Grouping using defaultdict
    fruit_bag = collections.defaultdict(int)
    for fruit in fruits:
        fruit_bag[fruit] += 1

    
---
With default list type

    !python
    # Grouping according to length
    fruits = ['apple','grapes','mango','banana','orange','guava',
              'sapota','strawberry','lemon']
    
    fruit_length = collections.defaultdict(list)
    for fruit in fruits:
        fruit_length[len(fruit)].append(fruit)

    print fruit_length
    defaultdict(<type 'list'>, {10: ['strawberry'], 
                                5: ['apple', 'mango', 'guava', 'lemon'], 
                                6: ['grapes', 'banana', 'orange', 'sapota']})
                         
---
Itertools 
=========

---
The ___itertools___ module provides a set of powerful functions
for building iterators.

Most of the functions in itertools module return generators.

    !python

    # itertools.count can provide an infinite counter.
    for i in itertools.count(stop=100):
        print i

    # itertools.cycle cycles through an iterator
    # Will keep printing 'python'
    for i in itertools.cycle(['python']):
        print i

---
Chaining iterators
         
__itertools.chain__ allows to return elements from
many iterators till each of them are exhausted.

    !python
    import itertools
    import collections

    # Make a dictionary of alphabet counts of
    # letters in a list of strings.
    birds = ['parrot','crow','dove','peacock','macaw','hen']
    frequency = collections.defaultdict(int)

    for letter in itertools.chain(*birds):
        frequency[letter] += 1 
---
Filter data using selectors


__itertools.compress__ filters elements from a sequence
by applying a list of selectors which evaluates to True.
Can be used to apply a list of filters against a list
of elements.

    !python
    # Drop every alternate letter in a string of alphabets
    import string

    for i in itertools.compress(string.letters, itertools.cycle([1,0])):
        print i,

    a c e g i k m o q s u w y A C E G I K M O Q S U W Y

    # Drop students who failed to get marks above a cut-off
    # in Python programming exam.
    marks = {'Kiran': 93, 'Anand': 85, 'Soujanya': 92,
             'Manohar': 98, 'Rakshith': 90, 'Nisha': 20}
    # Make sure the list is sorted in both cases
    selectors = [marks[student]>27 for student in sorted(marks)]   
    
    list(itertools.compress(sorted(marks), selectors))
    ['Kiran', 'Manohar', 'Nisha', 'Rakshith', 'Soujanya']

---
Filtering elements based on condition

___itertools.ifilter___ returns an iterator that applies
a condition to elements in an iterator and returns elements
that match the condition.

    !python
    # An infinite iterator for odd numbers
    for number in itertools.ifilter(lambda x: x%2, itertools.count()):
        print number

  * itertools.ifilter is similar to ___filter___ but returns
    an iterator instead of a list.
  * ___itertools.ifilterfalse___ performs the reverse operation,
    i.e returns an iterator for which the condition evaluates to 
    False.

---
Map a function to many iterables

__itertools.imap__ is similar to __map__ function in that it maps a function to an iterable and returns an iterator (___map___ returns a list).

    !python 
       
    # Multiply items of two lists in order
    for i in itertools.imap(operator.mul, [3,5,7,9], [2,3,4,5]):
        print i
    6
    15
    28
    45

---
Group together elements using similar property

___itertools.groupby___ allows to group elements in an
iterable to groups based on a _key function_.

    !python
    # Group together strings of same length.
    birds = ['parrot','crow','dove','peacock','macaw','hen']
    
    for k,g in itertools.groupby(sorted(birds,key=len), key=len):
        print k,'-->',list(g)

    3 --> ['hen']
    4 --> ['crow', 'dove']
    5 --> ['macaw']
    6 --> ['parrot']
    7 --> ['peacock']    
        
---
Repeatedly return an object again and again

___itertools.repeat___ itertools.repeat returns an object continously. An optional number of times can be specified as well.

    !python 
    
    # repeat and cycle can be combined to return items
    # in an iterator a fixed number of times each.
    for i in itertools.repeat(itertools.cycle(['python','java']), 3*2):
        print i.next()

    python
    java
    python
    java
    python
    java

    # A common use of repeat is to supply a continuous
    # stream of values to imap.
    
    # Produce tables of 7
    import operator
    list(itertools.imap(operator.mul, range(1,11), itertools.repeat(7)))
    [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]    
                                                                          
---
More magic with iterators

You often need to write code that returns till it
finds a ___sentinel___ value. 

    !python
    flag, data = False, []
    # Keep producing random numbers till a specific value
    sentinel = 49

    while True:
       num = random.randrange(1, 100)
       if num == sentinel: 
          break
       data.append(num)
       
    # Idiomatic
    import functools

    # Freeze function with all its arguments
    func = functools.partial(random.randrange, 1,100)

    for num in iter(func, sentinel):
        data.append(num)

---
Sentinel using itertools

You can right an equivalent code using a chain of itertools
functions.

    !python
    from itertools import cycle, takewhile, imap

    # Warning - the code below might look like magic.
    sentinel=49
    list(takewhile(lambda x: x!=sentinel, 
         imap(random.randrange, cycle([1]), cycle([100]))))

---
Prime number generator using itertools

    !python

    sieve = lambda n: not any(n % num==0 for num in range(2, int(pow(n,0.5))+1))

    def prime():
        """ Infinite prime number generator
        using Erastosthenes sieve """

        for num in itertools.ifilter(sieve, itertools.count()):
            yield num
        
---                        
Itertools help you to,

   * Avoid writing your own iterator classes but instead use the power
     of Python standard library modules.
   * You need a continous supply of values to your functions or generators.     
   * Perform a series of complex operations on a list or sequence without
     writing a lot of code.
   * ___Commodify___ operations like chaining, cycling, grouping, generating
     permutations, combinations, products etc without writing your own code.


Generator expressions
=====================
---
A generator expression is similar to a list comprehension,
except that the expression produces an iterable generator,
instead of a list.

Instead of the square brackets of a list comprehension,
a generator expression uses parens.

    !python
    # Generator expression producing an infinite
    # square iterator.
    ((x*x for x in itertools.count())

    # Generator producing an infinite list of odd numbers
    ((x for x in itertools.count() if x%2))

---
A generator expression is very useful where the final result
is that matters instead of the actual list or iterable.

    !python
    # Sum of first 100 natural numbers
    sum((x for x in range(101)))
    5050
    
    # Find out if any of the number in a list of 
    # random numbers is odd
    randlist = random.sample(range(100),10)
    any((num%2 for num in randlist))
    
---
Simplified syntax

If you are using the generator expression as an input
to a function such as __sum__, you can omit the outer
parantheses.

    !python
    sum(x for x in range(101))
    5050

    any(num%2 for num in random.sample(range(1,100), 20))
    True

---
Rule of thumb - Generator expressions vs List comprehensions

Use list comprehensions where,

   * The actual list or sequence you produce out of the list
     comprehension matters.
   * Your list or sequence is small enough to fit into memory.
     
Use generator expressions where,

   * The final output is what that matters instead of the actual 
     list or sequence. E.g: Functions like __sum__, __all__, __any__ etc.
   * You want to create quick generators using simple conditions
     without having to define a function.
   * When dealing with huge sequences where saving memory is important.

---
Summary

   * Iterators are at the heart of Python.
   * Iterators can be seen in core data structures (lists, dictionaries,
     tuples, strings, sets) as well as in language features like 
     list comprehensions, generators and generator expressions.
   * Use for loops for iteration as it "knows" how to work with
     iterators in Python.
   * List comprehensions provide a concise syntax for producing lists.
   * Generators produce memory-efficient, lazily computing iterators.
   * The itertools module provides a rich library of generator functions.       
   * Generator expressions provide a concise syntax for writing generators.

---

Feedback [@pythonhacker](http://twitter.com/pythonhacker)
======================




 
          
    
            








            





          











    














