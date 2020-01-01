from django.http import HttpResponse
from django.shortcuts import render
import operator


def index(request):
	return HttpResponse('Hello World')

def about(request):
	return render(request,'about.html')

def home(request):
	return render(request,'home.html')

def count(request):
	fulltext = request.GET['wordcnt']
	wordlist = fulltext.split()
	#print(wordlist)
	
	worddict = {}
	for i in wordlist:
		if i in worddict:
			worddict[i]+=1
		else:
			worddict[i]=1
	sortedwords = sorted(worddict.items(),key=operator.itemgetter(1),reverse=True)
	print(sortedwords)
	return render(request,'count.html',{'key1':fulltext,'key2':len(wordlist),'key3':sortedwords})