#!/usr/bin/python
# vim: set fileencoding=utf-8 :


from sqlalchemy import *
from sqlalchemy.sql import *

engine = create_engine('sqlite:///BaseCinema.db', echo=True)

metadata = MetaData()

cinema = Table('cinema', metadata, Column('Nom_du_Cinema', String, primary_key=True), Column('Ville', String), Column('Nombre_de_Salles', Integer), Column('Prix', Integer))

salle = Table('salle', metadata, Column('SalleId', Integer, autoincrement=True, primary_key=True), Column('Numero_de_Salle', Integer), Column('Cinema', None, ForeignKey('cinema.Nom_du_Cinema')), Column('Nombre_de_Sieges', Integer))

film = Table('film', metadata, Column('FilmId', Integer, autoincrement=True, primary_key = True), Column('Film', String), Column('Genre', String), Column('Realisateur', String), Column('Annee', Integer), Column('Tete_d_Affiche', String), Column('Note', FLOAT), Column('Nombre_de_notes', Integer))

client = Table('client', metadata, Column('ClientId', String, primary_key = True), Column('Mot_de_passe', String), Column('Ville', None, ForeignKey('cinema.Ville')))

projection = Table('projection', metadata, Column('ProjectionId', Integer, autoincrement = True, primary_key = True), Column('Numero_de_Salle', None, ForeignKey('salle.SalleId')), Column('FilmId', None, ForeignKey('film.FilmId')), Column('horaire', String), Column('date', String), Column('Nombre_de_Places', Integer))   
    
metadata.create_all(engine)
connection = engine.connect()

c_ins = cinema.insert()
  
s_ins = salle.insert()
f_ins = film.insert()
cl_ins = client.insert()
p_ins = projection.insert()

connection.execute(c_ins, [
  {'Nom_du_Cinema' : 'CineyPathey', 'Ville' : 'Mulhouse', 'Nombre_de_Salles' : 3, 'Prix' : 8},
  {'Nom_du_Cinema' : 'LOLComplexe', 'Ville' : 'Mulhouse', 'Nombre_de_Salles' : 4, 'Prix' : 10},
  {'Nom_du_Cinema' : '3DSwagg', 'Ville' : 'Lyon', 'Nombre_de_Salles' : 4, 'Prix' : 14},
  {'Nom_du_Cinema' : 'SmoothPopCorn', 'Ville' : 'Lyon', 'Nombre_de_Salles' : 3, 'Prix' : 10},
  {'Nom_du_Cinema' : 'IndySurLePouce', 'Ville' : 'Lyon', 'Nombre_de_Salles' : 1, 'Prix' : 4},
  {'Nom_du_Cinema' : 'LeMarais', 'Ville' : 'Paris', 'Nombre_de_Salles' : 1, 'Prix' : 5},
  {'Nom_du_Cinema' : 'LaToileDePaname', 'Ville' : 'Paris', 'Nombre_de_Salles' : 3, 'Prix' : 10},
  {'Nom_du_Cinema' : 'CaVaCouperCherie', 'Ville' : 'Paris', 'Nombre_de_Salles' : 4, 'Prix' : 12},
  {'Nom_du_Cinema' : 'RoyalPalace', 'Ville' : 'Paris', 'Nombre_de_Salles' : 5, 'Prix' : 14}
  ])

connection.execute(s_ins, [
  {'Cinema' : 'SmoothPopCorn', 'Numero_de_Salle' : 1, 'Nombre_de_Sieges' : 115},
  {'Cinema' : 'SmoothPopCorn', 'Numero_de_Salle' : 2, 'Nombre_de_Sieges' : 100},
  {'Cinema' : 'SmoothPopCorn', 'Numero_de_Salle' : 3, 'Nombre_de_Sieges' : 80},
  {'Cinema' : 'LeMarais', 'Numero_de_Salle' : 1, 'Nombre_de_Sieges' : 25},
  {'Cinema' : 'CineyPathey', 'Numero_de_Salle' : 1, 'Nombre_de_Sieges' : 135},
  {'Cinema' : 'CineyPathey', 'Numero_de_Salle' : 2, 'Nombre_de_Sieges' : 110},
  {'Cinema' : 'CineyPathey', 'Numero_de_Salle' :3, 'Nombre_de_Sieges' : 95},
  {'Cinema' : '3DSwagg', 'Numero_de_Salle' : 1, 'Nombre_de_Sieges' : 110},
  {'Cinema' : '3DSwagg', 'Numero_de_Salle' : 2, 'Nombre_de_Sieges' : 100},
  {'Cinema' : '3DSwagg', 'Numero_de_Salle' : 3, 'Nombre_de_Sieges' : 70},
  {'Cinema' : '3DSwagg', 'Numero_de_Salle' : 4, 'Nombre_de_Sieges' : 100},
  {'Cinema' : 'LOLComplexe', 'Numero_de_Salle' : 1, 'Nombre_de_Sieges' : 80},
  {'Cinema' : 'LOLComplexe', 'Numero_de_Salle' : 2, 'Nombre_de_Sieges' : 95},
  {'Cinema' : 'LOLComplexe', 'Numero_de_Salle' : 3, 'Nombre_de_Sieges' : 105},
  {'Cinema' : 'LOLComplexe', 'Numero_de_Salle' : 4, 'Nombre_de_Sieges' : 150},
  {'Cinema' : 'LaToileDePaname', 'Numero_de_Salle' : 1, 'Nombre_de_Sieges' : 75},
  {'Cinema' : 'LaToileDePaname', 'Numero_de_Salle' : 2, 'Nombre_de_Sieges' : 89},
  {'Cinema' : 'LaToileDePaname', 'Numero_de_Salle' : 3, 'Nombre_de_Sieges' : 100},
  {'Cinema' : 'CaVaCouperCherie', 'Numero_de_Salle' : 1, 'Nombre_de_Sieges' : 85},
  {'Cinema' : 'CaVaCouperCherie', 'Numero_de_Salle' : 2, 'Nombre_de_Sieges' : 110},
  {'Cinema' : 'CaVaCouperCherie', 'Numero_de_Salle' : 3, 'Nombre_de_Sieges' : 135},
  {'Cinema' : 'CaVaCouperCherie', 'Numero_de_Salle' : 4, 'Nombre_de_Sieges' : 94},
  {'Cinema' : 'RoyalPalace', 'Numero_de_Salle' : 1, 'Nombre_de_Sieges' : 95},
  {'Cinema' : 'RoyalPalace', 'Numero_de_Salle' : 2, 'Nombre_de_Sieges' : 120},
  {'Cinema' : 'RoyalPalace', 'Numero_de_Salle' : 3, 'Nombre_de_Sieges' : 153},
  {'Cinema' : 'RoyalPalace', 'Numero_de_Salle' : 4, 'Nombre_de_Sieges' : 175},
  {'Cinema' : 'RoyalPalace', 'Numero_de_Salle' : 5, 'Nombre_de_Sieges' : 112},
  {'Cinema' : 'IndySurLePouce', 'Numero_de_Salle' : 1, 'Nombre_de_Sieges' : 40}
  ])

connection.execute(f_ins, [
  {'Film' : 'Girls Only', 'Genre' : 'Comedie Romance', 'Realisateur' : 'Lynn Shelton', 'Tete_d_Affiche' : 'Keira Knightley', 'Annee' : 2015, 'Note' : 0.0, 'Nombre_de_notes' : 0},
  {'Film' : 'Mad Max Fury Road', 'Genre' : 'Action', 'Realisateur' : 'George Miller', 'Tete_d_Affiche' : 'Tom Hardy', 'Annee' : 2015, 'Note' : 0.0, 'Nombre_de_notes' : 0},
  {'Film' : 'A la poursuite de demain', 'Genre' : 'Science-Fiction', 'Realisateur' : 'Brad Bird', 'Tete_d_Affiche' : 'George Clooney', 'Annee' : 2015, 'Note' : 0, 'Nombre_de_notes' : 0},
  {'Film' : 'Diversion', 'Genre' : 'Thriller', 'Realisateur' : 'Glenn Ficarra', 'Tete_d_Affiche' : 'Will Smith', 'Annee' : 2015, 'Note' : 0.0, 'Nombre_de_notes' : 0},
  {'Film' : 'Fast & Furious', 'Genre' : 'Action', 'Realisateur' : 'James Wan', 'Tete_d_Affiche' : 'Paul Walker', 'Annee' : 2015, 'Note' : 0.0, 'Nombre_de_notes' : 0},
  {'Film' : 'Avengers L ere d Ultron', 'Genre' : 'Action', 'Realisateur' : 'Joss Whedon', 'Tete_d_Affiche' : 'Robert Downey Jr', 'Annee' : 2015, 'Note' : 0.0, 'Nombre_de_notes' : 0},
  {'Film' : 'Une bell fin', 'Genre' : ' Comedie Drame', 'Realisateur' : 'Uberto Pasolini', 'Tete_d_Affiche' : 'Eddie Marsan', 'Annee' : 2015, 'Note' : 0.0, 'Nombre_de_notes' : 0},
  {'Film' : 'Les Jardins du Roi', 'Genre' : 'Drame Romance', 'Realisateur' : 'Alan Rickman', 'Tete_d_Affiche' : 'Kate Winslet', 'Annee' : 2015, 'Note' : 0.0, 'Nombre_de_notes' : 0},
  {'Film' : 'Maggie', 'Genre' : 'Thriller_Drame', 'Realisateur' : 'Henry Hobson', 'Tete_d_Affiche' : 'Arnold Schwarzenegger', 'Annee' : 2015, 'Note' : 0.0, 'Nombre_de_notes' : 0},
  {'Film' : 'Nos femmes', 'Genre' : 'Comedie', 'Realisateur' : 'Richard Berry', 'Tete_d_Affiche' : 'Daniel Auteuil', 'Annee' : 2015, 'Note' : 0.0, 'Nombre_de_notes' : 0},
  {'Film' : 'Shaun le mouton', 'Genre' : 'Animation Comedie', 'Realisateur' : 'Richard Starzak', 'Tete_d_Affiche' : 'Justin Fletcher', 'Annee' : 2015, 'Note' : 0.0, 'Nombre_de_notes' : 0},
  {'Film' : 'Conasse Princesse des coeurs', 'Genre' : 'Comedie', 'Realisateur' : 'Eloise Lang', 'Tete_d_Affiche' : 'Camille Lottin', 'Annee' : 2015, 'Note' : 0.0, 'Nombre_de_notes' : 0},
  {'Film' : 'En route', 'Genre' : 'Animation', 'Realisateur' : 'Tim Johnson', 'Tete_d_Affiche' : 'Jim Parsons', 'Annee' : 2015, 'Note' : 0.0, 'Nombre_de_notes' : 0} 
  ])

connection.execute(p_ins, [
  {'Numero_de_Salle':1, 'FilmId':1, 'horaire':'13h30', 'date':'03/06/15', 'Nombre_de_Places': 115},
  {'Numero_de_Salle':1, 'FilmId':2, 'horaire':'17h30', 'date':'03/06/15', 'Nombre_de_Places': 115},
  {'Numero_de_Salle':1, 'FilmId':2, 'horaire':'10h30', 'date':'04/06/15', 'Nombre_de_Places': 115},
  {'Numero_de_Salle':2, 'FilmId':3, 'horaire':'16h30', 'date':'03/06/15', 'Nombre_de_Places': 100},
  {'Numero_de_Salle':2, 'FilmId':4, 'horaire':'14h00', 'date':'04/06/15', 'Nombre_de_Places': 100},
  {'Numero_de_Salle':2, 'FilmId':4, 'horaire':'11h30', 'date':'05/06/15', 'Nombre_de_Places': 100},
  {'Numero_de_Salle':3, 'FilmId':5, 'horaire':'10h30', 'date':'05/06/15', 'Nombre_de_Places': 80},
  {'Numero_de_Salle':3, 'FilmId':6, 'horaire':'18h00', 'date':'06/06/15', 'Nombre_de_Places': 80},
  {'Numero_de_Salle':3, 'FilmId':6, 'horaire':'20h30', 'date':'03/06/15', 'Nombre_de_Places': 80},
  {'Numero_de_Salle':4, 'FilmId':7, 'horaire':'10h30', 'date':'03/06/15', 'Nombre_de_Places': 25},
  {'Numero_de_Salle':4, 'FilmId':8, 'horaire':'15h00', 'date':'03/06/15', 'Nombre_de_Places': 25},
  {'Numero_de_Salle':4, 'FilmId':8, 'horaire':'19h30', 'date':'04/06/15', 'Nombre_de_Places': 25},
  {'Numero_de_Salle':5, 'FilmId':9, 'horaire':'13h30', 'date':'05/06/15', 'Nombre_de_Places': 135},
  {'Numero_de_Salle':5, 'FilmId':10, 'horaire':'10h00', 'date':'06/06/15', 'Nombre_de_Places': 135},
  {'Numero_de_Salle':5, 'FilmId':10, 'horaire':'21h30', 'date':'06/06/15', 'Nombre_de_Places': 135},
  {'Numero_de_Salle':6, 'FilmId':11, 'horaire':'12h30', 'date':'05/06/15', 'Nombre_de_Places': 110},
  {'Numero_de_Salle':6, 'FilmId':12, 'horaire':'18h45', 'date':'03/06/15', 'Nombre_de_Places': 110},
  {'Numero_de_Salle':6, 'FilmId':12, 'horaire':'21h30', 'date':'04/06/15', 'Nombre_de_Places': 110},
  {'Numero_de_Salle':7, 'FilmId':13, 'horaire':'11h00', 'date':'04/06/15', 'Nombre_de_Places': 95},
  {'Numero_de_Salle':7, 'FilmId':1, 'horaire':'18h30', 'date':'05/06/15', 'Nombre_de_Places': 95},
  {'Numero_de_Salle':7, 'FilmId':8, 'horaire':'13h30', 'date':'05/06/15', 'Nombre_de_Places': 95},
  {'Numero_de_Salle':8, 'FilmId':5, 'horaire':'14h30', 'date':'06/06/15', 'Nombre_de_Places': 110},
  {'Numero_de_Salle':8, 'FilmId':4, 'horaire':'19h30', 'date':'03/06/15', 'Nombre_de_Places': 110},
  {'Numero_de_Salle':8, 'FilmId':9, 'horaire':'10h30', 'date':'04/06/15', 'Nombre_de_Places': 110},
  {'Numero_de_Salle':9, 'FilmId':6, 'horaire':'20h30', 'date':'03/06/15', 'Nombre_de_Places': 100},
  {'Numero_de_Salle':9, 'FilmId':3, 'horaire':'13h30', 'date':'06/06/15', 'Nombre_de_Places': 100},
  {'Numero_de_Salle':9, 'FilmId':10, 'horaire':'10h30', 'date':'05/06/15', 'Nombre_de_Places': 100},
  {'Numero_de_Salle':10, 'FilmId':3, 'horaire':'16h30', 'date':'04/06/15', 'Nombre_de_Places': 70},
  {'Numero_de_Salle':10, 'FilmId':3, 'horaire':'12h00', 'date':'03/06/15', 'Nombre_de_Places': 70},
  {'Numero_de_Salle':10, 'FilmId':11, 'horaire':'21h30', 'date':'03/06/15', 'Nombre_de_Places': 70},
  {'Numero_de_Salle':11, 'FilmId':12, 'horaire':'21h30', 'date':'03/06/15', 'Nombre_de_Places': 100},
  {'Numero_de_Salle':11, 'FilmId':7, 'horaire':'14h30', 'date':'04/06/15', 'Nombre_de_Places': 100},
  {'Numero_de_Salle':11, 'FilmId':9, 'horaire':'10h30', 'date':'04/06/15', 'Nombre_de_Places': 100},
  {'Numero_de_Salle':12, 'FilmId':6, 'horaire':'13h30', 'date':'05/06/15', 'Nombre_de_Places': 80},
  {'Numero_de_Salle':12, 'FilmId':2, 'horaire':'18h00', 'date':'05/06/15', 'Nombre_de_Places': 80},
  {'Numero_de_Salle':12, 'FilmId':13, 'horaire':'21h00', 'date':'03/06/15', 'Nombre_de_Places': 80},
  {'Numero_de_Salle':13, 'FilmId':9, 'horaire':'13h30', 'date':'05/06/15', 'Nombre_de_Places': 95},
  {'Numero_de_Salle':13, 'FilmId':1, 'horaire':'16h30', 'date':'04/06/15', 'Nombre_de_Places': 95},
  {'Numero_de_Salle':13, 'FilmId':1, 'horaire':'20h30', 'date':'06/06/15', 'Nombre_de_Places': 95},
  {'Numero_de_Salle':14, 'FilmId':2, 'horaire':'13h30', 'date':'03/06/15', 'Nombre_de_Places': 105},
  {'Numero_de_Salle':14, 'FilmId':8, 'horaire':'17h00', 'date':'06/06/15', 'Nombre_de_Places': 105},
  {'Numero_de_Salle':14, 'FilmId':6, 'horaire':'20h30', 'date':'03/06/15', 'Nombre_de_Places': 105},
  {'Numero_de_Salle':15, 'FilmId':4, 'horaire':'13h30', 'date':'05/06/15', 'Nombre_de_Places': 150},
  {'Numero_de_Salle':15, 'FilmId':10, 'horaire':'17h30', 'date':'05/06/15', 'Nombre_de_Places': 150},
  {'Numero_de_Salle':15, 'FilmId':1, 'horaire':'21h00', 'date':'05/06/15', 'Nombre_de_Places': 150},
  {'Numero_de_Salle':16, 'FilmId':11, 'horaire':'11h30', 'date':'03/06/15', 'Nombre_de_Places': 75},
  {'Numero_de_Salle':16, 'FilmId':5, 'horaire':'16h00', 'date':'03/06/15', 'Nombre_de_Places': 75},
  {'Numero_de_Salle':16, 'FilmId':3, 'horaire':'12h30', 'date':'04/06/15', 'Nombre_de_Places': 75},
  {'Numero_de_Salle':17, 'FilmId':7, 'horaire':'21h30', 'date':'04/06/15', 'Nombre_de_Places': 89},
  {'Numero_de_Salle':17, 'FilmId':13, 'horaire':'17h00', 'date':'06/06/15', 'Nombre_de_Places': 89},
  {'Numero_de_Salle':17, 'FilmId':1, 'horaire':'12h30', 'date':'03/06/15', 'Nombre_de_Places': 89},
  {'Numero_de_Salle':18, 'FilmId':1, 'horaire':'18h30', 'date':'04/06/15', 'Nombre_de_Places': 100},
  {'Numero_de_Salle':18, 'FilmId':6, 'horaire':'14h00', 'date':'05/06/15', 'Nombre_de_Places': 100},
  {'Numero_de_Salle':18, 'FilmId':2, 'horaire':'21h30', 'date':'03/06/15', 'Nombre_de_Places': 100},
  {'Numero_de_Salle':19, 'FilmId':7, 'horaire':'10h30', 'date':'05/06/15', 'Nombre_de_Places': 85},
  {'Numero_de_Salle':19, 'FilmId':11, 'horaire':'13h30', 'date':'03/06/15', 'Nombre_de_Places': 85},
  {'Numero_de_Salle':19, 'FilmId':9, 'horaire':'18h30', 'date':'06/06/15', 'Nombre_de_Places': 85},
  {'Numero_de_Salle':20, 'FilmId':6, 'horaire':'16h45', 'date':'03/06/15', 'Nombre_de_Places': 110},
  {'Numero_de_Salle':20, 'FilmId':1, 'horaire':'13h30', 'date':'04/06/15', 'Nombre_de_Places': 110},
  {'Numero_de_Salle':20, 'FilmId':3, 'horaire':'20h30', 'date':'04/06/15', 'Nombre_de_Places': 110},
  {'Numero_de_Salle':21, 'FilmId':3, 'horaire':'14h30', 'date':'04/06/15', 'Nombre_de_Places': 135},
  {'Numero_de_Salle':21, 'FilmId':11, 'horaire':'11h15', 'date':'05/06/15', 'Nombre_de_Places': 135},
  {'Numero_de_Salle':21, 'FilmId':12, 'horaire':'20h30', 'date':'03/06/15', 'Nombre_de_Places': 135},
  {'Numero_de_Salle':22, 'FilmId':8, 'horaire':'13h30', 'date':'05/06/15', 'Nombre_de_Places': 94},
  {'Numero_de_Salle':22, 'FilmId':5, 'horaire':'18h00', 'date':'05/06/15', 'Nombre_de_Places': 94},
  {'Numero_de_Salle':22, 'FilmId':6, 'horaire':'21h45', 'date':'06/06/15', 'Nombre_de_Places': 94},
  {'Numero_de_Salle':23, 'FilmId':9, 'horaire':'15h30', 'date':'06/06/15', 'Nombre_de_Places': 95},
  {'Numero_de_Salle':23, 'FilmId':10, 'horaire':'11h30', 'date':'03/06/15', 'Nombre_de_Places': 95},
  {'Numero_de_Salle':23, 'FilmId':1, 'horaire':'19h00', 'date':'03/06/15', 'Nombre_de_Places': 95},
  {'Numero_de_Salle':24, 'FilmId':2, 'horaire':'13h30', 'date':'03/06/15', 'Nombre_de_Places': 120},
  {'Numero_de_Salle':24, 'FilmId':12, 'horaire':'10h45', 'date':'04/06/15', 'Nombre_de_Places': 120},
  {'Numero_de_Salle':24, 'FilmId':12, 'horaire':'21h30', 'date':'04/06/15', 'Nombre_de_Places': 120},
  {'Numero_de_Salle':25, 'FilmId':13, 'horaire':'14h30', 'date':'05/06/15', 'Nombre_de_Places': 153},
  {'Numero_de_Salle':25, 'FilmId':5, 'horaire':'18h30', 'date':'06/06/15', 'Nombre_de_Places': 153},
  {'Numero_de_Salle':25, 'FilmId':1, 'horaire':'11h15', 'date':'06/06/15', 'Nombre_de_Places': 153},
  {'Numero_de_Salle':26, 'FilmId':2, 'horaire':'21h30', 'date':'03/06/15', 'Nombre_de_Places': 175},
  {'Numero_de_Salle':26, 'FilmId':8, 'horaire':'10h30', 'date':'03/06/15', 'Nombre_de_Places': 175},
  {'Numero_de_Salle':26, 'FilmId':9, 'horaire':'15h30', 'date':'04/06/15', 'Nombre_de_Places': 175},
  {'Numero_de_Salle':27, 'FilmId':7, 'horaire':'15h30', 'date':'05/06/15', 'Nombre_de_Places': 112},
  {'Numero_de_Salle':27, 'FilmId':11, 'horaire':'19h00', 'date':'05/06/15', 'Nombre_de_Places': 112},
  {'Numero_de_Salle':27, 'FilmId':6, 'horaire':'10h30', 'date':'04/06/15', 'Nombre_de_Places': 112},
  {'Numero_de_Salle':28, 'FilmId':11, 'horaire':'13h30', 'date':'04/06/15', 'Nombre_de_Places': 40},
  {'Numero_de_Salle':28, 'FilmId':10, 'horaire':'20h00', 'date':'06/06/15', 'Nombre_de_Places': 40},
  {'Numero_de_Salle':28, 'FilmId':1, 'horaire':'16h45', 'date':'03/06/15', 'Nombre_de_Places': 40}
  ])

connection.close()

