# api-access-and-token-introspection


## API Application:
If you have an API that behaves as an OAuth resource server that can be accessed by user-facing applications and need to validate an access token by calling the ZITADEL introspection API, you can use the following methods to register these APIs in ZITADEL: 

- [JSON Web Token (JWT) Profile (Recommended)](https://zitadel.com/docs/apis/openidoauth/authn-methods#client-secret-basic) 
  - [Test JWT Profile for API Applications](https://github.com/dakshitha/api-access-and-token-introspection/tree/main/api-jwt)
- [Basic Authentication](https://zitadel.com/docs/apis/openidoauth/authn-methods#client-secret-basic) 
  - [Test Basic Authentication for API Applications](https://github.com/dakshitha/api-access-and-token-introspection/tree/main/api-basic-authentication)



## Service Users:
If there are client APIs or systems that need to access other protected APIs, these APIs or systems must be declared as service users. A service user is not considered an application type in ZITADEL. The following mechanisms are available for service users to obtain an access token: 

- [JSON Web Token (JWT) Profile  (Recommended)](https://zitadel.com/docs/guides/integrate/serviceusers) 
  - [Test JWT Profile for Service Users](https://github.com/dakshitha/api-access-and-token-introspection/tree/main/service-user-jwt)
- [Client Credentials](https://zitadel.com/docs/guides/integrate/client-credential) 
  - [Test Client Credentials for Serivce Users](https://github.com/dakshitha/api-access-and-token-introspection/tree/main/service-user-client-credentials)
- [Personal Access Tokens (PAT)](https://zitadel.com/docs/guides/integrate/pat) 
  - [Test Personal Access Tokens for Service Users](https://github.com/dakshitha/api-access-and-token-introspection/tree/main/service-user-pat)
  

## Prerequisites to Run the Samples: 

- Have Python3 installed in your machine.
- Create a free ZITADEL account here - https://zitadel.cloud/
- Create an instance as explained [here](https://zitadel.com/docs/guides/start/quickstart#2-create-your-first-instance). 
- Create a new project in your instance by following the steps [here](https://zitadel.com/docs/guides/start/quickstart#2-create-your-first-instance).


