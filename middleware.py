from flask import jsonify, request, abort

people_info = [{'name': 'Lisa Simpson', 'age': 43, 'job': 'Saxophone Player'},
               {'name': 'Bart Simpson', 'age': 47, 'job': 'Skateboarder'}]


# function returns a list of person as json
def people_details():
    return jsonify({"People": people_info})


def person_add():
    # extract data from the request
    # request.get_json
    # get attributes
    # validation
    # set to the list
    # response dict success


    #excepts
    # print ex
    # response failure
    # abort(status code) 400 bad request
    try:
        data = request.get_json(force=True)
        people_info.append(data)
        return jsonify({'status': 200, 'person': data})
    except Exception as ex:
        abort(400, str(ex))


def update_people():
    try:
        data = request.get_json(force=True)

        for people in people_info:
            people.update(data for k, v in people.items() if k == data["name"])
        print(data)
        # people_info.append(data)
        return jsonify({'status': 200, 'person': data})
    except Exception as ex:
        abort(400, str(ex))



def hello():
    return "Hello from Flask!!"


def db():
    return "Hello from Prafulla and Jonas!!"


def user_profile(id):
    return "Person info for user number {}".format(id)
