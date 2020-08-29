# heroku app - api for converting html to pdf

for creating new app follow : https://www.geeksforgeeks.org/deploy-python-flask-app-on-heroku/

how to deploy this application?

step 1.> clone this repo.

step 2.> Add the following build packs:
	1. https://github.com/dscout/wkhtmltopdf-buildpack.git	
	2. https://github.com/heroku/heroku-buildpack-python

How ?
use following command:

<pre>
	heroku buildpacks:add https://github.com/dscout/wkhtmltopdf-buildpack.git

	heroku buildpacks:add https://github.com/heroku/heroku-buildpack-python
</pre>

now push the app. 
<pre>
	> git push heroku master
</pre>

DONE!!


To get into the filesystem of the application:

Try run commands:

First you need to login, then you to see your apps and finally run bash

<pre>
heroku login
</pre>

Insert you user and password

<pre>
heroku apps

=== user@gmail.com Apps
myaplication
</pre>

then look at the list aps and write
<pre>
heroku run bash --app myaplication
</pre> 
