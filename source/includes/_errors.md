# Errors

The Majora API uses the following error codes:

Error Code | Meaning
---------- | -------
400 | Bad Request -- Your request is invalid or unauthorized (Majora never sends a 401).
403 | Forbidden -- You are not permitted to make this request.
404 | Not Found -- Your requested Artifact or Process could not be found.
429 | Too Many Requests -- You're requesting too many resources, try adding a small delay between queries.
500 | Internal Server Error -- Your action generated an error. Try again later. If the error persists, report to an administrator.
503 | Service Unavailable -- We're temporarily offline for maintenance. Please try again later.
