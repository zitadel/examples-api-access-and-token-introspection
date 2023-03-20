# Secure an API in ZITADEL using the JSON Web Token Profile

## 1. Register the API in ZITADEL and Generate Private and Public Keys

1. Go to your Project and click on the **New** button as shown below. 
2.  Give a name to your application (Test API is the name given below) and select type **API**. 
3. Select **JWT** as the authentication method and click **Continue**.  
4. Now review your configuration and click **Create**. 
5. You will now see the API’s **Client ID**. You will not see a Client Secret because we are using a private JWT key. 
6. Next, we must create the key pairs. Click on **New**. 
7. Select **JSON** as the type of key. You can also set an expiration time for the key or leave it empty. Click on **Add**. 
8. Download the created key by clicking the **Download** button and then click **Close**. 
9. The key will be downloaded. 
10. When you click on URLs on the left, you will see the relevant OIDC URLs. Note down the **issuer** URL, **token_endpoint** and **introspection_endpoint**.
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



