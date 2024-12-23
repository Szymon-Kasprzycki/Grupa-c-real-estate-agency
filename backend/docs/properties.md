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

Success response: 201 Created

