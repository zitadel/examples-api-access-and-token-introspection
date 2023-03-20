# Secure an API in ZITADEL using Basic Authentication

## ToC
1. [Register the API in ZITADEL](#1)
2. [Run this API](#2)
3. [Invoke this API](#3)


## 1. Register the API in ZITADEL<a name="1"></a>

1. Go to your Project and click on the **New** button as shown below. 

<img
    src="screenshots/1.png"
    width="75%"
    alt="Register the API"
/>

2.  Give a name to your application (Test API is the name given below) and select type **API**. 

<img
    src="screenshots/2.png"
    width="75%"
    alt="Register the API"
/>

3. Select **JWT** as the authentication method and click **Continue**.  

<img
    src="screenshots/3.png"
    width="75%"
    alt="Register the API"
/>

4. Now review your configuration and click **Create**.   

<img
    src="screenshots/4.png"
    width="75%"
    alt="Register the API"
/>

5. You will now see the API’s **Client ID**. You will not see a Client Secret because we are using a private JWT key.   

<img
    src="screenshots/5.png"
    width="75%"
    alt="Register the API"
/>

6. Next, we must create the key pairs. Click on **New**.   

<img
    src="screenshots/6.png"
    width="75%"
    alt="Register the API"
/>

7. Select **JSON** as the type of key. You can also set an expiration time for the key or leave it empty. Click on **Add**.   

<img
    src="screenshots/7.png"
    width="75%"
    alt="Register the API"
/>

8. Download the created key by clicking the **Download** button and then click **Close**.   

<img
    src="screenshots/8.png"
    width="75%"
    alt="Register the API"
/>

9. The key will be downloaded.   

<img
    src="screenshots/9.png"
    width="75%"
    alt="Register the API"
/>

10. When you click on URLs on the left, you will see the relevant OIDC URLs. Note down the **issuer** URL, **token_endpoint** and **introspection_endpoint**.  

<img
    src="screenshots/10.png"
    width="75%"
    alt="Register the API"
/>

11. The key that you downloaded will be of the following format. 
```
{
  "type":"application",
  "keyId":"<YOUR_KEY_ID>",
  "key":"-----BEGIN RSA PRIVATE KEY-----\<YOUR_PRIVATE_KEY>\n-----END RSA PRIVATE KEY-----\n",
  "appId":"<YOUR_APP_ID>",
  "clientId":"<YOUR_CLIENT_ID>"
}
```
12. Also note down the **Resource ID** of your project.   

<img
    src="screenshots/11.png"
    width="75%"
    alt="Register the API"
/>

## 2. Run this API <a name="2"></a>

The API has three routes:

- "/api/public" - No access token is required.
- "/api/private" - A valid access token is required.
- "/api/private-scoped" - A valid access token and a "read:messages" scope are required.


1. cd to this directory: `cd api-basic-authentication`
2. Replace the values of ZITADEL_DOMAIN, ZITADEL_INTROSPECTION_URL, API_CLIENT_ID and API_CLIENT_SECRET in the .env file with your values you obtained earlier. 
3. Run the API by running `python3 server.py` in the terminal. 


## 3. Invoke this API <a name="3"></a>

Obtain an access token as a ZITADEL service user via one of the following approaches (click the links to see instructions on how to obtain the token and invoke this API): 
- [JSON Web Token Profile](https://github.com/dakshitha/api-access-and-token-introspection/tree/main/service-user-jwt)
- [Client Credentials](https://github.com/dakshitha/api-access-and-token-introspection/tree/main/service-user-client-credentials) 
- [Personal Access Token](https://github.com/dakshitha/api-access-and-token-introspection/tree/main/service-user-pat)



