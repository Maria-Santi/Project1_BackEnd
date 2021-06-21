from flask import Flask

import logging

from flask_cors import CORS

from routes import employee_routes, manager_routes, reimbursement_routes

app: Flask = Flask(__name__)
CORS(app)

logging.basicConfig(filename="records.log", level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(message)s')

employee_routes.create_routes(app)
manager_routes.create_routes(app)
reimbursement_routes.create_routes(app)

if __name__ == '__main__':
    app.run()


