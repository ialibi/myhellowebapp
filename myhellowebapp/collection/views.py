from django.shortcuts import render

def index(request):
	#define the variable
	# return render(request, 'index.html') is the only original
    number=6
    song = "Christmas"
    #passing the variable to the view
    return render(request, 'index.html', {
    	'number': number,
    	'song': song,
    	})
