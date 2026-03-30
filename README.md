
# SMART NEWS-AGGREGATOR API
\
\
**This API interacts with a data pipeline to provide the latest news from Rwanda**
**and related news. Below is the structure of the data pipeline:**
\
1. **Web scraper bot (Node.js puppeteer)**: extracts the headlines from top news sites
                                            like igihe.com.
2. **API (FastAPI)**: provides endpoints to get headlines and article links based on the field
                      (e.g: general news, sports, tech, finance, politics).
\
\
**STEPS TO USE IT**
\
1. **Clone the repo**: git clone https://github.com/mgalen007/News-Aggregator
2. **Get the API dependencies**: cd api
                             pip3 install -r requirements.txt
3. **Get the bot dependencies**: cd ../bot
                             npm install
4. **Run the bot to scrape**: (in /bot): npm run bot / node index.js
5. **Start the API server**: cd ../api
                         uvicorn main:app --reload / fastapi dev main.py
\
-> You can now interact with the API at **http://localhost:8000**
\
\
**AVAILABLE ENDPOINTS**
\
GET **/docs**\
    ->  Swagger UI documentation\
GET **/api/news**\
    -> Access the general news articles.\
GET **/api/politics**\
    -> Access the latest news in Rwandan politics, and related articles.\
GET **/api/sports**\
    -> Access the latest sports news in Rwanda.\
GET **/api/finance**\
    -> Get the latest finance-related news from Rwanda.\
GET **/api/tech**\
    -> Tech news, but not mostly from Rwanda, but the world at large.\
\
\
**FEATURES THAT ARE YET TO COME**
\
1. **Integration of a database**
    - More precisely PostgreSQL instead of JSON files.
2. **Automating with cron jobs**
    - Using node-cron and APScheduler, to make sure the processes work on schedule.
    - You won't have to run the bot manually, it will run in the background.
3. **Personal mail delivery**
    - Users will be able to subscribe and get the latest news via email.
    - Use of libraries like fastapi-mail or smtpmail.
4. **Addition of AI features**
    - Integrating the AI in the data pipeline to summarize the data.
    - It will make it easier for subscribers to get a personalized experience.
