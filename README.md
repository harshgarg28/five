# CRUD API README

Welcome to the documentation for the CRUD API hosted at https://five-m1d0.onrender.com. This API provides endpoints for creating, reading, updating, and deleting posts.

## Endpoints

- **Create**: `POST /posts`
  - This endpoint is used to create a new entry in the database.

- **Read All Posts**: `GET /posts`
  - This endpoint retrieves all posts currently stored in the database.

- **Read Latest Post**: `GET /posts/latest`
  - This endpoint retrieves the latest post added to the database.

- **Read Post by ID**: `GET /posts/{id}`
  - This endpoint retrieves a specific post based on its unique identifier.

- **Update Post**: `PUT /posts/{id}`
  - This endpoint updates an existing post with the provided ID.

- **Delete Post**: `DELETE /posts/{id}`
  - This endpoint removes the post with the specified ID from the database.

## Usage

To interact with this API, you can send HTTP requests to the provided endpoints using your preferred method (e.g., using cURL commands, Postman, or any HTTP client library).

### Example Usage

#### Create a New Post

```http
POST /posts
Content-Type: application/json

{
  "title": "New Post",
  "content": "This is the content of the new post."
}
```

#### Get All Posts

```http
GET /posts
```

#### Get Latest Post

```http
GET /posts/latest
```

#### Get Post by ID

```http
GET /posts/{id}
```

Replace `{id}` with the ID of the post you want to retrieve.

#### Update Post

```http
PUT /posts/{id}
Content-Type: application/json

{
  "title": "Updated Post Title",
  "content": "Updated content goes here."
}
```

Replace `{id}` with the ID of the post you want to update.

#### Delete Post

```http
DELETE /posts/{id}
```

Replace `{id}` with the ID of the post you want to delete.

## Response Format

The API returns responses in JSON format, typically including the requested data or a relevant message.
