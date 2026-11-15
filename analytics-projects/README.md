# Analytics & Fraud Detection Projects

Collection of Python scripts for data analysis and security applications.

## Projects

### Last Click Attribution Model
`Last Click Attribution Model.py`

Standard attribution model used by most analytics platforms. Credits conversions to the last marketing channel a visitor touched before converting. Loads session data, filters for the final session per visitor, aggregates by channel, and creates a pie chart showing channel distribution.

Useful for understanding which channels close deals.

**Uses**: pandas, matplotlib

### Last Non-Direct Click Attribution Model
`Last Non Direct Click Attribution Model.py`

More sophisticated version that filters out direct traffic. When users are already familiar with your product, they often convert through direct visits, but that doesn't tell you which marketing channel brought them in originally. This model ignores "Direct" traffic and attributes to the last paid touchpoint.

Splits visitors into single-session and multi-session groups, removes direct traffic from multi-session data, then finds the last non-direct channel.

**Uses**: pandas, matplotlib

### IP Geolocation Distance Calculator
`Distance Between Two IP Addresses.py`

Fraud detection system that calculates the physical distance between two IP addresses. If someone tries to make a purchase from a location that's hundreds of miles from their usual IP, that's suspicious.

Uses IPStack API to get latitude/longitude for each IP, then calculates geodesic distance. Flags transactions over 500 miles as potentially fraudulent and generates a summary report.

You'll need a free API key from ipstack.com to run this.

**Uses**: requests, pandas, geopy

### Sorting Algorithms
`Sorting Algorithms.py`

Six sorting algorithm implementations: insertion sort, merge sort, quick sort, selection sort, shell sort, and bubble sort. Each includes time complexity notes.

Originally developed for priority-based systems (like hospital surgery scheduling where you need to sort patients by severity/weight), but applicable to any sorting problem.

**Uses**: Pure Python

## Setup

```bash
pip install pandas matplotlib geopy requests
```

For the IP distance calculator:
```bash
export IPSTACK_API_KEY='your_api_key_here'
```

## Running

```bash
python "Last Click Attribution Model.py"
python "Last Non Direct Click Attribution Model.py"
python "Distance Between Two IP Addresses.py"
python "Sorting Algorithms.py"
```

## Data Sources

The attribution models and fraud detection script pull from Dropbox-hosted CSV files. The sorting algorithms use hardcoded test arrays.

## Notes

Fixed some code quality issues in the original versions - updated deprecated pandas `.append()` to `pd.concat()`, added proper error handling to the IP distance calculator, and restructured the sorting algorithms file which had some functions nested incorrectly.
