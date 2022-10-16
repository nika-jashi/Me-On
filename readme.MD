<h1>Django Project Me-On</h1>

<h3>set up environment for project</h3>

<li>python3.8 -m venv env</li>
<li>source env/bin/activate</li>
<li><b>pip install -r requirements.txt</b></li>

<br>
<hr>
<h3>To Run Migrations Use Commands Below</h3>
<li>python manage.py makemigrations</li>
<li>python manage.py migrate</li>
<hr>
<h3>to run server locally Use command below</h3>
<li>python manage.py runserver</li>
<h3>to run server With Docker Use command below</h3>
<li>sudo docker build -t [name:tag] . </li>
<li>-t: name and a tag of image</li>
<li>'.': (current directory) should input location of Dockerfile</li>
<li>sudo docker run -d -it -p [docker port:outside port] [name:tag]</li>
<li>-d: detache mode of a container</li>
<li>-p: port to publish</li>
<hr>
