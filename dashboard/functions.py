import os
import openai
from django.conf import settings

# Load your API key from an environment variable or secret management service
openai.api_key = settings.OPENAI_API_KEYS




def generateBlogTopicIdeas(topic, keywords):
    blog_topics = []

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="generate blog topic ideas on the following topic: {}\nkeywords: {}\n*".format(topic,keywords),
        temperature=0.8,
        max_tokens=300,
        top_p=1,
        best_of=1,
        frequency_penalty=0,
        presence_penalty=0)
    
    if 'choices' in response:
        if len(response['choices'][0]['text'])>0:
            res = response['choices'][0]['text']
        else:
            return []
    else:
        return []
    a_list = res.split('*')
    if len(a_list) > 0:
        for blog in a_list:
            blog_topics.append(blog)
    else:
        return []
    return blog_topics




def generateBlogSectionHeadings(topic, keywords):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="generate blog section headings and section titles based on the follwoing blog section topic:\ntopic: {}\nkeywords: {}\n*".format(topic,keywords),
        temperature=0.8,
        max_tokens=300,
        top_p=1,
        best_of=1,
        frequency_penalty=0,
        presence_penalty=0)
    
    if 'choices' in response:
        if len(response['choices'][0]['text'])>0:
            res = response['choices'][0]['text']
    else:
        res = None
    return res



# res = generateBlogTopicIdeas(topic, keywords).replace('\n', '')
# b_list = res.split('*')
# for blog in b_list:
#     blog_topics.append(blog)
#     print('\n')
#     print(blog)