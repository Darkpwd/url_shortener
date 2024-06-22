from flask import Flask, render_template, request, flash
import pyshorteners

app = Flask(__name__)
app.secret_key = "secret_key_here"  # Set a secret key for flash messages

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        url_received = request.form.get("url")
        if not url_received:
            flash("Please enter a URL")
            return render_template("index.html")

        try:
            shortener = pyshorteners.Shortener()
            short_url = shortener.tinyurl.short(url_received)
            flash(f"Shortened URL: {short_url}")
            return render_template("index.html", old_url=url_received, new_url=short_url)
        except pyshorteners.ShorteningError as e:
            flash(f"Invalid URL: {str(e)}")
        except Exception as e:
            flash(f"An error occurred: {str(e)}")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)