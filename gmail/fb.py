import facebook

token = 'EAACEdEose0cBADhZBZBPZAAB0CSROco36cMZCwPfUsNtr3XUkyaulpdZAzutc6iZAOHoXZCKhal1PNpEUzQYNVIvGvrcm1z0hQb1vOwMXWwKTkI96zRKR9Bjm0XlzrGK5akVK9u006mWkZB6V5UAzWwCdQmHjk09ihqhACZBZCre705CnTj6QMgwx6ZC8eH6aK13YaAi4MPCw1QNgZDZD'
graph = facebook.GraphAPI(token)

me_info = graph.get_object('me')
status = graph.put_wall_post("Wow! 王鈞佑用graphAPI發了他第一篇文 想知道他如何辦到嗎? 不告訴你")
print ('User name:', me_info['name'])

graph.put_photo(image=open('img.png', 'rb'), message='Look at this cool photo!')
