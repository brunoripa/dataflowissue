echo 'Downloading jQuery'
curl https://code.jquery.com/jquery-2.2.4.min.js > static/js/jquery-2.2.4.min.js

echo 'Downloading Bootstrap JS'
curl https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.js.css > static/js/bootstrap-3.3.6.min.js

echo 'Downloading Bootstrap CSS'
curl https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css > static/css/bootstrap-3.3.6.min.css

echo 'Setting up virtualenv'
pip install -r dev_requirements.txt

echo 'Deleting PLACEHOLDER.txt files'
find static -name "PLACEHOLDER.txt" -delete

echo 'Setting up third party libs'
pip install -r requirements.txt -t lib