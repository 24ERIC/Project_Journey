# 3-Web-Scraping

# Note
- collect content and data from the internet
- Web scraping applications (or ‘bots’)
    - visit websites
    - grab the relevant pages 
    - extract useful information
- extract huge amounts of data in a very short time
- web scraper function
    - Step 1: Making an HTTP request to a server
    - Step 2: Extracting and parsing (or breaking down) the website’s code
        - extract the site’s HTML or XML code
            - XML (Extensible Markup Language) is a markup language similar to HTML,
            ```xml
                <?xml version="1.0" encoding="UTF-8"?>

                <?xml version="1.0" encoding="UTF-8"?>
                <message>
                    <warning>
                        Hello World
                    </warning>
                </message>

                <?xml version="1.0" encoding="UTF-8"?>
                <!DOCTYPE body [
                <!ENTITY warning "Warning: Something bad happened... please refresh and try again.">
                ]>
                <body>
                <message> &warning; </message>
                </body>

            ```
        - specific text, ratings, classes, tags, IDs, or other information.
        -  accessed, scraped, and parsed,
    - Step 3: Saving the relevant data locally
        - .csv or .xls
            - An XLS file is a Microsoft Excel 97-2003 Worksheet file.
            - Convert to XLSX, CSV, PDF, and others with those same programs.
            - XLS files store data in tables of rows and columns with support for formatted text, images, charts, and more. 
- How to scrape the web (step-by-step)
    - Step one: Find the URLs you want to scrape
    - Step two: Inspect the page
    - Step three: Identify the data you want to extract
    - Step four: Write the necessary code
        - if you’re looking for book reviews, you’ll want information such as the book title, author name, and rating.
    - Step five: Execute the code
    - Step six: Storing the data
        - Python Regex module (short for ‘regular expressions’) to extract a cleaner set of data that’s easier to read.
    - 5. What tools can you use to scrape the web?
        - BeautifulSoup
            - another Python library, commonly used to parse data from XML and HTML documents.
        - Scrapy
            - Python-based application framework that crawls and extracts structured data from the web
            - data mining, information processing, and for archiving historical content
            - web scraping
            - general-purpose web crawler, or to extract data through APIs
        - Pandas
            - multi-purpose Python library used for data manipulation and indexing. 
            - can be used to scrape the web in conjunction with BeautifulSoup.
        - Parsehub
- key
    - Have you refined your target data?
    - Have you checked the site’s robots.txt?
    - Have you checked the site’s terms of service?
        - website’s terms of service (TOS)
        - formal clause outlining what you can and can’t do with the data on their site. 
    - Are you following data protection protocols?
    - Are you at risk of crashing a website?
- example1
    ```bash
        pip install beautifulsoup4
    ```
    ```python
        from bs4 import BeautifulSoup
    ```
- 
- 
- 
- 
- 
- 
- 