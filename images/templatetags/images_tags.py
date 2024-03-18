from django import template

register = template.Library()



@register.filter("forward_slashes")
def forwarder(url):
    url = str(url)
    if "\\" in str(url):
        url = "/".join(url.split("\\"))
    print("finalyy",url)
    return url

