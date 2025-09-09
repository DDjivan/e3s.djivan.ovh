from flask import Flask
from argparse import ArgumentParser

from flask_routes.docs_app import app_docs

##————————————————————————————————————————————————————————————————————————————##

app = Flask(__name__)

##————————————————————————————————————————————————————————————————————————————##

app.register_blueprint(app_docs)

##————————————————————————————————————————————————————————————————————————————##
 
if (__name__ == '__main__'):
    web_parser = ArgumentParser(description='Deploy app.')
    web_parser.add_argument(
        '-d', '--debug', #type=?, choices=?, required=False,
        # default=False,
        action='store_true',
        help="Enable debug mode.",
        )

    them_args = web_parser.parse_args()
    # print(them_args)

    # app.run(host='0.0.0.0', debug=True)
    app.run(host='0.0.0.0', debug=them_args.debug)


