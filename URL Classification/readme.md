There are 5 features like long url, have @ symbol, presence of  redirection, presence of prefix suffix separation, no of subdomains.
Features are extracted by applying functions to URLs and constructing a new dataframe.
Classification is done using Randomforest.

Features
1) URL’s having “@” Symbol
Using “@” symbol in the URL leads the browser to ignore everything preceding the “@” symbol and the real address often follows the “@” symbol. URL containing “@” symbol is considered phishing.

2) Number of Subdomains
If no. of subdomains are greater than 3 then its likely phishing because more no of subdomain means the subdomain name and path is fully cantrollable by phisher.

3) Redirecting using “//”
The existence of “//” within the URL path means that the user will be redirected to another website
http://www.legitimate.com//http://www.phishing.com

4)Adding Prefix or Suffix Separated by (-) to the Domain
The dash symbol is rarely used in legitimate URLs. Phishers tend to add prefifixes or suffiffiffixes separated by (-) to the domain name so that users feel that they are dealing witha legitimate webpage.
 http://www.Confirme-paypal.com/

5)Long URL to Hide the Suspicious Part
http://federmacedoadv.com.br/3f/aze/ab51e2e319e51502f416dbe46b773a5e/?cmd=_home&amp;dispatch=11004d58f5b74f8dc1e7c2e8dd4105e811004d58f5b74f8dc1e7c2e8dd4105e8@phishing.website.html



