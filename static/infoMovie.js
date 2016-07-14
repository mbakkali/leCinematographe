
function getInfoMovie(){
	console.log('Hi');
	var split = window.location.search.split('=');
	var id=split[1];
	$.ajax({                                  
    url: "/api/getInfoMovie/",
    data: {
		Id: id,
	},
    dataType: "json",
  }).done(function(data) {
	  $('#divFilm').html("Film: "+data['Film']);
	  $('#divRealisateur').html(data['Realisateur']);
	  $('#divGenre').html(data['Genre']);
	  $('#divActeur').html(data['Tete_d_Affiche']);
	  $('#divDate').html(data['Annee']);
	  $('#divNote').html(data['Note']);
	  $('#divVote').html(data['Vote'])
  }).fail(function(args) {
	  console.warn('Bad request :', args);
  });
}
console.log('Hi');
var split = window.location.search.split('=');
var id=split[1];
getInfoMovie();

function noter(Note){
	console.log('Hi '+Note);
	$.ajax({                                  
    url: "/api/Notation/",
    data: {
		Note: Note,
		Id: id,
	},
    dataType: "json",
    type: 'PUT',
  }).done(function(data) {
	  $('#divNote').html(data['Note'])
	  $('#divVote').html(data['Vote'])
  }).fail(function(args) {
	  console.warn('Bad request :', args);
  });
}
