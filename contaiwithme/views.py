# from django.http import HttpResponse

# def robots_txt(request):
#     lines = [
#         "User-Agent: *",
#         "Disallow: /admin/",
#         "Sitemap: http://127.0.0.1:8000/sitemap.xml"
#     ]
#     return HttpResponse("\n".join(lines), content_type="text/plain")


from django.http import HttpResponse

def robots_txt(request):
    lines = [
        "User-agent: AhrefsBot",
        "Disallow: /",
        "",
        "User-agent: SemrushBot",
        "Disallow: /",
        "",
        "User-agent: BLEXBot",
        "Disallow: /",
        "",
        "User-agent: *",
        "Disallow: /admin/",
        "Disallow: /media/private/",
        "Allow: /",
        "",
        "Sitemap: http://127.0.0.1:8000/sitemap.xml"
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")
