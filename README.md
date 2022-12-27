# ImageTagging

Run python flaskapi.py 

There are four API in total 
  1.  Add image to the database - POST call to - {baseurl}/images 
    Request 
    It accepts a json request 
    {
      "location" : "path/to/image"
    }
    It responds with following parameter 
    {
    "id":"<uuid>,
    "name" : <string>
    }
 2. get an image - GET call to {baseurl}/images/<image_id>
  No payload required 
  It responds with following parameter 
    {
    "id":"<uuid>,
    "name" : <string>,
    "tags": null
    }
3. Get all image GET call to {baseurl}/images
  No payload required 
  It responds with list of array with following parameter 
    {
    "id":"<uuid>,
    "name" : <string>,
    "tags": <string>
    }
4. Adding tags to an image POST call to {baseurl}/images/<image_id>/tags
  Request 
  It accepts a json request 
    {
      "tags" : "<list_of_comma_separated_tags>"
    }
  {
    "id":"<uuid>,
    "name" : <string>,
    "tags": "<list_of_comma_separated_tags>"
    }
    
    
  
