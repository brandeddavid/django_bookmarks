from django.shortcuts import render
from django.http import HttpResponse

def main_page():

    output = '''

      <html>
        <head><title>%s</title></head>
          <body>
             <h1>%s</h1><p>%s</p>
          </body>
      </html>

      ''' %(

          'Django Bookmarks',
          'Welcome to Django Bookmarks',
          'You can store and share bookmarks!'
          )

    return HttpResponse(output)

# Create your views here.
