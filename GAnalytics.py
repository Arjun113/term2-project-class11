# Load Libraries
from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.discovery import build
import httplib2
import pandas as pd

# Create service credentials
credentials = ServiceAccountCredentials.from_json_keyfile_name('nth-clone-249009-9888620ae7fb.json',
                                                               ['https://www.googleapis.com/auth/analytics.readonly'])

# Create a service object
http = credentials.authorize(httplib2.Http())
service = build('analytics', 'v4', http=http,
                discoveryServiceUrl=('https://analyticsreporting.googleapis.com/$discovery/rest'))
response = service.reports().batchGet(
    body={
        'reportRequests': [
            {
                'viewId': '217876927',  # Add View ID from GA
                'dateRanges': [{'startDate': '30daysAgo', 'endDate': 'today'}],
                'metrics': [{'expression': 'ga:sessions'}],
                'dimensions': [{"name": "ga:pagePath"}],  # Get Pages
                "filtersExpression": "ga:pagePath=~products;ga:pagePath!@/translate",
                # Filter by condition "containing products"
                'orderBys': [{"fieldName": "ga:sessions", "sortOrder": "DESCENDING"}],
                'pageSize': 100
            }]
    }
).execute()

# create two empty lists that will hold our dimensions and sessions data
dim = []
val = []

# Extract Data
for report in response.get('reports', []):

    columnHeader = report.get('columnHeader', {})
    dimensionHeaders = columnHeader.get('dimensions', [])
    metricHeaders = columnHeader.get('metricHeader', {}).get('metricHeaderEntries', [])
    rows = report.get('data', {}).get('rows', [])

    for row in rows:

        dimensions = row.get('dimensions', [])
        dateRangeValues = row.get('metrics', [])

        for header, dimension in zip(dimensionHeaders, dimensions):
            dim.append(dimension)

        for i, values in enumerate(dateRangeValues):
            for metricHeader, value in zip(metricHeaders, values.get('values')):
                val.append(int(value))

# Sort Data
val.reverse()
dim.reverse()

df = pd.DataFrame()
df["Sessions"] = val
df["pagePath"] = dim
df = df[["pagePath", "Sessions"]]
df

# Export to CSV
df.to_csv("page_by_session.csv")