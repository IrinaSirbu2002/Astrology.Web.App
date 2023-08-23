# IrinaSirbu2002.github.io
#### Video Demo: <URL HERE>
####Description:

**The Flask Application**
    Firstly, the main idea of the project was to develop a web application which has strong relations to astrology. In order to make it more dynamic and be able to rely on server-side logic, routing, and database interactions, I used a web hosting platform that supports server-side processing, Heroku. This platform can support a flask application, but has a slightly different documentation: the files and directories had to be specific:
    - Procfile
    - requirements.txt
    - data files:
      - distances.csv
      - neo_data.db
    - Python files:
      - app.py
      - request.py
    - Templates:
      - layout.html
      - index.html
      - distcalc.html
      - calculated.html
    - static files:
      - styles.css

**Procfile**
    This file contains only one line of code in which it is specified the main Flask application file: app.py. It is used to provide information for the platform on how to run the application (via app.py).

**requirments.txt**
    This file lists the required packages for the application:
    - requests
    - Flask
    - Flask-Session
    - psycopg2-binary
    The psycopg2-binary package is included for supporting PostgreSQL (the recommended database for deployment to Heroku). 

**distances.csv**
    This is a csv file that containes data for the Distance Calculator. The first two columns are the planets that the user may want to know the distance between, and the last column is the distance in km.

####Templates:

**layout.html**
    Firstly, I used the bootstrap CSS an JavaScript for the layout of the web pages. Then, also from bootstrap I used the format of the navbar. For the title of the pages I used Jinja syntax for creating a block named _title_.
    Between the _body_ tags there is the configuration of the nvbar:
    - Closer to astrology, when clicked it takes the user to the main page("/")
    - NEO, when clicked it takes the user to the Near Earth Object page("/neo")
    - Distance Calculator, when clicked it takes the user to the Distance Calculator page("/distcalc")
    - Gallery, a dropdown menu that contains:
      - APOD (Astronomy Picture of the Day)
      - a link to NASA Image and Video Library
    There is also a block named _main_ which is specific to every page.

**distcalc.html**
    This file contains a form with two select-option dropdowns and a submit button. The first _select_ has the name _place1_ and its options are added via a loop of items from a list using Jinja syntax. The second _select_ has the name _place2_ and has the same options as the first one. This template is used when the user clicks on the _distance Calculator_ option from the navbar via _GET_.

**calculated.html**
    This file has the same title, but gives the user the result of their searched distance via _POST_. Also using Jinja syntax, the placeholders between {{}} are the values of a dictionary.

**index.html**