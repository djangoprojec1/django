from django.shortcuts import render
from django.http import HttpResponse
# pandas for reading the list of names and frequency from word_search.tsv in a faster rate
import pandas as pd

# difflib is used to find the closest match words
import difflib
import json


def index(request):
	""" 
	index - Returns the index page or list of matching words. 
  
	Extended description of function. 
  
	Parameters: 
	request (request object): The default request params
  
	Returns: 
	list or html: List of matching words to the corresponding input or simple html
  
	"""

	# check if there is a get request for a word
	if "word" in request.GET and request.GET.get('word'):
		matching_words = get_the_matching_words(request.GET.get('word'))
		return HttpResponse(json.dumps(matching_words))
	else:
		return render(request, 'search/index.html')

def get_the_matching_words(search_word):
	""" 
	get_the_matching_words - Returns the list of matching words. 
  
	Extended description of function. 
  
	Parameters: 
	search_word (string): The string which is inputed by user
  
	Returns: 
	list: List of matching words to the corresponding input
  
	"""
	list_of_names = []
	list_of_frequency = []
	# Read from the word_search.tsv and append to the corresponding lists

	reader = pd.read_csv('word_search.tsv', sep ='\t')
	# read col 0
	names = reader[reader.columns[0]].as_matrix()
	list_of_names = names.tolist()
	# convert all elements to strings
	list_of_names = [str(i) for i in list_of_names]
	# read col 1
	frequency = reader[reader.columns[1]].as_matrix()
	list_of_frequency = frequency.tolist()
	
	# difflib takes the string,list , number of expected outut and simiarity 
	# check while 0.1 being less similar and 0.9 being most similar
	# more details : https://docs.python.org/2/library/difflib.html
	list_of_matching_words = difflib.get_close_matches(search_word, list_of_names,25,0.7)

	final_list = []
	list_of_names_and_frequency = []

	if list_of_matching_words:
	    # if there is an ideal match it wil be first in the list
	    if search_word == list_of_matching_words[0]:
	        # add the ideal match to final list and remove the element
	        final_list.append(search_word)
	        list_of_matching_words.remove(search_word)
	    
	    # create a list of tuples with names and frequency for the matched datas 
	    for list_of_matching_word in list_of_matching_words:
	        list_of_names_and_frequency.append((list_of_matching_word, 
	        	list_of_frequency[list_of_names.index(list_of_matching_word)]))
	    
	    # lambda functions allows to add expressions and adding it to sort can perform sort after sort
	    # here we first pass the start with (in rev), then the frequency and then the char count
	    # more details available here https://www.w3schools.com/python/python_lambda.asp
	    data = sorted(list_of_names_and_frequency, key = lambda x: ((not x[0].startswith(search_word)),
	     -int(x[1]), len(x[0])))
	    res_list = [x[0] for x in data]
	    final_list = final_list + res_list

	return final_list