import streamlit as st
import requests

# Function to fetch reviews
def fetch_reviews():
    url = 'https://syften.com/api/0.0/items/get'
    headers = {
        'Authorization': 'Bearer YXV0aF8yOTBlNGRkNGE1MTVjNWVmYjQwZjAzYmE5ZTMxY2Q3NDr9IhbGASC5U3WOebiOX9iAADjLRfQQKlUYaIo5gxuhDg==',
        'Content-Type': 'application/json'
    }
    payload = {
        'limit': 100
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        return response.json()
    else:
        return f"Failed to fetch reviews. Status code: {response.status_code}"

# Streamlit UI
st.title("Review Fetcher and Listing Deletion")

# account_id = st.text_input("Enter Account ID", value="1888")

if st.button("Fetch Reviews"):
    reviews = fetch_reviews()
    # st.write(reviews)
    for i in range(len(reviews)):
        # st.write("Fetched Reviews:", reviews[i]['author'])

        st.write(reviews[i]['item']['text'])   
        st.write("__________________________")
