=================
POC: Python - HUG
=================

---------------
Getting Started
---------------

Prerequisites
=============

* Python 3.8+
* Pip

Requirements
============

Install::

    pip install -r requirements.txt

--------
Examples
--------

CLI
===

::

    › ./app.py
    __main__

    Available Commands:

            - dogs
            - dog

::

    › ./app.py dogs
    [{'name': 'German Shepherd Dog', 'abbreviation': 'GSD', 'id': 'a4594592-b7a5-11e9-be8d-acde48001122'}, {'name': 'Pomeranian', 'abbreviation': None, 'id': 'a4594678-b7a5-11e9-be8d-acde48001122'}, {'name': 'German Shepherd Dog', 'abbreviation': 'GSD', 'id': 'a45946be-b7a5-11e9-be8d-acde48001122'}, {'name': 'Australian Cattle Dog', 'abbreviation': 'ACD', 'id': 'a45946fa-b7a5-11e9-be8d-acde48001122'}, {'name': 'Pomeranian', 'abbreviation': None, 'id': 'a459472c-b7a5-11e9-be8d-acde48001122'}, {'name': 'German Shepherd Dog', 'abbreviation': 'GSD', 'id': 'a459475e-b7a5-11e9-be8d-acde48001122'}, {'name': 'Pomeranian', 'abbreviation': No ne, 'id': 'a4594786-b7a5-11e9-be8d-acde48001122'}, {'name': 'Pomeranian', 'abbreviation': None, 'id': 'a45947b8-b7a5-11e9-be8d-acde48001122'}, {'name': 'Pomeranian', 'abbreviation': None, 'id': 'a45947e0-b7a5-11e9-be8d-acde48001122'}, {'name': 'Australian Cattle Dog', 'abbreviation': 'ACD', 'id': 'a4594812-b7a5-11e9- be8d-acde48001122'}]


::

    › ./app.py dog
    usage: app.py [-h] id
    app.py: error: the following arguments are required: id

::

    › ./app.py dog $(uuidgen)
    {'abbreviation': 'ACD', 'id': '4c5efbfb-28f4-4533-8a83-3db54ecd48ca', 'name': 'Australian Cattle Dog'}

----
HTTP
----

::

    › hug -f app.py -p 8008

    /#######################################################################\
              `.----``..-------..``.----.
             :/:::::--:---------:--::::://.
            .+::::----##/-/oo+:-##----:::://
            `//::-------/oosoo-------::://.       ##    ##  ##    ##    #####
              .-:------./++o/o-.------::-`   ```  ##    ##  ##    ##  ##
                 `----.-./+o+:..----.     `.:///. ########  ##    ## ##
       ```        `----.-::::::------  `.-:::://. ##    ##  ##    ## ##   ####
      ://::--.``` -:``...-----...` `:--::::::-.`  ##    ##  ##   ##   ##    ##
      :/:::::::::-:-     `````      .:::::-.`     ##    ##    ####     ######
       ``.--:::::::.                .:::.`
             ``..::.                .::         EMBRACE THE APIs OF THE FUTURE
                 ::-                .:-
                 -::`               ::-                   VERSION 2.5.6
                 `::-              -::`
                  -::-`           -::-
    \########################################################################/

     Copyright (C) 2016 Timothy Edmund Crosley
     Under the MIT License


    Serving on :8008...
    127.0.0.1 - - [05/Aug/2019 10:27:39] "GET / HTTP/1.1" 404 1118
    127.0.0.1 - - [05/Aug/2019 10:30:20] "GET /dogs HTTP/1.1" 200 998
    127.0.0.1 - - [05/Aug/2019 10:32:29] "GET /dogs/ HTTP/1.1" 200 1020
    127.0.0.1 - - [05/Aug/2019 10:32:33] "GET /dogs/222548B0-D9D6-4815-958D-1B46DB7075C9 HTTP/1.1" 200 90

::

    HTTP/1.0 404 Not Found
    Date: Mon, 05 Aug 2019 17:27:39 GMT
    Server: WSGIServer/0.2 CPython/3.8.0b2+
    content-length: 1118
    content-type: application/json; charset=utf-8

    {
        "404": "The API call you tried to make was not defined. Here's a definition of the API to help you get going :)",
        "documentation": {
            "handlers": {
                "/dogs": {
                    "GET": {
                        "examples": [
                            "http://localhost/dogs"
                        ],
                        "outputs": {
                            "content_type": "application/json; charset=utf-8",
                            "format": "JSON (Javascript Serialized Object Notation)",
                            "type": "Dog"
                        }
                    }
                },
                "/dogs/{id}": {
                    "GET": {
                        "inputs": {
                            "id": {
                                "type": "A UUID field."
                            }
                        },
                        "outputs": {
                            "content_type": "application/json; charset=utf-8",
                            "format": "JSON (Javascript Serialized Object Notation)",
                            "type": "Dog"
                        }
                    }
                }
            }
        }
    }

::

    › http :8008/dogs
    HTTP/1.0 200 OK
    Date: Mon, 05 Aug 2019 17:30:20 GMT
    Server: WSGIServer/0.2 CPython/3.8.0b2+
    content-length: 998
    content-type: application/json; charset=utf-8

    [
        {
            "abbreviation": null,
            "id": "b2e8062e-b7a6-11e9-953e-acde48001122",
            "name": "Pomeranian"
        },
        {
            "abbreviation": null,
            "id": "b2e80750-b7a6-11e9-953e-acde48001122",
            "name": "Pomeranian"
        },
        {
            "abbreviation": "ACD",
            "id": "b2e80796-b7a6-11e9-953e-acde48001122",
            "name": "Australian Cattle Dog"
        },
        {
            "abbreviation": "GSD",
            "id": "b2e807c8-b7a6-11e9-953e-acde48001122",
            "name": "German Shepherd Dog"
        },
        {
            "abbreviation": "GSD",
            "id": "b2e807f0-b7a6-11e9-953e-acde48001122",
            "name": "German Shepherd Dog"
        },
        {
            "abbreviation": "ACD",
            "id": "b2e80818-b7a6-11e9-953e-acde48001122",
            "name": "Australian Cattle Dog"
        },
        {
            "abbreviation": "GSD",
            "id": "b2e80840-b7a6-11e9-953e-acde48001122",
            "name": "German Shepherd Dog"
        },
        {
            "abbreviation": null,
            "id": "b2e80868-b7a6-11e9-953e-acde48001122",
            "name": "Pomeranian"
        },
        {
            "abbreviation": "ACD",
            "id": "b2e80890-b7a6-11e9-953e-acde48001122",
            "name": "Australian Cattle Dog"
        },
        {
            "abbreviation": "ACD",
            "id": "b2e808b8-b7a6-11e9-953e-acde48001122",
            "name": "Australian Cattle Dog"
        }
    ]

::

    › http :8008/dogs/$(uuidgen)
    HTTP/1.0 200 OK
    Date: Mon, 05 Aug 2019 17:32:33 GMT
    Server: WSGIServer/0.2 CPython/3.8.0b2+
    content-length: 90
    content-type: application/json; charset=utf-8

    {
        "abbreviation": null,
        "id": "222548b0-d9d6-4815-958d-1b46db7075c9",
        "name": "Pomeranian"
    }
