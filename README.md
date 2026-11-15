# Data Science Portfolio

This repository contains projects demonstrating capabilities in natural language processing, data analytics, SQL, and software development.

## What's Here

### NLP Text Summarization Application
**Location**: `nlp-text-summarization/`

A web application that uses OpenAI's GPT-4o-mini to summarize long texts. Built with FastAPI for the backend and vanilla JavaScript for the frontend. The app maintains conversation history for context-aware responses and lets users adjust AI parameters like temperature and max tokens.

Includes Docker setup for deployment.

**Stack**: FastAPI, Python, OpenAI API, Docker

### Analytics & Fraud Detection
**Location**: `analytics-projects/`

Four Python scripts covering different analytical problems:

**Attribution Modeling** - Two approaches to measuring which marketing channels drive conversions. The first uses last-click attribution (credits the final touchpoint), the second uses last non-direct click (ignores direct traffic to better understand paid channel performance).

**IP Distance Calculator** - Fraud detection tool that calculates geographic distance between two IP addresses using the IPStack API. Flags suspicious transactions where the payment location is far from the user's base location.

**Sorting Algorithms** - Implementations of six sorting algorithms (insertion, merge, quick, selection, shell, bubble) with practical applications in priority-based systems like medical scheduling.

**Stack**: pandas, matplotlib, geopy, requests

### SQL Examples
**Location**: `sql-examples/`

A collection of SQL query patterns and techniques, organized by topic:

- Table creation and sample data
- Aggregate functions and window functions (PARTITION BY, DENSE_RANK)
- CASE statements for conditional logic
- Multi-table joins
- String manipulation (CONCAT, SUBSTR, REPLACE)
- Date functions and timezone handling
- Complex nested queries (4+ levels)
- Database access control (GRANT/REVOKE)

Works with Snowflake, PostgreSQL, MySQL, and Oracle.

## Running the Projects

### Text Summarization
```bash
cd nlp-text-summarization
docker-compose up
# Open http://localhost:8000
```

### Analytics Scripts
```bash
cd analytics-projects
pip install pandas matplotlib geopy requests

# For IP distance calculator, you'll need an IPStack API key
export IPSTACK_API_KEY='your_key'

python "Last Click Attribution Model.py"
python "Distance Between Two IP Addresses.py"
```

### SQL Examples
The SQL files are markdown documents with query examples. Browse them for reference patterns.

## Technical Skills Covered

**Machine Learning & NLP**: LLM integration, prompt engineering, conversation management, parameter tuning

**Data Analytics**: Attribution modeling, aggregation, visualization, fraud detection, geospatial analysis

**SQL**: Window functions, complex joins, nested subqueries, CTEs, date/timezone handling, access control

**Development**: REST APIs, Docker containerization, error handling, environment configuration

**Algorithms**: Sorting implementations, complexity analysis

## About the Code

The OpenAI project is production-ready with proper error handling and Docker support. The Python analytics scripts demonstrate practical data science techniques - attribution modeling for marketing analytics and geolocation for fraud detection. The SQL examples progress from basic to advanced patterns, including multi-level nested queries with window functions.

All code has been tested and cleaned up with modern practices (replaced deprecated pandas methods, added proper error handling, fixed structural issues).
