from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "index.html")

def result(request):
    sentence = str(request.POST.get('sentence'))
    sentence_to_list = sentence.split()

    dictionary = {}

    for word in sentence_to_list:
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1

    

    word_count = sorted(dictionary.items(), reverse=True, key = lambda item : item[1])


    #word_count = list(dictionary2.items())



    

    return render(request, "result.html", {'word_count': word_count})