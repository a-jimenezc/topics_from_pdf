import gradio as gr

intro_html = """
<html>
<head>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
</head>

<body>
    <p>
        This app  extracts topics from PDF documents.
        It works with ten-page documents as well as with books of over
        a thousand pages, and it's free! This is possible thanks to the use of
        Large Language Models (LLM for short in English),
        Vector Databases, and text processing algorithms.

        You're welcome to explore the GitHub repository associated with this web app:
    </p>

    <h4 style="text-align: center;">
        <a href="https://github.com/a-jimenezc">
            <i class="fab fa-github"></i> 
            GitHub
        </a>
    </h4>
</body>
</html>
"""

author_html = """
<html>
<head>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
</head>

<body>
    <h2 style="text-align: center;">
        About the Author:
    </h2>
    <p>
        My name is Antonio Jimenez. I am a Lecturer and Professional Engineer currently 
        developing Data Science web apps as personal projects.  
        Feel free to visit my GitHub to explore other projects I have been working on.
    </p>

    <h4 style="text-align: center;">
        <a href="https://github.com/a-jimenezc">
            <i class="fab fa-github"></i> 
            GitHub
        </a>
        &nbsp &nbsp &nbsp &nbsp
        <a href="https://www.linkedin.com/in/antonio-jimnzc">
            <i class="fab fa-linkedin linkedin-icon"></i> 
            Linkedin
        </a>
    </h4>

</body>
</html>
"""

