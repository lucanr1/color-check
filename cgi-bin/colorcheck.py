#!/usr/bin/env python3
import cgi

form = cgi.FieldStorage()

color = form.getvalue("color")

found = False
for color in colors.txt:
    if blabla in line:
        found = True
        break

if found:
    output = color+" is a color"
else:
    output = color+" is not a color"

page = """
    <!DOCTYPE html>
    <html lang="en" dir="ltr">
      <head>
        <meta charset="utf-8" />
        <title>Color-Check</title>
        <link rel="stylesheet" href="style.css">
      </head>
      <body>

        <h1>"""output"""</h1>

      </body>
    </html>
"""

print(page)
