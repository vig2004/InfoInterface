from flask import Flask
from flask_restful import Api,Resource

app=Flask(__name__)
api=Api(app)

class Hello_World(Resource):
    def get(self):
        return {"data":"helloworld"}

api.add_resource(Hello_World,'/helloworld')#creating the url for request Hello_World

app.run(debug=True)
