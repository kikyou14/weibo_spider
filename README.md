## How to use:

1. login https://m.weibo.cn or https://weibo.com, get your cookie in request headers; Cookies are begin with "SUB=_2A25". 
2. Add your cookie to the request `headers` in the code. 
3. Replace the weibo_id to the weibo that you want to get comments, the id consists of **16 digits**, you can get it at the URL of that weibo at **m.weibo.cn**

---

- Excessive requests will lead to a redirect to the login page.

- Only for learning and research.



e.g. Crawl a Weibo post with nearly 50,000 comments:

![shortcuts](image/img.png)

Due to the neglect of multi-level comments, the number of comments is less than the actual number.

