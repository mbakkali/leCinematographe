	
function addMovie(){	
	var Movie = $("#nom_film").val();
	var Realisateur = $("#nom_realisateur").val();
	var Tete_affiche = $("#tete_affiche").val();
	var Annee = $("#annee").val();
	var genre = "";
	
	var Comedie = document.getElementById("Comedie").checked;
	var Romance = document.getElementById("Romance").checked;
	var Drame = document.getElementById("Drame").checked;
	var Science_fiction = document.getElementById("Science_fiction").checked;
	var Action = document.getElementById("Action").checked;
	var Animation = document.getElementById("Animation").checked;
	var Tragedie = document.getElementById("Tragedie").checked;
	
	if(Comedie){
		genre+="Comedie ";
	}
	if(Romance){
		genre+="Romance "
	}
	if(Drame){
		genre+="Drame ";
	}
	if(Science_fiction){
		genre+="Science_fiction ";
	}
	if(Action){
		genre+="Action ";
	}
	if(Animation){
		genre+="Animation ";
	}
	if(Tragedie){
		genre+="Tragedie ";
	}
	
	$.ajax({                                  
    url: "/api/addMovie/",
    data: {
		Movie: Movie,
		Realisateur: Realisateur,
		Tete_affiche: Tete_affiche,
		Annee: Annee,
		Genre: genre,
	},
	type: 'POST',
    dataType: "json",
  }).done(function(data) {
	$('#result').html("Votre film a bien été ajouté");
  }).fail(function(args) {
	  console.warn('Bad request :', args);
  });
  
  
}

function addProjection(){
	var cinema = $("#Cinema").val();
	var num_salle = $("#num_salle").val();
	var FilmId = $("#FilmId").val();
	var horaire = $("#horaire").val();
	var date = $("#date").val();
	
	$.ajax({                                  
    url: "/api/addProjection/",
    data: {
		Cinema: cinema,
		Num_salle: num_salle,
		FilmId: FilmId,
		Horaire: horaire,
		date: date,
	},
	type: 'POST',
    dataType: "json",
  }).done(function(data) {
	$('#result').html("Votre projection a bien été ajouté");
  }).fail(function(args) {
	  console.warn('Bad request :', args);
  });
	
}

["#formMovie"].forEach(function(item) {
  $(item).on("submit", function(event) {
    addMovie();
  });
});


["#formProjection"].forEach(function(item) {
  $(item).on("submit", function(event) {
    addProjection();
  });
});
	
	
