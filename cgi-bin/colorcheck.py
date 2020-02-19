#!/usr/bin/env python
import cgi

form = cgi.FieldStorage()

color = form.getvalue("color")

cdoc = open("colors.txt", "r")

found = False
for color in cdoc:
    if color in cdoc:
        found = True
        break

cdoc.close()

if found:
    output = str(color) + " is a color"
else:
    output = str(color) + " is not a color"

page = """
    <!DOCTYPE html>
    <html lang="en" dir="ltr">
      <head>
        <meta charset="utf-8" />
        <title>Color-Check</title>
        <link rel="stylesheet" href="style.css">
      </head>
      <body>

        <h1>{}</h1>

      </body>
    </html>
""".format(output)

print(page)
