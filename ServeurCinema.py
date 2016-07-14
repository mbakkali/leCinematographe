from flask import *
from sqlalchemy import *
from sqlalchemy.sql import *
import time



def authentification(pseaudo, password) :
		connection = engine.connect()
		try:
			if connection.execute(select([client]).where(client.c.ClientID == request.form['pseudo1'])).fetchone() is None:
				
				return False
			else:
				sel = select([client]).where(
					and_(
						client.c.ClientID == pseudo1,
						client.c.Mot_de_passe == password
					)
				)
			print("Je suis dans select ok")
			return connection.execute(sel).fetchone() != None  
		finally:
		
			connection.close() 
			return jsonify({'result': 'Ok'})


def retrieveProfile( pseudo ) :
    db = engine.connect()
    try:
        if db.execute(select([client.c.ClientID]).where(client.c.ClientID == pseudo)).fetchone() != None:
            sel = select([client.c.ClientID, client.c.Ville]).where(and_(client.c.ClientID == pseudo))
            usr=db.execute(sel)
            for row in usr:
                return row
        else :
            return None
    finally :
        db.close()
        









app = Flask(__name__, static_folder='static', static_url_path='')

# fix for index page
@app.route('/')
def index():

	return app.send_static_file('Accueil.html')



@app.route('/api/login/', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		if authentification(request.form['pseudo1'], request.form['password1']):
			print("Je suis dans ok authentification")
			res = retrieveProfile ( request.form['pseudo1'])
			session['username'] = request.form['pseudo1']
			session['ville'] = res[1]
			session['pseudo'] =res[2]
			res = retrieveProfile ( request.form['pseudo1'] )
			print (res)
			return json.dumps({'ville':res[1], 'pseudo':res[2]})
		else:
			flash('Mot de passe/login invalide ou inexistant: ' + request.form['pseudo1'])
			print("Je suis dans erreur authentification")
			return json.dumps('error');
	else:
		return render_template('login.html')





@app.route('/api/addMovie/', methods=['POST'])
def addMovie():
	engine = create_engine('sqlite:///BaseCinema.db', echo=True)
	connection = engine.connect()
	connection.execute("insert into film (Film, Realisateur, Tete_d_Affiche, Genre, Annee, Note, Nombre_de_notes) values ('"+request.form['Movie']+
	"', '"+request.form['Realisateur']+"', '"+request.form['Tete_affiche']+"', '"+request.form['Genre']+"', '"+request.form['Annee']+"','0', '0')")
	
	connection.close()
	return jsonify({'result': 'Ok'})



@app.route('/api/addProjection/', methods=['POST'])
def addProjection():
	engine = create_engine('sqlite:///BaseCinema.db', echo=True)
	connection = engine.connect()
	Cinema = request.form['Cinema']
	Num_salle = request.form['Num_salle']
	FilmId = request.form['FilmId']
	Horaire = request.form['Horaire']
	Date = str(request.form['Date'])
	for row in connection.execute("SELECT salle.SalleId, Nombre_de_Sieges FROM projection, salle WHERE salle.Cinema='"+Cinema+"' AND salle.SalleId = projection.Numero_de_Salle AND salle.Numero_de_salle='"+Num_salle+"'"):
		IdSalle=row[0]
		Siege=row[1]
	connection.execute("insert into projection (Numero_de_salle, FilmId, horaire, date, Nombre_de_Places) values ('"+IdSalle+"', '"+FilmId+"', '"+Horaire+"', '"+Date+"', '"+Siege+"')")
	connection.close()
	return jsonify({'result': 'Ok'})
	connection.close()
	return jsonify({'result': 'Ok'})
	



@app.route('/api/allMovies/')
def allMovies():
	engine = create_engine('sqlite:///BaseCinema.db', echo=True)
	connection = engine.connect()
	listMovies=[]
	for row in connection.execute("select Film,Genre,Realisateur,Tete_d_Affiche,Annee,FilmId from film"):
		movie = [row['Film'], row['Realisateur'], row['Tete_d_Affiche'], row['Genre'], str(row['Annee']), str(row['FilmId'])]
		listMovies.append(movie)
	connection.close()
	return jsonify({'result': listMovies})


@app.route('/api/MoviesGenre/')
def MoviesGenre():
	engine = create_engine('sqlite:///BaseCinema.db', echo=True)
	connection = engine.connect()
	genre=request.args['Genre']
	movies = []
	print 'Genre: '+genre
	query = "select Film,Genre,Realisateur,Tete_d_Affiche,Annee,FilmId from film where Genre like '%"+genre+"%'"
	for row in connection.execute(query):
		movie = [row['Film'], row['Realisateur'], row['Tete_d_Affiche'], row['Genre'], str(row['Annee']), str(row['FilmId'])]
		movies.append(movie)
	connection.close()
	return jsonify({'result': movies})


@app.route('/api/MoviesPopulaire/')
def MoviesPopulaire():
	engine = create_engine('sqlite:///BaseCinema.db', echo=True)
	connection = engine.connect()
	movies = []
	query = "select FilmId, Film,Genre,Realisateur,Tete_d_Affiche,Annee,Note from film order by Note desc"
	for row in connection.execute(query):
		movie = [str(row['FilmId']), row['Film'], row['Realisateur'], row['Tete_d_Affiche'], row['Genre'], str(row['Annee']), str(row['Note'])]
		movies.append(movie)
	connection.close()
	return jsonify({'result': movies})
	

@app.route('/api/getInfoMovie/')
def getInfoMovie():
	engine = create_engine('sqlite:///BaseCinema.db', echo=True)
	connection = engine.connect()
	query = "select Film,Genre,Realisateur,Tete_d_Affiche,Annee,Note,Nombre_de_notes from film where FilmId = '"+request.args['Id']+"'"
	for row in connection.execute(query):
		Film = (row['Film'])
		Genre = (row['Genre'])
		Realisateur = (row['Realisateur'])
		Tete_d_Affiche = (row['Tete_d_Affiche'])
		Annee = (row['Annee'])
		Note = (row['Note'])
		Vote = (row['Nombre_de_notes'])
	connection.close()
	print Film
	return jsonify({'Film': Film, 'Genre': Genre, 'Realisateur' : Realisateur, 'Tete_d_Affiche' : Tete_d_Affiche, 'Annee' : Annee, 'Note' : Note, 'Vote': Vote})

@app.route('/api/Cinemas/')
def Cinemas():
	engine = create_engine('sqlite:///BaseCinema.db', echo=True)
	connection = engine.connect()
	ville=request.args['Ville']
	print 'Ville: '+ville
	myCinemas=[]
	for row in connection.execute("select Nom_du_Cinema,Nombre_de_Salles,Prix from cinema where Ville = '"+ville+"'"):
		cinema = [row['Nom_du_Cinema'], row['Nombre_de_Salles'], row['Prix']]
		myCinemas.append(cinema)
	connection.close()
	return jsonify({'result': myCinemas})


@app.route('/api/getInfoCine/')
def Salles():
	engine = create_engine('sqlite:///BaseCinema.db', echo=True)
	connection = engine.connect()
	Cinema = request.args['LeCinema']
	myEvents=[]
	for row in connection.execute("SELECT salle.Numero_de_Salle, date, horaire, film.Film, projection.Nombre_de_Places, projection.ProjectionId FROM projection, salle, film WHERE salle.Cinema='"+Cinema+"' AND salle.SalleId = projection.Numero_de_Salle AND projection.FilmId=film.FilmId"):
		movie = [row[0], row[1], row[2],row[3], row[4], row[5]]
		print row
		myEvents.append(movie)
	connection.close()
	print myEvents
	return jsonify({'result': myEvents})
	 


@app.route('/api/Notation/', methods=['PUT'])
def Notation():
	engine = create_engine('sqlite:///BaseCinema.db', echo=True)
	connection = engine.connect()
	Id = request.form['Id']
	newNote = int(request.form['Note'])
	for row in connection.execute("select Note,Nombre_de_notes from film where FilmId = '"+Id+"'"):
		oldNote = row['Note']
		nbrNote = row['Nombre_de_notes']
	oldSum = oldNote * nbrNote
	nbrNote = nbrNote + 1
	moyenne = (oldSum + newNote ) / nbrNote
	connection.execute("update film set Note = "+str(moyenne)+", Nombre_de_notes = "+str(nbrNote)+" where FilmId = "+str(Id))
	connection.close()
	return jsonify({'Note': moyenne, 'Vote': nbrNote})


@app.route('/api/Rerservation/', methods=['PUT'])
def Rerservation():
	engine = create_engine('sqlite:///BaseCinema.db', echo=True)
	connection = engine.connect()
	ProjectionId = request.form['ProjectionId']
	for row in connection.execute("select Nombre_de_Places from projection where ProjectionId = "+str(ProjectionId)+""):
		place = row['Nombre_de_Places']
	place = place - 1
	connection.execute("update projection set Nombre_de_Places = "+str(place)+" where ProjectionId = "+str(ProjectionId))
	connection.close()
	return jsonify({'Place': place})

if __name__ == '__main__':
    app.run(debug=True)
