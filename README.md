<!-- hide -->
<div align="center">

# Learn how to build HTTP requests with Python

![Certified tutorial by 4Geeks Academy](https://img.shields.io/badge/4Geeks%20Academy-certified%20tutorial-2563eb) ![13 autograded exercises with LearnPack](https://img.shields.io/badge/LearnPack-13%20autograded%20exercises-2563eb) [![Open in GitHub Codespaces](https://img.shields.io/badge/Open%20in-Codespaces-fb5a1f)](https://codespaces.new/?repo=4GeeksAcademy/python-http-requests-api-tutorial-exercises)

![Cover image of the tutorial Learn how to build HTTP requests with Python, showing the title over a light blue background decorated with code brackets, arrows and student name tags](https://raw.githubusercontent.com/4GeeksAcademy/python-http-requests-api-tutorial-exercises/master/preview.png)

</div>

*Estas instrucciones [están disponibles en español](https://github.com/4GeeksAcademy/python-http-requests-api-tutorial-exercises/blob/HEAD/README.es.md) 🇪🇸*
<!-- endhide -->

This interactive tutorial teaches HTTP requests in Python through **14 exercises**, 13 of them graded automatically by **35 pytest checks**. You start by pointing a single `requests.get()` at a URL and finish by sending a POST with a JSON body and a `Content-Type` header. Along the way you handle status codes, read `response.text`, parse `response.json()` and dig through nested dictionaries and lists. Estimated time: 4 hours. Difficulty: easy.

<!-- hide -->
## 📋 About this tutorial

+ **Difficulty:** easy — designed as a first contact with HTTP.
+ **Estimated duration:** 4 hours.
+ **Exercises:** 14 folders, 13 with automated tests and a reference solution.
+ **Technologies:** Python 3, the `requests` package, pytest and `mock` for grading.
+ **Grading:** automatic, powered by LearnPack.
+ **Languages:** English and Spanish instructions; the Spanish version also links a short video walkthrough on each of the 13 coding exercises.
<!-- endhide -->

## 🎯 What will you learn?

Every concept in this tutorial is practiced against a real endpoint, not explained in the abstract:

+ Sending a GET request with `requests.get(url)` and reading `response.status_code`.
+ Branching on status codes such as 200, 400, 404 and 503, and handling everything else as an unknown code.
+ Telling apart `response.text` (raw body as a string) from `response.json()` (body parsed into a Python dictionary or list).
+ Traversing nested JSON: a dictionary inside a list inside another dictionary, and picking items by index.
+ Building functions that *return* data instead of printing it, which is how you would wrap an API in real code.
+ Sending a POST request and attaching a JSON payload plus request headers.

> 💡 The tutorial drills the two verbs you use most, GET and POST. PUT and DELETE are named as part of the HTTP method family but are not practiced in the exercises.

## 👀 What will you build?

Fourteen steps, each one a folder inside `exercises/` with its own instructions and, from `01` onward, an `app.py` you edit plus a `test.py` that grades it:

+ **00 · welcome** — the only step with no code to write: what the `requests` package is and what is coming next.
+ **01 · creating-a-request** — change the `url` variable so the GET hits `hello.php` and prints a 200 status code.
+ **02 · random-status** — the endpoint returns a different status on every call; print one of five exact messages depending on it. This is the most heavily tested exercise, with 6 checks.
+ **03 · response-body** — print `response.text` when the status is 200 and `Something went wrong` for any other code.
+ **04 · response-body-json** — parse a JSON clock endpoint and print a line like `Current time: 19 hrs 45 min and 06 sec`.
+ **05 · project-name** — read the `name` key out of a JSON object and print just that value.
+ **06 · project-list** — the body is a JSON list; print the name of the **second** project using its index.
+ **07 · project-list-image** — print the **last** image URL of the **last** project, a list nested inside a list.
+ **08 · blog-post-author** — walk `body["posts"][0]["author"]["name"]` to get the author of the first post.
+ **09 · list-of-blog-titles** — write `get_titles()`, which loops the posts and **returns** a list of every title.
+ **10 · get-post-tags** — write `get_post_tags(post_id)`, which finds the post whose `id` matches and returns its list of tags.
+ **11 · get-attachment-by-id** — write `get_attachment_by_id(attachment_id)`, a double loop over posts and their attachments that returns the attachment title as a string.
+ **12 · post-request** — your first `requests.post(url)`, printing whatever the server replies.
+ **13 · post-request-body** — a POST carrying `headers={"Content-Type": "application/json"}` and a JSON body with `id` and `title`.

Exercises 08 to 11 all hit the same "weird portfolio" endpoint, whose response nests posts, authors, tags and attachments several levels deep. This diagram from exercise 08 maps the shape of that body:

![Diagram of a JSON response body annotated in red, showing that the whole body is a dict, that body posts is a list, that the first post is a dict, and that the tags key holds a list of tag dictionaries](https://raw.githubusercontent.com/4GeeksAcademy/python-http-requests-api-tutorial-exercises/master/assets/traversion_json.png)

## 🎓 What do you need before starting?

+ **Python basics.** Variables, `if` statements, `for` loops, lists, dictionaries and how to declare a function. Exercises 09 to 11 assume you can write a function that returns a value.
+ **No HTTP background.** Status codes, headers, request bodies and content types are all introduced from zero.
+ **No API keys, no accounts, no payment methods.** Every endpoint used is a public sample API that needs no authentication.
+ **A working environment.** Python 3 and the `requests` package, or one click on GitHub Codespaces, which builds a Python 3.10 container with everything preinstalled.

## ✅ How does the automatic grading work?

Thirteen of the fourteen folders ship a `test.py` file, and together they contain **35 pytest checks**. Each check prints a readable description when it fails, so you always know which requirement is unmet.

Almost every check replaces the network with the `mock` package: `requests.get` and `requests.post` are patched, and your code receives a fixed fake response instead of the live server. Two consequences worth knowing:

+ The grader is deterministic. Exercise 02 can test all five status-code branches in a single run even though the real endpoint returns a random one.
+ The fake data is not the live data. Exercise 05 is graded against `Sample Project`, a name that appears neither in the example JSON of its own instructions nor in what the live endpoint answers, so hardcoding what you read fails the check.

The one exception is exercise 12: one of its two checks lets the real POST go through and inspects the text the server sends back, so keep an internet connection while you work.

Each of the 13 graded exercises also ships a reference solution that LearnPack can reveal, and the tests check three different things depending on the exercise: the exact URL passed to `requests`, the exact text printed on the console, or the value your function returns.

## 💡 What mistakes should you avoid?

+ **Printing when the test wants a return.** In exercises 09, 10 and 11 the grader imports your function and inspects its return value. A `print()` inside the function is invisible to it; `return` is what counts.
+ **Leaving extra output behind.** Several checks compare the *entire* console output with `==`, not with "contains". A leftover debugging `print()`, or printing the status code before the message, breaks an otherwise correct answer.
+ **Calling the endpoint twice.** Some checks use `assert_called_once_with(url)`, so a stray extra request, or passing the URL as a keyword argument instead of the first positional one, fails the check.
+ **Copying values from the browser.** The graded responses are fabricated. Exercise 06 expects the second project of the *mocked* list and exercise 11 expects the title `Training Certificate`, neither of which you can guess by reading the live endpoint.
+ **Serializing the POST body by hand.** In exercise 13 the check reads the `json` keyword argument of `requests.post`, so `requests.post(url, json=payload, headers=...)` passes while `data=json.dumps(payload)` does not. The `Content-Type: application/json` header is verified separately.
+ **Translating the expected strings.** The five messages in exercise 02 are compared literally in English even when you are following the Spanish instructions.

## ❓ Frequently asked questions

### Do I need to know HTTP before starting this tutorial?

No. The tutorial assumes zero HTTP knowledge and introduces methods, status codes, response bodies and headers as they become necessary. What you do need is comfort with Python lists, dictionaries, loops and functions, because most exercises are really about navigating parsed JSON.

### What is the difference between response.text and response.json()?

`response.text` gives you the raw body as a Python string, which is what exercise 03 prints. `response.json()` parses that same body and hands you a dictionary or a list you can index into, which is what every exercise from 04 onward relies on. Calling `.json()` on a body that is not valid JSON raises an error.

### How do I send a JSON body with the requests package?

Pass your dictionary to the `json` keyword argument and let `requests` serialize it: `requests.post(url, json={"id": 2323, "title": "Very big project"}, headers={"Content-Type": "application/json"})`. That is exactly what exercise 13 is graded on. The `json` argument also sets the content type on its own, but the exercise asks you to declare it explicitly so you learn where headers live.

### Why does my exercise fail when the output looks correct?

Nine times out of ten it is whitespace or extra output. The checks compare the full captured console output character by character, so a trailing message, a different capitalization, or a missing space in `Current time: 19 hrs 45 min and 06 sec` will fail. Read the test description shown in the terminal: it names the exact string expected.

### Do the tests need an internet connection?

Almost all of them run offline, because `requests.get` and `requests.post` are patched with mocks that return canned data. The exception is exercise 12, where one check performs the real POST and reads the server's reply, so plan on being online.

### How long does it take and does it cost anything?

The pack is estimated at 4 hours for the 14 exercises, and it is realistic if you write the code yourself instead of pasting the solutions. Running it costs nothing: the repository is public on GitHub and every endpoint is a free sample API. Note that the repository does not ship a LICENSE file, so it is not released under an open source license; the solutions you write are your own.

<!-- hide -->
## 📚 Related interactive tutorials

If you are still building your Python foundations, or want to keep going after this one:

+ [Learn Python Interactively (beginner)](https://4geeks.com/en/interactive-exercise/python-beginner-exercises)
+ [Learn Python Functions Interactively](https://4geeks.com/en/interactive-exercise/python-function-exercises)
+ [Learn Python Loops and Lists Interactively](https://4geeks.com/en/interactive-exercise/python-loops-lists-exercises)
+ [Master Python by practice](https://4geeks.com/en/interactive-exercise/master-python-exercises)
+ [Learn Object Oriented Programming with Python](https://4geeks.com/en/interactive-exercise/object-oriented-programing-with-python)
+ [Learn Python Best Practices](https://4geeks.com/en/interactive-exercise/python-best-practices-tutorial)

## 🚀 How to start

The fastest path is [opening the repository in GitHub Codespaces](https://codespaces.new/?repo=4GeeksAcademy/python-http-requests-api-tutorial-exercises), which builds a Python 3.10 container with Node 22, LearnPack and every dependency already installed. [Gitpod](https://gitpod.io#https://github.com/4GeeksAcademy/python-http-requests-api-tutorial-exercises) also works.

Once VSCode opens, LearnPack should start on its own. If it does not, run this in the terminal:

```bash
learnpack start
```

## 💻 Local installation

1. Install [Python 3](https://www.python.org/downloads/), Node.js 14 or newer, and [LearnPack](https://learnpack.co/):

    ```bash
    npm i @learnpack/learnpack -g
    learnpack plugins:install @learnpack/python
    ```

2. Clone the repository and install the Python dependencies the tests need:

    ```bash
    pip3 install pytest==6.2.5 pytest-testdox mock requests toml
    ```

3. From the same folder as [learn.json](https://github.com/4GeeksAcademy/python-http-requests-api-tutorial-exercises/blob/HEAD/learn.json), start the tutorial:

    ```bash
    learnpack start
    ```

## 📝 How the exercises are organized

Each exercise lives in its own folder under `exercises/` and contains up to five files:

+ **README.md** and **README.es.md** — the instructions, in English and Spanish.
+ **app.py** — the file you edit and the one Python executes.
+ **test.py** — the grading script. You do not need to open it, but reading it is the fastest way to understand why a check fails.
+ **solution.hide.py** — a reference solution, hidden by LearnPack until you ask for it.

> 💡 The tests are strict on purpose. Treat a failing check as a hint about the exact wording or the exact return value being requested, not as a verdict on your code.

## 🤝 Contributors

Built by [Alejandro Sánchez](https://github.com/alesanchezr) (code, tests, tutorial, documentation), [Paolo (plucodev)](https://github.com/plucodev) (bug reports, code, translation) and [other contributors](https://github.com/4GeeksAcademy/python-http-requests-api-tutorial-exercises/graphs/contributors).

This project follows the [all-contributors](https://github.com/kentcdodds/all-contributors) specification and contributions of any kind are welcome. Found a typo, a broken endpoint or a confusing test? [Open an issue](https://github.com/learnpack/learnpack/issues/new).

This and many other interactive tutorials are built at [4Geeks Academy](https://4geeksacademy.com/us/coding-bootcamps/part-time-full-stack-developer).
<!-- endhide -->
