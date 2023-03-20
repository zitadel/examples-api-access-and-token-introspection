# Call a Secured API Using Client Credentials

## ToC
1. [Prerequisites](#1)
2. [Create a Service User and Private/Public Keys in ZITADEL](#2)
3. [Generate a Token](#3)
4. [Invoke the API](#4)

## 1. Prerequisites <a name="1"></a>

You must have the backend API running and secured with one of the following ways (follow either links for instructions on how to set up and run the API): 

1. [JSON Web Token (JWT) Profile](https://github.com/dakshitha/api-access-and-token-introspection/tree/main/api-jwt)
2. [Basic Authentication](https://github.com/dakshitha/api-access-and-token-introspection/tree/main/api-basic-authentication)

## 2. Create a Service User with Client Credentials in ZITADEL <a name="2"></a>

1. Go to the **Users** tab in your organization as shown below and click on the **Service Users** tab. To add a service user, click on the **New** button.

<img
    src="screenshots/1.png"
    width="75%"
    alt="Register the API"
/>


2. Next, add the details of the service user and select either **Bearer** or **JWT** for **Access Token Type** and click on **Create**. For this example, we will select **Bearer**.  

<img
    src="screenshots/2.png"
    width="75%"
    alt="Register the API"
/>


3. Click on **Actions**. 

<img
    src="screenshots/3.png"
    width="75%"
    alt="Register the API"
/>


4. Select **Generate Client Secret**. 

<img
    src="screenshots/4.png"
    width="75%"
    alt="Register the API"
/>


5. Copy your Client ID and Client Secret. Click **Close**. 

<img
    src="screenshots/5.png"
    width="75%"
    alt="Register the API"
/>


6. Next we will add a role to the created service user. Click on **Authorizations** and click on **New** as shown below: 

<img
    src="screenshots/6.png"
    width="75%"
    alt="Register the API"
/>


7. The user is already selected for you. Now select the **Project**. 

<img
    src="screenshots/7.png"
    width="75%"
    alt="Register the API"
/>


8. You will see the following screen afterwards. Click on **Continue**. 

<img
    src="screenshots/8.png"
    width="75%"
    alt="Register the API"
/>

<img
    src="screenshots/9.png"
    width="75%"
    alt="Register the API"
/>

<img
    src="screenshots/10.png"
    width="75%"
    alt="Register the API"
/>


9. The downloaded key will be of the following format: 

```
{
    "type":"serviceaccount",
    "keyId":"<YOUR_KEY_ID>",
    "key":"-----BEGIN RSA PRIVATE KEY-----\n<YOUR_KEY>\n-----END RSA PRIVATE KEY-----\n",
    "userId":"<YOUR_USER_ID>"
}
```

## 3. Generate a Token <a name="3"></a>

1. cd to this directory: `cd service-user-jwt`
2. Copy the content in your downloaded key file to `client-key-file.json`.
3. Replace the values of PROJECT_ID, ZITADEL_DOMAIN and ZITADEL_TOKEN_URL n the .env file with your values you obtained earlier.
4. Run the script to generate a token by running `python3 jwt-profile-token-generator.py` in the terminal.
5. Copy the printed access token and set the value to a shell variable called `TOKEN` as shown below: 

<img
    src="screenshots/9.png"
    width="75%"
    alt="Register the API"
/>

## 4. Invoke the API with Token

The API has three routes:

- "/api/public" - No access token is required.
- "/api/private" - A valid access token is required.
- "/api/private-scoped" - A valid access token and a "read:messages" scope are required.

1. Invoke the public resource using the following cURL command:

`curl -X GET http://localhost:5000/api/public`

You should get a response with Status Code 200 and the following message.

`{"message":"Public route - You don't need to be authenticated to see this."}`

2. Invoke the private resource using the following cURL command:

`curl -X GET -H "Authorization: Bearer $TOKEN" http://localhost:5000/api/private`

You should get a response with Status Code 200 and the following message.

`{"message":"Private route - You need to be authenticated to see this."}`

If you invoke the same resource without an access token (i.e., `curl -X GET http://localhost:5000/api/private`), you will see a 401 error. 

3. Invoke the private route that requires the user to have a certain role using the following cURL command: 

`curl -X GET -H "Authorization: Bearer $TOKEN" http://localhost:5000/api/private-scoped`

You should then get a Status Code 403, Forbidden error because the user does not have the role `read:messages`.

In order to access this route, you must create the role `read:messages` in your ZITADEL project and also create an authorization for the service user you created by adding the role to the user. Follow these steps to do so: 

1. Go to your project and select **Roles**. Click **New**. 

<img
    src="screenshots/scopes/1.png"
    width="75%"
    alt="Register the API"
/>

2. Add the `read:messages` role as shown below and click **Save**. 

<img
    src="screenshots/scopes/2.png"
    width="75%"
    alt="Register the API"
/>

3. You will see the created role listed. 

<img
    src="screenshots/scopes/3.png"
    width="75%"
    alt="Register the API"
/>

4. To assign this role to a user, click on **Authorizations**. 
<img
    src="screenshots/scopes/4.png"
    width="75%"
    alt="Register the API"
/>

5. Select the user you want to assign the role to. 
<img
    src="screenshots/scopes/5.png"
    width="75%"
    alt="Register the API"
/>

6. Select the project where this authorization is applicable. 
<img
    src="screenshots/scopes/6.png"
    width="75%"
    alt="Register the API"
/>

7. Click **Continue**.
<img
    src="screenshots/scopes/7.png"
    width="75%"
    alt="Register the API"
/>

8. Select the role **read:messages** and click **Save**. 
<img
    src="screenshots/scopes/8.png"
    width="75%"
    alt="Register the API"
/>

9. You will now see the your service user has been assigned the role **read:messages**. 
<img
    src="screenshots/scopes/9.png"
    width="75%"
    alt="Register the API"
/>

Regenerate the token and invoke the protected resource again: 

`curl -X GET -H "Authorization: Bearer $TOKEN" http://localhost:5000/api/private-scoped`

You should get a response with Status Code 200 and the following message.

`{"message":"Private, scoped route - You need to be authenticated and have the role read:messages to see this."}`

## 5. Reference
https://zitadel.com/docs/guides/integrate/serviceusers#3-with-this-jwt-request-an-oauth-token-from-zitadel


