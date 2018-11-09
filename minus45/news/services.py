import requests
import json


HACKER_NEWS_URL = 'https://newsapi.org/v2/top-headlines?sources=hacker-news&apiKey=fd46bc918f8641fc91edfdce37455ee8&pageSize=12'
TOP_HEADLINES_URL = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=fd46bc918f8641fc91edfdce37455ee8&pageSize=12'
NYT_BIZ_URL = 'https://api.nytimes.com/svc/topstories/v2/business.json?api-key=73bb4c440ded4fbfb6e423d6250873bb'

# data_model = {
#     'articles': [
#         {'source': {'id': None, 'name': 'Espn.com'},
#          'author': None,
#          'title': 'Air Force falcon improving after injury at West Point',
#          'description': "An Air Force falcon injured at West Point during a prank before Saturday's annual rivalry game between the two service academies is back home and showing signs of improvement.",
#          'url': 'http://www.espn.com/college-football/story/_/id/25176884/air-force-mascot-improving-injury-west-point',
#          'urlToImage': 'http://a1espncdn.com/combiner/i?img=%2Fphoto%2F2018%2F1103%2Fr458501_1296x729_16%2D9.jpg'},
#         {'source': {'id': None, 'name': 'Espn.com'},
#          'author': None,
#          'title': "Ethiopia's Lelisa Desisa, Kenya's Mary Keitany win NYC Marathon",
#          'description': "Mary Keitany and Lelisa Desisa won the New York City Marathon on Sunday, with Keitany dominating the strong women's field for her fourth victory in the event and Desisa surging ahead of two other runners near the finish line.",
#          'url': 'http:// www.espn.com/olympics/story/_/id/25175670/ethiopia-lelisa-desisa-kenya-mary-keitany-win-nyc-marathon',
#          'urlToImage': 'http://a2.espncdn.com/combiner/i?img=%2Fphoto%2F2018%2F1104%2Fr458740_1296x729_16%2D9.jpg'}]}


class Articles:

    @staticmethod
    def get_data():
        top_news = requests.get(TOP_HEADLINES_URL)
        hacker_news_articles = requests.get(HACKER_NEWS_URL)
        main = top_news.json()  # Convert fetched data to python dicts
        hacker = hacker_news_articles.json()
        for item in hacker['articles']:
            '''add any articles to main data source'''
            main_data['articles'].append(item)
        return()

    @staticmethod
    def fetch_top_news():
        top_news = requests.get(TOP_HEADLINES_URL)
        main = top_news.json()  # Convert fetched data to python dicts
        return(main)

    @staticmethod
    def fetch_hacker_news():
        hacker_news = requests.get(HACKER_NEWS_URL)
        main = hacker_news.json()  # Convert fetched data to python dicts
        return(main)

    @staticmethod
    def fetch_nyt_biz():
        data_model = {
            'articles': [

            ]
        }

        nyt_biz = requests.get(NYT_BIZ_URL)
        main = nyt_biz.json()
        for item in main['results']:
            article_dict = {}
            article_dict['author'] = item['byline']
            article_dict['title'] = item['title']
            article_dict['description'] = item['abstract']
            article_dict['url'] = item['url']

            article_dict['urlToImage'] = item['multimedia'][4]['url']

            data_model['articles'].append(article_dict)
        return(data_model)
