from django.shortcuts import render

# Create your views here.


def home1(request):
  return render(request, "base.html", {"name":"Richard Amoo"})

def home(request):
    context = {
        "properties": {
            "p1":{
                "images": ["img" + str(n) for n in range(1,5)]
            },
            "p2":{
                "images": ["set2_img" + str(n) for n in range(1,6)]
            },
            "p3":{
                "images": ["set3_img" + str(n) for n in range(1,8)]
            },
        },
        "all_properties":["img" + str(n) for n in range(1,5)] + ["set2_img" + str(n) for n in range(1,6)] + ["set3_img" + str(n) for n in range(1,8)],
        "news_list": [
            "The Ongoing BLUEMOON GARDENS Project in Asokoro 2 Now Close to Completion",
            "Bluemoon Global Services Limited Received a Prestigious Real Estate Award for Our Outstanding Services",
            "Exciting Updates About Our Logistics and Supplies Services"
        ]

    }

    return render(request, "bluemoonglobal.html", context)
