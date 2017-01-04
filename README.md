# counters.json
Display Counters as json.

This service receives a comma separated string containing the keys of the counters. Calls Redis and fetches those
counters and returns a JSON file with all the aggregated counters.


        -> % curl localhost:5000/visits,signups,password_reset,error500,error404
            {
              "counters": {
                "visits": "2098",
                "signups": "145",
                "password_reset": "12",
                "error500": "1",
                "error404": "5"
              }
            }

