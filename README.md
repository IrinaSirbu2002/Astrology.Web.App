# IrinaSirbu2002.github.io
#### Video Demo: <URL HERE>
####Description:

**The Flask Application**
    Firstly, the main idea of the project was to develop a web application which has strong relations to astrology. In order to make it more dynamic and be able to rely on server-side logic, routing, and database interactions, I used a web hosting platform that supports server-side processing, Heroku. This platform can support a flask application, but has a slightly different documentation: the files and directories had to be specific:
    - Procfile
    - requirements.txt
    - data file:
      - distances.csv
    - Python files:
      - app.py
      - request.py
    - Templates:
      - layout.html
      - index.html
      - distcalc.html
      - calculated.html
      - neo.html
      - neocalc.html
      - apod.html
    - static file:
      - styles.css

**Procfile**
    This file contains only one line of code in which it is specified the main Flask application file: app.py. It is used to provide information for the platform on how to run the application (via app.py).

**requirments.txt**
    This file lists the required packages for the application. Using the command _pip3 freeze > requirements.txt_ this file autocompleted itself with all the packages that I installed for this application.
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
    There is also a block named _main_ which is specific to each page.
    The background setted is an image of a sky with stars appropriate for the theme.

**distcalc.html**
    This file contains a form with two select-option dropdowns and a submit button. The first _select_ has the name _place1_ and its options are added via a loop of items from a list using Jinja syntax. The second _select_ has the name _place2_ and has the same options as the first one. This template is used when the user clicks on the _distance Calculator_ option from the navbar via _GET_. Also, in case the user doesn't choose any option or one of two options only, under the form I included a warning paragraph with a message in red, guiding the user to what may be the problem of submition.

**calculated.html**
    This file has the same title, but gives the user the result of their searched distance via _POST_. Also using Jinja syntax, the placeholders between {{}} are the values of the chosen places by the user and respectively, the distance between them. When it comes to styling the page, same as the distcalc.html page, I included all the information within a container in order to be more visible, as the background is quite busy.

**index.html**
    This is the home page of the application. This template is used when the user clicks on the _Closer to Astrology_ option from the navbar via _GET_. The section that containes the title of the page is from bootstrap examples, choosing the one on bold and italic in order to stand out from the rest of the content. Next, I used the html of a container, also from bootstrap examples on features(including the specific library in layout.html) to present some information about each planet that I took from a NASA site. The images of the planets are extracted from the internet from various sites. I used the tabs_grid container, tabs_grid_img and tabs_grid_desc classes to organize the information better and to adjust the layout depending on the screen's measurements.

**apod.html**
    This file has the name _Astronomy Picture of the Day_.This template is used when the user clicks on the _APOD_ option from the dropdown menu of the Gallery via _GET_. The title of the main part has an identical formatting to the one on the home page, extracted from bootstrap. Between the brackets, I included the actual name of the astronomy picture of the day provided by NASA. In the next paragraph, the image's URL is also between Jinja brackets, as it changes depending on the day the site is accessed. The next and final part of the page is a container with the same styling as the ones before, containing some information about the respective picture.

**neo.html**
    This template is used when the user clicks on the _NEO_ option from the navbar via _GET_. In this file I used the same format for the title of the page, for coherency reasons. Then, in the container with the exact same styling (also for the same reasons), I included a form with a text input with the name _date_, which has as a placeholder the format needed for it to be submitted. Then, underneath it there is a button for submitting a specific date. Next, I included two if clauses using Jinja syntax for two different reasons for not being able to sumit the form. Both of them use the variable _x_ which indicates which of the two is the inconvenience. Like the error message in the distcalc.html file, the warning text will appear underneath the form in red texting.

**neocalc.html**
    This file has the same title, but gives the user the result of their searched date via _POST_. As for the title of the main block, the same formating has been used, including the variable _date_, being the selected date by the user in the form. Then, within the container, there is a table of width 100% (appropriate for every screen dimensions) with a header, and the information about each asteroid which has been close to the Earth on that specific date. Using a for loop, I iterated through every row of the table, accessing the information for each column from the dictionary using Jinja brackets.

####Python Files:

**request.py**
    