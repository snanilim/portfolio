from fastapi.responses import HTMLResponse

def generate_html_response():
    html_content = """
    <html>
        <head>
            <title>It is a test</title>
            <style>
                body {
                    margin: 0;
                }

                ul {
                    list-style-type: none;
                    margin: 0;
                    padding: 0;
                    width: 25%;
                    background-color: #E8F8F5;
                    position: fixed;
                    height: 100%;
                    overflow: auto;
                }

                li a {
                    display: block;
                    color: #000;
                    padding: 8px 16px;
                    text-decoration: none;
                }

                li a.active {
                background-color: #555 ;
                color: white;
                }

                li a:hover:not(.active) {
                background-color: #A2D9CE;
                color: black;
                }

                #navlist li {
                    margin: 0;
                    padding: 0;
                    list-style: none;
                    position: absolute;
                    top: 0;
                }

                #navlist li, #navlist a {
                    height: 44px;
                    display: block;
                }
                #fb {
                    left: 0px;
                    width: 46px;
                    background: url('fb.png') 0 0;
                }
            </style>
        </head>
        <body>
            <ul>
                <h3>Creative</h3>
                <h3>Front runner</h3>
                <h3>Pacesetter</h3>
                A Creative, pacesetter programmer who have .. experience on ..<br><br>
                <hr>
                <li><a class="active" href="#home">Home</a></li>
                <li><a href="#news">News</a></li>
                <li><a href="#contact">Contact</a></li>
                <li><a href="#about">About</a></li>

            </ul>http://127.0.0.1:8000/images/FaceDetection.jpg
            <hr>
            <div style="margin-left:25%;padding:1px 16px;height:1000px;">
                <img src="FaceDetection.jpg" width="350" height="263" alt="hello">
                <div>The picture above is 350px wide. The total width of this element is also 350px.</div>
            </div>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)