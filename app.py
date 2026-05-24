from flask import Flask, render_template

app = Flask(__name__)

temples = [
    {
        "name": "Badrinath Temple",
        "location": "Uttarakhand",
        "deity": "Lord Badrinath (Vishnu)",
        "description": "One of the Char Dham pilgrimage sites, nestled in the Garhwal hill tracks in the Himalayas.",
        "best_time": "May to October (Closed in winter)"
    },
    {
        "name": "Sri Venkateswara Swami Temple",
        "location": "Tirupati, Andhra Pradesh",
        "deity": "Lord Venkateswara",
        "description": "Also known as Tirupati Balaji, it is one of the most visited and wealthiest temples in the world.",
        "best_time": "September to February"
    },
    {
        "name": "Jagannath Temple",
        "location": "Puri, Odisha",
        "deity": "Lord Jagannath",
        "description": "Famous for its annual Rath Yatra (Chariot Festival). Another key Char Dham site.",
        "best_time": "June to March"
    },
    {
        "name": "Sri Ranganathaswamy Temple",
        "location": "Srirangam, Tamil Nadu",
        "deity": "Lord Ranganatha",
        "description": "The largest functioning Hindu temple complex in the world, dedicated to the reclining form of Lord Vishnu.",
        "best_time": "October to March"
    },
    {
        "name": "Dwarkadhish Temple",
        "location": "Dwarka, Gujarat",
        "deity": "Lord Krishna (Dwarkadhish)",
        "description": "An ancient temple dedicated to Lord Krishna, the king of Dwarka. Part of the Char Dham.",
        "best_time": "October to March"
    }
]

@app.route('/')
def home():
    return render_template('index.html', temples=temples)

if __name__ == '__main__':
     app.run(debug=True, host='0.0.0.0', port=5000)
