# importing the module
import tweepy
 
# personal details
consumer_key ="Nd1ZtdisQIuYiZ9SIyVnhxd0i"
consumer_secret ="JLwV5KyhNSb3gVjnkDjnuqxQUgoVolccF7GvMVYbt22CDsRO0U"
access_token ="967251581677817857-DxpEmRRD9Q74sdHTOjpcb0nAtMR8jl9"
access_token_secret ="csXN0BKVxPHWnEQioaDGMDGucj9AupKUC531j5qo4PjeX"
 
# authentication of consumer key and secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
 
# authentication of access token and secret
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
 
# update the status
api.update_status(status ="Hello Everyone !")

