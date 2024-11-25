# File for storing customer profile information logic

class CustomerProfile:
    def __init__(self, name, address, phone_number, email):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.email = email

    def get_name(self):
        return self.name

    def get_address(self):
        return self.address

    def get_phone_number(self):
        return self.phone_number

    def get_email(self):
        return self.email

    def set_name(self, name):
        self.name = name

    def set_address(self, address):
        self.address = address

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    def set_email(self, email):
        self.email = email

    def update_profile(self, **kwargs):
        if "name" in kwargs:
            self.name = kwargs["name"]
        if "address" in kwargs:
            self.address = kwargs["address"]
        if "phone_number" in kwargs:
            self.phone_number = kwargs["phone_number"]
        if "email" in kwargs:
            self.email = kwargs["email"]
        
    @staticmethod
    def from_dict(customer_profile):
        return CustomerProfile(
            customer_profile["name"],
            customer_profile["address"],
            customer_profile["phone_number"],
            customer_profile["email"]
        )

    def to_dict(self):
        return {
            "name": self.name,
            "address": self.address,
            "phone_number": self.phone_number,
            "email": self.email
        }

    def __str__(self):
        return f"Name: {self.name}, Address: {self.address}, Phone Number: {self.phone_number}, Email: {self.email}"
    
    def __repr__(self):
        return str(self)
    
    def __eq__(self, other):
        return self.name == other.name and self.address == other.address and self.phone_number == other.phone_number and self.email == other.email
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __hash__(self):
        return hash((self.name, self.address, self.phone_number, self.email))


if __name__ == "__main__":
    customer_profile = CustomerProfile("John Doe", "1234 Main St", "123-456-7890", "johndoe@example.com")
    print(customer_profile)
    print(customer_profile.to_dict())
    print(CustomerProfile.from_dict(customer_profile.to_dict()))
    print(customer_profile == CustomerProfile.from_dict(customer_profile.to_dict()))