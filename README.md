# Webbot Microsoft 365 Admin Center example

This script showcases how one might use Webbot to access the MS365 Admin Center in an automated fashion. This example sets the Exchange online permissions for a list of users.

The script goes through the following steps:

- Open Chrome and navigate to the admin center
- Wait for input (pressing enter) to know when user has finished authenticating manually in the opened Chrome window
- Read list of user email addresses from a file, the filename must be given as the first parameter
- Iterate over users
  - Search for user
  - Open the user view
  - Navigate to Licences
  - Open App menu in Licences
  - Set checkmark for Exchange Online permission if not set
  - Save and close user view
