export FLASK_APP=flashcards.py  ---> Linux
set FLASK_APP=flashcards.py ---> Windows
set FLASK_ENV=development
set FLASK_DEBUG=1
set TEMPLATES_AUTO_RELOAD=1

flask --app flashcards run

python -m flask --app flashcards run
python -m flask --app flashcards --debug run

    $ flask --app flaskr init-db
    $ flask --app flaskr run --debug