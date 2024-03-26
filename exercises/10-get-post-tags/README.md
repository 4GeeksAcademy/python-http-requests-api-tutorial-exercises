# `10` Get post tags

## 📝 Instructions:

1. Using the same endpoint from the previous exercise, create a function `get_post_tags` that returns the array of tags of a given `post_id`

## 💡 Hints:

+ Create the function `get_post_tags`.
+ GET all the posts by sending a GET request to the endpoint.
+ Declare the variable to store the serialized body 
+ Using the `post_id` parameter, loop all the posts and compare their `id`s to see if they match the `post_id`.
+ When you find the post you want, return its list of tags.

