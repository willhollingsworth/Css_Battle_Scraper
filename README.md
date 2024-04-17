## A scraper to get CSS Battle solutions


### Issues
[CSSBattlesolution.com](https://www.cssbattlesolutions.com/) does not store the code solutions in the html on the website. 
### Options
- Grab the data from the linked gist file
    - All code is saved in [github gists](https://gist.github.com/Ullvang?direction=asc&sort=updated&language=html). Raw data in a gist [looks like this](https://gist.githubusercontent.com/Ullvang/887e5924aa27a6ecdfa0708ab3e334bd/raw/3481843e16cb77e4470f495be1a60db9883aeeb4/192-abstract-firefly.html)
        - This data can be retrieved via an api but the results are truncated ([See docs](https://docs.github.com/en/rest/gists/gists?apiVersion=2022-11-28#list-gists-for-a-user))
        - Could download the github search result's html and scrape them (messy and may be against TOS)
- try a browser simulator like selenium may make the imbedded gists files be included in the downloaded local HTML files 

