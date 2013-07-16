from django.shortcuts import render_to_response
from forms import ShortDomain
from shorturl import shortURL

def index(req):
    if req.method == "POST":
        sd = ShortDomain(req.POST)
	ld = req.POST.get('longdomain')
        nd = "http://sd.cn/%s" % shortURL(ld)
	return render_to_response('index.html',{'nd':nd,'sd':sd})

    else :
	sd = ShortDomain()


    return render_to_response('index.html',{'sd':sd})
