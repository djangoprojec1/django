# django-fuzzy-search-from-csv
Fuzzy search using Django from CSV file

Demo :- http://srinivasaravind5.pythonanywhere.com/search

Challenge

You are given a dataset that contains 333,333 English words and the frequency of their usage in some corpus. A very small sample is shown below:

track   		112385243
australia		112197265
discussion		111973466
archive		111971865
once			111882023
others		111397714
entertainment	111394818
agreement		111356320
format		111279626

Let us assume we’re building a web app where the user types in a single word from this list in a search box. We wish to autocomplete the input in the search box. 

Your objective is to write a Python app using Django framework that exposes a single endpoint:

GET /search?word=<input>

where input is the (partial) word that the user has typed so far. For example, if the user is looking up procrastination, the service might receive this sequence of requests:

GET /search?word=pro
GET /search?word=procr
GET /search?word=procra

and so on.

The response should be a JSON array containing upto 25 results, ranked by some criteria (see below).

Constraints

1. Matches can occur anywhere in the string, not just at the beginning. For example, eryx should match archaeopteryx (among others).

2. The ranking of results should satisfy the following:

a. We assume that the user is typing the beginning of the word. Thus, matches at the start of a word should be ranked higher. For example, for the input pract, the result practical should be ranked higher than impractical.

b. Common words (those with a higher usage count) should rank higher than rare words.

c. Short words should rank higher than long words. For example, given the input environ, the result environment should rank higher than environmentalism.

d. As a corollary to the above, an exact match should always be ranked as the first result.

Configuration Steps

1. Clone the project
2. Install Anaconda (https://conda.io/docs/user-guide/install/linux.html) and create a virtual env
3. Open Terminal at project location where manage.py file is present and activate the env
4. pip3 install -r requirements.txt
5. python manage.py runserver
6. Visit http://127.0.0.1:8000/search on browser and use the search box to search
