## Gauth

Authenticaltion APP for Frappe ERPNext by ERPGulf

#### License

mit# GAuth




## Generate token and refresh_key (GET)

The generate token secure API is designed to facilitate secure authentication and token generation for accessing resources within the system.It generate token and refresh key.Here the request parameters are api key, api secret and app key. user-related parameters are included in the request headers as cookies.

### Request

```
curl --location '/api/method/gauth.gauth.gauth.generate_token_secure' \
--header 'Cookie: full_name=Guest; sid=Guest; system_user=no; user_id=Guest; user_image=; full_name=Guest; sid=Guest; system_user=yes; user_id=Guest; user_image=' \
--form 'api_key="73935669a6be77a@erpgulf.com"' \
--form 'api_secret="K9sLpQvZrFyWm7N3"' \
--form 'app_key="MzM1ZjdkMmUzMzgxNjM1NWJiNWQwYzE3YjY3YjMyZDU5N2E3ODRhZmE5NjU0N2RiMWVjZGE0ZjE4OGM1MmM1MQ=="' \
--form 'client_secret="cfd619c909"'
```
### Response
```
{
    "data": {
        "access_token": "3FXrkLLCsFZL9GvU3kXOIcaCtnBrqB",
        "expires_in": 3600,
        "token_type": "Bearer",
        "scope": "all openid",
        "refresh_token": "QIEnLPBgrm7He0w8luRZWlcjHr5eX7"
    }
}

```

## Generate token for Users (GET)
This API is designed to securely generate authentication tokens for users based on their provided credentials and application key. It generate  each users token and refresh key. we pass the token that get from  generate token and refresh key  api to authenication bearer token field . Here the  parameters are api key, api secret and app key,user_name,password. user-related parameters are included in the request headers as cookies.
### Request

```
curl --location '/api/method/gauth.gauth.gauth.generate_token_secure_for_users' \
--header 'Cookie: full_name=Guest; sid=Guest; system_user=no; user_id=Guest; user_image=; full_name=Guest; sid=Guest; system_user=yes; user_id=Guest; user_image=; full_name=Guest; sid=Guest; system_user=yes; user_id=Guest; user_image=' \
--header 'Authorization: Bearer 3FXrkLLCsFZL9GvU3kXOIcaCtnBrqB' \
--form 'api_key="73935669a6be77a@erpgulf.com"' \
--form 'api_secret="K9sLpQvZrFyWm7N3"' \
--form 'app_key="MzM1ZjdkMmUzMzgxNjM1NWJiNWQwYzE3YjY3YjMyZDU5N2E3ODRhZmE5NjU0N2RiMWVjZGE0ZjE4OGM1MmM1MQ=="' \
--form 'client_secret="cfd619c909"' \
--form 'username="rishal@testgmail.com1"' \
--form 'password="rishal@123"'
```
### Response
```
{
    "data": {
        "token": {
            "access_token": "AgSUgPwZzuO9TSlcwPK64NIJNFNBBY",
            "expires_in": 3600,
            "token_type": "Bearer",
            "scope": "all openid",
            "refresh_token": "zNVB71XJzJM9sr0wZAoWH5gzTxBid5"
        },
        "user": {
            "id": "rishal@testgmail.com1",
            "full_name": "rishal",
            "email": "rishal@testgmail.com1",
            "phone": "12398712312"
        }
    }
}

```

## User available or not (GET)
This api checks the availability of a user based on either their email or mobile phone number.parameters are user email and phone number, Here authentication  is required,user-related parameters are included in the request headers as cookies.
### Request

```
curl --location --request GET 'api/method/gauth.gauth.gauth.is_user_available' \
--header 'Authorization: Bearer 3FXrkLLCsFZL9GvU3kXOIcaCtnBrqB' \
--header 'Cookie: full_name=Guest; sid=Guest; system_user=yes; user_id=Guest; user_image=' \
--form 'mobile_phone="55124924"' \
--form 'user_email="mumtaz32@erpgulf.com3"'
```
### Response
```
{
    "message": "Mobile exists",
    "user_count": 1
}
```

## create user (POST)
  This api  creating a new user and related records in a system,parameters are full_name,password,mobile_no,email,id,role, Here authentication  is required.user-related parameters are included in the request headers as cookies.
### Request

```
curl --location 'api/method/gauth.gauth.gauth.g_create_user' \
--header 'Authorization: Bearer 3FXrkLLCsFZL9GvU3kXOIcaCtnBrqB' \
--header 'Cookie: full_name=Guest; sid=Guest; system_user=yes; user_id=Guest; user_image=' \
--form 'full_name="Aysha"' \
--form 'password="Friday2000@$"' \
--form 'mobile_no="323232243"' \
--form 'email="72763671@erpgulf.com"' \
--form 'role="Auction"' \
--form 'id=""'

```
### Response
```
{
    "message": "User already exists",
    "user_count": 1
}
```

## who am i (GET)
Api is used to get the username of token which used in bearer token for authentication,The primary purpose of this api is to return the current user's information,Here authentication is required.user-related parameters are included in the request headers as cookies.
### Request

```
curl --location 'api/method/gauth.gauth.gauth.whoami' \
--header 'Authorization: Bearer 3FXrkLLCsFZL9GvU3kXOIcaCtnBrqB' \
--header 'Cookie: full_name=Guest; sid=Guest; system_user=yes; user_id=Guest; user_image='

```
### Response
```
{
    "data": {
        "user": "73935669a6be77a@erpgulf.com"
    }
}
```

## delete user (DELETE)
 Api is designed for deleting user records. It takes three parameters username, email, and mobile_no  to identify the user to be deleted. This api verifies the existence of the user based on these parameters, and if found, deletes the user record from the database.Authentication is required.user-related parameters are included in the request headers as cookies.
### Request

```
curl --location 'api/method/gauth.gauth.gauth.g_delete_user' \
--header 'Authorization: Bearer 3FXrkLLCsFZL9GvU3kXOIcaCtnBrqB' \
--header 'Cookie: full_name=Mumtaz%2032; sid=834d08adda118bf4a9761bade5ab686f4afcdd40db680ff103663ea7; system_user=yes; user_id=mumtaz32%40erpgulf.com; user_image=' \
--form 'email="25801478@erpgulf.com"' \
--form 'mobile_no=""' \
--form 'username="sfdwsw"'
```
### Response
```
{
    "message": "User not found",
    "user_count": 0
}
```



## get user name (GET)
Api is used to retrieve user details from a Frappe-based system based on either the user's email address or mobile phone number. The api allows flexibility by accepting one of these parameters as input. It fetches information such as the user's name and whether the user is enabled or not. Authentication is required,user-related parameters are included in the request headers as cookies.

### Request

```
curl --location --request GET 'api/method/gauth.gauth.gauth.get_user_name' \
--header 'Authorization: Bearer IYPuOij4ywRPGHEfWQJgYNdrJxzUzh' \
--header 'Cookie: full_name=Guest; sid=Guest; system_user=yes; user_id=Guest; user_image=' \
--form 'user_email="72763671@erpgulf.com"' \
--form 'mobile_phone="72763671"'
```
### Response
```
{
    "data": [
        {
            "name": "72763671@erpgulf.com",
            "enabled": 1
        }
    ],
    "user_count": 0
}
```

##  update password (POST)
 This api is used to update the password for a user in a system.it takes a username and a new password as parameters and ensures the password update is performed securely.Here authentication  is required.user-related parameters are included in the request headers as cookies. needed.
### Request

```
curl --location 'api/method/gauth.gauth.gauth.g_update_password' \
--header 'Authorization: Bearer IYPuOij4ywRPGHEfWQJgYNdrJxzUzh' \
--header 'Cookie: full_name=Guest; sid=Guest; system_user=yes; user_id=Guest; user_image=' \
--form 'username="72763671@erpgulf.com"' \
--form 'password="Friday"'
```
### Response
```
{
    "message": "Password successfully updated",
    "user_count": 1
}
```

## create_user (POST)
This api is  designed to create new user accounts in a system. It takes several parameters such as full_name, password, mobile_no, email, id, and an optional role.Here authentication  is required.user-related parameters are included in the request headers as cookies. needed.

### Request

```
curl --location --request GET 'api/method/gauth.gauth.gauth.is_user_available' \
--header 'Authorization: Bearer 3FXrkLLCsFZL9GvU3kXOIcaCtnBrqB' \
--form 'mobile_phone="72763671"' \
--form 'user_email="72763671@erpgulf.com"'
```
### Response
```
{
    "reset_key": "261907",
    "generated_time": "2024-02-12 07:35:21.903321",
    "URL": "https://erp.dallahmzad.com:8012/update-password?key=261907"
}
```

<!-- ##  test passwordstrength

### Request

```
curl --location --request GET '/api/method/frappe.core.doctype.user.user.test_password_strength' \
--header 'Authorization: Bearer EaIt6IRFwJNcu3LSebgtT0wfs4Cz8i' \
--header 'Cookie: full_name=Guest; sid=Guest; system_user=yes; user_id=Guest; user_image=' \
--form 'new_password="&^&*JKJ&^WD878BHerw"'
```
### Response
```
{
    "message": {}
}

``` -->

## Enable  or disable user (POST)
This api is designed to enable or disable a user in a system based on the provided parameters.Here authentication  is required.user-related parameters are included in the request headers as cookies  needed.

### Request

```
curl --location '/api/method/gauth.gauth.gauth.g_user_enable' \
--header 'Authorization: Bearer rSO1GXm41IXbyrK8VSJDrBlM6bBHyn' \
--header 'Cookie: full_name=Guest; sid=Guest; system_user=yes; user_id=Guest; user_image=' \
--form 'username="72763671@erpgulf.com1"' \
--form 'email="72763671@erpgulf.com1"' \
--form 'mobile_no="727636711"' \
--form 'enable_user="True"'
```
### Response
```
{
    "message": "User successfully enabled ",
    "user_count": 1
}
```

## Current time (GET)
This api shows the current time.
### Request

```
curl --location '/api/method/gauth.gauth.gauth.time' \
--header 'Cookie: full_name=Guest; sid=Guest; system_user=yes; user_id=Guest; user_image='
```
### Response
```
{
    "message": {
        "data": {
            "serverTime": "2024-02-12 08:09:00.081533",
            "unix_time": 1707714540.081707
        }
    }
}

``` 

## get account balance (GET)
This api is designed to find the balance of a user, here authentication is required, which user token is passed here that user account balance we get.

### Request
```
curl --location --request GET 'api/method/gauth.gauth.gauth.get_account_balance' \
--header 'Authorization: Bearer YYVazI6ZM6dKh1JBeaQy6jzl8CTQBe' \
--header 'Cookie: full_name=Guest; sid=Guest; system_user=yes; user_id=Guest; user_image=' \
--form 'customer="mumtaz32@erpgulf.com"' \
--form 'mobile_phone="323232422"'
```
### Response

```
{
    "data": {
        "balance": 0.0
    }
}
```