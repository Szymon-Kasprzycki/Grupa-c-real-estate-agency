# Property template documentation

## General overview
This template allows users to create new property listings by filling out a web form. The form dynamically adjusts based on the selected property type (House, Flat, Apartment, or Studio).

---

## Fields

### 1. Common fields
These fields are required for all property types and have consistent data types and validation constraints.

| Field Name    | Data Type      | Validation Constraints                                    | Description                                |
|---------------|----------------|-----------------------------------------------------------|--------------------------------------------|
| `owner`       | JSON           | Must include first name, last name, email, and phone      | Contact details of the property owner.     |
| `name`        | String         | Max length: 100, Required                                 | Name of the property.                      |
| `description` | String         | Max length: 5000, Required                                | Detailed description of the property.      |
| `type`        | Enum (String)  | Values: "House", "Flat", "Apartment", "Studio". Required. | Type of the property.                      |
| `city`        | String         | Max length: 100, Required                                 | City where the property is located.        |
| `country`     | String         | Max length: 100, Required                                 | Country where the property is located.     |
| `price`       | Decimal (float)| Min: 1, Step: 0.01, Required                           | Price of the property in USD.              |
| `sqft`        | Decimal (float)| Min: 1, Step: 0.01, Required                              | Total square footage of the property.      |
| `photo_main`  | URL            | Valid URL format, Required                                | Main photo URL of the property.            |
| `photo`       | URL            | Valid URL format, Required                                | Additional photo URL of the property.      |

---

### 2. Dynamic fields by property type
The following fields are displayed dynamically based on the selected property type.

| Property Type | Field Name  | Data Type      | Validation Constraints                  |
|---------------|-------------|----------------|-----------------------------------------|
| **House**     | `bedrooms`  | Integer        | Min: 1, Required                        | 
|               | `bathrooms` | Integer        | Min: 1, Required                        | 
|               | `garage`    | Integer        | Min: 0, Required                        | 
|               | `lot_size`  | Decimal (float)| Min: 1, Required                        | 
| **Flat**      | `bedrooms`  | Integer        | Min: 1, Required                        | 
|               | `bathrooms` | Integer        | Min: 1, Required                        | 
| **Apartment** | `bedrooms`  | Integer        | Min: 1, Required                        | 
|               | `bathrooms` | Integer        | Min: 1, Required                        | 
| **Studio**    | `bathrooms` | Integer        | Min: 1, Required                        | 

---

## Validation notes

### Required fields
- All common fields are required for submission.
- Dynamic fields depend on the selected property type.

### Default values
- `garage`, `lot_size` and `bedrooms` default to `0` when not applicable.

### Dynamic adjustments
- The `showFields` JavaScript function dynamically updates the form to include only the fields relevant to the selected property type.

### URL validation
- The `photo_main` and `photo` fields must contain valid URLs.

---
