## DESCRIPTION

The Tech News Scrapper is a project written in Python that scrapes tech news from Trybe's news blog, processes them and saves them in a MongoDB instance run as a Docker container. The user can interact with the application through the terminal to scrape the desired number of news, as well as filter them.

## STACKS

-   Python

#### The files I have worked on are indicated in the diagram below. Other files, such as database configs, Dockerfile, docker-compose and reading_plan.py were provided by Trybe's team.

```
.
├── tech_news
│   ├── analyzer
│   │   ├── ratings.py
│   │   └── search_engine.py
│   ├── menu.py
│   └── scraper.py
└── tests
    └── reading_plan
        └── test_reading_plan.py
```

## Intructions for running the applications locally

(expected python installed locally)

1. Clone the repository  
   `git clone git@github.com:P-dPF/tech-news-scrapper.git`
2. Navigate into the directory created in the previous step  
   `cd tech-news-scrapper`
3. Create virtual environment  
   `python3 -m venv .venv && source .venv/bin/activate`
4. Install depedencies  
   `python3 -m pip install -r dev-requirements.txt`
5. Pull MongoDB image from docker and run its container  
   `docker-compose up -d mongodb`
6. Run the application  
   `tech-news-analyzer`

Interact with the application accordingly to the numbers in each instruction.
