# importing all the required modules 
from django.shortcuts import render, redirect 
from pytube import *


# defining function 
def youtube(request): 
    
	# checking whether request.method is post or not 
	if request.method == 'POST': 
        	
		# getting link from frontend 
		link = request.POST['link'] 
		video = YouTube(link) 

		# setting video resolution 
		stream = video.streams.get_lowest_resolution() 
		
		# downloads video 
		stream.download() 
        
		# returning HTML page 
		return render(request, "youtube/youtube.html")
    
	return render(request, "youtube/youtube.html")


from .forms import Robot
def robot(request): 
    if request.method == 'POST': 
        form = Robot(request.POST) 
          
        if form.is_valid(): 
            return render(request, "youtube/youtube.html")
        else: 
            return HttpResponse("OOPS! Bot suspected.") 
            
    else: 
        form = Robot() 
          
    return render(request, "captcha/captcha.html", {'form':form})