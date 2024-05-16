import requests
import json
import os

from langchain.tools import tool
from langchain_community.document_loaders import WebBaseLoader

class SearchTools:
  
  @tool('search internet')
  def search_internet(query: str) -> str:
    """
    使用此工具在互联网上搜索信息。该工具可从 Google 搜索引擎返回 5 条结果。
    """
    return SearchTools.search(query)
  
  @tool('search weibo')
  def search_weibo(query: str) -> str:
    """
    使用此工具搜索微博。该工具可从微博页面返回 5 条结果。
    """
    return SearchTools.search(f"site:weibo.com {query}", limit=5)
    
  @tool('open page')
  def open_page(url: str) -> str:
    """
    使用该工具打开网页并获取内容。
    """
    loader = WebBaseLoader(url)    
    return loader.load()
    

  def search(query, limit=5):

    url = "https://google.serper.dev/search"
    payload = json.dumps({
      "q": query,
      "num": limit,
      "gl": "cn",
    })
    headers = {
      'X-API-KEY': os.getenv("SERPER_API_KEY"),
      'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    results = response.json()['organic']
    
    string = []
    for result in results:
      string.append(f"{result['title']}\n{result['snippet']}\n{result['link']}\n\n")
      
    return f"Search results for '{query}':\n\n" + "\n".join(string)
  
  
if __name__ == "__main__":
  print(SearchTools.open_page("https://www.python.org/"))