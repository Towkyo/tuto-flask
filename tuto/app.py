from flask import Flask, render_template
import mysql.connector 


app = Flask(__name__)

# Configuration de la base de données MariaDB
DATABASE = {
     'user': 'lucidor',
     'password': 'lucidor',
     'host': 'servinfo-maria',
     'database': 'DBlucidor',
}

def get_db_connection():
    return mysql.connector.connect(**DATABASE)

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor_concert = conn.cursor(dictionary=True)
    
    # Exécutez une requête SQL pour récupérer des données de la table
    cursor_concert.execute("SELECT * FROM CONCERT")
    
    # Récupérez toutes les lignes de résultats dans une liste
    concert = cursor_concert.fetchall()

    # Fermez le curseur et la connexion à la base de données
    cursor.close()
    conn.close()
    return render_template(
        "home.html",
        concert=concert  # Passez les données récupérées à votre modèle HTML
    )

@app.route('/programmation')
def programmation():
    conn = get_db_connection()
    cursor = conn.cursor()

    curso_artiste = conn.cursor(dictionary=True)
    curso_artiste.execute("SELECT * FROM ARTISTE")
    artiste = curso_artiste.fetchall()

    cursor.close()
    conn.close()
    return render_template(
        "programmation.html", title="programmation", 
        artiste=artiste
        )

if __name__ == '__main__':
    app.run(debug=True)
