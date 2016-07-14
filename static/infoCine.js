function getInfoCine(){
	
	//sort le nom du cine selectionné du l'url
	var split = window.location.search.split('=');
	var cine=split[1];
	document.getElementById('nomCine').innerHTML += 'Cinema :'+cine
	$.ajax({                                  
    url: "/api/getInfoCine/",
    data: {
		LeCinema: cine,
	},
    dataType: "json",
  }).done(function(data) {
		var programmation = data['result'];
		document.getElementById('uneSalle').innerHTML ='' //uneSalle est le id dans le html
		var salle = 0; //initialisation de la variable salle
		for (var i = 0; i < programmation.length; i++) {
			 //On cree la projection suivante
			 var projection = programmation[i];
			 //On test si la salle est deja cree
			 if( salle != projection[0]){
				 //Nouvelle salle
				 CreerSalle(projection[0]);
				 salle = projection[0];
			 }
			 AfficheFilmSalle(projection, salle);
		 } //fin for
  }).fail(function(args) {
	  console.warn('Bad request :', args);
  });
}

function CreerSalle(numsalle){
	document.getElementById('uneSalle').innerHTML +='<h4>Numero de la salle: #'+numsalle+'</h4><table class="table2"><thead><tr><th>Date</th><th>Heure</th><th>Film</th><th>Places disponibles</tr></thead><tbody  id="'+numsalle+'"></tbody></table>'
}

function AfficheFilmSalle(projection, numsalle){
	text=projection[5];
	if (projection[4] == 0){
			document.getElementById(numsalle).innerHTML += '<tr><td>'+projection[1]+'</td><td>'+projection[2]+'</td><td>'+projection[3]+'</td><td>Aucune place disponible</td></tr>'
	}else{
		document.getElementById(numsalle).innerHTML += '<tr><td>'+projection[1]+'</td><td>'+projection[2]+'</td><td>'+projection[3]+'</td><td>'+projection[4]+'</td><td><input type="submit" value="Reserver" OnClick="ReserverPlace('+text+');"></td></tr>'
	}
}

function ReserverPlace(ProjectionId){
	$.ajax({                                  
    url: "/api/Rerservation/",
    data: {
		ProjectionId : ProjectionId
	},
    dataType: "json",
    type: 'PUT',
  }).done(function(data) {
	  location.reload() ; 
  }).fail(function(args) {
	  console.warn('Bad request :', args);
  });
}

getInfoCine();
