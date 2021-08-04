from flask import jsonify

from middleware import *


def initialize_routes(app):
    # 2.
    # parameters: url, function_name,
    app.add_url_rule('/api/db/grads', 'db', db)

    app.add_url_rule('/api/hello', 'hello', hello)
    app.add_url_rule('/api/', 'list_routes', list_routes, defaults={'app': app})
    app.add_url_rule('/api/profile/<id>', 'user_profile', user_profile)
    app.add_url_rule('/api/people/', 'people_details', people_details)  # GET
    app.add_url_rule('/api/people/', 'person_add', person_add, methods=["POST"])  # POST
    app.add_url_rule('/api/people/', 'update_people', update_people, methods=["PUT"])  # PUT


def list_routes(app):
    lst = []
    for route in app.url_map.iter_rules():
        print(route)
        print(route.endpoint)
        print(route.methods)

        # create a dict

        route_dic = {}
        route_dic['route'] = str(route)
        route_dic['endpoint'] = str(route.endpoint)
        route_dic['methods'] = str(route.methods)

        lst.append(route_dic)
    return jsonify({"routes": lst, "total": len(lst)})
