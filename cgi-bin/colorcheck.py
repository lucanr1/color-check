#!/usr/local/bin/python3
import cgi
import os

form = cgi.FieldStorage()

path = "/Users/luca/Projects/Foundations/color-check/cgi-bin/colors.txt"
color = form.getvalue("color")

cdoc = open(path, "r")
content = cdoc.read()

found = False
if(color in content):
    found = True

cdoc.close()

if found:
    output = color + " is a color"
else:
    output = color + " is not a color"

page = """
    <!DOCTYPE html>
    <html lang="en" dir="ltr">
      <head>
        <meta charset="utf-8" />
        <title>Color-Check</title>
        <link rel="stylesheet" href="/style.css">
      </head>
      <body>

        <h1>{}</h1>

      </body>
    </html>
""".format(output)

print(page)
