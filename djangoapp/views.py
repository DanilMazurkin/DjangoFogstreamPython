from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect, render


def index(request):
    return render(request, "index.html")

def about(request):
    return HttpResponse("About")

def contact(request):
    return HttpResponse("Contact @tgvoluzhev")

def info(request):
    return redirect("about")

def all(request):
    data = {
        'list_goods': [
            "thermometer",
            "candy wrapper",
            "pool stick",
            "buckel",
            "drawer",
            "cell phone",
            "flag",
            "glass",
            "cork",
            "milk",
            "chapter book",
            "drill press",
            "lip gloss",
            "key chain",
            "leg warmers",
            "bookmark",
            "floor",
            "sand paper",
            "hair brush",
            "outlet",
            "pencil",
            "beef",
            "needle",
            "rusty nail",
            "glow stick",
            "deodorant",
            "canvas",
            "boom box",
            "fork",
            "cookie jar",
            "television",
            "seat belt",
            "lamp shade",
            "nail clippers",
            "carrots",
            "hair tie",
            "tissue box",
            "slipper",
            "flowers",
            "mop",
            "fridge",
            "keyboard",
            "mouse pad",
            "model car",
            "towel",
            "water bottle",
            "speakers",
            "glasses",
            "toe ring",
            "candle",
            "rubber band",
            "shoes"
        ]
    }

    return render(request, "all.html", context=data)

def good(request):
    
    
    data = {
        'cat': request.GET['category'],
        'id': request.GET['id']
    }

    return render(request, "good.html", context=data)