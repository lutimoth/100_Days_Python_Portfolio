# habit tracker
import os
from datetime import datetime
from dotenv import load_dotenv
import requests

load_dotenv()

PIXELA_TOKEN = os.getenv("PIXELA_TOKEN")
PIXELA_USER = os.getenv("PIXELA_USER")
GRAPH_ID = "graph1"
CURRENT_DAY = datetime.now().strftime("%Y%m%d")

pixela_endpoint = "https://pixe.la/v1/users"
create_endpoint = f"{pixela_endpoint}/{PIXELA_USER}/graphs"
graph_endpoint = f"{pixela_endpoint}/{PIXELA_USER}/graphs/{GRAPH_ID}"
delete_endpoint = f"{graph_endpoint}/{CURRENT_DAY}"

headers ={
    "X-USER-TOKEN": PIXELA_TOKEN
}


# user_params = {
#     "token": PIXELA_TOKEN,
#     "username": PIXELA_USER,
#     "agreeTermsOfService":"yes",
#     "notMinor":"yes"
# }

# create_params = {
#     "id":GRAPH_ID,
#     "name":"Coding Graph",
#     "unit":"days",
#     "type":"int",
#     "color":"momiji"
# }
# graph_req = requests.post(url=create_endpoint, json=create_params, headers=headers)
# print(graph_req.text)

# Updating Graph with PUT request
# put_params = {
#     "unit": "GIT Commits"
# }
# put_graph = requests.put(url=graph_endpoint, json=put_params, headers=headers)


#How to post a point to the tracker

commits = input("How many commits did you make today?:")

post_params = {
    "date": CURRENT_DAY,
    "quantity": commits
}

post_graph = requests.post(url=graph_endpoint, json=post_params,headers=headers)
print(post_graph.text)

#delete a point
delete_point = requests.delete(url=delete_endpoint, headers=headers)
print(delete_point.text)


