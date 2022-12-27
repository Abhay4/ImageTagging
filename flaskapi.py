from flask import Flask, request, jsonify, Response
import uuid
import json
from services.imagesevice import imageService
from Util.error import HandleError
app = Flask(__name__)

service = imageService()

@app.route('/images',methods=['GET'])
def get_images():
    # get from DB
    service_res = service.getall()
    resp = Response(response=service_res,mimetype="application/json")
    return resp


@app.route('/images/<image_id>',methods=['GET'])
def get_images_by_id(image_id):
    # get from DB
    ser_res = service.get(image_id)
    resp = Response(response=ser_res,
                    mimetype="application/json")
    return resp


@app.route('/images',methods=['POST'])
def add_images():
    '''
    Accept a json containing
    location : "path/to/image"
    :return: return a unique identifier of the image
    '''
    body_data = request.get_json()
    if "location" not in body_data:
        return HandleError("location input is missing",status_code=400).handle_invalid_usage()
    image_data = body_data
    image_data["id"] = str(uuid.uuid1())
    request_id = image_data["id"]
    # save in db
    service.save(image_data)

    # prepare a response
    service_res = {"request_id": f"{request_id}","message":"Image added"}
    json_res = json.dumps(service_res)
    return Response(response=json_res,mimetype="application/json")


# Tags related APIs
@app.route('/images/<image_id>/tags',methods=['POST'])
def add_tag_to_image(image_id):
    """
        Add tag to given image
    :param image_id:
    :return: image_id,name,tags
    """
    tags = request.get_json()
    print(id,tags)
    #tags = json.loads(json_tags)
    if "tags" not in tags:
        return HandleError("tags input is missing",status_code=400).handle_invalid_usage()

    service_res = service.add_tag(image_id,tags["tags"])
    json_res = json.dumps(service_res)
    return Response(response=json_res,mimetype="application/json")


if __name__ == '__main__':
    app.run()