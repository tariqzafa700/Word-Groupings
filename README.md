# Word-Groupings
Create a virtual env

`python3 -m venv venv`

Activate it

`source venv/bin/activate`

Install requirements
`pip install -r requirements.txt`

endpoints

GET http://localhost:5000/groupedWords/   - to group existing words
POST http://localhost:5000/addWord/<new_word>   -  to add a new word

Run the server using command
(If needed please set PYTHONPATH=src)

`flask run`

Run the ui app using command

`npm install`
`npm start`

To add a new string.

1. Click on the + sign next to the top level folder.
2. Add the new string name.
3. Click somewhere else on the page to shift focus from the textfield.
4. New entry gets shown below existing entries.
