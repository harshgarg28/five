from fastapi import FastAPI, HTTPException, status, Query, Response
from pydantic import BaseModel
from typing import Optional
from random import randrange


app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    ratings: Optional[int] = None
    
    
my_list = [
    {"title": "Nu-Style", "content": "Standard book of the given name ", "id": 1},
    {"title": "Zebronics23", "content": "A Wireless Mouse bought by Harsh", "id": 2}
]


# CRUD operations
# Create (Create)

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
    post_dict = post.dict()
    post_dict["id"] = randrange(0, 1000000)
    my_list.append(post_dict)
    return {"data": post_dict}

# Read (GET)

@app.get("/posts")
def get_all_posts():
    return {"data": my_list}

@app.get("/posts/latest")
def get_latest_post():
    post = my_list[-1]
    return {"post_detail": post}

@app.get("/posts/{id}")
def get_post_by_id(id: int):
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with ID {id} not found")
    return {"post_detail": post}


# Update (PUT)

@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    indx = find_index_post(id)
    if indx is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with ID {id} does not exist")
    post_dict = post.dict()
    post_dict['id'] = id
    my_list[indx] = post_dict
    return {"message": f"Post with ID {id} successfully updated"}


# Delete (DELETE)

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    indx = find_index_post(id)
    if indx is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with ID {id} does not exist")
    my_list.pop(indx)
    return {"message": f"Post with ID {id} successfully deleted"}


# helper functions - find_post and find_index_post
def find_post(id):
    for p in my_list:
        if p["id"] == id:
            return p

def find_index_post(id):
    for i, p in enumerate(my_list):
        if p['id'] == id:
            return i
        

