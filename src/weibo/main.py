#!/usr/bin/env python
from weibo.crew import WeiboCrew
import datetime


def run():
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    inputs = {
        'current_date': datetime.datetime.now().strftime("%Y-%m-%d"),
        'weibo_description': input('在此输入页面描述: '),
        'topic_of_the_week': input('在此输入本周主题: '),
    }
    WeiboCrew().crew().kickoff(inputs=inputs)