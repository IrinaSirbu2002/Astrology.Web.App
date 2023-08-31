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
    This file contains the functions I needed for app.py.
    The first function is _adddays_ which takes as an argument a string that represents a date and returns another string represing tha date plus one day. Firstly, it converts it to a date datatype using the _strptime_ function from the _datetime_ library. Then, using the _timedelta_ function from the same library, I added one day to the existing date. Finally, I converted the date back to a string and returned it.
    The second function called _lookup_ also takes as an argument a string representing a date and returns a list of tuples. The _baseurl_ is the base of the url extracted from a NASA page that provides APIs for different sets of data. I chose the one that has information about asteroids that came near Earth on specific dates. The api_key is my personal API that I signed up for. Next, the end_date I automatically setted one day after the start_date in order to be easier for users to find the information about asteroids and not having to enter both dates every time. Then, in the actual url I replaced the parameters. The API request I made using the requests library and also a json file for the data. For the storing of the data I further used a PSQLite Database (required by the Heroku platform). The variable db_connection_params stores the parameters required for the connection to the database which I found on the Heroku app once I created the db. Then, I created the table neo_data with the information that I needed from the data sets. Iterating over every element, I inserted into the table the data and then returned the information from the asteroids on the specific date that the user required.
    The last function, api_apod, takes no argument and returns a disctionary. Similarly to the second function, I used my own api_key and the url from the NASA site in order to connect to a set of data about the astronomy picture of the day (the title, the image_url and the explanation of the photo).

**app.py**
    This is the main file of the application. Here, I configured the Flask app. For each of the routes, I made a function. For the main page, I only render the html template by the method _GET_, being a static page. 
    For the _distcalc_ route, there are two methods, _GET_ and _POST_, because there is a form to complete. In this function, I read the data from the csv file into a list of dictionaries using the _DictReader_ from the csv library. Then, using the list _places_, I selected all the planets present in the file only once for the option button in the distcalc.html. In case the page is accessed using the method _POST_, meaning the form is submitted, the places chosen by the user are extracted into two variables, dist1 and dist2, and then are compared with every dictionary in the distances list to find the distance between the places, lastly, rendering the template calculated.html with the variables found. In case the user hadn't chosen any place or only one place, I returned the distcalc.html template to show the warning message. Via the _GET_ method, the distcalc template is returned with the list of places that the user can choose from.
    There are also the two _GET and _POST_ methods for the _neo_ route. If the page is accessed via _POST_, I used the conditional try-except to avoid any ValueError that the user may enter. If the user doesn't use the format suggested, then the _strptime_ function will rise the ValueError, and then the template neo.html will be returned with x having the value of 1, signaling to the user to use the format. Also, if the user doesn't enter any value, then x of value 2 will signal to the user to enter a date. Into the neo_data variable I stored the list of tuples returned by the lookup function, therefor, changing them to a list of dictionaries and returning the neocalc template with the data. In case the page is accessed via _GET_, it is simply returned the neocalc.html with x having the value of 0, meaning there is no error yet.
    Finally, the route _apod_ is only accessed via _GET_. I stored the data from the day the page is being viewed into the variable apod_info and then returned the template with the information.

####Static File:

**styles.css**
    This file containes some styling choices I made with some paragraphs, tables or forms. The first two I took from the bootstrap documentation. The _p1_ is used for the paragraphs in neo and distcalc to have the Garamond font, as I found out is one of the clearest and easiest to read. The _tit_ class sets the font of the titles of the neo, neocalc, distcalc, apod and index pages to Times New Roman as it is also easy to read and I wanted for it to be slightly different from the font of the paragraph. the three tabs_grid classes are for the index page, and are used to store the information about the planets. I wanted them to fit on any screen and I arrenged the margins and padding so it looks better overall. For the table on the neoclac page, I chose to not have vorders between columns so it looks cleaner, and have a width of 100% to occupy all the container. The rows I alligned to the left and have a padding of 8px to set some distance between them and all the information to be clearly seen and read. I chose a style of table with different coloured rows to add a personal touch.