# Technical documentation for the properties module

## Properties

The properties module provides a way to manage properties listed in the system. It is used to create, update, delete, and list properties.

Main endpoint: `/properties`

### Create a property

To create a property, you need to provide the following information:

- Name
- Description
- Type
- City
- Country
- Owner
- Price
- Image

Specific endpoint: `/properties/create`
HTTP Method: POST
Content-Type: application/json
Body structure:
```
{
    "name": string (required, up to 100 characters),
    "description": string (required, up to 5000 characters),
    "type": string (required, up to 100 characters) - one chosen from 'House', 'Flat', 'Apartment', 'Studio',
    "city": string (required, up to 100 characters),
    "country": string (required, up to 100 characters),
    "owner": 
        {
            "name": string (required, up to 100 characters),
            "email": string (required, up to 100 characters),
            "phone": string (required, up to 100 characters),
            "notes": string (up to 5000 characters)
        },
    "price": float (required) - price in USD,
    "image": string (required) - URL to the image
}
```

Sample request:
```
POST /properties/create
Content-Type: application/json
{
    "name": "Beautiful house in the countryside",
    "description": "A beautiful house in the countryside with a large garden and a swimming pool.",
    "type": "House",
    "city": "Countryside",
    "country": "USA",
    "owner": 
        {
            "name": "John Doe",
            "email": "john.doe@example.com",
            "phone": "+1234567890",
            "notes": "Owner is willing to negotiate the price."
        },
    "price": 500000.00,
    "image": "https://example.com/house.jpg"
}
```
Sample success response:
```
201 Created
{
    "message": "Success",
    "property": 1,
    "photo": 12
}
```

Error response: 
```
400 Bad Request
{
    "message": "Bad request",
}
```