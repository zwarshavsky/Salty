"""OpenAQ Air Quality Dashboard with Flask."""
from flask import Flask
from hackernews import HackerNews
import nest_asyncio



APP = Flask(__name__)
API = HackerNews()

@APP.route('/')
def root():
    """Base view."""
    # user = API.get_user('ryanspahn')
    # return API.get_items_by_ids([70149, 37236, 2345], item_type='story')
    # for comment in user.comments:
    #     return comment.kids
    return "Hello8475843758586758967587685!"


# query the database for any Record objects that have value greater 
# or equal to 10. The filter method of SQLALchemy queries will be 
# invaluable for this. Hint - your query should look like 
# Record.query.filter(condition).all(), where condition is a 
# comparison/statement that returns a boolean (true/false), and you 
# can access the fields of Record to make that comparison.



# def get_record():
#     status, body = API.measurements(city='Los Angeles', parameter='pm25')
#     results = []
#     for result in body["results"]:
#         results.append((result["date"]["utc"], result["value"]))
#     return results

if __name__ == '__main__':
    app.run(debug=True)