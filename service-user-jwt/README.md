# Call a Secured API Using JSON Web Token (JWT) Profile 

## ToC
1. [Create a Service User and Private/Public Keys in ZITADEL](#1)
2. [Generate a Token](#2)
3. [Invoke the API](#3)


## 1. Create a Service User and Private/Public Keys in ZITADEL <a name="1"></a>

1. Go to the **Users** tab in your organization as shown below and click on the **Service Users** tab.

<img
    src="screenshots/1.png"
    width="75%"
    alt="Register the API"
/>


2. To add a service user, click on the **New** button. 

<img
    src="screenshots/2.png"
    width="75%"
    alt="Register the API"
/>


3. Next, add the details of the service user and select either **Bearer** or **JWT** for Access Token Type and click on **Create**. For this example, we will select **JWT**. 

<img
    src="screenshots/3.png"
    width="75%"
    alt="Register the API"
/>


4. Now you will see the saved details. 

<img
    src="screenshots/4.png"
    width="75%"
    alt="Register the API"
/>


5. Next,  we need to generate a private-public key pair in ZITADEL and you must get the private key to sign your JWT.  Go to **Keys** and click on **New**.

<img
    src="screenshots/5.png"
    width="75%"
    alt="Register the API"
/>


6. Select type **JSON** and click **Add**. 

<img
    src="screenshots/6.png"
    width="75%"
    alt="Register the API"
/>


7. Download the key by clicking **Download**. After the download, click **Close**. 

<img
    src="screenshots/7.png"
    width="75%"
    alt="Register the API"
/>


8. You will see the following screen afterwards. 

<img
    src="screenshots/8.png"
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


