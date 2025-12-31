from flask import Flask, render_template_string, request, session

app = Flask(__name__)
app.secret_key = "techno-kids-secret"

PAGE = """
<!DOCTYPE html>
<html>
<head>
<title>Techno Kids Platform</title>

<style>
:root {
    --bg1:#667eea;
    --bg2:#764ba2;
    --card:#ffffff22;
}

body.light {
    --bg1:#f9f9f9;
    --bg2:#e0e0ff;
    --card:#00000011;
    color:black;
}

body {
    margin:0;
    font-family: Comic Sans MS, Arial;
    background: linear-gradient(135deg,var(--bg1),var(--bg2));
    text-align:center;
}

nav {
    background:#000000aa;
    padding:15px;
}

nav button {
    margin:5px;
    padding:10px 20px;
    font-size:16px;
    border-radius:12px;
    border:none;
    cursor:pointer;
}

section { display:none; padding:40px; }
section.active { display:block; }

.card {
    background:var(--card);
    padding:20px;
    margin:15px auto;
    border-radius:15px;
    width:320px;
}

input, select {
    padding:10px;
    width:80%;
    margin:8px;
    border-radius:8px;
    border:none;
}

button.action {
    background:orange;
    font-size:18px;
}

#chat {
    height:200px;
    overflow-y:auto;
    background:#00000044;
    padding:10px;
    border-radius:10px;
}
</style>

<script>
function show(page){
    document.querySelectorAll("section").forEach(s=>s.classList.remove("active"));
    document.getElementById(page).classList.add("active");
}

/* THEME OPTION */
function toggleTheme(){
    document.body.classList.toggle("light");
}

/* CHATBOT OPTIONS */
function sendMsg(){
    let input=document.getElementById("msg");
    let chat=document.getElementById("chat");
    let mode=document.getElementById("mode").value;
    let text=input.value.toLowerCase();
    if(!text) return;

    chat.innerHTML+=`<p>👦 You: ${input.value}</p>`;
    let reply="🤖 I'm thinking...";

    if(mode==="kids"){
        if(text.includes("python")) reply="🐍 Python is easy and fun!";
        else reply="😊 Ask me about coding or games!";
    }
    if(mode==="tech"){
        if(text.includes("python")) reply="🐍 Python is a high-level interpreted language.";
        else reply="💡 Try asking technical questions.";
    }

    chat.innerHTML+=`<p>${reply}</p>`;
    chat.scrollTop=chat.scrollHeight;
    input.value="";
}

/* GAME OPTIONS */
let score=0;
function clickGame(){
    let diff=document.getElementById("difficulty").value;
    score += diff==="hard"?3:1;
    document.getElementById("score").innerText=score;
}
</script>
</head>

<body>

<nav>
<button onclick="show('home')">🏠 Home</button>
<button onclick="show('learn')">📚 Learn</button>
<button onclick="show('games')">🎮 Games</button>
<button onclick="show('chatbot')">🤖 Chat</button>
<button onclick="show('login')">🔐 Login</button>
<button onclick="toggleTheme()">🎨 Theme</button>
</nav>

<section id="home" class="active">
<h1>🚀 Techno Kids Platform</h1>
<p>Learn • Play • Innovate</p>
<div class="card">Options Enabled ✔</div>
</section>

<section id="learn">
<h1>📚 Learn</h1>
<div class="card">Python</div>
<div class="card">HTML/CSS</div>
<div class="card">AI Basics</div>
</section>

<section id="games">
<h1>🎮 Click Game</h1>
<select id="difficulty">
<option value="easy">Easy</option>
<option value="hard">Hard</option>
</select><br>
<button class="action" onclick="clickGame()">CLICK!</button>
<h2>Score: <span id="score">0</span></h2>
</section>

<section id="chatbot">
<h1>🤖 AI Chatbot</h1>
<select id="mode">
<option value="kids">Kids Mode</option>
<option value="tech">Tech Mode</option>
</select>
<div id="chat"></div>
<input id="msg" placeholder="Ask something">
<br>
<button class="action" onclick="sendMsg()">Send</button>
</section>

<section id="login">
<h1>🔐 Login</h1>
<form method="post" action="/login">
<input name="user" placeholder="Username"><br>
<input name="pass" type="password" placeholder="Password"><br>
<button class="action">Login</button>
</form>
<p>{{msg}}</p>
</section>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(PAGE, msg="")

@app.route("/login", methods=["POST"])
def login():
    session["user"] = request.form["user"]
    return render_template_string(PAGE, msg=f"Welcome {session['user']} 🎉")

if __name__=="__main__":
    app.run(debug=True)