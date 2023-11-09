# Handling-APIGW-HTTP-API-cookies
Currently when you integrate AWS API Gateway HTTP API with Lambda, a cookie header value wrapped with double quotes ("") which is passed to the Lambda backend gets stripped automatically by API Gateway. 

This may affect business logic and cleanliness as values passed to API Gateway are not identical in the Lambda function's payload. 

This script demonstrates how we can re-add the double quotes in a unified way (ie. handles both cases where double quotes are present or not). 

Note: This only takes into account cookie values that require the values to be wrapped in double quotes. If not your requirement, you may ingore this post. 
